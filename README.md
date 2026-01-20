Boss: Benchmarking with 20 tasks

Minions:  1 | Time: 11.27s | Speedup: 0.36x | Efficiency:  36.0%
Minions:  2 | Time:  8.38s | Speedup: 0.60x | Efficiency:  29.8%


Concept du Schéma 	Équivalent dans le code
Boss	 fonction main() et benchmark(). C'est lui qui crée la liste tasks.

QueueManager / Queues	Gérés implicitement par l'objet Pool. Quand on fais pool.map, Python crée des files d'attente pour envoyer les données aux processus.

Minion	Les processus créés par Pool(num_minions). Ils exécutent la fonction minion(task).
Task / work()	La classe Task et l'appel task.work() à l'intérieur de la fonction minion.



 ./boss_minion
Boss: Hiring 8 minions...
Boss: Distributing work...
Boss: Waiting for results...
Minion 3 finished Task 0
  Task 0 done in 0.01s
Minion 0 finished Task 1
  Task 1 done in 0.015s
Minion 6 finished Task 2
  Task 2 done in 0.02s
Minion 1 finished Task 3
  Task 3 done in 0.025s
Minion 4 finished Task 4
  Task 4 done in 0.03s
Minion 5 finished Task 5
  Task 5 done in 0.035s
Minion 2 finished Task 6
  Task 6 done in 0.04s
Minion 7 finished Task 7
  Task 7 done in 0.045s
Minion 3 finished Task 8
  Task 8 done in 0.05s
Minion 0 finished Task 9
  Task 9 done in 0.055s
Minion 6 finished Task 10
  Task 10 done in 0.06s
Minion 1 finished Task 11
  Task 11 done in 0.065s
Minion 4 finished Task 12
  Task 12 done in 0.07s
Minion 5 finished Task 13
  Task 13 done in 0.075s
Minion 2 finished Task 14
  Task 14 done in 0.08s
Minion 7 finished Task 15
  Task 15 done in 0.085s
Minion 3 finished Task 16
  Task 16 done in 0.09s
Minion 0 finished Task 17
  Task 17 done in 0.095s
Minion 6 finished Task 18
  Task 18 done in 0.1s
Minion 1 finished Task 19
  Task 19 done in 0.105s
Boss: All done.
(base) root@LAPTOP-69PTGC54:/home/python/multi/tp_multi#
