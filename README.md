# 13519010/Rexy Gamaliel R.

## Description
Pada persoalan ini setiap matkul memiliki dependensi *prerequisite* mata kuliah lain, sehingga hubungan dependensi ini dapat digambarkan dengan *Directed Acyclic Graph/DAG*.
Pada *graph* ini, *node* adalah kode mata kuliah, sementara *edge* dari *node* i ke *node* j berarti mata kuliah j memiliki *prerequisite* mata kuliah i. DAG digambarkan menggunakan struktur data *dictionary* Python di mana *key* adalah suatu kode mata kuliah dan *value* adalah list kode mata kuliah yang menjadi *prerequisite* mata kuliah tersebut.
Menurut jenisnya, algoritma ini menerapkan jenis strategi *Decrease and Conquer* yang mengurangi persoalan sebesar suatu variabel, di mana variabel bergantung pada banyaknnya mata kuliah yang dapat diambil pada suatu semester.

## Requirement:
-

## How to Use:
1.Direktkori defult file yang dijadikan bahan uji adalah `./input.txt`, pastikan direktori file yang digunakan sesuai.
1.Jalankan program python melalui command line.
