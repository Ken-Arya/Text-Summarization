import os
import streamlit as st
import exsum
import absum
import meta
from exsum import procexsum
from absum import procabsum

st.set_page_config(
    page_title="Aplikasi Text Summarization",
    page_icon="🖥️",
    initial_sidebar_state="expanded",
    layout="wide",
)
# Remove whitespace from the top of the page and sidebar
st.markdown(meta.REMOVEHEADER, unsafe_allow_html=True)
st.title(meta.HEADER)

col1, col2 = st.columns([5, 5])
with col1:
    rawtext = st.text_area(
        label="Masukkan teks yang ingin diringkas :",
        value="",
        max_chars=None,
        placeholder="Masukkan teks yang ingin diringkas",
        disabled=False,
        height=200,
    )
    panjang = st.slider("Pilih panjang ringkasan dalam skala 1-3(Kalimat) :", 1, 3, 1)
    exsummary = st.button("Extractive Summarization (Bahasa Indonesia)")
    absummary = st.button("Abstractive Summarization (English)", disabled=True)
    st.title("Petunjuk Penggunaan:")
    with st.expander("Baca petunjuk penggunaan!", expanded=False):
        st.markdown(meta.PETUNJUKPENGGUNAAN, unsafe_allow_html=True)
    with st.expander("Apa Itu Text Summarization?", expanded=False):
        st.markdown(meta.APAITUTEXTSUMMARIZATION, unsafe_allow_html=True)
    with st.expander(
        "Apa perbedaan Extractive Summarization dan Abstractive Summarization?",
        expanded=False,
    ):
        st.markdown(meta.PERBEDAANMETODE, unsafe_allow_html=True)

with col2:
    if exsummary:
        exsum.procexsum(rawtext, panjang)
    if absummary:
        absum.procabsum(rawtext)
