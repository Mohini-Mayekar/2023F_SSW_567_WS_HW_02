# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
"""

import unittest

from Triangle import classifyTriangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    def testRightTriangleA(self): #T_02a_1
        self.assertEqual(classifyTriangle(3,4,5),'Right','3,4,5 is a Right triangle')

    def testRightTriangleB(self): #T_02a_2
        self.assertEqual(classifyTriangle(5,3,4),'Right','5,3,4 is a Right triangle')
        
    def testEquilateralTriangles(self): #T_02a_3
        self.assertEqual(classifyTriangle(1,1,1),'Equilateral','1,1,1 should be equilateral')

    #test case for isosceles triangle
    def test_isosceles_triangle(self): #T_02a_4
        self.assertEqual(classifyTriangle(4,4,5),"Isosceles", "(4,4,5) is an Isosceles triangle")

    #test case for scalene triangle
    def test_scalene_triangle(self): #T_02a_5
        self.assertEqual(classifyTriangle(7,8,9),"Scalene", "(7,8,9) is a Scalene triangle")

    #test case for not a triangle
    def test_not_a_triangle(self): #T_02a_6
        self.assertEqual(classifyTriangle(2,2,5),"NotATriangle", "(2,2,5) is not a triangle")

    #test case - all negative inputs
    def test_neg_int_values(self): #T_02a_7
        self.assertEqual(classifyTriangle(-1,-1,-1),"InvalidInput", "(-1,-1,-1) is Invalid Input")
    
    #test case - invalid input string
    def test_neg_invalid_input_str(self): #T_02a_8
        self.assertEqual(classifyTriangle(1,1,"d"),"InvalidInput", "(1,1,d) is Invalid Input")

    #test case - invalid input
    def test_neg_invalid_input(self): #T_02a_9
        self.assertEqual(classifyTriangle(True,["i","j"],None),"InvalidInput", "(True,['i','j'],None) is Invalid Input")

    #test case - Equilateral - Triangle can have sides with length in float values
    def test_neg_equilateral(self): #T_02a_10
        self.assertEqual(classifyTriangle(1.1,1.1,1.1),"Equilateral", "(1.1,1.1,1.1) is an Equilateral triangle")

    #test case - does not satisfy basic triangle property
    def test_neg_isosceles(self): #T_02a_11
        self.assertEqual(classifyTriangle(2,5,2),"NotATriangle", "(2,5,2) is not a Triangle")

    #test case - few negative inputs
    def test_neg_int_values_2(self): #T_02a_12
        self.assertEqual(classifyTriangle(2,5,-2),"InvalidInput", "(2,5,-2) is Invalid Input")

    #test case - max permitted value
    def test_neg_max_values(self): #T_02a_13
        self.assertEqual(classifyTriangle(200,200,200),"InvalidInput", "(200,200,200) is Invalid Input")

    #test case - exceed max permitted value
    def test_neg_exceed_max_values(self): #T_02a_14
        self.assertEqual(classifyTriangle(201,220,2),"InvalidInput", "(201,220,2) is Invalid Input")

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()

