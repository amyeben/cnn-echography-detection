#!/usr/bin/env python
# coding: utf-8

# In[4]:


#Importation librarie 

import numpy as np
import tensorflow
import cv2 as cv
 


# In[6]:


import cv2
import os

import cv2
import os

# Dossier contenant les vidéos
base_dir = "/Users/chirine/DEEP LEARNING ING5/TP_Video/train"
output_base_dir = "output_images"

# Paramètres pour le rectangle centré
rect_width = 1500  # Largeur du rectangle centré
rect_height = 1500  # Hauteur du rectangle centré
num_images = 20    # Nombre d'images à extraire par vidéo

# Parcourir les sous-dossiers
for label in ["no_pregnancy", "pregnancy"]:
    video_folder = os.path.join(base_dir, label)
    output_folder = os.path.join(output_base_dir, label)
    os.makedirs(output_folder, exist_ok=True)
    
    # Parcourir chaque fichier vidéo dans le sous-dossier
    for video_name in os.listdir(video_folder):
        video_path = os.path.join(video_folder, video_name)
        
        print(f"Traitement de la vidéo : {video_path}")
        
        # Ouvrir la vidéo
        cap = cv2.VideoCapture(video_path)
        total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
        
        # Calcul de l'intervalle pour extraire 20 images de chaque vidéo
        interval = max(total_frames // num_images, 1)
        image_count = 0
        
        # Extraire les images
        while cap.isOpened() and image_count < num_images:
            frame_position = image_count * interval
            cap.set(cv2.CAP_PROP_POS_FRAMES, frame_position)
            
            # Lire la frame
            ret, frame = cap.read()
            if not ret:
                print(f"Fin de la vidéo ou problème de lecture à la frame {frame_position}.")
                break
            
            # Dimensions de la frame
            frame_height, frame_width = frame.shape[:2]
            
            # Calculer les coordonnées du rectangle centré
            x1 = max((frame_width - rect_width) // 2, 0)
            y1 = max((frame_height - rect_height) // 2, 0)
            x2 = x1 + rect_width
            y2 = y1 + rect_height
            
            # Extraire et sauvegarder le rectangle centré
            cropped_image = frame[y1:y2, x1:x2]
            output_image_path = os.path.join(output_folder, f"{video_name}_img_{image_count + 1}.jpg")
            cv2.imwrite(output_image_path, cropped_image)
            
            print(f"Sauvegardé : {output_image_path}")
            image_count += 1

        # Libérer la vidéo après traitement
        cap.release()
        print(f"Traitement terminé pour la vidéo : {video_path}\n")

print("Extraction des images terminée pour toutes les vidéos.")


# In[ ]:




