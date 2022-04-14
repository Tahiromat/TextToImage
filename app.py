import streamlit as st 
from googletrans import Translator
from  translate_input_text import translate_inputtext2eng

translator = Translator()

st.title('Text To Image Application')
INPUT_TEXT = st.text_input("Type what you want to draw: ").click()
result = translate_inputtext2eng(translator, INPUT_TEXT)
st.write(result.text)