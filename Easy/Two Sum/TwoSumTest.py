import unittest
import TwoSum_Naive
import TwoSum_Optimal
from TwoSum_Naive import *
from TwoSum_Optimal import *


class TestTwoSum(unittest.TestCase):

    def test_regular_pattern(self):
        self.assertEqual(TwoSum_Naive.twoSum([2,7,11,15], 9), [0,1])
        self.assertEqual(TwoSum_Optimal.twoSum([2,7,11,15], 9), [0,1])

    def test_same_number(self):
        self.assertEqual(TwoSum_Naive.twoSum([3,3], 6), [0,1])
        self.assertEqual(TwoSum_Optimal.twoSum([3,3], 6), [0,1])

    def test_end_of_array(self):
        self.assertEqual(TwoSum_Naive.twoSum([3,2,4], 6), [1,2])
        self.assertEqual(TwoSum_Optimal.twoSum([3,2,4], 6), [1,2])

    def test_first_solution_only(self):
        self.assertEqual(TwoSum_Naive.twoSum([3,3,3], 6), [0,1])
        self.assertEqual(TwoSum_Optimal.twoSum([3,3,3], 6), [0,1])
        
        
if __name__ == '__main__':
    unittest.main()
