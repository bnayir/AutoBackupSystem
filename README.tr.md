#  Otomatik Yedekleme Sistemi

Kaynak dizindeki dosyaların zaman damgalı yedeklerini oluşturan, Python tabanlı basit ve etkili bir otomasyon aracı.

##  Amaç
Bu proje, önemli dosyaların manuel olarak yedeklenmesi işini otomatize etmek amacıyla geliştirilmiştir. Özellikle **otomasyon, günlük kaydı (logging) ve hata yönetimi** gibi temel mühendislik prensiplerine odaklanır.

##  Özellikler
- **Otomatik Yedekleme:** Tek bir komutla tüm dizini hedef klasöre aktarır.
- **Akıllı İsimlendirme:** `datetime` kullanarak her yedek için benzersiz klasör isimleri oluşturur (Örn: `backup_2026-05-05_01-15`).
- **İşlem Günlüğü (Logging):** Başarılı ve hatalı tüm işlemleri `backup_log.txt` dosyasına detaylıca kaydeder.
- **Platform Bağımsız:** `os.path.join` yapısı sayesinde Windows, macOS ve Linux sistemlerinde sorunsuz çalışır.

##  Kullanılan Teknolojiler
- **Dil:** Python 3.x
- **Kütüphaneler:** `shutil`, `os`, `datetime`

