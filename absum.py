import os
import pandas
from unicodedata import decimal
import streamlit as st
import time
from transformers import PegasusForConditionalGeneration, PegasusTokenizer


def procabsum(rawtext):
    with st.spinner("Mohon tunggu, teks sedang dalam proses peringkasan"):
        simpantime = time.time()
        # menyimpan input text
        text = rawtext
        simpantime = time.time() - simpantime

        siaptime = time.time()
        # Mempersiapkan package yang akan digunakan

        # Untuk mendownload model terlebih dahulu
        # tokenizer = PegasusTokenizer.from_pretrained("google/pegasus-xsum")

        # Untuk menyimpan model yang telah selesai di download secara lokal
        # tokenizer.save_pretrained("local_pegasus-xsum_tokenizer")
        
        # Untuk mendownload model terlebih dahulu
        # model = PegasusForConditionalGeneration.from_pretrained("google/pegasus-xsum")
        
        # Untuk mendownload model yang telah selesai di download secara lokal
        # model.save_pretrained("local_pegasus-xsum_tokenizer_model")

        # Import tokenizer secara lokal
        tokenizer = PegasusTokenizer.from_pretrained("local_pegasus-xsum_tokenizer")
        # Import model secara lokal
        model = PegasusForConditionalGeneration.from_pretrained("local_pegasus-xsum_tokenizer_model")
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
        "Teks telah diringkas dengan metode Abstractive selama %.2f detik" % jmlhtime
    )

    # Bagian Penjelasan Cara Kerja
    st.title("Proses Peringkasan :")
    with st.expander("1. Teks disimpan untuk di proses"):
        st.text_area(
            label="Langkah pertama adalah program akan menyimpan teks yang telah dimasukkan. Berikut adalah teks yang dimasukkan:",
            value=text,
            height=200,
        )

    with st.expander("2. Mempersiapkan Library Google Pegasus"):
        st.write(
            """Langkah kedua adalah program menyiapkan Library Google Pegasus untuk memproses peringkasan teks. Berikut adalah library yang digunakan:<br>
            
             - Tokenizer = PegasusTokenizer.from_pretrained("google/pegasus-xsum")<br>
             
             - Model     = PegasusForConditionalGeneration.from_pretrained("google/pegasus-xsum")
             """
        )

        st.write(
            """Program menyiapkan Library yang akan digunakan untuk meringkas pada proses diatas selama %2f detik.
        """
            % siaptime
        )

    with st.expander("3. Kalimat diubah menjadi token"):
        st.write(
            """Langkah ketiga adalah teks diubah menjadi token token atau per kata dengan cara Tokenisasi serta diubah menjadi angka agar dapat di proses oleh program. Berikut adalah hasil teks yang sudah diubah menjadi token:
        """
        )
        inputid = []
        attentionmask = []
        for i in tokens["input_ids"]:
            for a in i:
                inputid.append(a)
        for i in tokens["attention_mask"]:
            for a in i:
                attentionmask.append(a)

        x = len(inputid)
        y = inputid
        z = attentionmask
        df = pandas.DataFrame(
            {"Input ID": y, "Attention Mask":z}
        )
        style = df
        st.write("",
            style.to_html(),
            unsafe_allow_html=True,
        )
        st.write(
            """Teks diubah menjadi token pada proses diatas selama %2f detik.
        """
            % tokentime
        )
    
    with st.expander("4. Token di proses untuk diringkas"):
        jml = len(summary[0])
        st.write(
        """Token diproses untuk diringkas, program memilih sebanyak %i token. Berikut adalah hasil kumpulan token yang sudah dipilih sebagai ringkasan: """ % jml
        )
        st.dataframe(
            data = summary
        )
        st.write(
        "Token telah diringkas dengan metode Abstractive selama %.2f detik" % summtime
        )

    with st.expander("5. Token yang dipilih, dirangkai menjadi kalimat"):
        st.write(
        """Langkah terakhir adalah program mendecode token token yang sudah dipilih, proses ini mengubah token kembali menjadi kata. Berikut adalah hasil ringkasan: """
        )
        st.success(summarized)
        st.write(
        """Token dirangkai pada proses diatas selama %.2f detik""" % dectime
        )
        st.write(
         """Keseluruhan proses peringkasan diatas dari awal hingga akhir diproses selama %2f detik.
        """
            % jmlhtime
        )

    st.success(
        "Seperti itulah cara kerja peringkasan teks dengan menggunakan metode Abstractive Summarization Google Pegasus's Library. Selamat! Sekarang anda sudah mengerti bagaimana proses peringkasan teks bekerja."
    )
