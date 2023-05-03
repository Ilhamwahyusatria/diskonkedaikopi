class AnandaCoffee:
    def __init__(self):
        self.__menu = {
            "a": {"nama": "ES Kopi Susu", "harga": 11000},
            "b": {"nama": "ES Kopi Coklat", "harga": 12000},
            "c": {"nama": "ES Kopi Hitam", "harga": 11000},
            "d": {"nama": "Ice Americano", "harga": 14000}
        }
        self.__pilihan = "y"

    def __input_pesan(self):
        pesan = input("Masukkan list abjad menu kopi: ").lower()
        while pesan not in self.__menu:
            pesan = input("Menu tidak tersedia, silakan masukkan abjad menu yang tersedia: ").lower()
        jumlah_pesan = int(input("Masukkan jumlah pesanan: "))
        return pesan, jumlah_pesan

    def __hitung_harga(self, pesan, jumlah_pesan, diskon):
        harga = self.__menu[pesan]["harga"] * jumlah_pesan
        ppn = int(harga * 0.1)
        diskon = diskon / 100 * harga if diskon <= 50 else 0
        total_harga = harga - diskon + ppn
        return harga, diskon, ppn, total_harga

    def __output_pesan(self, menu, jumlah_pesan, harga, diskon, ppn, total_harga):
        print("--------------------------")
        print("Ananda Coffee")
        print("--------------------------")
        print("Menu :", menu)
        print("Jumlah Pesan :", jumlah_pesan)
        print("Harga :", harga)
        print("Diskon :", diskon)
        print("PPN :", ppn)
        print("--------------------------")
        print("Jumlah Bayar :", total_harga)
        print("--------------------------")

    def pesan(self):
        while self.__pilihan == "y":
            print("""
            ==============================
            
            Ananda Coffee
            List Menu Minuman Kopi
            
            ==============================
            A. ES Kopi Susu : Rp 11.000
            B. ES Kopi Coklat : Rp 12.000
            C. ES Kopi Hitam : Rp 11.000
            D. Ice Americano : Rp 14.000
            ==============================
            """)
            pesan, jumlah_pesan = self.__input_pesan()
            diskon = Diskon.get_diskon(jumlah_pesan)
            harga, diskon_value, ppn, total_harga = self.__hitung_harga(pesan, jumlah_pesan, diskon)
            self.__output_pesan(self.__menu[pesan]["nama"], jumlah_pesan, harga, diskon_value, ppn, total_harga)
            self.__pilihan = input("Apakah anda ingin order kembali Y/N = ").lower()


class Diskon:
    @staticmethod
    def get_diskon(jumlah_pesan):
        if jumlah_pesan >= 10:
            return 50
        elif jumlah_pesan >= 7:
            return 30
        elif jumlah_pesan >= 5:
            return 20
        elif jumlah_pesan >= 3:
            return 10
        else:
            return 0


if __name__ == "__main__":
    AnandaCoffee().pesan()
