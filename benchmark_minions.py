import time
from multiprocessing import Pool

from task import Task
from boss import minion


def benchmark():
    """Le boss teste différentes configurations de minions"""
    num_tasks = 20
    print(f"Boss: Benchmarking with {num_tasks} tasks\n")

    # Créer des tâches de référence
    reference_tasks = [Task(identifier=i) for i in range(num_tasks)]

    for num_minions in [1, 2, 4, 8, 16]:
        # Recréer les mêmes tâches
        tasks = [
            Task(identifier=i, size=reference_tasks[i].size) for i in range(num_tasks)
        ]

        start = time.perf_counter()
        with Pool(num_minions) as pool:
            results = pool.map(minion, tasks)
        elapsed = time.perf_counter() - start

        total_work = sum(t.time for t in results)
        efficiency = (total_work / elapsed) / num_minions * 100

        print(
            f"Minions: {num_minions:2d} | "
            f"Time: {elapsed:5.2f}s | "
            f"Speedup: {total_work / elapsed:4.2f}x | "
            f"Efficiency: {efficiency:5.1f}%"
        )


if __name__ == "__main__":
    benchmark()
