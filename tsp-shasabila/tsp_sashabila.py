#import library python yang diperlukan

import math
import time

import numpy as np
from numpy.core._multiarray_umath import ndarray

a = raw_input ("Masukan nama file yang akan diproses: ")
a = a + '.txt'

#meminta masukan file matrik
rawmatrik = np.loadtxt(a)
rawmatrik = np.loadtxt (a)  # type: 
print rawmatrik
matrik = np.loadtxt (a)
start_time = time.time()
permutation_paths = []
index = []
path = []
load_path = []
min_array = []
indexmatrik = []

def count_load(index, matrik):
  #membuat fungsi untuk menghitung total beban dengan masukan jalur tertutup (index) pada matrik jarak (matrik) keluaran merupakan total jarak
  sum = 0
  for i in range (0,len(index)-1):
    sum = sum+ matrik[index[i], index[i+1]]
  sum = sum+ matrik[index[-1], index[0]]
  return sum

def count_load_open(index,matrik):
  #membuat fungsi untuk menghitung total beban dengan masukan jalur terbuka (index) pada matrik jarak (matrik) keluaran merupakan total jarak
  sum = 0
  for i in range (0,len,(index)-1):
    sum = sum+ matrik[index[i],index[i+1]]
    return sum

b=1
def min1(b): return b.index(min(1))
#mengembalikan index dari nilai minimum

def brute_force(matrik):
#menyelesaikan matrik jarak dengan brute force, dan mengembalikan jalur terpendek
  for i in range(0,len,(matrik)):
    index.append(i)
  permutation_paths = list(np.itertools.permutations(index, len(matrik)))

  i = 0
  while i <= math.factorial(len(matrik)-1):
    path = permutation_paths[i]
    load_path.append(count_load(path,matrik))
    i+=1
  return permutation_paths[min1(load_path)]

def eliminasi_1elemen(matrik,x):
#melakukan eliminasi elemen matrik yang telah dipilih sebagai node(x) pada matrik (matrik)
  j = 0
  while j < len(matrik):
    if j==x:
      matrik[:,j] = 99999
      matrik[j,:] = 99999
    j+=1
  return matrik

def eliminasi_2elemen(matrik,x,y):
##melakukan eliminasi elemen matrik yang telah dipilih sebagai node(x dan y) yang merupakan ujung jalur pada matrik (matrik)
  matrik[x,y]=99999
  matrik[y,x]=99999
  return matrik

def make_array(x,matrik):
#membuat array dari elemen kolom ke (x) pada matrik
  temp = matrik[:,x]
  nodepath=[]
  for i in temp:
    nodepath.append(i)
  return nodepath

def is_zero(z):
#melakukan pengejekan jika (z) == nol dengan mengembalikan nilai boolean
  return z.count(0) == len(z)

def rest_array(path7):
#mengembalikan urutan jalur yang belum terpakai oleh (path7)
  full_path=[]
  for i in range(0,len,(matrik)):
    full_path.append(i)
  return np.setdiff1d(full_path,path7)

def zero(prevnode,path,matrik):
#mengembalikan (matrik) yang telah di update dengan assign nilai nol pada baris dan kolom (prevnode) dan pada dua ujung (path)
  j=0
  while j<len(matrik):
    if j==prevnode:
      matrik[:,j]=0
      matrik[j,:]=0
    j+=1
  matrik[path[-1],path[0]]=0
  matrik[path[0],path[-1]]=0
  return matrik

def tupletoarray(x):
  array=[]
  i=0
  while i<len(x):
    array.append(x[i])
    i=i+1
  return array

  if len(matrik)<12:
    loadlist=[]
    pathlist=[]
    path=brute_force(matrik)
    loadlist.append(count_load(path,matrik))
    pathlist.append(path)
    print pathlist[0]
    print loadlist[0]
  else:
    minval(matrik)

def minval(matrik):

  minval=[]
  i=0
  while i < len(matrik):
    minval.append(sorted(matrik[:,i])[1]+sorted(matrik[:,i])[2])
    i+=1
  return minval

def solve(matrik,n):
#mencari solusi penyelesaian masalah dengan memilih node terdekat pada matrik dengan menyisakan n-3 node sisa untuk diselesaikan secara brute force
  mat = np.matrix.copy(matrik)
  center=minval(matrik)
  print center
  path.append(center.index(min(center)))
  nextarray=make_array(path[0],matrik)
  left=sorted(nextarray[1], path.insert(0, nextarray.index(left)))
  right=sorted(nextarray[2], path.insert(0,nextarray.index(right)))

  prevnode=center.index(min(center))
  leftindex=path[0]
  rightindex=path[-1]
  leftarray=make_array(leftindex,mat)
  rightarray=make_array(rightindex,mat)
  prevnode=center.index(min(center))
  count=len(mat)-n
  for x in range(1,count):
    zero(prevnode,path,mat)
    leftarray=make_array(leftindex,mat)
    rightarray=make_array(rightindex,mat)
    left=min(i for i in leftarray if i>0)
    right=min(i for i in rightarray if i>0)
    if left<right:
      prevnode=leftindex
      leftindex=leftarray.index(left)
      leftarray=make_array(leftindex,mat)
      path.insert(0,leftindex)
    else:
      prevnode=rightindex
      rightindex=rightarray.index(right)
      rightarray=make_array(rightindex,mat)
      path.append(rightindex)
    left=min(i for i in leftarray if i>0)
    right=min(i for i in rightarray if i>0)
  return path
finalpath=solve(matrik,4)
load=count_load_open(path,rawmatrik)

#menyelesaikan sisa node dengan menggunakan brute format
rest_array=rest_array([])
leftindex=path[0]
rightindex=path[-1]
loadrest=[]
permutation_paths_rest=list(np.itertools.permutations(rest_array, len(rest_array)))

i=0
while i < len(permutation_paths_rest):
  temp=permutation_paths_rest[i]
  lefta=temp[-1]
  righta=temp[0]




