import unittest
from pagerank import transition_model


class TestTransitionModel(unittest.TestCase):
    def test_transition_model(self):
        model_1 = transition_model(
            {"1.html": {"2.html", "3.html"}, "2.html": {"3.html"}, "3.html": {"2.html"}},
            "1.html",
            0.85
        )

        model_2 = {"1.html": 0.05, "2.html": 0.475, "3.html": 0.475}

        for link in model_1:
            if link in model_2:
                self.assertAlmostEqual(model_1[link], model_2[link], places=2)

    def test_transition_model_no_links(self):
        model_1 = transition_model(
            {"1.html": {}, "2.html": {"3.html"}, "3.html": {"2.html"}},
            "1.html",
            0.85
        )

        model_2 = {"1.html": 0.33, "2.html": 0.33, "3.html": 0.33}

        for link in model_1:
            if link in model_2:
                self.assertAlmostEqual(model_1[link], model_2[link], places=2)


if __name__ == '__main__':
    unittest.main()
