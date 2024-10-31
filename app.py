import streamlit as st
from streamlit_option_menu import option_menu
from harry_potter import HarryPotterActivity

st.set_page_config(page_title="Noela's Wizarding Hub", page_icon="🪄", layout="wide")

st.sidebar.image("image/hogwarts-logo.png", width=280)  # Add your image file here

# Sidebar for navigation and API key input
api_key = st.sidebar.text_input("Enter your OpenAI API Key:", type="password")
hp = HarryPotterActivity(api_key=api_key)

with st.sidebar:
    page = option_menu(
        "Wizarding Hub",
        ["Magical World", "Spell Archive", "Wizard Encyclopedia", "The Enchanting Exchange", "Dumbledore's Army"],
        icons=['magic', 'book', 'person-badge', 'chat-dots', 'person-circle'],
        menu_icon="image/deathly.png", 
        default_index=0,
    )

if not api_key:
    st.warning("Please enter your OpenAI API Key in the sidebar to use the application.")

else:
    if page == "Magical World":
        st.title("Welcome to Hogwarts!")
        st.markdown("""
        This is the Wizarding Hub, where magic comes alive! 

        ✨ **Meet Wizopedia**  
        Wizopedia is your magical talking book that knows everything about Harry Potter characters! Just enter the name of a wizard or witch, and Wizopedia will share enchanting details and fascinating stories. Whether you want to learn about Harry, Hermione, or any other character, Wizopedia has you covered!

        📜 **Explore the Spell Archive**  
        Dive into the **Spell Archive** to search for spells and uncover the secrets of the wizarding world. From simple charms to complex curses, discover how each spell works and the lore behind them.

        🧙‍♂️ **Talk to Your Favorite Wizard**  
        Feel free to chat with your favorite wizard! Ask questions, learn about their adventures, and dive deeper into the magic. Whether you want to know about Dumbledore's wisdom or Ron's bravery, the conversation is just a click away.

        Let the journey begin!
        """)

    elif page == "Dumbledore's Army":
        st.header("About Me")
        st.markdown("""

        Connect with me on [LinkedIn](https://www.linkedin.com/in/noela-bunag/).
        
        Check out my portfolio at [noelabu.github.io](https://noelabu.github.io/).
        """)

    elif page == "Spell Archive":
        st.header("Spell Archive")
        text = st.text_input("You are talking to a powerful wizard, please tell the name of the spell you want to know")
        if st.button("Search"):
            response = hp.spell_identifier(spell=text)
            st.write(response)

    elif page == "Wizard Encyclopedia":
        st.header("I'm Wizopedia!")
        st.write("If you’ve ever wanted to delve deeper into the lives of your favorite wizards and witches, you’ve come to the right place. Whether you’re curious about the bravery of Harry Potter, the brilliance of Hermione Granger, or the cleverness of Luna Lovegood, I’ve got all the enchanting details right here.")
        st.write("Just enter the name of the wizard or witch you want to learn about, and I’ll share fascinating insights, spellbinding stories, and all the little-known facts that make the wizarding world so captivating. So, which wizard or witch would you like to know more about today?")
        text = st.text_input("")
        if st.button("Inqure"):
            response = hp.wizard_search(text)
            st.write(response)
    
    elif page == "The Enchanting Exchange":
        st.header("Talk to a Wizard!")
        if "messages" not in st.session_state:
            st.session_state.messages = []

        # Display chat messages from history on app rerun
        for message in st.session_state.messages:
            if message["role"] == "assistant":
                with st.chat_message(message["role"], avatar="image/witch-hat.png"):
                    st.markdown(message["content"])
            else:
                with st.chat_message(message["role"], avatar="image/wizard.png"):
                    st.markdown(message["content"])

        # Accept user input
        if prompt := st.chat_input("Who do you want to talk to?"):
            # Add user message to chat history
            st.session_state.messages.append({"role": "user", "content": prompt})
            # Display user message in chat message container
            with st.chat_message("user", avatar="image/wizard.png"):
                st.markdown(prompt)
            # Display assistant response in chat message container
            with st.chat_message("assistant", avatar="image/witch-hat.png"):
                response = st.write_stream(hp.wizard_chat(st.session_state.messages))

            # Add assistant response to chat history
            st.session_state.messages.append({"role": "assistant", "content": response})
        
