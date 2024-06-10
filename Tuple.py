"""
    sintaks tuple menggunakan tanda kurung lengkung ()
"""

# tuple satu tipe data
tuple1 = (1, 2, 3)

#tuple tipe data berbeda
tuple1 = ("satu", 2, 3.5, 6j)

# tiple bertingkat (nested tuple)
tuple1 = (1, (1, 2), 3)

# sifat & properti data tuple
tuple1 = (1,2,3,4,5)

    # indexing & slicing
tuple1[2]
tuple1[-1]
tuple1[1:3]

    # bersifat immutable (tidak dapat diubah)
tuple1[2]
# tuple1[2] = 14    # error

    # concatenation dan multiplication
a = (1,2,3,4,5)
b = (10,20)
print(a+b)
print(a*4)

"""
    Method tuple
"""

# count() menghitung jumlah data tertentu dalam tuple
c = (1,2,3,3,5,5)
print(c.count(3))

# index() menghembalikan & menemukan posisi index dari data tertentu dalam tuple
print(c.index(5))

"""
    build-in function untuk tuple
"""
d = [2,3,4,5]
d = tuple(d)
print(d)

## build-in function yg lain
tipe = type(d)
panjang = len(d)
print(tipe)
print(panjang)
