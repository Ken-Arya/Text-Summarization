# import library yang akan digunakan
import os
import streamlit as st
import numpy as np
import re
import nltk
import time
import pandas
from nltk.corpus import stopwords
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
from sklearn.feature_extraction.text import TfidfVectorizer

nltk.download("stopwords")
nltk.download("punkt")

# proses extractive summary yang akan dijalankan dengan metode TF-IDF


def procexsum(rawtext, panjang):

    with st.spinner("Mohon tunggu, teks anda sedang dalam proses peringkasan"):
        # Teks dibersihkan :
        #   1. Menghapus Garis baru (new line)
        #   2.Teks dipecah menjadi per kalimat
        brs1time = time.time()
        text = rawtext.replace("\n", "")
        sentence = re.split("\. |\.", text)
        brs1time = time.time() - brs1time

        # Teks di tokenisasi :
        #   1. Tokenizer membaca
        #   2. Ditokenisasi (Dipecah menjadi kata per kata) dan diubah menjadi huruf kecil
        tkstime = time.time()
        tokenizer = nltk.RegexpTokenizer(r"\w+")
        tokenized = [tokenizer.tokenize(s.lower()) for s in sentence]
        tkstime = time.time() - tkstime

        # Teks difilter dengan stopword:
        #   1. Mengimport Stopword
        #   2. Memfilter kata yang tidak penting
        #   3. Kata yang penting disimpan pada array
        brs2time = time.time()
        listStopword = set(stopwords.words("indonesian"))

        important_token = []
        for sent in tokenized:
            filtered = [s for s in sent if s not in listStopword]
            important_token.append(filtered)
        brs2time = time.time() - brs2time

        # Teks digabung :
        #   1. Stopword dihapus
        #   2. Teks yang penting digabungkan
        gbgtime = time.time()
        sw_removed = [" ".join(t) for t in important_token]
        gbgtime = time.time() - gbgtime

        # Teks distem :
        #   1. Mengimport Stemmer
        #   2. Penghilangan imbuhan pada kata
        stmtime = time.time()
        factory = StemmerFactory()
        stemmer = factory.create_stemmer()

        stemmed_sent = [stemmer.stem(sent) for sent in sw_removed]
        stmtime = time.time() - stmtime

        # Teks divektorisasi :
        #   1. Mengimport Vectorizer
        #   2. Teks diubah menjadi angka agar dapat diproses oleh mesin
        vkttime = time.time()
        vec = TfidfVectorizer(lowercase=True)
        document = vec.fit_transform(stemmed_sent)

        documents = document.toarray()
        vkttime = time.time() - vkttime

        # Teks dipilih dan diurutkan
        #   1. Kalimat dipilih (n) sebagai ringkasan
        #   2. Kalimat diurutkan
        urttime = time.time()

        n = panjang
        result = np.sum(documents, axis=1)
        sorted(result)

        top_n = np.argsort(result)[-n:]

        summ_index = sorted(top_n)
        urttime = time.time() - urttime

        # Teks diringkas
        rkstime = time.time()

        summarized = []
        for i in summ_index:
            summarized.append(sentence[i])
        rkstime = time.time() - rkstime
        jmlhtime = (
            brs1time
            + tkstime
            + brs2time
            + gbgtime
            + stmtime
            + vkttime
            + urttime
            + rkstime
        )
        st.text_area(
            label="Teks yang sudah diringkas:",
            height=200,
            value=("".join(map(str, summarized))),
        )
    st.success("Sukses!")
    st.text(
        "Teks anda telah diringkas dengan metode extractive selama %.2f detik"
        % jmlhtime
    )

    # Bagian Penjelasan Cara Kerja
    st.title("Proses Peringkasan :")
    with st.expander("1. Teks disimpan untuk di proses"):
        st.text_area(
            label="Langkah pertama adalah program akan menyimpan teks yang telah anda masukkan ke dalam variabel bernama text. Berikut adalah teks yang anda masukkan :",
            value=rawtext,
            height=200,
        )
    with st.expander("2. Teks Dibersihkan (1/2)"):
        st.text_area(
            label="Langkah kedua adalah teks dibersihkan dengan cara menghilangkan garis baru atau paragraf. Berikut adalah hasil teks anda yang sudah dihilangkan garis baru atau paragraf nya:",
            value=text,
            height=200,
        )
        x = len(sentence)
        y = np.array(sentence)
        df = pandas.DataFrame({"No.": (1 + i for i in range(x)), "Kalimat": y})
        style = df.style.hide_index()
        st.write(
            """Setelah teks di bersihkan, lalu teks dipecah menjadi per kalimat. Berikut adalah hasil teks anda yang sudah dipecah menjadi %i kalimat:"""
            % x,
            style.to_html(),
            unsafe_allow_html=True,
        )
        st.write(
            """Teks anda dibersihkan dan diubah menjadi kalimat pada proses diatas selama %2f detik.
        """
            % brs1time
        )
    with st.expander("3. Kalimat diubah menjadi token"):
        x = len(tokenized)
        y = np.array(tokenized)
        df = pandas.DataFrame({"No.": (1 + i for i in range(x)), "Token": y})
        style = df.style.hide_index()
        st.write(
            """Langkah ketiga adalah kalimat yang sudah dibersihkan dan dipecah, diubah menjadi token token atau per kata dengan cara Tokenisasi serta diubah menjadi huruf kecil. Berikut adalah hasil teks anda yang sudah diubah menjadi token:""",
            style.to_html(),
            unsafe_allow_html=True,
        )
        st.write(
            """Kalimat anda ditokenisasi pada proses diatas selama %2f detik.
        """
            % tkstime
        )

    with st.expander("4. Token Dibersihkan (2/2)"):
        x = len(important_token)
        y = np.array(important_token)
        df = pandas.DataFrame({"No.": (1 + i for i in range(x)), "Token": y})
        style = df.style.hide_index()
        st.write(
            """Langkah keempat adalah sistem akan membuang token atau kata tidak penting yang ada pada kamus Stopword indonesia dan hanya menyimpan token atau kata penting saja untuk diproses nanti nya. Berikut adalah hasil token yang disimpan:""",
            style.to_html(),
            unsafe_allow_html=True,
        )
        st.write(
            """Token anda dibersihkan pada proses diatas selama %2f detik.
        """
            % brs2time
        )

    with st.expander("5. Token Digabungkan"):
        x = len(sw_removed)
        y = np.array(sw_removed)
        df = pandas.DataFrame({"No.": (1 + i for i in range(x)), "Kalimat": y})
        style = df.style.hide_index()
        st.write(
            """Langkah kelima adalah token token yang penting akan digabung kembali menjadi kalimat. Berikut adalah hasil kalimat yang telah diproses:""",
            style.to_html(),
            unsafe_allow_html=True,
        )
        st.write(
            """Token anda digabungkan pada proses diatas selama %2f detik.
        """
            % gbgtime
        )
    with st.expander("6. Menghilangkan imbuhan pada kata"):
        x = len(stemmed_sent)
        y = np.array(stemmed_sent)
        df = pandas.DataFrame({"No.": (1 + i for i in range(x)), "Kalimat": y})
        style = df.style.hide_index()
        st.write(
            """Langkah keenam adalah proses menghilangkan imbuhan pada kata dengan proses Stemming. Berikut adalah hasil kalimat yang telah di proses:""",
            style.to_html(),
            unsafe_allow_html=True,
        )
        st.write(
            """Token anda digabungkan pada proses diatas selama %2f detik.
        """
            % stmtime
        )
    with st.expander("7. Mengubah teks agar dapat di proses"):
        tokenizer = nltk.RegexpTokenizer(r"\w+")
        tokenized2 = [tokenizer.tokenize(s.lower()) for s in stemmed_sent]
        mylist = []
        for tokendua in tokenized2:
            for tokenkedua in tokendua:
                tokke = tokenkedua
                mylist.append(tokke)
        mylist

        st.dataframe(data=documents)
        st.dataframe(data=mylist)

        st.write(
            """Token anda digabungkan pada proses diatas selama %2f detik.
        """
            % vkttime
        )

    st.success("Thats how its done! now you know how it works, congratulations!")

    # st.success("""
    # gelar
    # perdana
    # motogp
    # mandalika
    # gp
    # indonesia
    # red
    # bull
    # ktm
    # miguel
    # oliveira
    # minggu
    # 20
    # 3
    # 2022
    # tempat
    # yamaha
    # podium
    # tiga
    # menang
    # pramac
    # ducati
    # johann
    # zarco
    # pertamina
    # grand
    # prix
    # of
    # saji
    # tegang
    # fabio
    # quartararo
    # balap
    # pole
    # position
    # hasil
    # tahan
    # posisi
    # start

    # """)
