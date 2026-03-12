import streamlit as st
import pandas as pd
# from main import artist_df

# 1. Set the page title
st.set_page_config(page_title="Tam & Plam 19 July 2026",
                   layout="wide",
                   initial_sidebar_state="expanded")

st.title("Tam & Plam 19 July 2026")
st.subheader("Generic information for our most special day ❤️")
st.divider()
st.write("Welcome to our wedding page! We are so happy you’re here.")


# 2. Add the text and the link
# Streamlit supports Markdown for easy link formatting
st.write(
    "They say all roads lead to love, and ours has led us to the beautiful streets of Vienna. ")

st.write("We are Tamar and Plamen, and we couldn’t be more thrilled to invite you to join us as we say “I do.” To us, this day isn’t just about a ceremony, it’s a celebration of the journey we’ve shared and the many adventures yet to come.On July 19, 2026, amidst the history and charm of this incredible city, we will start our new chapter. Having our favorite people by our side as we celebrate our love means the world to us. We can’t wait to dance, laugh, and make memories with you all!")

st.image('hands.jpg', width=500)

# height sizing
# st.markdown(
#     '<style>img {max-height: 300px; object-fit: contain;}</style>', unsafe_allow_html=True)

st.divider()


# 3. Background image
def add_bg_from_url():
    st.markdown(
        f"""
         <style>
         .stApp {{
             background-image: url("https://images.unsplash.com/photo-1507525428034-b723cf961d3e");
             background-attachment: fixed;
             background-size: cover;
         }}
         .stApp::before {{
            content: "";
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background-color: rgba(255, 255, 255, 0.9); /* This creates the 90% transparency effect */
            z-index: -1;
         }}
         </style>
         """,
        unsafe_allow_html=True
    )


add_bg_from_url()
