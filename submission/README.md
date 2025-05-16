# 🚀 Proyek Akhir: Menyelesaikan Permasalahan Perusahaan Edutech

## 🏢 Business Understanding

**Jaya Jaya Maju** merupakan salah satu perusahaan multinasional yang telah berdiri sejak tahun 2000 dan memiliki lebih dari 1000 karyawan yang tersebar di seluruh penjuru negeri. Walaupun telah menjadi perusahaan yang cukup besar, Jaya Jaya Maju masih mengalami kesulitan dalam mengelola karyawan, yang berdampak pada tingginya attrition rate (rasio jumlah karyawan yang keluar dengan total karyawan keseluruhan) hingga lebih dari **10%**.

Untuk mencegah hal ini semakin parah, manajer departemen HR meminta bantuan untuk mengidentifikasi berbagai faktor yang mempengaruhi tingginya attrition rate tersebut. Selain itu, HR juga membutuhkan business dashboard untuk memonitor berbagai faktor tersebut secara real-time.

---

## ❓ Permasalahan Bisnis

Perusahaan Jaya Jaya Maju menghadapi permasalahan tingginya attrition rate (rasio karyawan keluar) yang melebihi 10%. Berdasarkan hasil eksplorasi data pada kolom `Attrition`, dari total 1.470 karyawan, sebanyak **879 karyawan tidak mengalami attrition** (tetap bekerja di perusahaan), sedangkan **179 karyawan mengalami attrition** (keluar dari perusahaan). Meskipun mayoritas karyawan masih bertahan, jumlah karyawan yang keluar tetap signifikan dan dapat berdampak negatif pada produktivitas, biaya rekrutmen, serta stabilitas operasional perusahaan. Oleh karena itu, diperlukan analisis lebih lanjut untuk memahami faktor-faktor utama yang menyebabkan attrition dan merumuskan solusi untuk meminimalisirnya.

---

## 📋 Cakupan Proyek

- 📈 Analisis data karyawan untuk memahami pola dan faktor yang mempengaruhi attrition.
- 🤖 Pengembangan model machine learning untuk memprediksi attrition.
- 📱 Pembuatan business dashboard untuk visualisasi dan monitoring faktor-faktor attrition.
- 💡 Memberikan rekomendasi actionable bagi perusahaan berdasarkan hasil analisis.

---

## 🛠️ Persiapan

### **Sumber Data:**  
Dataset yang digunakan adalah `employee_data.csv`, berisi data karyawan Jaya Jaya Maju dengan berbagai fitur terkait demografi, pekerjaan, dan status attrition.  
Sumber dataset: [Dicoding Employee Dataset](https://github.com/dicodingacademy/dicoding_dataset/tree/main/employee)

---

### **Setup Environment**

#### **Menggunakan Anaconda**
```bash
conda create --name main-ds python=3.9
conda activate main-ds
pip install -r requirements.txt
```

#### **Menggunakan Shell/Terminal**
```bash
pip install pipenv
pipenv install
pipenv shell
pip install -r requirements.txt
```

---

### **Menjalankan Notebook Analisis**
Buka dan jalankan notebook analisis di:
```
model/model.ipynb
```

---

### **Menjalankan File Prediksi (Opsional)**
Jika ingin menjalankan file prediksi berbasis Python, gunakan perintah berikut di dalam environment yang sudah aktif:

```bash
python ./submission/prediction.py
```

---

## 📊 Business Dashboard

Business dashboard dibuat menggunakan **Metabase** untuk membantu HR dalam memonitor faktor-faktor utama yang mempengaruhi attrition, seperti usia, departemen, tingkat kepuasan kerja, dan lainnya. Dashboard ini menampilkan visualisasi interaktif yang memudahkan pengambilan keputusan.

**File database Metabase:**  
`/submission/metabase.db.mv.db`

### Cara Mengakses Dashboard Metabase

#### ✅ Melalui Antarmuka Web (Metabase Lokal dengan Docker)

1. Pastikan file database Metabase (`metabase.db.mv.db`) sudah ada di direktori lokal Anda, misal di `/submission/`.
2. Jalankan Metabase menggunakan Docker dengan perintah berikut (pastikan port 3000 belum digunakan):
   ```bash
   docker run -d -p 3000:3000 \
     -v $(pwd)/submission:/metabase-data \
     -e "MB_DB_FILE=/metabase-data/metabase.db.mv.db" \
     --name metabase metabase/metabase
   ```
3. Buka browser dan akses:  
   `http://localhost:3000`
4. Login menggunakan:
   - **Email:** 232153079@student.unsil.ac.id
   - **Password:** KsXV6Trq$C8L5uB
5. Navigasi ke menu **Dashboard** untuk melihat dashboard yang telah dibuat.

#### 🖥️ Melalui API Metabase

**1. Autentikasi (Mendapatkan Token Session)**
```bash
curl -X POST http://localhost:3000/api/session \
  -H "Content-Type: application/json" \
  -d '{"username":"232153079@student.unsil.ac.id","password":"KsXV6Trq$C8L5uB"}'
```

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
