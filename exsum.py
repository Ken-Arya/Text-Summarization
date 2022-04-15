# import library yang akan digunakan
import os
import streamlit as st
import numpy as np
import re
import nltk
import time
from nltk.corpus import stopwords
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
from sklearn.feature_extraction.text import TfidfVectorizer

nltk.download("stopwords")
nltk.download("punkt")

# proses extractive summary yang akan dijalankan dengan metode TF-IDF


def procexsum(rawtext, panjang):

    # Teks dibersihkan :
    #   1. Menghapus Garis baru (new line)
    #   2.Teks dipecah menjadi per kalimat
    brs1time = time.time()
    with st.spinner("Mohon tunggu, teks anda sedang dibersihkan 1/3"):
        text = rawtext.replace("\n", "")
        sentence = re.split("\. |\.", text)
    brs1time = time.time() - brs1time

    # Teks di tokenisasi :
    #   1. Tokenizer membaca
    #   2. Ditokenisasi (Dipecah menjadi kata per kata) dan diubah menjadi huruf kecil
    tkstime = time.time()
    with st.spinner("Mohon tunggu, teks anda sedang ditokenisasi"):
        tokenizer = nltk.RegexpTokenizer(r"\w+")
        tokenized = [tokenizer.tokenize(s.lower()) for s in sentence]
    tkstime = time.time() - tkstime

    # Teks difilter dengan stopword:
    #   1. Mengimport Stopword
    #   2. Memfilter kata yang tidak penting
    #   3. Kata yang penting disimpan pada array
    brs2time = time.time()
    with st.spinner("Mohon tunggu, teks anda sedang dibersihkan 2/3"):
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
    with st.spinner("Mohon tunggu, teks anda sedang digabungkan kembali"):
        sw_removed = [" ".join(t) for t in important_token]
    gbgtime = time.time() - gbgtime

    # Teks distem :
    #   1. Mengimport Stemmer
    #   2. Penghilangan imbuhan pada kata
    stmtime = time.time()
    with st.spinner("Mohon tunggu, teks anda sedang dibersihkan 3/3"):
        factory = StemmerFactory()
        stemmer = factory.create_stemmer()

        stemmed_sent = [stemmer.stem(sent) for sent in sw_removed]
    stmtime = time.time() - stmtime

    # Teks divektorisasi :
    #   1. Mengimport Vectorizer
    #   2. Teks diubah menjadi angka agar dapat diproses oleh mesin
    vkttime = time.time()
    with st.spinner("Mohon tunggu, teks anda sedang disiapkan untuk diproses"):
        vec = TfidfVectorizer(lowercase=True)
        document = vec.fit_transform(stemmed_sent)

        document = document.toarray()
    vkttime = time.time() - vkttime

    # Teks dipilih dan diurutkan
    #   1. Kalimat dipilih (n) sebagai ringkasan
    #   2. Kalimat diurutkan
    urttime = time.time()
    with st.spinner("Mohon tunggu, teks anda sedang diringkas"):

        n = panjang
        result = np.sum(document, axis=1)
        sorted(result)

        top_n = np.argsort(result)[-n:]

        summ_index = sorted(top_n)
    urttime = time.time() - urttime

    # Teks diringkas
    rkstime = time.time()
    with st.spinner("Mohon tunggu, teks anda sedang disiapkan"):
        summarized = []
        for i in summ_index:
            summarized.append(sentence[i])
    rkstime = time.time() - rkstime
    jmlhtime = (
        brs1time + tkstime + brs2time + gbgtime + stmtime + vkttime + urttime + rkstime
    )
    st.text_area(
        label="Teks yang sudah diringkas:",
        height=200,
        value=("".join(map(str, summarized))),
    )
    st.success(
        "Selamat! teks anda telah diringkas dengan metode extractive selama %.2f detik"
        % jmlhtime
    )

    # Bagian Penjelasan Cara Kerja
    st.title("How it works :")
    with st.expander("1. Input Text"):
        st.text_area(
            label="Langkah pertama adalah program akan menyimpan teks yang telah anda masukkan ke dalam variabel bernama text. Berikut adalah teks yang anda masukkan :",
            value=text,
            height=200,
        )
    st.success("Thats how its done! now you know how it works, congratulations!")
