# ##### Tugas Kecil 2: Penyusunan Rencana Kuliah dengan Topological Sorting #####
# NIM     : 13519010
# Nama    : Rexy Gamaliel Rumahorbo
# Kelas   : K01

# Untuk mengimplementasikan DAG pada persoalan ini, digunakan dictionary in_kode_matkul:
#   key berupa suatu kode mata kuliah, dan value berupa list of kode mata kuliah yang menjadi prerequisite-nya
#   Dengan kata lain, in_kode_matkul merupakan "adjacency list" untuk edge "hubungan prerequsite" yang *masuk* ke setiap node "kode mata kuliah"


def parseTxt(in_kode_matkul):
  # Melakukan parsing dari file .txt dengan format kode mata kuliah diikuti
  # prerequisite-nya ke dalam bentuk dictionary dengan key adalah kode mata kuliah dan
  # value berupa list of kode mata kuliah lainnya yang menjadi prerequisite bagi mata kuliah tersebut.
  with open("../test/test8.txt") as file:
    nth_row = 0
    for row in file:
      i = 0
      parent_kode_matkul = True
      current_parent_kode = ''
      temp_kode_list = []
      while (True):
        # akuisisi baris kode mata kuliah dan prerequisite-nya
        current_kode = ''
        while (row[i] != ','):
          if (row[i] == '.'): # end of line
            break
          current_kode += row[i]
          i += 1
        # selesai mengakuisisi 1 kode mata kuliah
        if (parent_kode_matkul):  # jika kode matkul yang dibaca adalah kode pertama di baris
          current_parent_kode = current_kode
          in_kode_matkul.update({current_parent_kode: []})
          parent_kode_matkul = False
        else:
          temp_kode_list.append(current_kode)
        if (row[i] == '.'): # end of line
          break
        i += 1        
      in_kode_matkul.update({current_parent_kode: temp_kode_list})
      nth_row += 1
  file.close()

def deleteDependency(in_kode_matkul, list_deleted_kode_matkul):
  dictionary = in_kode_matkul.copy()
  # menghapus kode_matkul dari dictionary
  for kode_matkul in list_deleted_kode_matkul:
    if kode_matkul in dictionary:
      dictionary.pop(kode_matkul)
  
  # menghapus kode_matkul yang menjadi prerequisite matkul lain
  for kode_matkul in list_deleted_kode_matkul:
    list_deleted_prerequisite = []
    for key in dictionary:
      temp_list = dictionary.get(key)
      if kode_matkul in temp_list:
        temp_list.remove(kode_matkul)
        dictionary.update({key: temp_list})
  
  return dictionary

def TopologicalSort(kode_matkul_in, result, current_semester):
  in_kode_matkul = kode_matkul_in.copy()

  if in_kode_matkul:  # masih ada mata kuliah yang belum dijadwalkan pada result
    result.update({current_semester: []})
    deleted_matkul = []
    for key in in_kode_matkul:
      if len(in_kode_matkul.get(key)) == 0:
        # menambahkan kode mata kuliah ke hasil
        temp_list = result.get(current_semester)
        temp_list.append(key)
        result.update({current_semester: temp_list})
        deleted_matkul.append(key)
    in_kode_matkul = deleteDependency(in_kode_matkul, deleted_matkul)
    result = TopologicalSort(in_kode_matkul, result, current_semester+1)
  
  # semua mata kuliah telah di-assign pada semester tertentu
  return result

def printHasil(result):
  print("Solusi urutan pengambilan mata kuliah:")
  for key in result:
    print("Semester", key, ":", result.get(key))

# Menampilkan hasil parsing file .txt
in_kode_matkul = {}
parseTxt(in_kode_matkul)
print(in_kode_matkul)

print("# of prerequisites setiap matkul: ")
for key in in_kode_matkul:
  print(key, end=': ')
  print(len(in_kode_matkul.get(key)))

result = {}
result = TopologicalSort(in_kode_matkul, {}, 1)
print("Result: ")

printHasil(result)
