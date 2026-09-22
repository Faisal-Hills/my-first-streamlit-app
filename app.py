import streamlit as st

# 1. Page Configuration (This sets the title on the browser tab)
st.set_page_config(page_title="My First Python Webpage", page_icon="🎈")

# 2. Adding Page Headings and Text
st.title("🎈 Welcome to My First Python Webpage!")
st.write("This entire website was built using pure Python code!")

st.header("✨ Interactive Widgets")

# 3. Getting User Input
user_name = st.text_input("What is your name?")

# 4. Interactive Button & Conditional Output
if st.button("Click Me!"):
    if user_name:
        st.success(f"Hello, {user_name}! You successfully ran your first web app!")
    else:
        st.warning("Please enter your name first!")

# 5. Adding a slider (Exactly like your math operators!)
score = st.slider("Select your score", 0, 100, 85)
st.write(f"The score you selected is: **{score}**")
