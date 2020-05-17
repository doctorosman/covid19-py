# COVID-19 Python Modülü
[English](README.en.md) | Türkçe

Güncel COVID-19 verilerini Python ile çekmek için kullanılabilecek bir modül.

### Kurulum
Bu proje [BeautifulSoup4](https://pypi.org/project/beautifulsoup4/) sınıfını kullanmaktadır.
~~~
pip install beautifulsoup4
~~~
### Kullanım
~~~python
country_url = "https://www.worldometers.info/coronavirus/country/turkey"
~~~
* Verisini almak istediğiniz ülkeyi değiştirebilirsiniz.<br>
* total ile başlayan fonksiyonlar Dünya'daki verileri döndürür.<br>
* Diğer fonksiyonlar seçtiğiniz ülkenin verilerini döndürür.