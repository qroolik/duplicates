# jpgi o tej samej rozdzielczości
# Im MSE jest większe tym obrazki bardziej się różnią - duplikaty na 99% to przedział od 0 do 0.5
# Im SSIM jest bliżej 1 tym są bardziej podobne
# jak skalować obrazy to tylko przy zachowaniu aspect ratio
# DO ZROBIENIA - import danych z excela

from PIL import Image
import numpy as np
import os
import csv
from itertools import combinations

images_to_compare = [] # lista mieszkań do przeróbki na grayscale z excela - ścieżki

print('Wpisz id inwestycji: ')

inv_id = input()
path = 'C:/Users/rafal/OneDrive/Pulpit/' + inv_id

for f in os.listdir(path):
    if f.endswith('.jpg'):
        images_to_compare.append(f)

images_grayscale = []

# img_size = (2000, 2000)

for img in images_to_compare:
    image = Image.open(path + '/' + img)
    # image = image.resize(img_size)
    image_gray = image.convert('L')
    images_grayscale.append(image_gray)

# img1 = np.array(images_grayscale[8])
# img2 = np.array(images_grayscale[9])
# mse_error = np.mean((img1 - img2)**2)
        
#liczenie mean squared error
def mse_error(imgA, imgB):
    np_img1 = np.array(imgA)
    np_img2 = np.array(imgB)

    mse = np.mean((np_img1 - np_img2)**2)
    return mse

#inicjowanie dict i setu
img_pairs = {}
img_added = set()

for img1_path, img2_path in combinations(images_to_compare, 2):

    img1 = images_grayscale[images_to_compare.index(img1_path)]
    img2 = images_grayscale[images_to_compare.index(img2_path)]
    
    mse = mse_error(img1, img2)

    if mse < 0.5 and img2_path not in img_pairs and img1_path not in img_added:
        if img1_path in img_pairs:
            img_pairs[img1_path].append(img2_path)
        else:
            img_pairs[img1_path] = [img2_path]
        img_added.add(img2_path)

print(img_pairs)

with open(f'duplicates{inv_id}.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter = ';')
    for key, value in img_pairs.items():
        row = [key] + value
        writer.writerow(row)
    print('DONE')



    
    



 









   



