import streamlit as st
import random

def main():
    if "yes_clicks" not in st.session_state:
        st.session_state.yes_clicks = 0
    
    if "page" not in st.session_state:
        st.session_state.page = "home"

    if st.session_state.page == "home":
        st.title("🎉 Happy Birthday Didi! 🎂")
        st.markdown(
            "### May God accept you in **hell** soon! 🔥🤣 "
            "\n\nJust Kidding! Enjoy your day to the fullest! 🥳"
        )
        
        if st.button("🎁 Here is a surprise for you! 👉"):
            st.session_state.page = "gift"
            st.experimental_set_query_params(page="gift")
            st.rerun()
    
    elif st.session_state.page == "gift":
        st.title("🎁 Do you want a gift?")
        
        # Generate a random position for the "Yes" button
        yes_position = random.randint(0, 3)  # Choose a column index
        
        cols = st.columns(4)  # Create 4 columns
        
        # Place "Yes" button randomly
        with cols[yes_position]:
            if st.button("Yes 😍", key=f"yes_{st.session_state.yes_clicks}"):
                st.session_state.yes_clicks += 1
                st.experimental_set_query_params(page="gift")
                st.rerun()
        
        # "No" button is fixed in the last column
        with cols[3]:
            if st.button("No ❌"):
                st.session_state.page = "no_gift"
                st.experimental_set_query_params(page="no_gift")
                st.rerun()
    
    elif st.session_state.page == "no_gift":
        st.title("😆 I knew it!")
        st.markdown(
            "### You don’t want a gift from me? 💔😭\n"
            "But wait... there’s **another** surprise for you! 😜"
        )
        
        if st.button("🎊 Another Surprise! 👀"):
            st.success("Haha! No gifts! Just have a great day! 🎂🤣")
            st.balloons()

if __name__ == "__main__":
    main()
