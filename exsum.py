import streamlit as st
import numpy as np
import re
import nltk
import time
from nltk.corpus import stopwords
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
from sklearn.feature_extraction.text import TfidfVectorizer
nltk.download('stopwords')
nltk.download('punkt')

def procexsum(rawtext):
    
    start_time = time.time()
    with st.spinner('Please wait, your text is being Cleaned (1/2)'):
        text = rawtext.replace('\n', '')
        sentence = re.split('\. |\.',text)
    st.text("Teks telah dibersihkan selama %.2f detik" % (time.time() - start_time))
     

    start_time = time.time()
    with st.spinner('Please wait, your text is being Tokenized'):
        tokenizer = nltk.RegexpTokenizer(r"\w+")
        tokenized = [tokenizer.tokenize(s.lower()) for s in sentence]
    st.text("Teks telah ditokenisasi selama %.2f detik" % (time.time() - start_time))
     

    start_time = time.time()
    with st.spinner('Please wait, your text is being work on Stopword'):
        listStopword =  set(stopwords.words('indonesian'))

        important_token = []
        for sent in tokenized:
            filtered = [s for s in sent if s not in listStopword]
            important_token.append(filtered)
    st.text("Teks telah dilakukan stopword selama %.2f detik" % (time.time() - start_time))
     
    
    start_time = time.time()
    with st.spinner('Please wait, your text is being Cleaned (2/2)'):
        sw_removed = [' '.join(t) for t in important_token]
    st.text("Teks telah dibersihkan selama %.2f detik" % (time.time() - start_time))
     

    start_time = time.time()
    with st.spinner('Please wait, your text is being Stemmed'):
        factory = StemmerFactory()
        stemmer = factory.create_stemmer()

        stemmed_sent = [stemmer.stem(sent) for sent in sw_removed]
    st.text("Teks telah distem selama %.2f detik" % (time.time() - start_time))
     

    start_time = time.time()
    with st.spinner('Please wait, your text is being Vectorized'):
        vec = TfidfVectorizer(lowercase=True)
        document = vec.fit_transform(stemmed_sent)

        document = document.toarray()

        n = 2 
        result = np.sum(document, axis=1)
    st.text("Teks telah divektorisasi selama %.2f detik" % (time.time() - start_time))
     

    start_time = time.time()
    with st.spinner('Please wait, your text is being Sorted'):
        sorted(result)

        top_n = np.argsort(result)[-n:]
        
        summ_index = sorted(top_n)
    st.text("Teks telah disortir selama %.2f detik" % (time.time() - start_time))
     

    
    start_time = time.time()
    with st.spinner('Please wait, your text is being Summarized'):
        summarized = [] 
        for i in summ_index:
            summarized.append(sentence[i]) 
    st.text("Teks telah diringkas selama %.2f detik" % (time.time() - start_time))
     
        
    st.text_area(label="Teks yang sudah diringkas :", height=200, value=(''.join(map(str, summarized))))
    st.success('Done!')

    st.title('How it works :')
    with st.expander("1. Input Text"):
        st.text_area(label="Langkah pertama adalah program akan menyimpan teks yang telah anda masukkan ke dalam variabel bernama text. Berikut adalah teks yang anda masukkan :", value=text, height=200)
    st.success('Thats how its done! now you know how it works, congratulations!')