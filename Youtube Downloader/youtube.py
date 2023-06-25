import pytube


class YT:

    def download(link):
        
        video = pytube.YouTube(link)
        video = video.streams.get_highest_resolution()
        try:
            video.download('İndirilenler')
        except:
            print('Hata oluştu lütfen tekrar dene')
        print('Video indirildi')
        return link


    def spin(link):
        while True:
            YT.download(link)
            result = input('Çıkmak için "q" ya basınız, devam etmek için entera basınız: ')
            if result == 'q':
                break
            else:
                YT.vlink()


    def vlink():
        link = input('Lütfen video linkini giriniz: ')
        YT.spin(link)
        return link

YT.vlink()



