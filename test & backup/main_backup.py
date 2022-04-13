import streamlit as st
import numpy as np
import re
import nltk
from nltk.corpus import stopwords
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
from sklearn.feature_extraction.text import TfidfVectorizer
nltk.download('stopwords')
nltk.download('punkt')


st.set_page_config(
        page_title="2 Text Summarization",
        page_icon="🖥️",
        initial_sidebar_state="expanded"
    )

st.title('Aplikasi Peringakasan Teks')
st.write(
    """
    Halaman web ini dapat meringkas teks menggunakan metode ekstraktif maupun deksriptif.
    """
)

rawtext = st.text_area(label="Masukkan teks yang akan diringkas :", value="", max_chars=None, placeholder="Masukkan teks yang akan diringkas", disabled=False, height=200)

st.spinner(text="In progress...")
exsum = st.button("Extractive Summarization")

if exsum:
    with st.spinner('Please wait, your text is being summarized'):
        text = rawtext.replace('\n', '')
        sentence = re.split('\. |\.',text)

        tokenizer = nltk.RegexpTokenizer(r"\w+")
        tokenized = [tokenizer.tokenize(s.lower()) for s in sentence]

        listStopword =  set(stopwords.words('indonesian'))

        important_token = []
        for sent in tokenized:
            filtered = [s for s in sent if s not in listStopword]
            important_token.append(filtered)
        
        sw_removed = [' '.join(t) for t in important_token]

        factory = StemmerFactory()
        stemmer = factory.create_stemmer()

        stemmed_sent = [stemmer.stem(sent) for sent in sw_removed]

        vec = TfidfVectorizer(lowercase=True)
        document = vec.fit_transform(stemmed_sent)

        document = document.toarray()

        n = 2 
        result = np.sum(document, axis=1)

        sorted(result)

        top_n = np.argsort(result)[-n:]
        
        summ_index = sorted(top_n)

        summarized = [] 
        for i in summ_index:
            summarized.append(sentence[i]) 
        
        st.text_area(label="Teks yang sudah diringkas :", height=200, value=(''.join(map(str, summarized))))
    st.success('Done!')
    st.title('How it works :')
    with st.expander("1. Input Text"):
        st.text_area(label="Langkah pertama adalah program akan menyimpan teks yang telah anda masukkan ke dalam variabel bernama text. Berikut adalah teks yang anda masukkan :", value=text, height=200)
    st.success('Thats how its done! now you know how it works, congratulations!')