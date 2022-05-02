#import to zmapReporter
#create viz from dataframes

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import geopandas as gpd
from shapely.geometry import Point, Polygon
from matplotlib.backends.backend_pdf import PdfPages


class Plotter:

    def __init__(self, output_directory):
        self.output_dir = output_directory

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
        pp = PdfPages(self.output_dir+'/out.pdf')
        pp.savefig(fig)
        pp.close()
        plt.show()


