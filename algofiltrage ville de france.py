import geopandas as gpd
import pandas as pd

# Définir les coordonnées des quatre points
sud_est = (41, 8.5)
sud_ouest = (42, -6)
nord_ouest = (51.5, -6)
nord_est = (51.5, 8.5)

# Créer les limites du polygone contenant la France métropolitaine
limites_france = gpd.GeoSeries([sud_est, sud_ouest, nord_ouest, nord_est]).convex_hull

# Lire le fichier CSV contenant les coordonnées des villes
villes_df = pd.read_csv('chemin_vers_le_fichier/villes.csv')

# Filtrer les coordonnées des villes en France métropolitaine
villes_france_metropolitaine = []
for index, ville in villes_df.iterrows():
    point = gpd.Point(ville['longitude'], ville['latitude'])
    if point.within(limites_france):
        villes_france_metropolitaine.append(ville)

# Créer un nouveau DataFrame avec les coordonnées filtrées
nouveau_df = pd.DataFrame(villes_france_metropolitaine)

# Écrire le nouveau DataFrame dans un fichier CSV
nouveau_df.to_csv('chemin_vers_le_fichier/villes_france_metropolitaine.csv', index=False)
