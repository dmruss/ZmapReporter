#import to zmapReporter
#run zmap/zgrab
import os
import datetime
import src.parser as parser
import src.reporter as reporter
import src.nmap_script as nmap
import pandas as pd


class ZmapReporter:

    def __init__(self, port, sample, scan_size):
        self.port = port
        self.sample = sample
        self.scan_size = scan_size
        self.working_dir = os.getcwd() + '/' + 'output'
        self.datetime = datetime.datetime.now().strftime("%Y%m%d-%H%M")
        working_folder = self.datetime + '-' + str(self.port)
        self.working_dir = self.working_dir+'/'+working_folder
        self.temp_dir = self.working_dir+'/temp'
        self.ip_address_file = self.temp_dir+'/ipaddresses.csv'
        self.banner_temp = self.temp_dir+'/banners'
        self.nmap_temp = self.temp_dir+'/nmapscans'
        os.system('mkdir {}'.format(self.working_dir))
        os.system('mkdir {}'.format(self.temp_dir))  
        os.system('mkdir {}'.format(self.banner_temp))  
        os.system('mkdir {}'.format(self.nmap_temp))
        os.system('mkdir {}'.format(self.working_dir+'/banners'))
        os.system('mkdir {}'.format(self.working_dir+'/nmapscans'))
        os.system('mkdir {}'.format(self.working_dir+'/final_output'))
        self.zgrab_dir = '~/go/pkg/mod/github.com/zmap/zgrab2@v0.1.7/zgrab2'


    def zmap(self):
        os.system('sudo zmap -p {} -N {} -o {}'.format(str(self.port), str(self.sample), self.ip_address_file))

    def zgrab_scans(self):
        grab_types = ['http', 'smtp', 'ftp', 'mysql', 'ssh', 'tls']
        for grab_type in grab_types:
            out_file_path = self.banner_temp + '/{}.json'.format(grab_type)
            os.system('cat {} | {} {} -o {}'.format(self.ip_address_file, self.zgrab_dir, grab_type, out_file_path))

    def parse_banners(self):
        banner_parser = parser.Parser(self.temp_dir)
        loaded_banners = banner_parser.load_banners()
        parsed_banners = banner_parser.parse_banners(loaded_banners)
        for banner_type in parsed_banners.keys():
            parsed_banners[banner_type].to_csv(self.working_dir+'/banners/{}.csv'.format(banner_type))
        return parsed_banners

    def nmap_scans(self, banner_dfs):
        nmap_ = nmap.NmapScanner(self.nmap_temp, banner_dfs, self.sample, self.scan_size)
        nmap_.http_scan()
        nmap_.smtp_scan()
        nmap_.smb_scan()
        nmap_.proftp_scan()
        nmap_.vsftpd_scan()
        nmap_.authspoof_scan()

    def nmap_parser(self):
        nmap_parser = parser.Parser(self.temp_dir)
        print('HERE')
        scan_dict = nmap_parser.parse_nmap_scans()
        for scan_type in scan_dict.keys():
            scan_dict[scan_type].to_csv(self.working_dir+'/nmapscans/{}.csv'.format(scan_type))


def runZmap(a, b):
    os.system("cd")
    os.system("sudo zmap -p " + str(a) + " -N " + str(b) + "| ztee maybeSSH.csv | ~/go/pkg/mod/github.com/zmap/zgrab2@v0.1.7/zgrab2 ssh -o banners.json")
