# Membuat class bernama PersegiPanjang
class PersegiPanjang:

    # Constructor, dijalankan otomatis saat objek dibuat
    # self = objek yang sedang digunakan
    # panjang dan lebar = nilai yang akan diberikan ke objek
    def __init__(self, panjang, lebar):

        # Menyimpan nilai panjang ke atribut objek
        self.panjang = panjang

        # Menyimpan nilai lebar ke atribut objek
        self.lebar = lebar

    # Method untuk menghitung luas persegi panjang
    def luas(self,):

        # Mengembalikan hasil perkalian panjang × lebar
        return self.panjang * self.lebar

    # Method untuk menghitung keliling persegi panjang
    def keliling(self):

        # Mengembalikan hasil rumus 2 × (panjang + lebar)
        return 2 * (self.panjang + self.lebar)

    # Special method untuk menentukan tampilan objek saat di-print
    def __str__(self):

        # f-string digunakan agar nilai atribut bisa dimasukkan ke dalam teks
        return f"Persegi Panjang dengan panjang {self.panjang} cm, dan lebar {self.lebar} cm"


# Mengecek apakah file sedang dijalankan secara langsung
if __name__ == "__main__":

    # Membuat objek pp dari class PersegiPanjang
    # Nilai panjang = 3 dan lebar = 2
    pp = PersegiPanjang(3, 2)

    # Menampilkan informasi objek menggunakan method __str__
    print(pp)

    # Memanggil method keliling() dan menampilkan hasilnya
    print("keliling:", pp.keliling(), "cm")

    # Memanggil method luas() dan menampilkan hasilnya
    print("luas:", pp.luas(), "cm^2")