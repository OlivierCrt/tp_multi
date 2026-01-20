import time
from multiprocessing import Pool

from task import Task


def minion(task: Task) -> Task:
    """Un minion exécute une tâche et rapporte au boss"""
    print(f"  [Minion] Starting task {task.identifier} (size: {task.size})")
    task.work()
    print(f"  [Minion] Finished task {task.identifier} in {task.time:.3f}s")
    return task


def main():
    num_tasks = 8
    num_minions = 4

    print(f"[Boss] Creating {num_tasks} tasks")
    print(f"[Boss] Hiring {num_minions} minions")

    tasks = [Task(identifier=i, size=500) for i in range(num_tasks)]

    print("\n[Boss] Sending tasks to minions...\n")
    start = time.perf_counter()

    with Pool(num_minions) as pool:
        results = pool.map(minion, tasks)

    elapsed = time.perf_counter() - start

    print(f"\n[Boss] All work completed in {elapsed:.2f}s")
    print("[Boss] Thanking the minions and closing shop")


if __name__ == "__main__":
    main()
