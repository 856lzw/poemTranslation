import streamlit as st
import os
from utils import generate_poem_translation

st.header("诗词翻译器 ✏️")

theme = st.text_input("诗句")
submit = st.button("开始翻译")

if submit and not theme:
    st.info("请输入待翻译的诗句")
    st.stop()
if submit:
    with st.spinner("AI正在努力创作中，请稍等..."):
        result = generate_poem_translation(theme, openai_api_key)

    st.divider()
    st.markdown("##### 翻译结果")
    st.write(result.content)
