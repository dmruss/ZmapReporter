#import to zmapReporter
#parse banner outputs to dataframes
import pandas as pd
import numpy as np
import os
import json


class Parser:

    def __init__(self, working_dir_path):
        self.working_dir = working_dir_path

    def load_banners(self):
        '''
        Load banner json files generated from zgrab

        returns: loaded banners
        '''
        bannerdf_dict = {}
        banner_dir = self.working_dir+'/banners'
        #load http, ssh,, ftp, imap, telnet, tls, smtp, and mysql banner.json files
        print('Listing files in:', banner_dir)
        file_list = os.listdir(banner_dir)
        print('Banners:', file_list)

        for banner_name in file_list:
            grab_type = banner_name.split('.')[0]
            file_path = banner_dir+'/'+banner_name
            request_list = []
            print('Reading json:', file_path)
            with open(file_path, 'r') as f:
                for line in f:
                    try:
                        line_json = json.loads(line)
                        request_list.append(line_json)
                    except Exception as e:
                        continue
            
            bannerdf_dict[grab_type] = request_list
           
            print(grab_type)
            print(bannerdf_dict[grab_type][0])
            print()

    
    def parse_banners(self):
        '''
        Parse loaded banners to pandas dataframes with select features

        returns: dict of dataframes
        '''

