
try:
    angka = int(input("Masukkan angka:"))

    # Memeriksa apakah input adalah bilangan non-negatif
    if angka >= 0:
        angka_biner = bin(angka)
        
        # Menghilangkan awalan '0b' dari string biner
        hasil_biner = angka_biner[2:]
        
        print(f"Bentuk biner dari {angka} adalah: {hasil_biner}")
    else:
        print("Angka harus >0")

except ValueError:
    print("Angka harus bilangan bulat")