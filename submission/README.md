# 🚀 Proyek Akhir: Menyelesaikan Permasalahan Perusahaan Edutech

## 🏢 Business Understanding

**Jaya Jaya Maju** merupakan salah satu perusahaan multinasional yang telah berdiri sejak tahun 2000 dan memiliki lebih dari 1000 karyawan yang tersebar di seluruh penjuru negeri. Walaupun telah menjadi perusahaan yang cukup besar, Jaya Jaya Maju masih mengalami kesulitan dalam mengelola karyawan, yang berdampak pada tingginya attrition rate (rasio jumlah karyawan yang keluar dengan total karyawan keseluruhan) hingga lebih dari **10%**.

Untuk mencegah hal ini semakin parah, manajer departemen HR meminta bantuan untuk mengidentifikasi berbagai faktor yang mempengaruhi tingginya attrition rate tersebut. Selain itu, HR juga membutuhkan business dashboard untuk memonitor berbagai faktor tersebut secara real-time.

---

## ❓ Permasalahan Bisnis

- 🔍 Mengidentifikasi faktor-faktor utama yang mempengaruhi tingginya attrition rate di perusahaan.
- 🔮 Memprediksi kemungkinan karyawan akan keluar dari perusahaan.
- 📊 Menyediakan dashboard interaktif untuk memonitor faktor-faktor yang berpengaruh terhadap attrition.

---

## 📋 Cakupan Proyek

- 📈 Analisis data karyawan untuk memahami pola dan faktor yang mempengaruhi attrition.
- 🤖 Pengembangan model machine learning untuk memprediksi attrition.
- 📱 Pembuatan business dashboard untuk visualisasi dan monitoring faktor-faktor attrition.
- 💡 Memberikan rekomendasi actionable bagi perusahaan berdasarkan hasil analisis.

---

## 🛠️ Persiapan

### **Sumber Data:**  
- `employee_data.csv`: Berisi data karyawan Jaya Jaya Maju dengan berbagai fitur terkait demografi, pekerjaan, dan status attrition.

### **Setup Environment:**  
1. Pastikan Python telah terinstal.
2. Install dependencies dengan perintah:
   ```bash
   pip install -r requirements.txt
   ```
3. Buka dan jalankan notebook analisis di `model/model.ipynb`.

---

## 📊 Business Dashboard

Business dashboard dibuat menggunakan **Metabase** untuk membantu HR dalam memonitor faktor-faktor utama yang mempengaruhi attrition, seperti usia, departemen, tingkat kepuasan kerja, dan lainnya. Dashboard ini menampilkan visualisasi interaktif yang memudahkan pengambilan keputusan.

**File database Metabase:**  
`/submission/metabase.db.mv.db`

### Cara Mengakses Dashboard Metabase

#### ✅ Melalui Antarmuka Web
1. Jalankan Metabase di server Anda.
2. Buka browser dan akses:  
   `http://localhost:3000`  
   *(atau alamat Metabase Anda)*
3. Login dengan akun Anda.
4. Navigasi ke menu **Dashboard** untuk melihat dashboard yang telah dibuat.

#### 🖥️ Melalui API Metabase

**1. Autentikasi (Mendapatkan Token Session)**
```bash
curl -X POST http://localhost:3000/api/session \
  -H "Content-Type: application/json" \
  -d '{"username":"your_email@example.com","password":"your_password"}'
```
*Ganti email dan password sesuai akun Anda.*

**2. Mendapatkan Daftar Dashboard**
```bash
curl -X GET http://localhost:3000/api/dashboard \
  -H "X-Metabase-Session: your_token"
```
*Ganti `your_token` dengan token session dari langkah sebelumnya.*

**3. Menampilkan Data JSON dengan jq (opsional)**
```bash
curl -X GET http://localhost:3000/api/dashboard \
  -H "X-Metabase-Session: your_token" | jq
```

> **Catatan Penting:**
> - Pastikan Metabase sudah berjalan dan file database sudah terhubung.
> - Jika ada error, cek log Metabase.

---

## 📝 Conclusion

Berdasarkan analisis data dan pemodelan yang dilakukan, ditemukan beberapa faktor utama yang berkontribusi terhadap tingginya attrition rate di Jaya Jaya Maju, antara lain:
- Tingkat kepuasan kerja
- Frekuensi lembur
- Jarak rumah ke kantor
- Tingkat pendidikan

Model prediksi yang dikembangkan dapat membantu HR dalam mengidentifikasi karyawan yang berisiko tinggi untuk keluar, sehingga dapat dilakukan intervensi lebih dini.

---

## ⚡ Rekomendasi Action Items

### 1. **Meningkatkan Program Retensi Karyawan** 🏆  
   Fokus pada peningkatan kepuasan kerja dan work-life balance, terutama bagi karyawan yang sering lembur atau memiliki tingkat kepuasan rendah.

### 2. **Pengembangan Karir dan Pelatihan** 📚  
   Sediakan program pengembangan karir dan pelatihan yang relevan untuk meningkatkan loyalitas dan motivasi karyawan.

### 3. **Monitoring Berkelanjutan** 📈  
   Gunakan dashboard secara rutin untuk memonitor faktor-faktor attrition dan melakukan evaluasi kebijakan HR secara berkala.

---
