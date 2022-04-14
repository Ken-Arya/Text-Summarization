import streamlit as st
import exsum
import absum
from exsum import procexsum
from absum import procabsum

st.set_page_config(
        page_title="2 Text Summarization",
        page_icon="🖥️",
        initial_sidebar_state="expanded"
    )

st.title('Aplikasi Peringakasan Teks')
st.write(
    """
    Halaman web ini dapat meringkas teks menggunakan metode ekstraktif maupun abstraktif.
    """
)

rawtext = st.text_area(label="Masukkan teks yang akan diringkas :", value="", max_chars=None, placeholder="Masukkan teks yang akan diringkas", disabled=False, height=200)

st.spinner(text="In progress...")
exsummary = st.button("Extractive Summarization")
absummary = st.button("Abstractive Summarization")

if exsummary:
    exsum.procexsum(rawtext)

if absummary:
    absum.procabsum(rawtext)

    

