import streamlit as st
from spacy_streamlit import visualize_spans
import spacy
import toml

st.image("https://github.com/wjbmattingly/ww2-spacy/raw/main/images/header.png")
st.write("Currently using en_ww2spacy version 0.0.8")
with open("default_text.txt", "r") as f:
    default_text = f.read()

project_data = toml.load("project.toml")
text = st.text_area("Paste Text Here", value=default_text, height=500)

nlp = spacy.load("en_ww2spacy")
doc = nlp(text)
visualize_spans(doc, spans_key="ruler", displacy_options={"colors": project_data["colors"]})
