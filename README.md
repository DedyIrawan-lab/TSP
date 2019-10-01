# TSP

Travelling Salesman Problem adalah sebuah masalah untuk menentukan rute terpendek dan tercepat dari node awal ke node tujuan dan kembali ke node awal.

Tugas TSP
  - menentukan algoritma untuk mencari rute terpendek dengan kasus matrik 10x10
  - membuat pseudo code dan uji coba 
  - membandingkan dengan algoritma brute force 
  - membandingkan rute dan waktu perjalanan
  - menggunakan referensi paper salsabila ITB

Kelebihan Algoritma Brute Force
  - Metode brute force dapat digunakan untuk memecahkan hampir sebagian besar masalah (wide applicability).
  - Metode brute force sederhana dan mudah dimengerti.
  - Metode brute force menghasilkan algoritma yang layak untuk beberapa masalah penting seperti pencarian, pengurutan, pencocokan string, perkalian matriks.
  - Metode brute force menghasilkan algoritma baku (standard) untuk tugas-tugas komputasi seperti penjumlahan/perkalian n buah bilangan, menentukan elemen minimum atau maksimum di dalam tabel (list).

Kekurangan Algoritma Brute Force
  - Metode brute force jarang menghasilkan algoritma yang mangkus.
  - Beberapa algoritma brute force lambat sehingga tidak dapat diterima.
  - Tidak sekontruktif/sekreatif teknik pemecahan masalah lainnya.

Hasil TSP menggunakan algoritma brute force dalam bentuk tabel

|N    |K      |Cost   |Rute                                                 |   
|-----|-------|-------|-----------------------------------------------------|
|4    |3      |76     |'A', 'B', 'D', 'C', 'A'                              |   
|5    |12     |85     |'A', 'B', 'C', 'D', 'E', 'A'                         |   
|6    |60     |101    |'A', 'B', 'D', 'C', 'F', 'E', 'A'                    |   
|7    |360    |115    |'A', 'B', 'D', 'C', 'F', 'G', 'E', 'A'               |   
|8    |2520   |133    |'A', 'B', 'D', 'C', 'H', 'E', 'G', 'F', 'A'          |  
|9    |20160  |135    |'A', 'B', 'C', 'H', 'E', 'G', 'F', 'D', 'I', 'A'     |  
|10   |181440 |157    |'A', 'B', 'I', 'D', 'C', 'H', 'E', 'G', 'F', 'J', 'A'|  

Langkah-langkah penyelesaian TSP
  1. Untuk n buah simpul semua perjalanan dibangkitkan dengan permutasi dari n-1 buah simpul.
      - permutasi dari n-1 buah simpul adalah (n-1)!
      - setengah perjalanan adalah hasil pencerminan dari setengah rute yang lain, maka dapat dihilangkan dengan dibagi 2
  2. Hitung cost setiap permutasi dan simpan nilai cost minimum
      - asumsikan node A sebagai simpul awal dan simpul akhir
      - ambil nilai rata-rata
      - ambil link terkecil
  3. Kembalikan nilai permutasi dengan cost minimum
      
Pseudo code kemungkinan semua rute perjalanan
```
fungsi pertama (n : integer) --> integer
{ Menghitung (n-1)!/2 }
Deklarasi :
  i : integer
  fak : real
  
Algoritma :
n <-- n-1
  fak <-- 1
  for i <-- 1 to n do
    fak <-- fak * 1
  end
fak/2  
return fak
```

Pseudo code hitung cost setiap permutasi
```
fungsi kedua (input A : Matriks,
              input n : integer,
              output  : nilai cost minimum)
{ mencari nilai dengan cost minimum dengan asusmsi node A simpul awal dan akhir 
dengan cara ambil nilai rata-rata dan link terkecil }
Deklarasi :
  ...
  ...
Algoritma :
  ...
  ...
```
