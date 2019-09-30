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
|5    |12     |85     |'A', 'E', 'D', 'C', 'B', 'A'                         |   
|6    |60     |105    |'A', 'F', 'E', 'D', 'C', 'B', 'A'                    |   
|7    |360    |118    |'A', 'E', 'G', 'F', 'D', 'C', 'B', 'A'               |   
|8    |2520   |154    |'A', 'E', 'H', 'G', 'F', 'D', 'C', 'B', 'A'          |  
|9    |20160  |180    |'A', 'I', 'H', 'G', 'F', 'E', 'D', 'C', 'B', 'A'     |  
|10   |181440 |207    |'A', 'J', 'I', 'H', 'G', 'F', 'E', 'D', 'C', 'B', 'A'|  

Langkah-langkah penyelesaian TSP
  - Untuk n buah simpul semua perjalanan dibangkitkan dengan permutasi dari n-1 buah simpul.
    - permutasi dari n-1 buah simpul adalah (n-1)!
    - setengah perjalanan adalah hasil pencerminan dari setengah rute yang lain, maka dapat dihilangkan dengan dibagi 2
  - Asumsikan node A sebagai simpul awal dan simpul akhir

Pseudo code kemungkinan semua rute perjalanan
```
fuction faktorial (n : integer) --> integer
{ Menghitung (n-1)!/2 }
Deklarasi
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
