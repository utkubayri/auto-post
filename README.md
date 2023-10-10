# Cipher Bot

Bu kod, Cipher.fan'da otomatik olarak post göndermek için tasarlanmış bir Python botudur.

## Kurulum

1. Bu kodu bilgisayarınıza kopyalayın.
2. `txt_file_path` değişkenini, postlarınızın bulunduğu metin dosyasının yoluna ayarlayın.
3. İlk `pyautogui.click(x=..., y=...)` ve İkinci `pyautogui.click(x=..., y=...)` değişkenlerini, Cipher.fan'daki ilgili butonların konumlarına ayarlayın. ( İlk konum cipher tuşu ikinci konum post tuşu)

## Kullanım

1. Kodu çalıştırın.
2. Kod, metin dosyanızdaki her satır için bir post gönderecektir.


## Çalıştırma
Bu kod, `cipher.txt` adlı bir metin dosyasındaki her satırı Cipher.fan'da bir post olarak gönderecektir. İlk `pyautogui.click(x=..., y=...)` değişkeni, Cipher.fan'daki cipher butonunun konumunu temsil eder. İkinci `pyautogui.click(x=..., y=...)` değişkeni, Cipher.fan'daki post butonunun konumunu temsil eder.

Bu kodu kendi ihtiyaçlarınıza göre özelleştirebilirsiniz. Örneğin, farklı bir metin dosyası kullanmak veya farklı konumları kullanmak isteyebilirsiniz.

İşte bu kod için bir örnek README.md dosyasının bir başka versiyonu:

## Nasıl çalışır?

Bu kod, aşağıdaki adımları izleyerek çalışır:

1. Metin dosyasını açar ve her satırı okur.
2. Cipher.fan'da bir tarayıcı açar.
3. Cipher.fan'daki cipher butonuna tıklar.
4. Metin dosyasından okunan satırı pencereye kopyalar.
5. Cipher.fan'daki post butonuna tıklar.
