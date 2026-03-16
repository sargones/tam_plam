import streamlit as st
import pandas as pd
from streamlit_option_menu import option_menu

# 0. Set the page title
st.set_page_config(page_title="Tam & Plam 19 July 2026",
                   page_icon="❤️", layout="wide")

# 1. Create the horizontal navigation bar

selected = option_menu(
    menu_title=None,        # No title needed for the top bar
    options=["Home", "Locations",  "FAQ", "About Us"],  # "Menu",
    icons=["house", "geo-alt", "patch-question", "info-circle"],  # "cake2",
    menu_icon="cast",
    default_index=0,
    orientation="horizontal",
)


st.title("Tam & Plam")
st.title("19 July 2026")
st.subheader("❤️Generic information for our most special day❤️")
st.divider()


# --- 1. DEFINE YOUR "PAGES" AS FUNCTIONS ---


def show_home():
    st.write("Welcome to our wedding page! We are so happy you’re here.")
    st.write(
        "They say all roads lead to love, and ours has led us to the beautiful streets of Vienna.")
    st.write("We are Tamar and Plamen, and we couldn’t be more thrilled to invite you to join us as we say “I do.” To us, this day isn’t just about a ceremony, it’s a celebration of the journey we’ve shared and the many adventures yet to come.")
    st.write("On July 19, 2026, amidst the history and charm of this incredible city, we will start our new chapter. Having our favorite people by our side as we celebrate our love means the world to us. We can’t wait to dance, laugh, and make memories with you all!")

    st.image('new_Ai.jpg', width=500)

    st.write("As many aspects around the wedding organization are yet to be planned. Feel free to check the site more frequently towards our BIG day!")

    st.write(""
             ""
             ""
             ""
             "")
    st.divider()
    st.title("Main locations for Sunday 19 July 2026")
    st.subheader(
        "As we organize further details of the wedding day - further locations and time-table will be posted.")

    # 3. Add a Google Map frame for the church ()
    st.subheader("Armenische Kirche Wien")
    st.write("Address: Kolonitzgasse 11, 1030 Wien")
    st.text("From 15:30")

    simple_map_url = "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d2658.802470030058!2d16.386907376844075!3d48.2104205460865!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x476d070c5857a5fb%3A0x9e8c33afc607b242!2sArmenische%20Kirche%20Wien!5e0!3m2!1sde!2sat!4v1773255546996!5m2!1sde!2sat"

    st.components.v1.html(
        f'<iframe src="{simple_map_url}" width="100%" height="450" style="border:0;" allowfullscreen="" loading="lazy"></iframe>', height=460)

    # 4. Add a Google Map frame for the restaurant (Vabene)
    st.subheader("Location: Ristorante Vabene")
    st.write("Lindmayer Straße 1, Dammhaufengasse 50, 1020 Wien")
    st.text("From 17:00")

    simple_map_url = "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d5168.031708593825!2d16.451891614532386!3d48.19249238494649!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x476d00bc287b8277%3A0xcffa4f8fe89495b1!2sRistorante%20Vabene!5e0!3m2!1sde!2sat!4v1773255031475!5m2!1sde!2sat"

    st.components.v1.html(
        f'<iframe src="{simple_map_url}" width="100%" height="450" style="border:0;" allowfullscreen="" loading="lazy"></iframe>', height=460)

    st.write(""
             ""
             ""
             ""
             "")
    st.divider()
    st.title("FAQ")
    st.subheader("Frequently Asked Questions")
    st.write("Here are some common questions and answers about our wedding day. If you have any other questions, please feel free to reach out to us directly!")
    st.divider()
    st.subheader("What is the dress code?")
    st.write("We want everyone to feel comfortable and stylish! The dress code is semi-formal. Think cocktail dresses, dressy separates, or a nice suit. We encourage you to add a pop of color or a fun accessory to make it your own!")
    st.divider()
    st.subheader("Will there be vegetarian or vegan meal options?")
    st.write("Absolutely! We will have a variety of meal options to accommodate different dietary preferences, including some vegetarian dishes. Please let us know if you have any specific dietary restrictions or allergies so we can ensure there are delicious options for everyone.")
    st.divider()
    st.subheader("How can I confirm my attendance?")
    st.write("You can confirm your attendance by calling or texting us directly.")
    st.divider()
    st.subheader("How can I come to the church?")
    st.write("The church is located in the 3rd district of Vienna and is easily accessible by public transportation. Please check the Location page for the address details.")
    st.divider()
    st.subheader("How can I come to the restaurant?")
    st.write("There will be organized transportation from the church to the restaurant via bus shuttle. "
             "If you plan to come with own car or taxi, please check the Location page for the address details.")
    st.divider()
    st.subheader(
        "Will there be transportation from the restaurant at the end of the wedding party?")
    st.write("No. As everyone will have own energy-level at the end of the exciting day, feel free to organize your own transportation."
             "We recommend using Uber to get back to your accommodation safely.")
    st.divider()
    st.subheader("Do we have a list with preferred wedding gifts?")
    st.write("No. We do prefer to receive monetary gifts, which will help us to create our dream honeymoon and future together.")
    st.divider()


def show_locations():
    st.title("Main locations for Sunday 19 July 2026")
    st.subheader(
        "As we organize further details of the wedding day - further locations and time-table will be posted.")

    # 3. Add a Google Map frame for the church ()
    st.subheader("Armenische Kirche Wien")
    st.write("Address: Kolonitzgasse 11, 1030 Wien")
    st.text("From 15:30")

    simple_map_url = "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d2658.802470030058!2d16.386907376844075!3d48.2104205460865!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x476d070c5857a5fb%3A0x9e8c33afc607b242!2sArmenische%20Kirche%20Wien!5e0!3m2!1sde!2sat!4v1773255546996!5m2!1sde!2sat"

    st.components.v1.html(
        f'<iframe src="{simple_map_url}" width="100%" height="450" style="border:0;" allowfullscreen="" loading="lazy"></iframe>', height=460)

    # 4. Add a Google Map frame for the restaurant (Vabene)
    st.subheader("Location: Ristorante Vabene")
    st.write("Lindmayer Straße 1, Dammhaufengasse 50, 1020 Wien")
    st.text("From 17:00")

    simple_map_url = "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d5168.031708593825!2d16.451891614532386!3d48.19249238494649!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x476d00bc287b8277%3A0xcffa4f8fe89495b1!2sRistorante%20Vabene!5e0!3m2!1sde!2sat!4v1773255031475!5m2!1sde!2sat"

    st.components.v1.html(
        f'<iframe src="{simple_map_url}" width="100%" height="450" style="border:0;" allowfullscreen="" loading="lazy"></iframe>', height=460)


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


def show_questions():
    st.title("FAQ")
    st.subheader("Frequently Asked Questions")
    st.write("Here are some common questions and answers about our wedding day. If you have any other questions, please feel free to reach out to us directly!")
    st.divider()
    st.subheader("What is the dress code?")
    st.write("We want everyone to feel comfortable and stylish! The dress code is semi-formal. Think cocktail dresses, dressy separates, or a nice suit. We encourage you to add a pop of color or a fun accessory to make it your own!")
    st.divider()
    st.subheader("Will there be vegetarian or vegan meal options?")
    st.write("Absolutely! We will have a variety of meal options to accommodate different dietary preferences, including some vegetarian dishes. Please let us know if you have any specific dietary restrictions or allergies so we can ensure there are delicious options for everyone.")
    st.divider()
    st.subheader("How can I confirm my attendance?")
    st.write("You can confirm your attendance by calling or texting us directly.")
    st.divider()
    st.subheader("How can I come to the church?")
    st.write("The church is located in the 3rd district of Vienna and is easily accessible by public transportation. Please check the Location page for the address details.")
    st.divider()
    st.subheader("How can I come to the restaurant?")
    st.write("There will be organized transportation from the church to the restaurant via bus shuttle. "
             "If you plan to come with own car or taxi, please check the Location page for the address details.")
    st.divider()
    st.subheader(
        "Will there be transportation from the restaurant at the end of the wedding party?")
    st.write("No. As everyone will have own energy-level at the end of the exciting day, feel free to organize your own transportation."
             "We recommend using Uber to get back to your accommodation safely.")
    st.divider()
    st.subheader("Do we have a list with preferred wedding gifts?")
    st.write("No. We do prefer to receive monetary gifts, which will help us to create our dream honeymoon and future together.")
    st.divider()


def show_about():
    st.title("About Us")
    st.subheader("Our Story")
    # st.write("We met in Vienna in 2018 and instantly connected over our shared love of travel, food, and adventure. From exploring the charming streets of Vienna to embarking on unforgettable trips around the world, our journey together has been filled with laughter, love, and countless memories. We are so excited to continue this adventure as we say “I do” and start our new chapter together!")
    st.image('ring.jpg', width=500)
    st.divider()


if selected == "Home":
    show_home()

elif selected == "Locations":
    show_locations()

# elif selected == "Menu":
#     show_menu()

elif selected == "FAQ":
    show_questions()

elif selected == "About Us":
    show_about()
