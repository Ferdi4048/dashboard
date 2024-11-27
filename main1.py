import os
import streamlit as st
from PIL import Image

# Dossiers disponibles
folders = {
    'Cluster': 'Cluster',
    'Cluster1': 'Cluster1',
    'Cluster2': 'Cluster2',
    'GoodCluster': 'GoodCluster',
    'GoodCluster1': 'GoodCluster1',
    'GoodCluster2': 'GoodCluster2'
}

# Vérification de l'existence des dossiers
for folder in folders.values():
    if not os.path.exists(folder):
        st.warning(f"Le dossier {folder} n'est pas trouvé.")

# Fonction pour afficher l'image
def display_image(cluster_folder, goodcluster_folder, selected_image):
    cluster_image_path = os.path.join(cluster_folder, selected_image)
    goodcluster_image_path = os.path.join(goodcluster_folder, selected_image)
    
    # Vérification si l'image existe dans 'goodcluster'
    if os.path.exists(goodcluster_image_path):
        # Affichage des deux images côte à côte avec Streamlit
        col1, col2 = st.columns(2)
        
        # Calcul de la taille de l'image multipliée par 10
        cluster_image = Image.open(cluster_image_path)
        goodcluster_image = Image.open(goodcluster_image_path)
        
        # Obtenir les dimensions de l'image et les multiplier par 10
        cluster_width, cluster_height = cluster_image.size
        goodcluster_width, goodcluster_height = goodcluster_image.size
        
        # Affichage de l'image du dossier 'cluster' avec taille augmentée
        with col1:
            st.image(cluster_image_path, caption=f"Cluster: {selected_image}", width=cluster_width*10)
        
        # Affichage de l'image du dossier 'goodcluster' avec taille augmentée
        with col2:
            st.image(goodcluster_image_path, caption=f"GoodCluster: {selected_image}", width=goodcluster_width*10)
        
    else:
        st.warning(f"L'image {selected_image} n'existe pas dans '{goodcluster_folder}'.")

# Sélection des dossiers avec Streamlit
cluster_choice = st.selectbox('Choisir un dossier Cluster:', ['Cluster', 'Cluster1', 'Cluster2'])
goodcluster_choice = st.selectbox('Choisir un dossier GoodCluster:', ['GoodCluster', 'GoodCluster1', 'GoodCluster2'])

# Sélection des images disponibles dans le dossier choisi
cluster_folder = folders[cluster_choice]
goodcluster_folder = folders[goodcluster_choice]

# Liste des images disponibles dans le dossier 'cluster'
cluster_images = [f for f in os.listdir(cluster_folder) if os.path.isfile(os.path.join(cluster_folder, f))]

# Sélection de l'image à afficher
selected_image = st.selectbox('Sélectionner une image:', cluster_images)

# Affichage de l'image
if selected_image:
    display_image(cluster_folder, goodcluster_folder, selected_image)
