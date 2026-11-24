# Petalpop büyüme rehberi

Bu dosya oyunu büyütmek için yapılanları ve senin yapman gerekenleri sırayla anlatır.

## 1. Oyuncuyu geri getiren özellikler (hazır)

- **Günlük ödül:** 7 günlük takvim. Üst üste gelen oyuncunun ödülü büyür, 7. gün büyük ödül var.
- **Yardımcı aletler:** Makas (bir taşı temizler), karıştır ve +5 hamle. Makas her bulmacada 1 kez ücretsiz, sonrası envanterden.
- **Sandık:** Her 3 galibiyette 2 rastgele yardımcı alet.
- **Haftalık Çiçek Festivali:** Hafta boyunca toplanan çiçeklerle 60, 150 ve 300'de ödül. Her pazartesi sıfırlanır.

## 2. Ölçüm

Oyun şu olayları sayar: oyun açılışı, bulmaca başlangıcı, galibiyet, kayıp, bırakma, yardımcı alet kullanımı, günlük ödül.

- **Kendi tarayıcında görmek için:** Oyunun adresinin sonuna `?stats` ekle. Bu senin cihazındaki sayımları gösterir.
- **Bütün oyuncuları görmek için:** Ücretsiz bir GoatCounter hesabı aç (https://www.goatcounter.com). Sana `ornek.goatcounter.com` gibi bir adres verir; `ornek` kısmı kodundur.
  - GitHub sayfası için: `index.html` içindeki `const STATS_CODE='';` satırına kodu yaz.
  - Oyun siteleri için: `python3 tools/build_platforms.py GD_OYUN_KIMLIGI ornek`
- Kişisel veri gönderilmez. Yalnızca olay adı, bulmaca numarası ve platform adı gider.
- **En önemli sayı:** Hangi bulmacada "start" çok, "win" az? O bulmaca fazla zor demektir, kolaylaştırılmalı.

## 3. Oyun siteleri

`python3 tools/build_platforms.py` komutu `dist/` altında CrazyGames, Poki ve GameDistribution paketlerini üretir.

- **CrazyGames:** Basic Launch için reklamsız. Full Launch onayı gelince build betiğindeki `window.__ADS=false` kaldırılmalı.
- **Poki:** https://developers.poki.com adresinden başvur.
- **GameDistribution:** Oyun kimliğini al ve betiğe ver.

## 4. Telefon uygulaması

Oyun artık telefona "uygulama" olarak yüklenebilir (PWA). Bunun için `manifest.webmanifest`, `sw.js` ve `icons/` dosyaları var. Oyun internetsiz de açılabilir.

- **Hemen denemek için:** Telefonda GitHub sayfasını aç.
  - Android Chrome'da menüden "Ana ekrana ekle" seç.
  - iPhone Safari'de Paylaş menüsünden "Ana Ekrana Ekle" seç.
- **Google Play için:**
  1. https://www.pwabuilder.com adresine oyunun GitHub sayfası adresini gir.
  2. "Package for stores" bölümünden Android paketini indir.
  3. Google Play Console'da geliştirici hesabı aç (tek seferlik 25 dolar).
  4. Paketi yükle. Sayfadaki talimatlara göre `assetlinks.json` dosyasını depoya eklemek gerekir; bunu birlikte yapabiliriz.
- **App Store için:** PWABuilder iOS paketi de üretir. Ancak Apple geliştirici hesabı (yıllık 99 dolar), bir Mac ve Xcode gerekir.

### Mağazada para kazanma

Mağaza sürümünde en büyük gelir iki yerden gelir:

- **Ödüllü reklam:** Örneğin "reklam izle, +5 hamle". Bunun için AdMob hesabı gerekir.
- **Uygulama içi satın alım:** Yardımcı alet paketleri ve reklamsız sürüm.

İkisi de mağaza hesapların açıldıktan sonra eklenir.
