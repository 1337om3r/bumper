<div align="center">

  <h1>🤖 BUMPER</h1>
  <h3>Discord Otomatik Sunucu & Bağlantı Öne Çıkarıcı Dashboard</h3>

  <p>
    Discord sunucularını ve kanallarını belirlenen zaman aralıklarında otomatik olarak öne çıkaran (<code>/bump</code>), geri sayım sayacı, maskeli token yönetimi ve canlı aktivite günlükleri sunan <b>Glassmorphism Web UI</b> ve Python tabanlı yönetim platformu.
  </p>

  <p>
    <a href="https://bumper-nu.vercel.app"><img src="https://img.shields.io/badge/🚀_Canlı_Demo-Vercel-black?style=for-the-badge&logo=vercel" alt="Live Demo"></a>
    <a href="https://github.com/1337om3r/bumper"><img src="https://img.shields.io/badge/GitHub-1337om3r/bumper-5865f2?style=for-the-badge&logo=github" alt="GitHub Repo"></a>
    <a href="https://python.org"><img src="https://img.shields.io/badge/Python-3.9+-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python"></a>
    <a href="https://opensource.org/licenses/MIT"><img src="https://img.shields.io/badge/License-MIT-emerald?style=for-the-badge" alt="License"></a>
  </p>

  <br>

  <p align="center">
    <img src="assets/hero.png" alt="BUMPER Discord Auto-Bump Dashboard Showcase" width="100%" style="border-radius: 12px; box-shadow: 0 10px 30px rgba(0,0,0,0.5);">
  </p>

</div>

---

## ⚡ Proje Hakkında

**BUMPER**, Discord topluluk yöneticileri ve sunucu sahipleri için tasarlanmış modern bir otomasyon aracıdır. Discord sunucularını Disboard gibi botlarda en üst sırada tutmak için otomatik `/bump` komutları gönderir.

Geleneksel komut satırı araçlarının aksine, **BUMPER** sunduğu **Discord Glassmorphism Dark UI** arayüzü sayesinde tüm süreci canlı dairesel sayaçlar, renk kodlu aktivite günlükleri ve güvenli token yönetim paneli ile izlemenizi sağlar.

---

## 🔥 Öne Çıkan Özellikler

| Özellik | Açıklama |
| :--- | :--- |
| 💜 **Discord Glassmorphic UI** | Discord Blurple (`#5865f2`) ve neon siyan vurguları ile tasarlanmış cam efektli karanlık tema. |
| ⏱️ **Dairesel Geri Sayım Sayacı** | Bir sonraki otomatik bump işlemine kalan süreyi dairesel SVG ring ve canlı yüzde ile takip edin. |
| 🚀 **Tek Tıkla Manüel Bump** | Zamanlayıcıyı beklemeden istediğiniz an tek tıkla `/bump` komutunu tetikleyin. |
| 🔑 **Kullanıcı Token Yönetimi** | Kendi Discord hesap token'larınızı güvenli maskelenmiş (`MTI0...****`) olarak ekleyin ve yönetin. |
| 📜 **Canlı Aktivite Günlükleri** | Zaman damgalı, `SUCCESS` (Yeşil) ve `RATE_LIMITED` (Kırmızı) durum rozetli canlı bump raporları. |
| 🌐 **Vercel Serverless Uyumlu** | Kuruluma gerek kalmadan Vercel üzerinde %100 canlı interaktif demo modu. |

---

## 💻 Dashboard Bileşenleri

1. **AUTOBUMP MONITORING (Sol Panel):**
   - Mor ve Siyan degrade geçişli canlı dairesel sayaç (%74, `NEXT BUMP IN: 01m 26s`, `Bump Target: #general-chat | server-1`).
   - 4 Metrik Sayacı: `Bumps (142)`, `Servers (12)`, `Tokens (8)`, `Failures (1)`.
   - Kontrol Butonları: `START / STOP`, `SETTINGS`, `REFRESH`.

2. **LIVE ACTIVITY LOGS (Sağ Üst Panel):**
   - Renk kodlu zaman damgalı aktivite akışı ve hata bildirimleri.

3. **TOKEN MANAGEMENT (Sağ Alt Panel):**
   - Maskelenmiş token listesi, `Online` durum rozetleri, `Performance %100` göstergesi ve `+ Add Token` modal açılır penceresi.

---

## 🚀 Hızlı Başlangıç & Yerel Kurulum

### 1. Repozitörü Klonlayın

```bash
git clone https://github.com/1337om3r/bumper.git
cd bumper
```

### 2. Bağımlılıkları Yükleyin

```bash
pip install -r requirements.txt
```

### 3. Web GUI Dashboard'u Başlatın

```bash
python3 gui_main.py
```

> **Not:** Komut çalıştırıldığında varsayılan tarayıcınız otomatik olarak **`http://localhost:8085`** adresinde açılacaktır.

---

## 🛠️ Teknoloji Yığını

- **Backend:** Python 3.9+, HTTP Server & SSE Real-time Stream Engine
- **Frontend:** HTML5, Modern CSS3 (Glassmorphism, CSS Variables), JavaScript (ES6+), Lucide Icons
- **Deployment:** Vercel Serverless Functions (`api/index.py`), Zero-Config Deployment

---

## 👨‍💻 Geliştirici & Yazar

**Ömer Ali Bayrakçı**
- 🌐 **Web Portfolyo:** [omerbayrakci.vercel.app](https://omerbayrakci.vercel.app)
- 💻 **GitHub:** [@1337om3r](https://github.com/1337om3r)
- 📧 **İletişim:** `omeralibayrakcii@gmail.com`

---

## 📄 Lisans

Bu proje **MIT** lisansı altında yayınlanmıştır. Özgürce çatallayabilir (fork), geliştirebilir ve kullanabilirsiniz!

<div align="center">
  <sub>Made with ❤️ by <a href="https://github.com/1337om3r">1337om3r</a></sub>
</div>
