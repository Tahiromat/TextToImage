# import click
# import streamlit as st 
from googletrans import Translator
# from  translate_input_text import translate_inputtext2eng

translator = Translator()
INPUT_TEXT = input("Type something that you want to convert an image: ")

# def translate_inputtext2eng(translator, INPUT_TEXT):
#     result = translator.translate(INPUT_TEXT)
#     return result

# st.title('Text To Image Application')
# INPUT_TEXT = st.text_input("Type what you want to draw: ")

result = result = translator.translate(INPUT_TEXT)

text = result.text
# st.markdown(result.text)


from big_sleep import Imagine

dream = Imagine(
    text = text,
    lr = 5e-2,
    save_every = 25,
    save_progress = True
)

dream()