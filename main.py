import streamlit as st
from streamlit_option_menu import option_menu

# --- CONSTANTS & CONFIG ---
MAP_CHURCH = "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d2658.802470030058!2d16.386907376844075!3d48.2104205460865!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x476d070c5857a5fb%3A0x9e8c33afc607b242!2sArmenische%20Kirche%20Wien!5e0!3m2!1sde!2sat!4v1773255546996!5m2!1sde!2sat"
MAP_RESTAURANT = "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d5168.031708593825!2d16.451891614532386!3d48.19249238494649!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x476d00bc287b8277%3A0xcffa4f8fe89495b1!2sRistorante%20Vabene!5e0!3m2!1sde!2sat!4v1773255031475!5m2!1sde!2sat"

st.set_page_config(
    page_title="Tam & Plam | 19 July 2026",
    page_icon="❤️",
    layout="wide"
)

# Custom CSS for a more polished look
st.markdown("""
    <style>
    .main {
        font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
    }
    .stTitle {
        font-weight: 700;
        color: #2E4053;
    }
    hr {
        margin-top: 1rem;
        margin-bottom: 1rem;
    }
    /* Sticky Navigation Logic */
    [data-testid="stHeader"] {
        display: none;
    }
    .main .block-container {
        padding-top: 2rem;
    }
    div[data-testid="stVerticalBlock"] > div:nth-child(2) {
        position: sticky;
        top: 0;
        z-index: 1000;
        background-color: white;
    }
    </style>
    """, unsafe_allow_html=True)


# 1. Create the horizontal navigation bar
selected = option_menu(
    menu_title=None,
    options=["Home", "Locations", "FAQ", "About Us"],
    icons=["house", "geo-alt", "patch-question", "info-circle"],
    menu_icon="cast",
    default_index=0,
    orientation="horizontal",
)

# --- SHARED COMPONENTS (REUSABLE) ---


def render_locations():
    st.title("Main locations for Sunday 19 July 2026")
    st.info("As we organize further details of the wedding day - further locations and time-table will be posted.")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("⛪ Armenische Kirche Wien")
        st.write("**Address:** Kolonitzgasse 11, 1030 Wien")
        st.caption("Arrival: From 15:30")
        st.components.v1.html(
            f'<iframe src="{MAP_CHURCH}" width="100%" height="400" style="border:0;" allowfullscreen="" loading="lazy"></iframe>',
            height=410
        )

    with col2:
        st.subheader("🍴 Ristorante Vabene")
        st.write("**Address:** Lindmayer Straße 1, 1020 Wien")
        st.caption("Arrival: From 17:00")
        st.components.v1.html(
            f'<iframe src="{MAP_RESTAURANT}" width="100%" height="400" style="border:0;" allowfullscreen="" loading="lazy"></iframe>',
            height=410
        )


def render_faq():
    st.title("FAQ")
    st.subheader("Frequently Asked Questions")
    st.write(
        "If you have any other questions, please feel free to reach out to us directly!")

    with st.expander("What is the dress code?"):
        st.write("The dress code is **semi-formal**. Think cocktail dresses or a nice suit. Feel free to add a pop of color!")

    with st.expander("Will there be vegetarian or vegan meal options?"):
        st.write("Absolutely! We will have a variety of options. Please let us know if you have specific dietary restrictions.")

    with st.expander("How can I confirm my attendance?"):
        st.write("You can confirm your attendance by calling or texting us directly.")

    with st.expander("How do I get to the church?"):
        st.write("The church is in the 3rd district and easily accessible by public transport. See the Locations page for details.")

    with st.expander("How do I get to the restaurant?"):
        st.write("There will be an organized **bus shuttle** from the church to the restaurant. You can also arrive via own car or taxi.")

    with st.expander("Will there be return transportation at the end of the night?"):
        st.write(
            "No. We recommend using Uber or local taxis to return to your accommodation safely.")

    with st.expander("Do you have a wedding gift registry?"):
        st.write(
            "We prefer monetary gifts to help us create our dream honeymoon and future together.")

# --- PAGE FUNCTIONS ---


def show_home():
    t1, t2 = st.columns([2, 1])
    with t1:
        st.title("Tam & Plam")
        st.header("19 July 2026")
        st.subheader("❤️ Generic information for our most special day ❤️")

    st.divider()

    col1, col2 = st.columns([3, 2])
    with col1:
        st.write("### Welcome!")
        st.write(
            "They say all roads lead to love, and ours has led us to the beautiful streets of Vienna.")
        st.write("We are Tamar and Plamen, and we couldn’t be more thrilled to invite you to join us as we say “I do.” To us, this day isn’t just about a ceremony, it’s a celebration of the journey we’ve shared and the many adventures yet to come.")
        st.write("Having our favorite people by our side as we celebrate our love means the world to us. We can’t wait to dance, laugh, and make memories with you all!")

    with col2:
        st.image('new_Ai.jpg', use_container_width=True,
                 caption="Tamar & Plamen")

    st.warning(
        "As many aspects are still being planned, please check back frequently for updates!")


def show_menu():
    st.title("Menu")
    st.subheader("Aperitif")
    st.write(
        "Includes Prosecco, Mimosa (Prosecco Orange), Aperol Spritz, and Hugo. For our younger guests: orange juice, fruit juices, soda water.")
    st.divider()
    st.subheader("Mediterranean Appetizer Platter")
    st.write(
        "Mediterranean olive and feta salad, savory meatballs, Parmesan, Chorizo, caper berries, stuffed grape leaves, Norwegian smoked salmon, pesto, San Daniele prosciutto, baby mozzarella with cherry tomatoes and basil pesto. Served with oven-fresh garlic bread.")
    st.divider()
    st.subheader("Main course")
    # st.write("Pork Medallions in a green peppercorn cream sauce.")
    st.write("Marinated Corn-fed Chicken Breast in a wild mushroom ragout.")
    st.write("Cannelloni stuffed with spinach and feta, gratinéed with mozzarella.")
    st.write("Salmon with lemon-caper butter.")
    st.write(" Mixed Roast(Chicken, Pork, Cured Pork, and Vegetables).")
    st.divider()
    st.subheader("Beverages")
    st.write("Cocktails: Aperol Spritz, Hugo.")
    st.write(
        "Soft Drinks: Apple juice, Cola, Fanta, Iced tea, Orange juice, Soda water.")
    st.write("Draught Beer: Budweiser")
    st.write(
        "Wines: Grüner Veltliner (White) and Zweigelt (Red) from the Pridt Winery.")
    st.write("Coffee & Hot Drinks: Wiener Melange, Kleiner Brauner (Espresso with a dash of milk), Hot Cocoa, Caffè Latte, and various Teas")
    st.divider()


def show_about():
    st.title("About Us")
    st.subheader("Our Story")
    st.write(
        "We met in Vienna and instantly connected over our shared love of travel and adventure...")
    st.image('ring.jpg', width=600)
    st.divider()


# --- ROUTING ---
if selected == "Home":
    show_home()
elif selected == "Locations":
    render_locations()
elif selected == "FAQ":
    render_faq()
elif selected == "About Us":
    show_about()
