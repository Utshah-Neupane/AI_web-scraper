#Front-end designing

import streamlit as st

st.title("AI Web Scraper")
url = st.text_input("Enter a website URL: ")

if st.button("Scraper Site"):
    st.write("Scraping the website)")