#import to zmapReporter
#create viz from dataframes

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import geopandas as gpd
from shapely.geometry import Point, Polygon

def plot_map(banner_dfs):
    df = banner_dfs['geo']
    crs = {'init': 'epsg:4396'}
    geometry = [Point(xy) for xy in zip( df['longitude'], df['latitude'])]
    geo_df = gpd.GeoDataFrame(df, crs=crs, geometry=geometry)
    print(geo_df.head())
    world_map = gpd.read_file('./src/WB_countries_Admin0_lowres.geojson')
    fig, ax = plt.subplots(figsize=(15,15))
    world_map.plot(ax=ax, alpha=0.4)
    geo_df.plot(ax=ax, markersize=40)
    plt.show()


