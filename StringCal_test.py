
import unittest
import StringCal

class TestStringCal(unittest.TestCase):
    
    def test_Empty_String(self):
        result=StringCal.calculator("")
        self.assertEqual(result,0)

    def test_Single_Number_String(self):
        result=StringCal.calculator("1")
        self.assertEqual(result,1)

