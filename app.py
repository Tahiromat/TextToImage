import click
import streamlit as st 
from googletrans import Translator
# from  translate_input_text import translate_inputtext2eng

translator = Translator()

def translate_inputtext2eng(translator, INPUT_TEXT):
    result = translator.translate(INPUT_TEXT)
    return result

st.title('Text To Image Application')
INPUT_TEXT = st.text_input("Type what you want to draw: ")
result = translate_inputtext2eng(translator, INPUT_TEXT)

st.markdown(result.text)