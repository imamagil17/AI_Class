x = [i % 10 + 1 for i in range(20)]
input = int(input("masukan input= "))


panjang = x.count(input)
print("Jumlah data: ",panjang)
hasil = []
for i in range(len(x)):
    if x[i] == input:
        if input % 2 == 0:
            hasil.append(i)
        else:
            print("bukan genap")
            break
print("berada di: ", hasil)