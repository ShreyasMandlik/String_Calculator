
from cgitb import reset
import pytest
import unittest
import StringCal

class TestStringCal(unittest.TestCase):
    
    def test_Empty_String(self):
        result=StringCal.calculator("")
        self.assertEqual(result,0)


    def test_Single_Numeric_String(self):
        result=StringCal.calculator("1")
        self.assertEqual(result,1)

    def test_More_than_one_Numeric_Number_String_having_Delimiter(self):
        result=StringCal.calculator("//;\n1;2")
        self.assertEqual(result,3)

        result1=StringCal.calculator("//1,2,3")
        self.assertEqual(result1,6)

    def test_Negative_numbers(self):
        result=StringCal.calculator("-42")
        self.assertEqual(result,"negative not allowed")