from lib2to3.pgen2 import token
import os
from unicodedata import decimal
import streamlit as st
import time
from tokenizers import Tokenizer
from transformers import PegasusForConditionalGeneration, PegasusTokenizer


def procabsum(rawtext):
    with st.spinner("Mohon tunggu, teks anda sedang dalam proses peringkasan"):
        simpantime = time.time()
        # menyimpan input text
        text = rawtext
        simpantime = time.time() - simpantime

        siaptime = time.time()
        # Mempersiapkan package yang akan digunakan
        # Import tokenizer
        tokenizer = PegasusTokenizer.from_pretrained("google/pegasus-xsum")
        # Import model
        model = PegasusForConditionalGeneration.from_pretrained("google/pegasus-xsum")
        siaptime = time.time() - siaptime

        tokentime = time.time()
        # Create tokens - number representation of our text
        tokens = tokenizer(
            text, truncation=True, padding="longest", return_tensors="pt"
        )
        tokentime = time.time() - tokentime

        summtime = time.time()
        # Summarize
        summary = model.generate(**tokens)
        summtime = time.time() - summtime

        dectime = time.time()
        # Decode summary
        summarized = tokenizer.decode(summary[0])
        dectime = time.time() - dectime

        jmlhtime = simpantime + siaptime + tokentime + summtime + dectime

    st.text_area(
        label="Teks yang sudah diringkas :",
        height=200,
        value=("".join(map(str, summarized))),
        key="main",
    )
    st.success("Sukses!")
    st.text(
        "Teks anda telah diringkas dengan metode Abstractive selama %.2f detik"
        % jmlhtime
    )

    # Bagian Penjelasan Cara Kerja
    st.title("Proses Peringkasan :")
    with st.expander("1. Teks disimpan untuk di proses"):
        st.text_area(
            label="Langkah pertama adalah program akan menyimpan teks yang telah anda masukkan. Berikut adalah teks yang anda masukkan:",
            value=text,
            height=200,
        )
    with st.expander("2. Mempersiapkan Library Google Pegasus"):
        st.write(
            """Langkah kedua adalah program menyiapkan Library Google Pegasus untuk memproses peringkasan teks. Berikut adalah library yang digunakan:
            
             - Tokenizer = PegasusTokenizer.from_pretrained("google/pegasus-xsum")
             
             - Model     = PegasusForConditionalGeneration.from_pretrained("google/pegasus-xsum")
             """
        )

    st.success(
        "Seperti itulah cara kerja peringkasan teks dengan menggunakan metode Abstractive Google Pegasus's Library. Selamat! Sekarang anda sudah mengerti bagaimana proses peringkasan teks bekerja."
    )
