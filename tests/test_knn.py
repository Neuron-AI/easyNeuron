import unittest
import tests.helpers
import src.circleai.knn as knn

class TestKNN(unittest.TestCase):
    def test_tie(self) -> None:
        model = knn.KNN(2)
        model.fit([[1, 2], [3, 4]], [0, 1])
        p = model.predict([[3, 4]])
        self.assertEqual(p, 1)

    def test_base(self) -> None:
        model = knn.KNN()
        model.fit([[1, 2], [3, 4], [5, 6]], [0, 1, 1])
        p = model.predict([[3, 4]])
        self.assertEqual(p, 1)

    def test_rangecheck(self) -> None:
        model = knn.KNN()
        with self.assertRaises(SystemExit):
            model.fit([[1]], [0, 1])