import time
from multiprocessing import Pool, cpu_count

from task import Task


def minion(task: Task) -> Task:
    """Un minion exécute une tâche.

    Args:
        task: La tâche à exécuter

    Returns:
        La tâche avec les résultats calculés
    """
    task.work()
    return task


def main():
    # Configuration du boss
    num_tasks = 20
    num_minions = cpu_count()

    print(f"Boss: Creating {num_tasks} tasks...")
    print(f"Boss: Hiring {num_minions} minions")

    tasks = [Task(identifier=i) for i in range(num_tasks)]

    # Le boss distribue le travail aux minions
    print("\nBoss: Distributing work to minions...")
    start = time.perf_counter()

    with Pool(num_minions) as pool:
        results = pool.map(minion, tasks)

    elapsed = time.perf_counter() - start

    # Le boss analyse les résultats
    print("\nBoss: All minions finished!")
    print(f"Boss: Total time: {elapsed:.2f}s")

    total_work_time = sum(task.time for task in results)
    print(f"Boss: Total work by minions: {total_work_time:.2f}s")
    print(f"Boss: Average task time: {total_work_time / num_tasks:.2f}s")
    print(f"Boss: Speedup: {total_work_time / elapsed:.2f}x")

    # Statistiques par minion
    print("\nBoss: Task statistics:")
    for i, task in enumerate(results):
        print(f"  Task {task.identifier}: {task.time:.3f}s (size: {task.size})")


if __name__ == "__main__":
    main()
