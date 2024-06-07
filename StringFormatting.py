"""
    METODE MODULO (%)
"""
nama = "Bret"
ipk = 3.1235312

# menggunakan %s dan %r untuk string
# kita harus menambahkan % di belakang kutip yang diikuti urutan variabel yang akan ditampilkan
# %s untuk string biasa dan %r untuk string dengan output menggunakan kutip (')
print("nama saya adalah %s"%(nama))
print("nama saya %s, atau bisa pakai petik jadinya %r"%(nama, nama))

# menggunakan %d untuk integer
print("nama saya %s, ipk saya sebesar %d"%(nama, ipk))

# menggunakan %width.precissionf untuk float
# width = panjang data, jika data lebih pendek dari panjang data maka akan ditambahkan spasi di depan angka 
# precissionf = angka dibelakang koma
# kita harus memasukkan f, kalau tidak akan terinput sebagai integer bukannya float
print("nama saya %s, ipk saya sebesar %2.3f"%(nama, ipk))



"""
    METODE .format()
"""
nilai_andi = 50
nilai_ani = 70
print("nilai ulangan Andi adalah {} dan Ani adalah {}".format(nilai_andi, nilai_ani))

# menggunakan index
# dalam kondisi ini variabel nilai_andi berada pada index 0 karena dideklarasikan lebih dulu
# yang artinya index ditentukan secara urutan sesuai tempat deklarasi variabelnya
print("nilai ulangan Andi adalah {1} dan Ani adalah {0}".format(nilai_andi , nilai_ani))

# menggunakan keyword
# dalam kondisi ini kita seperti membuat variabel tambahan di dalam format string
# kita bebas menentukan urutan asal kita memasukkan keyword yang sesuai dengan variabel yang kita inginkan
print("nilai ulangan Andi adalah {a} dan Ani adalah {b}".format(a = nilai_andi , b = nilai_ani))

# menggunakan sintak {value:width.precisionf} untuk data float
# value = keyword , width = panjang digit angka yang ditampung , precisionf = angka di belakang koma
nilai_andi = 50.1234567
print("nilai ulangan Andi adalah {a:2.4f} dan Ani adalah {b}".format(a = nilai_andi , b = nilai_ani))

"""
    METODE f-string
"""
nama = "Bret"
ipk = 3.1235123

# menggunakan variabel
# dapat menggunakan format sintaks f'...{}...'
# pada kurung kurawal ({}) kita memasukkan variabel secara langsung
print(f'{nama} berhasil meraih nilai {ipk}')

# menggunakan sintak {value:{width}.{precision}f} untuk data float
# value dalam konteks ini berarti variabel
print(f'{nama} berhasil meraih nilai {ipk:2.3f}')