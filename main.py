"""
Aplikasi Deteksi Gempa Terkini
MODULARISASI DENGAN FUNCTION
"""


def extraksi_data():
    """
    Tanggal: 05 Desember 2021, 12:19:49 WIB
    Magnitudo: 4.0
    Kedalaman: 10 km
    Lokasi: 3.46 LS - 129.47 BT
    Keterangan: Pusat gempa berada di laut 9 km Selatan Tehoru-Maluku Tengah
    Dirasakan: Dirasakan (Skala MMI): III Masohi
    :return:
    """
    hasil = dict()
    hasil['tanggal'] = '05 desember 2021'
    hasil['waktu'] = '12:19:49 WIB'
    hasil['magnitudo'] = 4.0
    hasil['kedalaman'] = '10 km'
    hasil["lokasi"] = {'ls':3.46, 'bt':129.47}
    hasil['keterangan'] = 'Pusat gempa berada di laut 9 km Selatan Tehoru-Maluku Tengah'
    hasil['dirasakan'] = 'Dirasakan (Skala MMI): III Masohi'
    print(hasil)
    return hasil



def tampilkan_data(result):
    print('Hasil terkini gempa bumi dari BMKG')
    print(f"Tanggal: {result['tanggal']}")
    print(f"Waktu: {result['waktu']}")
    print(f"Magnitudo: {result['magnitudo']}")
    print(f"Kedalaman: {result['kedalaman']}")
    print(f"Lokasi: LS={result['lokasi']['ls']}, BT={result['lokasi']['bt']}")
    print(f"Keterangan: {result['keterangan']}")
    print(f"Dirasakan: {result['dirasakan']}")
    pass


if __name__ == '__main__':
    print("aplikasi utama")
    result =extraksi_data()
    tampilkan_data(result)
    
