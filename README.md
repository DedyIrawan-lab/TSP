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

langkah-langkah penyelesaian TSP
  - Untuk n buah simpul semua perjalanan dibangkitkan dengan permutasi dari n-1 buah simpul.
    - permutasi dari n-1 buah simpul adalah (n-1)!
    - setengah perjalanan adalah hasil pencerminan dari setengah rute yang lain, maka dapat dihilangkan dengan dibagi 2
  - Asumsikan node A sebagai simpul awal dan simpul akhir

Psudocode 
fuction faktorial (n : integer) --> integer
{ Menghitung n! }
Deklarasi
  i : integer
  fak : real
  
Algoritma :
  fak <-- 1
  for i <-- 1 to n do
    fak <-- fak * 1
  end
return fak
