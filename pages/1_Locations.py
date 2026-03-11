import streamlit as st
import pandas as pd
# from main import artist_df

st.set_page_config(page_title="Locations info", page_icon="👋")

st.title("Tam & Plam 19 July 2026")
st.subheader("Generic information")


# 1. Set the page title
st.set_page_config(page_title="My Test Page")

# 2. Add the text and the link
# Streamlit supports Markdown for easy link formatting
st.write(
    "Test case, please check details on: [google.com](https://www.google.com)")

st.divider()

# 3. Add a Google Map frame for Los Angeles Beach (Santa Monica area)
st.subheader("Location: Ristorante Vabene")
st.text("From 17:00")

# Note: For a quick test without an API key, we can use a standard embed URL:
simple_map_url = "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d5168.031708593825!2d16.451891614532386!3d48.19249238494649!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x476d00bc287b8277%3A0xcffa4f8fe89495b1!2sRistorante%20Vabene!5e0!3m2!1sde!2sat!4v1773255031475!5m2!1sde!2sat"

st.components.v1.html(
    f'<iframe src="{simple_map_url}" width="100%" height="450" style="border:0;" allowfullscreen="" loading="lazy"></iframe>', height=460)
