#import to zmapReporter
#create viz from dataframes

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import geopandas as gpd
from shapely.geometry import Point, Polygon
from matplotlib.backends.backend_pdf import PdfPages


class Plotter:

    def __init__(self, output_directory):
        self.output_dir = output_directory
        self.pp = PdfPages(self.output_dir+'/out.pdf')

    def plot_map(self, banner_dfs):
        df = banner_dfs['geo']
        crs = {'init': 'epsg:4396'}
        geometry = [Point(xy) for xy in zip( df['longitude'], df['latitude'])]
        geo_df = gpd.GeoDataFrame(df, crs=crs, geometry=geometry)
        print(geo_df.head())
        world_map = gpd.read_file('./src/WB_countries_Admin0_lowres.geojson')
        fig, ax = plt.subplots(figsize=(15,15))
        world_map.plot(ax=ax, alpha=0.4)
        geo_df.plot(ax=ax, markersize=40)        
        self.pp.savefig(fig)
        # plt.show()


    def plot_success(self, banner_dfs):
        
        #get percent success for each key in banner dfs
        #then create pie charts for each
        fig, ax = plt.subplots(1, 5)
        fig.set_size_inches(15, 5)
        fig.tight_layout()
        col = 0
        for grab_type in banner_dfs.keys():
            if grab_type == 'geo': continue
            ax[col].pie(banner_dfs[grab_type]['success'].value_counts())
            ax[col].set_title(grab_type)
            col += 1
        self.pp.savefig()
        plt.show()
       

    def close_pp(self):
        self.pp.close()

    def report(self, banner_dfs):
        self.plot_map(banner_dfs)
        self.plot_success(banner_dfs)
        self.close_pp()