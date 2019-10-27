# TSP

Travelling Salesman Problem adalah sebuah masalah untuk menentukan rute terpendek dan tercepat dari node awal ke node tujuan dan kembali ke node awal.

Tugas TSP
  - menentukan algoritma untuk mencari rute terpendek dengan kasus matrik 10x10
  - membuat pseudo code dan uji coba 
  - membandingkan dengan algoritma brute force 
  - membandingkan rute dan waktu perjalanan
  - menggunakan referensi paper salsabila ITB

| 0  | 10 | 30 | 31 | 20 | 28 | 44 | 43 | 10 | 21 |
|----|----|----|----|----|----|----|----|----|----|
| 10 | 0  | 22 | 18 | 40 | 26 | 37 | 39 | 19 | 39 |
| 30 | 22 | 0  | 18 | 26 | 23 | 50 | 18 | 41 | 41 |
| 31 | 18 | 18 | 0  | 15 | 22 | 42 | 20 | 12 | 30 |
| 20 | 40 | 26 | 15 | 0  | 12 | 10 | 15 | 47 | 34 |
| 28 | 26 | 23 | 22 | 12 | 0  | 16 | 33 | 28 | 18 |
| 44 | 37 | 50 | 42 | 10 | 16 | 0  | 31 | 37 | 48 |
| 43 | 39 | 18 | 20 | 15 | 33 | 31 | 0  | 34 | 45 |
| 10 | 19 | 41 | 12 | 47 | 28 | 37 | 34 | 0  | 28 |
| 21 | 39 | 41 | 30 | 34 | 18 | 48 | 45 | 28 | 0  |

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

Langkah-langkah penyelesaian TSP menggunakan algoritma Brute Force
  1. Untuk n buah simpul semua perjalanan dibangkitkan dengan permutasi dari n-1 buah simpul.
      - permutasi dari n-1 buah simpul adalah (n-1)!
      - setengah perjalanan adalah hasil pencerminan dari setengah rute yang lain, maka dapat dihilangkan dengan dibagi 2
  2. Hitung cost setiap permutasi dan simpan nilai cost minimum
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

Langkah-langkah penyelesaian TSP menggunakan algoritma Dedy Irawan
  1. Asumsikan node A sebagai simpul awal dan simpul akhir
  2. Ambil nilai rata-rata
  3. Ambil link dengan nilai terkecil
