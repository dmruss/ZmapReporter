import unittest
from src.parser import *
from src.reporter import *
import json
import pandas as pd


# class TestParser(unittest.TestCase):

#     def test_constructor(self):
#         parser = Parser('/home/guest/Desktop/zmaptemp/port80grabs/202205011231_p80/')
#         self.assertEqual(parser.working_dir, '/home/guest/Desktop/zmaptemp/port80grabs/202205011231_p80/')

#     def test_load_banners(self): 
#         parser = Parser('/home/guest/Desktop/zmaptemp/port80grabs/202205011231_p80/')
#         loaded_banners = parser.load_banners()
#         self.assertEqual(str(loaded_banners['imap'][0]), "{'ip': '198.1.123.24', 'data': {'imap': {'status': 'success', 'protocol': 'imap', 'result': {'banner': '* OK [CAPABILITY IMAP4rev1 SASL-IR LOGIN-REFERRALS ID ENABLE IDLE NAMESPACE LITERAL+ STARTTLS AUTH=PLAIN AUTH=LOGIN] Dovecot ready.\\r\\n'}, 'timestamp': '2022-04-30T15:18:22-06:00'}}}")
    
#     def test_parse_banners(self):
#         parser = Parser('/home/guest/Desktop/zmaptemp/port80grabs/202205011231_p80/')
#         loaded_banners = parser.load_banners()
#         parsed_banners = parser.parse_banners(loaded_banners)
#         self.assertEqual(len(parsed_banners['ftp']), 50)
#         self.assertEqual(len(parsed_banners['http']), 50)
#         self.assertEqual(len(parsed_banners['ssh']), 50)
#         self.assertEqual(len(parsed_banners['tls']), 50)
#         self.assertEqual(len(parsed_banners['mysql']), 50)
#         self.assertEqual(len(parsed_banners['geo']), 50)


class TestReporter(unittest.TestCase):

    def test_geo(self):
        geo_test_data = pd.read_csv('./tests/data/geotest.csv', index_col='ip_address')
        banner_dfs = {'geo': geo_test_data}
        # parser = Parser('/home/guest/Desktop/zmaptemp/port80grabs/202205011231_p80/')
        # loaded_banners = parser.load_banners()
        # parsed_banners = parser.parse_banners(loaded_banners)
        plot_map(banner_dfs)
        self.assertEqual(1,0)


if __name__ == '__main__':
    unittest.main()