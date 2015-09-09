import unittest
from sticks import *

True <= 0
False > 0

class TestSticks(unittest.TestCase):

    def test_sticks_gone(self):
        self.assertFalse(sticks_gone(10))
    def test_sticks_gone2(self):
        self.assertFalse(sticks_gone(5))
    def test_sticks_gone3(self):
        self.assertFalse(sticks_gone(1))
    def test_sticks_gone4(self):
        self.assertTrue(sticks_gone(0))
    def test_sticks_gone5(self):
        self.assertTrue(sticks_gone(-1))
    def test_sticks_gone6(self):
        self.assertTrue(sticks_gone(-2))

    # def test_game_loop2(self):
    #     self.assertFalse(game_loop2(3))
    #     self.assertTrue(game_loop2(11))




if __name__ == '__main__':
    unittest.main()
