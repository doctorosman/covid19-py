<h2>COVID-19 Python Sınıfı</h2>
Güncel COVID-19 verilerini Python ile çekmek için kullanılabilecek bir sınıf.

<h3>Kurulum</h3>
Bu proje <a href="https://pypi.org/project/beautifulsoup4/">BeautifulSoup4</a> sınıfını kullanmaktadır.
```cmd
pip install beautifulsoup4
```
<h3>Kullanım</h3>
```Python
country_url = "https://www.worldometers.info/coronavirus/country/turkey"
```
- Verisini almak istediğiniz ülkeyi değiştirebilirsiniz.<br>
- total ile başlayan fonksiyonlar Dünya'daki verileri döndürür.<br>
- Diğer fonksiyonlar seçtiğiniz ülkenin verilerini döndürür.