<div align="center">

  <h1>🤖 BUMPER</h1>
  <h3>Discord Otomatik Sunucu Öne Çıkarıcı & Yönetim Platformu</h3>

  <p>
    <b>Ömer Ali Bayrakçı</b> tarafından geliştirilmiş; Discord sunucularını ve kanallarını belirlenen zaman aralıklarında otomatik olarak öne çıkaran (<code>/bump</code>), geri sayım sayacı, maskeli token yönetimi ve canlı aktivite günlükleri sunan <b>Glassmorphism Web UI</b> ve Python tabanlı otomasyon projesi.
  </p>

  <p>
    <a href="https://bumper-nu.vercel.app"><img src="https://img.shields.io/badge/🚀_Canlı_Demo-Vercel-black?style=for-the-badge&logo=vercel" alt="Live Demo"></a>
    <a href="https://github.com/1337om3r/bumper"><img src="https://img.shields.io/badge/GitHub-1337om3r/bumper-5865f2?style=for-the-badge&logo=github" alt="GitHub Repo"></a>
    <a href="https://omerbayrakci.vercel.app"><img src="https://img.shields.io/badge/🌐_Kişisel_Blog-omerbayrakci.vercel.app-blue?style=for-the-badge" alt="Portfolio"></a>
    <a href="https://python.org"><img src="https://img.shields.io/badge/Python-3.9+-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python"></a>
  </p>

  <br>

  <p align="center">
    <img src="assets/hero.png" alt="BUMPER Discord Auto-Bump Dashboard Showcase" width="100%" style="border-radius: 12px; box-shadow: 0 10px 30px rgba(0,0,0,0.5);">
  </p>

</div>

---

## ⚡ Proje Hakkında

**BUMPER**, Discord sunucularını Disboard ve benzeri platformlarda sürekli olarak en üst sırada tutmak için otomatik `/bump` zamanlaması gerçekleştiren **kullanıcı dostu bir Web GUI otomasyon platformudur**.

Geleneksel terminal araçlarının aksine, sunduğu **Discord Glassmorphism Dark UI** arayüzü sayesinde tüm süreci canlı dairesel sayaçlar, renk kodlu aktivite günlükleri ve kullanıcıya özel token yönetim paneli ile izlemenizi sağlar.

---

## 🔥 Öne Çıkan Özellikler

| Özellik | Açıklama |
| :--- | :--- |
| 💜 **Discord Glassmorphic UI** | Discord Blurple (`#5865f2`) ve neon siyan vurguları ile tasarlanmış cam efektli karanlık tema. |
| ⏱️ **Dairesel Geri Sayım Sayacı** | Bir sonraki otomatik bump işlemine kalan süreyi dairesel SVG ring ve canlı yüzde ile takip edin. |
| 🚀 **Tek Tıkla Manüel Bump** | Zamanlayıcıyı beklemeden istediğiniz an tek tıkla `/bump` komutunu tetikleyin. |
| 🔑 **Kullanıcı Token Yönetimi** | Kendi Discord hesap token'larınızı güvenli maskelenmiş (`MTI0...****`) olarak ekleyin, silin ve yönetin. |
| 📜 **Canlı Aktivite Günlükleri** | Zaman damgalı, `SUCCESS` (Yeşil) ve `RATE_LIMITED` (Kırmızı) durum rozetli canlı bump raporları. |
| 📱 **Tam İnteraktif Sekmeler** | `Dashboard`, `Token Manager`, `Logs`, `Settings` ve `Help` sekmeleri arasında anında geçiş yapın. |
| 🌐 **Vercel Serverless Uyumlu** | Kuruluma gerek kalmadan Vercel üzerinde %100 canlı interaktif demo modu. |

---

## 💻 Arayüz Bileşenleri (Dashboard Breakdown)

1. **AUTOBUMP MONITORING (Sol Panel):**
   - Mor ve Siyan degrade geçişli canlı dairesel sayaç (%74, `NEXT BUMP IN: 01m 26s`, `Bump Target: #general-chat | server-1`).
   - 4 Metrik Sayacı: `Bumps (142)`, `Servers (12)`, `Tokens (8)`, `Failures (1)`.
   - Kontrol Butonları: `START / STOP`, `SETTINGS`, `REFRESH`.

2. **LIVE ACTIVITY LOGS (Sağ Üst Panel):**
   - Renk kodlu zaman damgalı aktivite akışı ve hata bildirimleri.

3. **TOKEN MANAGEMENT (Sağ Alt Panel):**
   - Maskelenmiş token listesi, `Online` durum rozetleri, `Performance %100` göstergesi ve `+ ADD TOKEN` modal açılır penceresi.

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

## 🛠️ Kullanılan Teknolojiler

- **Backend:** Python 3.9+, HTTP Server Engine, SSE Real-time Stream API
- **Frontend:** HTML5, Modern CSS3 (Glassmorphism, CSS Variables, FontAwesome Icons), JavaScript (ES6+)
- **Deployment:** Vercel Serverless Functions (`api/index.py`), Zero-Config Deployment

---

## 👤 Geliştirici Bilgileri

<table align="center">
  <tr>
    <td align="center">
      <b>Ömer Ali Bayrakçı</b><br>
      <i>Bilişim Öğrencisi & Açık Kaynak Katılımcısı</i><br><br>
      📍 <b>Konum:</b> İstanbul, Türkiye<br>
      🎓 <b>Eğitim:</b> FSM Bilişim Bölümü<br>
      🌐 <b>Kişisel Blog:</b> <a href="https://omerbayrakci.vercel.app">omerbayrakci.vercel.app</a><br>
      💻 <b>GitHub:</b> <a href="https://github.com/1337om3r">@1337om3r</a><br>
      💼 <b>LinkedIn:</b> <a href="https://www.linkedin.com/in/ömer-bayrakçı-4884a73b1/">ömer-bayrakçı</a><br>
      📧 <b>E-Posta:</b> <a href="mailto:omeralibayrakcii@gmail.com">omeralibayrakcii@gmail.com</a>
    </td>
  </tr>
</table>

---

## 📄 Lisans

Bu proje **MIT** lisansı altında yayınlanmıştır. Özgürce kullanabilir ve geliştirebilirsiniz!

<div align="center">
  <sub>Made with ❤️ by <a href="https://github.com/1337om3r">1337om3r</a></sub>
</div>
