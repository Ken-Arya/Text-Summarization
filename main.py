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
    layout="wide"
)
# Remove whitespace from the top of the page and sidebar
st.markdown(meta.REMOVEHEADER, unsafe_allow_html=True)
st.title(meta.HEADER)

col1, col2 = st.columns([5, 5])
with col1:  
    rawtext = st.text_area(label="Masukkan teks yang ingin diringkas :", value="", max_chars=None, placeholder="Masukkan teks yang ingin diringkas", disabled=False, height=200)

    exsummary = st.button("Extractive Summarization")
    absummary = st.button(label="Abstractive Summarization", disabled=True)
    st.title('Petunjuk Penggunaan:')
    with st.expander("Harap dibaca petunjuk dibawah ini sebelum menggunakan fitur peringkas teks!", expanded=True):
            st.markdown(meta.CAPTIONS, unsafe_allow_html=True)

with col2:
    if exsummary:
        exsum.procexsum(rawtext)
    if absummary:
        absum.procabsum(rawtext)
    
