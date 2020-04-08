import unittest
from heredity import joint_probability


class TestTransitionModel(unittest.TestCase):
    def test_joint_probability(self):
        people = {
            'Harry': {'name': 'Harry', 'mother': 'Lily', 'father': 'James', 'trait': None},
            'James': {'name': 'James', 'mother': None, 'father': None, 'trait': True},
            'Lily': {'name': 'Lily', 'mother': None, 'father': None, 'trait': False}
        }

        self.assertAlmostEqual(
            joint_probability(people, {"Harry"}, {"James"}, {"James"}),
            0.0026643247488,
            places=5
        )


if __name__ == '__main__':
    unittest.main()
