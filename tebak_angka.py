import random

secret_number = random.randint(1, 100)
print('Saya berpikir tentang satu angka antara 1-100')
print("Bisakah kamu menebaknya?")

kesempatan = int(input("Masukkan berapa kesempatan kamu untuk menebaknya: "))
print(f"Kamu punya kesempatan {kesempatan} kali")

while kesempatan > 0:
    angka= int(input("Masukkan angka tebakanmu: "))
    if angka < secret_number:
        print("Terlalu rendah")
    elif angka > secret_number:
        print("Terlalu tinggi")
    else:
        print(f"Selamat tebakanmu benar yaitu {secret_number}")
        break
    kesempatan -= 1
    print(f"kesempatanmu tinggal = {kesempatan}")

if kesempatan == 0:
    print(f"Yah kesempatan kamu telah habis, angkanya adalah {secret_number}")
