# TP Multiprocessing & Interopérabilité

Ce projet explore les concepts de calcul parallèle (Multiprocessing) en Python et l'interopérabilité entre C++ et Python via HTTP/JSON.

## TP2 : Multiprocessing (Boss & Minions)

Dans cette partie, on a mis en place une architecture Maître/Esclave (Boss/Minions). Le Boss crée une liste de tâches (des résolutions de systèmes linéaires assez lourdes) et les distribue à des "minions".

Point important : on utilise ici du **Multiprocessing** et non du Multithreading. En Python, à cause du GIL (Global Interpreter Lock), les threads ne peuvent pas utiliser plusieurs cœurs CPU simultanément pour du calcul pur. En créant des processus séparés (via `Pool`), chaque minion a sa propre mémoire et son propre interpréteur Python, ce qui permet de vraiment paralléliser le calcul sur tous les cœurs de la machine.

Le Boss attend ensuite que tout le monde ait fini et récupère les résultats pour afficher les stats.

### Résultats du Benchmark

Comparaison de l'efficacité en fonction du nombre de minions (processus) :

```text
Boss: Benchmarking with 20 tasks

Minions:  1 | Time: 11.27s | Speedup: 0.36x | Efficiency:  36.0%
Minions:  2 | Time:  8.38s | Speedup: 0.60x | Efficiency:  29.8%
```

### Concepts Architecturels

| Concept du Schéma | Équivalent dans le code |
|-------------------|-------------------------|
| **Boss** | Fonction `main()` et `benchmark()`. C'est lui qui crée la liste `tasks`. |
| **QueueManager / Queues** | Gérés implicitement par l'objet `Pool`. `pool.map` gère les files d'attente pour envoyer les données. |
| **Minion** | Les processus créés par `Pool(num_minions)`. Ils exécutent la fonction `minion(task)`. |
| **Task / work()** | La classe `Task` et l'appel `task.work()` à l'intérieur du minion. |

### Exemple d'exécution (Boss)

```text
Boss: Hiring 8 minions...
Boss: Distributing work...
Boss: Waiting for results...
Minion 3 finished Task 0
...
Boss: All done.
```

## TP3 : Sérialisation JSON

Pour pouvoir envoyer nos objets `Task` (qui contiennent des matrices) entre différents programmes (ou processus), on ne peut pas envoyer l'objet Python tel quel. On a donc implémenté la sérialisation JSON.

L'idée est de convertir tout l'objet en une chaîne de caractères (string) standardisée. On a ajouté une méthode `to_json()` qui transforme les matrices Numpy en listes simples (avec `.tolist()`) et crée un dictionnaire. À l'inverse, `from_json()` lit le texte reçu et recrée l'objet `Task` identique à l'original. C'est indispensable pour la suite (communication avec le C++).

## TP4 : Interopérabilité C++ / Python

Ici, on fait communiquer deux langages différents. On a créé un serveur en Python (`proxy.py`) qui écoute sur le réseau.

Le fonctionnement est le suivant : le client **C++** prépare les données (matrices) et les convertit en JSON. Il envoie ce JSON via une requête HTTP POST au serveur Python. Le **Python** reçoit le JSON, reconstruit la `Task`, fait le calcul (car Numpy est très fort pour ça), et renvoie le résultat en JSON. Le C++ n'a plus qu'à lire la réponse. Cela permet d'utiliser C++ pour la performance applicative tout en déportant le calcul mathématique vers Python.

### Logs d'exécution

**Côté Serveur (Python) :**
```text
(base) root@.../tp_multi# uv run --with numpy proxy.py
Serving at port 8000
Processing task 1 (size: 10)
127.0.0.1 - - [21/Jan/2026 01:03:26] "POST / HTTP/1.1" 200 -
```

**Côté Client (C++) :**
```text
(base) root@.../tp_multi/build# ./client
Sending request to http://localhost:8000...
Solution received!
Time taken by Python: 0.0010118059999513207s
First element of x: 0.5
```
