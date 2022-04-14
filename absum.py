import os
import streamlit as st
import time
from transformers import PegasusForConditionalGeneration, PegasusTokenizer


def procabsum(rawtext):
    start_time = time.time()
    with st.spinner('Please wait, your text is being summarized (1/2)'):
        tokenizer = PegasusTokenizer.from_pretrained("google/pegasus-xsum")

        model = PegasusForConditionalGeneration.from_pretrained("google/pegasus-xsum")

        text = rawtext
    
    st.text("Teks telah diimport selama %.2f detik" % (time.time() - start_time))

    start_time = time.time()
    with st.spinner('Please wait, your text is being Tokenized'):
        # Create tokens - number representation of our text
        tokens = tokenizer(text, truncation=True, padding="longest", return_tensors="pt")

        # Input tokens
        tokens
    
    st.text("Teks telah ditokenisasi selama %.2f detik" % (time.time() - start_time))

    start_time = time.time()
    with st.spinner('Please wait, your text is being Summarized (2/2)'):
        # Summarize 
        summary = model.generate(**tokens)

        # Output summary tokens
        summary[0]
    
    st.text("Teks telah diringkas selama %.2f detik" % (time.time() - start_time))

    start_time = time.time()
    with st.spinner('Please wait, your text is being Decoded'):
        # Decode summary
        summarized = tokenizer.decode(summary[0])
    
    st.text("Teks telah dibdecode selama %.2f detik" % (time.time() - start_time))

        
    st.text_area(label="Teks yang sudah diringkas :", height=200, value=(''.join(map(str, summarized))))
    st.success('Done!')

    st.title('How it works :')
    with st.expander("1. Input Text"):
        st.text_area(label="Langkah pertama adalah program akan menyimpan teks yang telah anda masukkan ke dalam variabel bernama text. Berikut adalah teks yang anda masukkan :", value=text, height=200)
    st.success('Thats how its done! now you know how it works, congratulations!')