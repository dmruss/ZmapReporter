#import to zmapReporter
#create viz from dataframes

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import geopandas as gpd
import seaborn as sns
from shapely.geometry import Point
from matplotlib.backends.backend_pdf import PdfPages
from mpl_toolkits.axes_grid1 import make_axes_locatable


class Plotter:

    def __init__(self, output_directory, port, sample):
        self.output_dir = output_directory
        self.pp = PdfPages(self.output_dir+'/out.pdf')
        # self.fig, self.ax = plt.subplots(5,5,figsize=(50,50))
        self.fig = plt.figure(figsize=(60,40))
        self.grid_size = (6,8)
        plt.rcParams["font.size"] = "30"
        self.fig.suptitle('Zmap/Zgrab scan of port {} with sample size {}'.format(port, sample), fontsize=50)
        sns.set_style("whitegrid")
        sns.set_palette('deep')

    def plot_map(self, banner_dfs):
        df = banner_dfs['geo']
        crs = {'init': 'epsg:4396'}
        geometry = [Point(xy) for xy in zip( df['longitude'], df['latitude'])]
        geo_df = gpd.GeoDataFrame(df, crs=crs, geometry=geometry)
        print(geo_df.head())
        world_map = gpd.read_file('./src/WB_countries_Admin0_lowres.geojson')
        # world_map = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
        ax0 = plt.subplot2grid(self.grid_size, (0,0), colspan=3, rowspan=2)
        # divider = make_axes_locatable(ax0)
        # cax = divider.append_axes("right", size="5%", pad=0.1)
        # ax0.figure(figsize=(10,10))
        # ax0.set_xlim([20, 80])
        # ax0.set_ylim([10, 50])
        ax0.set_aspect('equal')
        world_map.plot(ax=ax0, alpha=0.4)
        ax0.set_axis_off()
        ax0.set_title('Ip Address Geolocation')

        geo_df.plot(ax=ax0, markersize=200, c='darkorange')        
        # self.pp.savefig(fig)
        # plt.show()


    def plot_success(self, banner_dfs):
        
        #get percent success for each key in banner dfs
        #then create pie charts for each
        # fig, ax = plt.subplots(1, 5)
        # fig.set_size_inches(15, 5)
        # fig.tight_layout()
        col = 1
        for grab_type in banner_dfs.keys():
            if grab_type == 'geo': continue
            ax = plt.subplot2grid(self.grid_size, (2,col))
            labels = banner_dfs[grab_type]['success'].value_counts().keys()
            if labels[1] == True: 
                labels = ['No Connection', 'Connected']
                values = banner_dfs[grab_type]['success'].value_counts()
            else: 
                labels = ['No Connection', 'Connected']
                values = [banner_dfs[grab_type]['success'].value_counts()[1], banner_dfs[grab_type]['success'].value_counts()[0]]
            ax.pie(values, labels=labels, autopct='%.0f%%')
            
            ax.set_title('{} Percent Connection'.format(grab_type.upper()))
            col += 1
        # plt.show()

    def plot_http_server(self, banner_dfs):
        # fig, ax = plt.subplots(figsize=(15,15))
        ax = plt.subplot2grid(self.grid_size, (3,0), colspan=4)
        http_df = banner_dfs['http']['server'].dropna()
        ax.bar(http_df.value_counts().keys(), height=http_df.value_counts())
        ax.set_title('Web Servers')
        plt.setp(ax.get_xticklabels(), rotation=30, horizontalalignment='right')
        # self.pp.savefig()

    def plot_ssh_software(self, banner_dfs):
        ssh_df = banner_dfs['ssh']
        # fig, ax = plt.subplots(figsize=(15,15))
        ax = plt.subplot2grid(self.grid_size, (5,0), colspan=4)
        ax.bar(ssh_df['software'].dropna().value_counts().keys(), height=ssh_df['software'].dropna().value_counts())
        ax.set_title('SSH Servers')
        # self.pp.savefig()

    def plot_countries(self, banner_dfs):
        geo_df = banner_dfs['geo']
        ax = plt.subplot2grid(self.grid_size, (0,3), colspan=2, rowspan=2)
        ax.bar(geo_df['country'].value_counts().keys(), height=geo_df['country'].value_counts())
        ax.set_title('Ip Address by Country')
        plt.setp(ax.get_xticklabels(), rotation=30, horizontalalignment='right')

    def plot_ftp_software(self, banner_dfs):
        ftp_df = banner_dfs['ftp']
        ax = plt.subplot2grid(self.grid_size, (5,4), colspan=4)
        ax.bar(ftp_df['ftp_software'].value_counts().keys(), height=ftp_df['ftp_software'].value_counts())
        ax.set_title('FTP Servers')

    def plot_tls_company(self, banner_dfs):
        tls_df = banner_dfs['tls']
        ax = plt.subplot2grid(self.grid_size, (3,4), colspan=4)
        ax.bar(tls_df['company'].value_counts().keys(), height=tls_df['company'].value_counts())
        ax.set_title('Company on TLS Certificate')
        plt.setp(ax.get_xticklabels(), rotation=30, horizontalalignment='right')

    def plot_nmap_scans(self, nmap_dict):
        ax = plt.subplot2grid(self.grid_size, (0,5), rowspan=2, colspan=3)
        vals = []
        for scan_type in nmap_dict.keys():
            df = nmap_dict[scan_type]
            counts = df[df.keys()[0]].value_counts()
            print()
            print(counts)
            print()
            if len(counts.keys()) > 1:
                if counts.keys()[0] == True:
                    vals.append(counts[0])
                else:
                    vals.append(counts[1])
            else:
                vals.append(0)
        ax.bar(nmap_dict.keys(), height = vals)
        ax.set_title('Malware Scan Detection')


    def close_pp(self):
        self.fig.tight_layout()
        self.fig.subplots_adjust(wspace=0.5, hspace=.6)
        self.fig.subplots_adjust(top=.9)
        self.pp.savefig()
        self.pp.close()

    def report(self, banner_dfs, nmap_dict):
        self.plot_map(banner_dfs)
        self.plot_countries(banner_dfs)
        self.plot_success(banner_dfs)
        self.plot_http_server(banner_dfs)
        self.plot_ssh_software(banner_dfs)
        self.plot_ftp_software(banner_dfs)
        self.plot_tls_company(banner_dfs)
        self.plot_nmap_scans(nmap_dict)
        self.close_pp()