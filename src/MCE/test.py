# -*- coding: utf-8 -*-
"""
Created on Tue May  9 14:45:59 2023

@author: gy22stp
"""

# Modules Imported
import unittest
import model


# A test case for the 'get_weighted_sum' function in the 'model2' module.
class TestCode(unittest.TestCase):
    def test_get_weighted_sum(self):
        '''
        Test that the 'get_weighted_sum' function returns the correct result.

        Returns
        -------
        None.

        '''
        # Set the input parameters and data for the test case
        gw = 0.3
        tw = 0.4
        pw = 0.3
        geology = [[1], [2]]
        transport = [[0], [1]]
        population = [[3], [0]]
        
        # Call the function being tested
        ws = model.get_weighted_sum(gw, tw, pw, geology, transport, population)
        
        # Check that the function returned the correct result
        self.assertEqual(ws, [[1.2], [1.0]])
        
    def test_get_min_max(self):
        '''
        Test that the 'get_min_max' function returns the correct result.

        Returns
        -------
        None.

        '''
        # Test with a valid input
        weighted_sum = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        min_val, max_val = model.get_min_max(weighted_sum)
        self.assertEqual(min_val, 1)
        self.assertEqual(max_val, 9)

        # Test with a negative input
        weighted_sum = [[-1, -2, -3], [-4, -5, -6], [-7, -8, -9]]
        min_val, max_val = model.get_min_max(weighted_sum)
        self.assertEqual(min_val, -9)
        self.assertEqual(max_val, -1)

        # Test with a single-element input
        weighted_sum = [[0]]
        min_val, max_val = model.get_min_max(weighted_sum)
        self.assertEqual(min_val, 0)
        self.assertEqual(max_val, 0)

        # Test with an empty input
        weighted_sum = []
        with self.assertRaises(IndexError):
            min_val, max_val = model.get_min_max(weighted_sum)
            
    def test_get_rescaled_output(self):
        '''
        Test that the 'get_rescaled_output' function returns the correct result.

        Returns
        -------
        None.

        '''
        # Test with a valid input
        weighted_sum = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        rescaled_output = model.get_rescaled_output(weighted_sum)
        expected_output = [[0, 31, 63], [95, 127, 159], [191, 223, 255]]
        self.assertEqual(rescaled_output, expected_output)

        # Test with an empty input
        weighted_sum = []
        with self.assertRaises(IndexError):
            rescaled_output = model.get_rescaled_output(weighted_sum)

   
# Run the unit tests when this module is executed            
if __name__ == '__main__':
    unittest.main()