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
        return bannerdf_dict

    
    def parse_banners(self, bannerdf_dict):
        '''
        Parse loaded banners to pandas dataframes with select features

        returns: dict of dataframes
        '''
        def parse_ftp_banner(bannerdf_dict):
            ftp_software_types = ['cerberus', 'completeftp', 'crushftp', 'filezilla', 'microsoft', 'sysax', 'war', 'giftpd', 'proftpd', 'pure-ftpd', 'vsftpd', 'wu-ftpd']
            ftp_responses = bannerdf_dict['ftp']
            ip_addresses = []
            success = []
            software_names = []
            for resp in ftp_responses:
                ip_addresses.append(resp['ip'])
                status = resp['data']['ftp']['status']
                if status == 'success':
                    success.append(True)
                    #attempt to find software name in banner
                    try:
                        banner = resp['data']['ftp']['result']['banner'].lower()
                        found = False
                        for sw_name in ftp_software_types:
                            if sw_name in banner:
                                software_names.append(sw_name)
                                found=True
                                break
                        if not found:
                            software_names.append('Not Found')
                    except Exception as e:
                        print(e)
                        software_names.append(None)
                else:
                    software_names.append(None)
                    success.append(False)
            ftp_df = pd.DataFrame()
            ftp_df['ip_address'] = ip_addresses
            ftp_df = ftp_df.set_index('ip_address')
            ftp_df['success'] = success
            ftp_df['ftp_software'] = software_names
            return ftp_df

        ftp_df = parse_ftp_banner(bannerdf_dict)
        