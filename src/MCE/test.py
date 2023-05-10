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
        
   
            
if __name__ == '__main__':
    unittest.main()