import os

class NmapScanner:

    def __init__(self, working_dir_path, banner_dfs, sample, scan_size):
        self.banner_dfs = banner_dfs
        self.working_dir = working_dir_path
        if scan_size == 'small':
            self.scan_size = int(sample/5)
        elif scan_size == 'medium':
            self.scan_size = int(sample/10)
        elif scan_size == 'large':
            self.scan_size = int(sample/2)
        
        

    def http_scan(self):
        http_ips = self.banner_dfs['http'][self.banner_dfs['http']['success'] == True]
        if len(http_ips) > 0:
            count = 0
            while count <= self.scan_size:
                for ip_address in http_ips.index:
                    os.system('nmap -sV --script=http-malware-host {} -oN ./tests/data/nmapscans/http.txt --append-output'.format(ip_address))
                    count += 1

    def smtp_scan(self):
        http_ips = self.banner_dfs['http'][self.banner_dfs['http']['success'] == True]
        if len(http_ips) > 0:
            count = 0
            while count <= self.scan_size:
                for ip_address in http_ips.index:
                    os.system('nmap -sV --host-timeout 60s -script=smtp-strangeport {} -oN ./tests/data/nmapscans/smtp.txt --append-output'.format(ip_address))
                    count += 1
        
    def smb_scan(self):
        http_ips = self.banner_dfs['http'][self.banner_dfs['http']['success'] == True]
        if len(http_ips) > 0:
            count = 0
            while count <= self.scan_size:
                for ip_address in http_ips.index:
                    os.system('nmap -p 445 --host-timeout 60s {} -script=smb-double-pulsar-backdoor -oN ./tests/data/nmapscans/smb.txt --append-output'.format(ip_address))
                    count += 1
    def proftp_scan(self):
        ftp_ips = self.banner_dfs['ftp'][self.banner_dfs['ftp']['success'] == True]
        if len(ftp_ips) > 0:
            count = 0
            while count <= self.scan_size:
                for ip_address in ftp_ips.index:
                    os.system('nmap --script ftp-proftpd-backdoor -p 21 {} -oN ./tests/data/nmapscans/proftp.txt --append-output'.format(ip_address))
                    count += 1
            
    def vsftpd_scan(self):
        ftp_ips = self.banner_dfs['ftp'][self.banner_dfs['ftp']['success'] == True]
        if len(ftp_ips) > 0:
            count = 0
            while count <= self.scan_size.index:
                for ip_address in ftp_ips:
                    os.system('nmap --script ftp-vsftpd-backdoor -p 21 {} -oN ./tests/data/nmapscans/vsftp.txt --append-output'.format(ip_address))
                    count += 1
                    
    def authspoof_scan(self):
        tls_ips = self.banner_dfs['tls'][self.banner_dfs['tls']['success'] == True]
        if len(tls_ips) > 0:
            count = 0
            while count <= self.scan_size:
                for ip_address in tls_ips.index:
                    os.system('nmap -sV --script=auth-spoof {} -oN ./tests/data/nmapscans/auth.txt --append-output'.format(ip_address))
                    count += 1