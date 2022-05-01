import unittest
from src.parser import *

class TestParser(unittest.TestCase):

    def test_constructor(self):
        parser = Parser('/home/guest/Desktop/zmaptemp/port80grabs/')
        self.assertEqual(parser.working_dir, '/home/guest/Desktop/zmaptemp/port80grabs/')

    

if __name__ == '__main__':
    unittest.main()