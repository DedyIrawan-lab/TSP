# TSP

Travelling Salesman Problem adalah sebuah masalah untuk menentukan rute terpendek dan tercepat dari node awal ke node tujuan dan kembali ke node awal.

Tugas TSP
  - membuat matrik 10x10 secara random
  - membuat pseudo code / algoritma 
  - membuat program dari pseudo code menggunakan bahasa pemogramman 
  - membandingkan hasil program dengan program ant colony, brute force, dan program sasha 
  - menggunakan referensi paper dan tesis sasha

Bentuk matrik 10x10

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

Pseudo code algortitma yang dibuat
  1. Asumsikan node A sebagai simpul awal dan simpul akhir
  2. Ambil nilai rata-rata
  3. Ambil link dengan nilai terkecil

Pseudo code algoritma brute force
  1. Untuk n buah simpul semua perjalanan dibangkitkan dengan permutasi dari n-1 buah simpul.
      - permutasi dari n-1 buah simpul adalah (n-1)!
      - setengah perjalanan adalah hasil pencerminan dari setengah rute yang lain, maka dapat dihilangkan dengan dibagi 2
  2. Hitung cost setiap permutasi dan simpan nilai cost minimum
  3. Kembalikan nilai permutasi dengan cost minimum
  
Pseudo code algoritma ant colony
  ...
  ...
  ...

Pseudo code algoritma sasha
  ...
  ...
  ...

Hasil TSP menggunakan algoritma brute force, ant colony, sasha, algoritma sendiri

| Jumlah Node | Minimum Value | Minimum Value | Minimum Value  | Minimum Value |
|-------------|---------------|---------------|----------------|---------------|
|             | Brute Force   | Ant Colony    | Algoritma Sasha| Algoritma Dedy|
| 4           | 76            | 76            | #error#        | #empty#       |
| 5           | 85            | 85            | #error#        | #empty#       |
| 6           | 101           | 104           | #error#        | #empty#       |
| 7           | 115           | 118           | #error#        | #empty#       |
| 8           | 133           | 133           | #error#        | #empty#       |
| 9           | 135           | 135           | #error#        | #empty#       |
| 10          | 157           | 157           | #error#        | #empty#       |

Pola rute

| Node | Pola Rute             |                       |                |                |
|------|-----------------------|-----------------------|----------------|----------------|
|      | Brute Force           | Ant Colony            | Algoritma Shasa| Algoritma Dedy |
| 4    | A,B,C,D,A             | D,B,A,C,D             | #error#        | #empty#        |
| 5    | A,B,C,D,E,A           | B,A,E,D,C,B           | #error#        | #empty#        |
| 6    | A,B,D,C,F,E,A         | E,F,D,C,B,A,E         | #error#        | #empty#        |
| 7    | A,B,D,C,F,G,E,A       | E,G,F,D,C,B,A,E       | #error#        | #empty#        |
| 8    | A,B,D,C,H,E,G,F,A     | F,G,E,H,C,D,B,A,F     | #error#        | #empty#        |
| 9    | A,B,C,H,E,G,F,D,I,A   | H,E,G,F,D,I,A,B,C,H   | #error#        | #empty#        |
| 10   | A,B,I,D,C,H,E,G,F,J,A | C,H,E,G,F,J,A,B,I,D,C | #error#        | #empty#        |
