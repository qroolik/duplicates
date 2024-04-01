# jpgi o tej samej rozdzielczości
# Im MSE jest większe tym obrazki bardziej się różnią - duplikaty na 99% to przedział od 0 do 0.5
# Im SSIM jest bliżej 1 tym są bardziej podobne
# jak skalować obrazy to tylko przy zachowaniu aspect ratio
# DO ZROBIENIA - import danych z excela

from PIL import Image
import numpy as np
import os
import csv
images_to_compare = [] # lista mieszkań do przeróbki na grayscale z excela - ścieżki

print('Wpisz id inwestycji: ')

inv_id = input()
path = 'C:/Users/rafal/OneDrive/Pulpit/' + inv_id

for f in os.listdir(path):
    if f.endswith('.jpg'):
        images_to_compare.append(f)

# print(images_to_compare)

images_grayscale = [] #lista img w grayscale - przy założeniu że mieszkania są przesortowane po metrażu

# img_size = (2000, 2000)

for img in images_to_compare:
    image = Image.open(path + '/' + img)
    # image = image.resize(img_size)
    image_gray = image.convert('L')
    images_grayscale.append(image_gray)

# img1 = np.array(images_grayscale[8])
# img2 = np.array(images_grayscale[9])
# mse_error = np.mean((img1 - img2)**2)

def mse_error(imgA, imgB):
    # err = np.sum((imgA.astype('float') - imgB.astype('float'))**2)
    # err /= float(imgA.shape[0]*imgB.shape[1])
    err = np.mean((imgA - imgB)**2)
    return err

img1 = np.array(images_grayscale[0])

duplicates = []
list = []
count = 0

for i in images_grayscale[1:]:
    
    img2 = np.array(i)
    mse = mse_error(img1, img2)
    list.append(images_to_compare[count])
    count+=1
    # print(list)
    if mse > 0.5:
        duplicates.append(list)
        list = []
        img1 = img2
    
list.append(images_to_compare[-1])
duplicates.append(list)

# print(duplicates)

with open(f'duplicates{inv_id}.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=';')
    for row in duplicates:
        writer.writerow(row)
    print('DONE')



    
    



 









   



