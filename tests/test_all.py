from .context import tic_tac_toe_agent
import unittest


class TestApp(unittest.TestCase):
    def test_hello(self):
        self.assertEqual("hello", tic_tac_toe_agent.hello())


if __name__ == "__main__":
    unittest.main()
