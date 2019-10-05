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

Representasi adjacency matrik dalam bahasa C

|   |   | A  | B  | C  | D  | E  | F  | G  | H  | I  | J  |
|:-:|---|----|----|----|----|----|----|----|----|----|----|
|   |   | 0  | 1  | 2  | 3  | 4  | 5  | 6  | 7  | 8  | 9  |
| A | 0 | 0  | 10 | 30 | 31 | 20 | 28 | 44 | 43 | 10 | 21 |
| B | 1 | 10 | 0  | 22 | 18 | 40 | 26 | 37 | 39 | 19 | 39 |
| C | 2 | 30 | 22 | 0  | 18 | 26 | 23 | 50 | 18 | 41 | 41 |
| D | 3 | 31 | 18 | 18 | 0  | 15 | 22 | 42 | 20 | 12 | 30 |
| E | 4 | 20 | 40 | 26 | 15 | 0  | 12 | 10 | 15 | 47 | 34 |
| F | 5 | 28 | 26 | 23 | 22 | 12 | 0  | 16 | 33 | 28 | 18 |
| G | 6 | 44 | 37 | 50 | 42 | 10 | 16 | 0  | 31 | 37 | 48 |
| H | 7 | 43 | 39 | 18 | 20 | 15 | 33 | 31 | 0  | 34 | 45 |
| I | 8 | 10 | 19 | 41 | 12 | 47 | 28 | 37 | 34 | 0  | 28 |
| J | 9 | 21 | 39 | 41 | 30 | 34 | 18 | 48 | 45 | 28 | 0  |

Pseudo Code Uji coba 4 buah Simpul

```

DEKLARASI
simpul  : array[0...3] of string
A       : array[0..3, 0..3] of integer              

procedure Proses(input Matriks : A, input baris, kolom: integer)
{ Pemrosesan elemen matriks A[0..3, 0..3] per baris per kolom }
{ K.Awal  : Matriks A sudah terdenifisi elemen-elemennya }
{ K.Akhir : Setiap elemen matriks A telah di proses }

DEKLARASI
  i : integer { indeks baris }
  j : integer { indeks kolom }
  min : integer { nilai minimum di isi dengan 99 }

ALGORITMA: 
{ Mencetak semua simpul dengan busur terpendek }
  for i <-- to 3 do
    for j <-- to 3 do
      if A[i,j] != 0 && A[i,j] != 99 do
        if A[i,j] < min do
          min <-- A[i,j]
        end if
      end if
    end for
  end for

{ Mencetak hubungan antar simpul }
  for i <-- to 3 do
    cetak(simpul baris[i]);
      for j <-- to 3 do
        if A[i,j] != 0 && A[i,j] != 99 do
          cetak(simpul kolom[j]);
        end if
      end for
   end for
```

Traslate Program C

```
#include <stdio.h>
#include <stdlib.h>

#define Nbaris 4
#define Nkolom 4

typedef int MatriksInt [Nbaris+1] [Nkolom+1];
MatriksInt M;

int M[4][4] = {0,10,30,31,
               10,0,22,18,
               30,22,0,18,
               31,18,18,0};
 
 char simpul [4] = "ABCD";
 
int i, j, baris, kolom, min;
min = 99; // asumsi tidak ada busur yang bobotnya lebih dari 99

//Mencetak Hubungan Antar Simpul
for(i=0; i<=3; i++)
{
    printf("\n %c : ", simpul[i]);
    for(j=0; j<=3; j++)
    {
        if(A[i][j] != 0 && A[i][j] != 99)
        {
            printf("%c ", simpul[j]);
        }
    }
}
printf("\n");

//Mencari bobot nilai busur terkecil
for(i=0; i<=3; i++)
  {
    for(j=0; j<=3; j++)
      {
        if(A[i][j] != 0 && A[i][j] != 99)
          {
            if(A[i][j] < min)
              {
                min = A[i][j];
              }
           }
       }
   }
 printf("\n %i", min);
 
 //Mencetak simpul yang memiliki bobot nilai terkecil
 for(i=0; i<=3; i++)
  {
    for(j=0; j<=3; j++)
      {
        if(A[i][j] == min;
          {
            printf("\n %c %c", simpul[i], simpul[j]);
           }
       }
   }
 ```
