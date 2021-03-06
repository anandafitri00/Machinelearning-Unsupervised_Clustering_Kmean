# -*- coding: utf-8 -*-
"""Ananda Fitri Karimah_1301170774_UNSUPERVISED.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1LgLFJs6hBY0LfkiKDOmpG04ktsHik-ah

Ananda Fitri Karimah (1301170774)

IFIK - 41 - 01

DATASET : FIFA20

# 1. Data Prepocessing & Data Exploring 

Bersihkan data yang akan dipakai untuk clustering. Disini saya memakai hanya dua buah atribut saja yaitu height_cm dan weight_kg. Lalu saya ambil atribut yang akan saya gunakan ke dataframe yang baru. Lalu apabila ada missing value maka saya drop/replace dengan mean. 

Namun karena di data ini tidak ada missing value maka data tidak ada yang di drop
"""

#import pandas untuk membaca data
import pandas as pd
#import math untuk bisa menggunakan akar atau sqrt
from math import sqrt
#import numpy untuk menggunakan mean
import numpy as np 
#import copy untuk mengcopy fungsi
import copy
#import random untuk memakai randint 
from random import randint
#import matplotlib untuk bisa memnunculkan model
import matplotlib.pyplot as plt

#upload dataset ke google collab 
  from google.colab import files
  uploaded = files.upload()

#import io untuk read dataset
  import io
  #baca dataset
  data = pd.read_csv(io.BytesIO(uploaded['fifa20.csv']))

#tampilkan dataset
data

#ambil dataset yang ingin di cluster
data = (data[['height_cm', 'weight_kg']])
#tampilkan 5 data awal
data.head()

#cek apakah ada missing value, jika ada relace dengan mean atau drop row tersebut
data.isnull().sum()

#inisialisasi banyaknya centroid 
K = 2

#ubah nama kolom menjadi x dan y
data.rename(columns={"height_cm" : "x","weight_kg":"y"}, inplace = True)
#tampilkan dataframe
data

#mendapatkan centroid iterasi pertama dengan merandom angka yang ada diantara dataset yang telah dipilih
lx= []
ly =[]
lxy=[]
#untuk centroid awal ambil 1 nilai acak dari data frame
for i in range (K)  :
  #ambil satu ddata secara acak dengan 
  randx = randint(156,206)
  randy = randint(50,110)
  lx.append(randx)
  ly.append(randy)
lxy.append(lx)
lxy.append(ly)
print(lxy)

#untuk melihat centroid yang sudah terbentuk, saya memakai matplotlib
fig = plt.figure(figsize=(5,5))
#diinisialisasikan data x dan y dengan warna abu2 
#agar terlihat mana yang sudah terupdate dan yang mana yang belum  
plt.scatter(data['x'], data['y'], color='gray')
#masukkan cetroid yang sudah dirandom sebelumnya dengan warna-warna yang sudah
#diinisialisasikan sebelumnya 
for i in range(len(lx)):
     #plot lalu beri warna 
    # plt.scatter(*awal_centroid[i], color = sign[i])
    if i== 1 :
      plt.scatter(lx[i], ly[i], color = 'red')
    else :
      plt.scatter(lx[i], ly[i], color = 'blue')

#menghitung jarak ke masing-masing centroid
clust1 = []
clust2 = []
for i in range (18277) :
  formula1 = sqrt((data['x'][i]-lx[0])**2+(data['y'][i]-ly[0])**2) #untuk C1 
  formula2 = sqrt((data['x'][i]-lx[1])**2+(data['y'][i]-ly[1])**2) #untuk C2
  clust1.append(formula1)
  clust2.append(formula2) 
print(clust1)
print(clust2)

#untuk menentukan pilihan apakah masuk cluster 1 atau 2 
clustfin = [] #list untuk decision apakah dia masuk cluster 1 atau 2
rowc1 = []
rowc2 = []
for i in range(len(clust1)):
  if clust1[i] < clust2[i] : #jika lebih dekat dengan 1 akan di append 1
    clustfin.append(1) 
    rowc1.append(i)
  else : #jika lebih dekat dengan 2/ nilai sama akan di append 2
    clustfin.append(2)
    rowc2.append(i)
print(clustfin)
print(rowc1)
print(rowc2)

#untuk melihat centroid yang sudah terbentuk, saya memakai matplotlib
fig = plt.figure(figsize=(5,5))
#diinisialisasikan data x dan y dengan warna abu2 
#agar terlihat mana yang sudah terupdate dan yang mana yang belum  
for i in range(len(lx)):
     #plot lalu beri warna 
    if i== 1 :
      plt.scatter(lx[i], ly[i], color = 'red')
    else :
      plt.scatter(lx[i], ly[i], color = 'blue')
#masukkan cetroid yang sudah dirandom sebelumnya dengan warna-warna yang sudah
#diinisialisasikan sebelumnya 
for i in range(len(clustfin)):
     #plot lalu beri warna 
    # plt.scatter(*awal_centroid[i], color = sign[i])
    if clustfin[i]==1 :
      plt.scatter(data['x'][i], data['y'][i], color = 'red', edgecolor = 'black')
    elif clustfin[i]==2 :
      plt.scatter(data['x'][i], data['y'][i], color = 'blue', edgecolor = 'black')

#fungsi untuk mencari mean dari data yang masuk di cluster 1 untuk nantinya di cari kembali centroidnya
def meanc1(rowc1, data):
  itx = 0
  ity = 0
  updatec1 = []
  for i in range (len(rowc1)):
    itx = itx + data.iloc[rowc1[i], 0]
    ity = ity + data.iloc[rowc1[i], 1]
  sumx = itx/len(rowc1)
  sumy = ity/len(rowc1)
  updatec1.append(sumx)
  updatec1.append(sumy)
  return updatec1

#fungsi untuk mencari mean dari data yang masuk di cluster 2 untuk nantinya di cari kembali centroidnya
def meanc2(rowc2, data):
  itx = 0
  ity = 0
  updatec2 = []
  for i in range (len(rowc2)):
    itx = itx + data.iloc[rowc2[i], 0]
    ity = ity + data.iloc[rowc2[i], 1]
  sumx = itx/len(rowc2)
  sumy = ity/len(rowc2)
  updatec2.append(sumx)
  updatec2.append(sumy)
  return updatec2

ratac1 = meanc1(rowc1, data)
ratac2 = meanc2(rowc2, data)
print(ratac1)
print(ratac2)

#untuk melihat centroid yang sudah terbentuk, saya memakai matplotlib
fig = plt.figure(figsize=(5,5))
#diinisialisasikan data x dan y dengan warna abu2 
#agar terlihat mana yang sudah terupdate dan yang mana yang belum  
plt.scatter(data['x'], data['y'], color='gray')
#masukkan cetroid yang sudah dirandom sebelumnya dengan warna-warna yang sudah
#diinisialisasikan sebelumnya 
for i in range(len(ratac1)):
     #plot lalu beri warna 
    if i==0 :
      plt.scatter(ratac1[0], ratac1[1], color = 'red')
    elif i==1 :
      plt.scatter(ratac2[0], ratac2[1], color = 'blue')

oldlxy = lxy
for i in range (len(lxy)):
  lxy.pop()
lxy.append(ratac1)
lxy.append(ratac2)
print(lxy)

oldlx = lx
oldly = ly
oldclust1 = clust1
oldclust2 = clust2 
for i in range (len(lx)):
  lx.pop()
  ly.pop()
for i in range (len(clust1)):
  clust1.pop()
for i in range (len(clust2)):
  clust2.pop()

lx.append(lxy[0])
ly.append(lxy[1])

for i in range (18277) :
  formula1 = sqrt((data['x'][i]-lx[0][0])**2+(data['y'][i]-ly[0][1])**2) #untuk C1 
  formula2 = sqrt((data['x'][i]-lx[0][1])**2+(data['y'][i]-ly[0][1])**2) #untuk C2
  clust1.append(formula1)
  clust2.append(formula2) 
print(clust1)
print(clust2)

oldclustfin = clustfin
oldrowc1 = rowc1
oldrowc2 = rowc2
for i in range (len(clustfin)):
  clustfin.pop()
for i in range (len(rowc1)):
  rowc1.pop()
for i in range (len(rowc1)):
  rowc1.pop()

#untuk menentukan pilihan apakah masuk cluster 1 atau 2 
for i in range(len(clust1)):
  if clust1[i] < clust2[i] : #jika lebih dekat dengan 1 akan di append 1
    clustfin.append(1) 
    rowc1.append(i)
  else : #jika lebih dekat dengan 2 / nilai sama akan di append 2
    clustfin.append(2)
    rowc2.append(i)
print(clustfin)
print(rowc1)
print(rowc2)

#untuk melihat centroid yang sudah terbentuk, saya memakai matplotlib
fig = plt.figure(figsize=(5,5))
#diinisialisasikan data x dan y dengan warna abu2 
#agar terlihat mana yang sudah terupdate dan yang mana yang belum  
for i in range(len(lx)):
     #plot lalu beri warna 
    if i == 1 :
      plt.scatter(lx[i], ly[i], color = 'red')
    else :
      plt.scatter(lx[i], ly[i], color = 'blue')
#masukkan cetroid yang sudah dirandom sebelumnya dengan warna-warna yang sudah
#diinisialisasikan sebelumnya 
for i in range(len(clustfin)):
     #plot lalu beri warna 
    # plt.scatter(*awal_centroid[i], color = sign[i])
    if clustfin[i]==1 :
      plt.scatter(data['x'][i], data['y'][i], color = 'red', edgecolor = 'black')
    elif clustfin[i]==2 :
      plt.scatter(data['x'][i], data['y'][i], color = 'blue', edgecolor = 'black')

