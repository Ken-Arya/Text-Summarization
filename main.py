import os
import streamlit as st
import exsum
import absum
import meta
from exsum import procexsum
from absum import procabsum

st.set_page_config(
    page_title="Peringaksan Teks",
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
    panjang = st.slider("Pilih panjang ringkasan dalam skala 1-3 :", 1, 3, 2)
    exsummary = st.button("Extractive Summarization")
    absummary = st.button("Abstractive Summarization", disabled=True)
    st.title("Petunjuk Penggunaan:")
    with st.expander("Petunjuk penggunaan!"):
        st.markdown(meta.CAPTIONS, unsafe_allow_html=True)

with col2:
    if exsummary:
        exsum.procexsum(rawtext, panjang)
    if absummary:
        absum.procabsum(rawtext)
