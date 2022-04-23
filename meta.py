REMOVEHEADER = """
        <style>
               .css-18e3th9 {
                    padding-top: 1rem;
                    padding-bottom: 10rem;
                    padding-left: 5rem;
                    padding-right: 5rem;
                }
        </style>
        """
HEADER = """Aplikasi Text Summarization"""
PETUNJUKPENGGUNAAN = """<p>
Untuk Menggunakan aplikasi diatas, ikuti langkah langkah berikut :

1. Masukkan teks, artikel maupun berita yang akan diringkas pada kolom teks.

2. Pilih panjang ringkasan yang diinginkan dalam skala 1-3:

   - 1 = Ringkasan pendek.
   - 2 = Ringkasan sedang.
   - 3 = Ringkasan panjang.

3. Pilih metode untuk proses peringkasan teks:

   - Extractive Summarization (Bahasa Indonesia).
   - Abstractive Summarization (English). <b>(Khusus untuk metode peringakasan teks ini, panjang ringkasan teks tidak digunakan karena program akan membuat ringkasan teks secara otomatis)</b>

4. Tunggu proses peringkasan teks sampai selesai.
5. Teks yang telah diringkas akan tertampil pada bagian sebelah kanan.
</p>

""".strip()

APAITUTEXTSUMMARIZATION = """
Text Summarization atau dapat disebut juga peringkasan teks adalah proses untuk mengambil dan mengekstrak informasi penting dari sebuah teks sehingga menghasilkan teks yang lebih singkat dan mengandung poin-poin penting dari teks sumber (Indriani, 2014).
""".strip()

PERBEDAANMETODE = """Perbedaan Metode Extractive Summarization dan Abstractive Summarization adalah :
   - Extractive Summarization (Bahasa Indonesia) digunakan untuk meringkas teks dalam bahasa indonesia. Metode ini menghitung bobot setiap kata yang ada pada kalimat, dan mengambil kata tersebut untuk dirangkai menjadi sebuah ringkasan.
   - Abstractive Summarization (English) digunakan untuk meringkas teks dalam bahasa inggris. Metode ini menghitung bobot setiap kata yang ada pada kalimat dan mengambil kata tersebut untuk dirangkai menjadi sebuah ringkasan, namun hasil ringkasan telah dimofidikasi oleh program dengan makna yang sama, agar hasil teks ringkasan tidak sama dengan teks yang akan diringkas.
""".strip()
