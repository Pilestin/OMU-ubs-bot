from my_info import * 
from selenium import webdriver 
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.by import By

import time

class UBS_Savar():
    
    def __init__(self):
        self.options    = webdriver.ChromeOptions() 
        self.options.add_experimental_option('excludeSwitches', ['enable-logging'])
        self.options.add_argument("--start-maximized")
        self.driver     = webdriver.Chrome(executable_path=r"driver\chromedriver.exe",chrome_options= self.options)  

        self.login()

    def login(self):
        """
            Bu metod sisteme ilk girişi yapar. ad ve şifreyi my_info.py dosyasından alır.
            my_info içerisinde doğru bilgileri girdiğinizden emin olun.
        """

        self.driver.get("https://ubs.omu.edu.tr")
        self.driver.implicitly_wait(1)

        nameBox   = self.driver.find_element(By.XPATH, '//*[@id="txtLogin"]')
        self.driver.implicitly_wait(1)
        passBox   = self.driver.find_element(By.XPATH, '//*[@id="txtPassword"]')
        self.driver.implicitly_wait(1)
        loginBox  = self.driver.find_element(By.XPATH, '//*[@id="btnLogin"]')

        # ogr_name ve ogr_sifre my_info dosyasından alınır.
        nameBox.send_keys(ogr_name)
        self.driver.implicitly_wait(1)
        passBox.send_keys(ogr_sifre)
        self.driver.implicitly_wait(1)
        loginBox.click()
        
        # artık ders seçim ekranına geçebiliriz
        self.secimEkrani()
    
    def secimEkrani(self):
        """
            Bu metod ders seçim ekranına geçer. Bunu menüden ilgili kısma tıklayarak yapar.
            Bu butona tıkladığında tarayıcı yeni sekmeye geçeceği için ve driver hala önceki sekmeyi tuttuğu için 
            iki farklı sekmeyi tutan referansa ihtiyaç duyulur. 
           
        """
        self.driver.implicitly_wait(1)
        ders_secimi_screen = self.driver.find_element(By.XPATH, '//*[@id="ctl00_treeMenu12"]/li[5]')
        ders_secimi_screen.click()
        # Burada ders seçim ekranı yeni sekmede açıldı.
    
        self.window_before = self.driver.window_handles[0]   # login olduğumuzdaki ekranı tutan referans
        self.window_after  = self.driver.window_handles[1]   # ders seçim ekranını tutan referans
        # ama driver hala önceki sekmede kaldığı için bunu yeni sekmeye geçirmeliyiz.
        self.driver.switch_to.window(self.window_after) # artık son açtığımız sekmeye geldik
        
        # şimdi burada url kısmındaki değeri almalı ve bunu biraz değiştirmeliyiz.
        targetUrl = self.urlDegistirme()           # değiştirilmiş url
        time.sleep(1)
        # Son olarak yeni url'e geçebiliriz.
        self.driver.get(targetUrl)

    def urlDegistirme(self):
        """
            Bu metod açık olan sayfanın url kısmını alıp , biraz değiştirip
            geri string olarak döndürür. 
            
            https://ubs.omu.edu.tr/Ogrenci/Ogr.../SecilenDersler.aspx
                                |
                                v
            https://ubs.omu.edu.tr/Ogrenci/Ogr.../AcilanDersler.aspx
        """

        currentUrl     = self.driver.current_url.split("/") # aşağıdaki gibi liste döndürür.
        # ['https:', '', 'ubs.omu.edu.tr', 'Ogrenci', 'Ogr...', 'SecilenDersler.aspx']
        currentUrl[-1] = "AcilanDersler.aspx"           # son öge istenen şekilde değiştirilir.
        # ['https:', '', 'ubs.omu.edu.tr', 'Ogrenci', 'Ogr...', 'AcilanDersler.aspx']
        newUrl         = "/".join(currentUrl)                   # birleştirilir.
        # https://ubs.omu.edu.tr/Ogrenci/Ogr.../AcilanDersler.aspx
        
        return newUrl


def main():
    start = UBS_Savar()

main()








def fazlalikBunlar():
    # rows = driver.find_elements(By.XPATH, '//*[@id="divTabSheet"]/div/table')
    # for row in rows:
    #     print(row)
    #     print("-----")
    #     print(row.text)
    def tiklayarak():  
        pass
        # Bu fonksiyon pyautogui kullanarak ekrandaki konuma tıklayarak sayfayı açmaya yarar.
        # 212 , 413 
        # pyautogui.click(x=212 , y=413)
        # driver.implicitly_wait(2)
        # print("açıldı")