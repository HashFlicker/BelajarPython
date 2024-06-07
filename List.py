"""
    tipe data list bisa digunakan dengan format sintaks kurung kotak
    [data1, data2, ...., data_n]
"""

# list dengan satu tipe data
list1 = [1,2,3,4]

# list dapat menyimpan tipe data berbeda
list2 = [1, 2.341, "Test"]

# list dapat digunakan untuk menyimpan list (list bertingkat / nested list)
list3 = [1, [1,2], 2]

"""
    SIFAT DAN PROPERTI TIPE DATA LIST
"""
a = [1,2,3]
b = [4,5,6]

# list bersifat berurutan berdasarkan index
print(a[1])
print(b[-2])
print(b[:1])
print(a[:2])
print("="*4)

# list bersifat mutable (dapat diubah)
print(a[0])
a[0] = "siji"
print(a)
print("="*4)

# list dapat ditempelkan/digabungkan dengan list lain (concantenation)
gabungan = a + b
print(gabungan)
print("="*4)

# list dapat diulang/dikalikan dengan integer (repetition)
pengulangan = b*4
print(pengulangan)
print("="*4)


"""
    METODE
"""
a = [5,3,6,2,1]
b = ["a", "b", "c"]

# append() , menambahkan anggota list
a.append(7)
print(a)
b.append("d")
print(b)
print("="*4)

# sort() , mengurutkan anggota list
a.sort()
print(a)
a.sort(reverse=True)
print(a)
print("="*4)

# reverse() , membalikkan urutan anggota list
b.reverse()
print(b)
print("="*4)

# clear() , menghapus semua anggota list
a.clear()
print(a)
print("="*4)


# pop(i) , menghapus dan mengembalikan anggota list
popped_element = b.pop(2) # mengeluarkan anggota dari list dan memasukkannya ke variabel baru
print(b)
print(popped_element)
print("="*4)


"""
    BUILD-IN FUNCTION UNTUK LIST
"""

# list(), konversi menjadi tipe data list
b = (1, 3) # bukan tipe data list
listed_b = list(b)
a = ("T", "A", "I") # bukan tipe data list
listed_a = list(a)
print(listed_b)
print(listed_a)
print("="*4)

# max() , mengambil nilai maksimal
d = [42,5325, 123, 3987234, 12312, 1256]
print(max(d))
print("="*4)

# min() , mengambil nilai minimal
print(min(d))
print("="*4)

# fungsi lain seperti type, len dan print
print(type(d))
print(len(d))
print(d)
print("="*4)