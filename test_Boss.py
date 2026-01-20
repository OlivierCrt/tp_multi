import unittest
from multiprocessing import Pool

from boss import minion
from task import Task


class TestBossMinions(unittest.TestCase):
    def test_minion_executes_task(self):
        """Vérifie qu'un minion exécute correctement une tâche"""
        task = Task(identifier=0, size=100)
        result = minion(task)
        
        self.assertGreater(result.time, 0)
        self.assertEqual(len(result.x), 100)
    
    def test_boss_distributes_to_minions(self):
        """Vérifie que le boss distribue correctement aux minions"""
        num_tasks = 4
        num_minions = 2
        tasks = [Task(identifier=i, size=50) for i in range(num_tasks)]
        
        with Pool(num_minions) as pool:
            results = pool.map(minion, tasks)
        
        # Toutes les tâches ont été exécutées
        self.assertEqual(len(results), num_tasks)
        
        # Chaque minion a travaillé
        for task in results:
            self.assertGreater(task.time, 0)
            self.assertEqual(task.size, 50)


if __name__ == "__main__":
    unittest.main()