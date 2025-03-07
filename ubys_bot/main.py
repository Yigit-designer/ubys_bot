import login
import requests
import sys
import time
import os
import users
import telegram
sys.stdout.reconfigure(encoding="utf-8")

print("Application started")
class Manager:
    def __init__(self, name, password, sapid):
        self.name = name
        self.password = password
        self.sapid = sapid
        self.omu = login.OMULogin(self.name, self.password)  # Her kullanıcı için farklı login nesnesi
    
    def start(self, ogrenciNo, sifre, student_sapid):
        session = self.omu.login()

        if isinstance(session, requests.Session):
            print(f"{ogrenciNo}: Oturum başlatıldı.")
            start_time = time.time()  # Başlangıç zamanını al

            # 30 dakika geçtikten sonra oturum yenileme
            if time.time() - start_time >= 1800:  # 30 dakika sonra oturum yenileme
                print(f"{ogrenciNo}: Oturum yenileniyor...")
                session = self.omu.login()  # Tekrar giriş yap
                start_time = time.time()  # Zamanı sıfırla

            # Verileri çek
            self.omu.get_page_content(student_sapid)
            time.sleep(4)

            # Eğer işlem çok uzun sürerse durdurma
            if time.time() - start_time >= 1800:  # Tekrar kontrol
                print(f"{ogrenciNo}: İşlem tamamlandı, bir sonraki kullanıcıya geçiliyor.")
                return  # Bu satır, işlem tamamlandığında geri dönüp döngüye geçer

            # Ekranı temizle (isteğe bağlı)
            os.system("cls" if os.name == "nt" else "clear")
        else:
            print(f"{ogrenciNo}: Hata detayları:", session.text)

if __name__ == "__main__":
    while True:
        for user in users.user_list:
            manager = Manager(user["name"], user["password"], user["sapid"])
            print(f"{user['name']} verisi çekiliyor...")
            manager.start(user["name"], user["password"], user["sapid"])
            time.sleep(4)  # Her kullanıcıdan sonra biraz bekle
