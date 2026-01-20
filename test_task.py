# test_task.py

import unittest
import numpy.testing as npt
from task import Task


class TestTask(unittest.TestCase):
    def test_work_solves_linear_system(self):
        """Vérifie que Task.work calcule correctement x tel que A x = B"""
        size = 5
        task = Task(size=size)

        A = task.a.copy()
        B = task.b.copy()

        task.work()

        npt.assert_allclose(A @ task.x, B, rtol=1e-7, atol=0)

    def test_serialization_equality(self):
        """Vérifie que la sérialisation/désérialisation préserve l'égalité"""
        a = Task()
        txt = a.to_json()
        b = Task.from_json(txt)
        self.assertEqual(a, b)


if __name__ == "__main__":
    unittest.main()
