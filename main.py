"""
Aplikasi Deteksi Gempa Terkini
MODULARISASI DENGAN FUNCTION
"""
import gempaterkini

if __name__ == '__main__':
    print("aplikasi utama")
    result =gempaterkini.extraksi_data()
    gempaterkini.tampilkan_data(result)
    
