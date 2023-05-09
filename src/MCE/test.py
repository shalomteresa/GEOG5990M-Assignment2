# -*- coding: utf-8 -*-
"""
Created on Tue May  9 14:45:59 2023

@author: gy22stp
"""

import unittest
import model2
from unittest.mock import Mock


class TestCode(unittest.TestCase):
    def test_get_weighted_sum(self):
        gw = 0.3
        tw = 0.4
        pw = 0.3
        geology = [[1], [2]]
        transport = [[0], [1]]
        population = [[3], [0]]
        ws = model2.get_weighted_sum(gw, tw, pw, geology, transport, population)
        self.assertEqual(ws, [[1.2], [1.0]])
        
    def test_plot_rescaling(self):
        gw = 0.3
        tw = 0.4
        pw = 0.3
        geology = [[1, 2], [3, 4]]
        transport = [[0, 1], [2, 3]]
        population = [[5, 6], [7, 8]]
    
        # expected output
        expected = [[0, 74], [149, 255]]
    
        # call the function
        rescaled_output =  model2.plot(gw, tw, pw, geology, population, transport)

        # check that the rescaled output matches the expected output
        self.assertEqual(rescaled_output == expected)
    
    def test_update(self):
        # Set up mock scales and labels
        scale1 = Mock()
        scale1.get.return_value = 5.0
        scale1_label = Mock()
        
        scale2 = Mock()
        scale2.get.return_value = 2.5
        scale2_label = Mock()
        
        scale3 = Mock()
        scale3.get.return_value = 10.0
        scale3_label = Mock()
        
        # Call the update function
        model2.update(scale1, scale1_label, scale2, scale2_label, scale3, scale3_label)
        
        # Check that the labels have been updated correctly
        scale1_label.config.assert_called_with(text='geology=5.0')
        scale2_label.config.assert_called_with(text='transport=2.5')
        scale3_label.config.assert_called_with(text='population=10.0')
        
        # Check that the plot function has been called with the correct arguments
        model2.plot.assert_called_with(5.0, 2.5, 10.0)
            
if __name__ == '__main__':
    unittest.main()