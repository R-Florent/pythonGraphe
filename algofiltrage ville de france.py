import geopandas as gpd
import pandas as pd
from shapely.geometry import Point

# Lire le fichier CSV avec les coordonnées des villes
villes_df = pd.read_csv('villes_france.csv')

# Filtrer les villes en fonction des conditions de latitude et longitude
villes_filtrees = villes_df[
    (villes_df['latitude'] >= 41) & (villes_df['latitude'] <= 51.5) &
    (villes_df['longitude'] >= -5) & (villes_df['longitude'] <= 8.2)
]

# Créer les objets géographiques Point à partir des colonnes latitude et longitude
geometry = [Point(xy) for xy in zip(villes_filtrees['longitude'], villes_filtrees['latitude'])]

# Créer un GeoDataFrame à partir des données et des objets géographiques
gdf = gpd.GeoDataFrame(villes_filtrees)

# Écrire le GeoDataFrame dans un fichier CSV
gdf.to_csv('villes_france_metropolitaine.csv', index=False)
