import unittest
from src.parser import *
import json


class TestParser(unittest.TestCase):

    def test_constructor(self):
        parser = Parser('/home/guest/Desktop/zmaptemp/port80grabs/202205011231_p80/')
        self.assertEqual(parser.working_dir, '/home/guest/Desktop/zmaptemp/port80grabs/202205011231_p80/')

    def test_load_banners(self):
        parser = Parser('/home/guest/Desktop/zmaptemp/port80grabs/202205011231_p80/')
        loaded_banners = parser.load_banners()
        self.assertEqual(str(loaded_banners['imap'][0]), "{'ip': '198.1.123.24', 'data': {'imap': {'status': 'success', 'protocol': 'imap', 'result': {'banner': '* OK [CAPABILITY IMAP4rev1 SASL-IR LOGIN-REFERRALS ID ENABLE IDLE NAMESPACE LITERAL+ STARTTLS AUTH=PLAIN AUTH=LOGIN] Dovecot ready.\\r\\n'}, 'timestamp': '2022-04-30T15:18:22-06:00'}}}")
    
    def test_parse_banners(self):
        parser = Parser('/home/guest/Desktop/zmaptemp/port80grabs/202205011231_p80/')
        loaded_banners = parser.load_banners()
        parsed_banners = parser.parse_banners(loaded_banners)
        self.assertEqual(1,0)

if __name__ == '__main__':
    unittest.main()