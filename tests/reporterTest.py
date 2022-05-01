import unittest
from src.parser import *


class TestParser(unittest.TestCase):

    def test_constructor(self):
        parser = Parser('/home/guest/Desktop/zmaptemp/port80grabs/202205011231_p80/')
        self.assertEqual(parser.working_dir, '/home/guest/Desktop/zmaptemp/port80grabs/202205011231_p80/')

    def test_load_banners(self):
        cwd = os.getcwd()
        parser = Parser('/home/guest/Desktop/zmaptemp/port80grabs/202205011231_p80/')
        loaded_banners = parser.load_banners()
        self.assertEqual(1,0)
    
    def test_parse_banners(self):
        cwd = os.getcwd()
        parser = Parser('/home/guest/Desktop/zmaptemp/port80grabs/202205011231_p80/')
        parsed_banners = parser.parse_banners()

if __name__ == '__main__':
    unittest.main()