
import unittest
import StringCal

class TestStringCal(unittest.TestCase):
    
    def test_Empty_String(self):
        result=StringCal.calculator("")
        self.assertEqual(result,0)

