# AIRepublic_CharacterAI

Welcome to **Wizarding Hub**—your magical portal into the enchanting world of Harry Potter! Here, you can interact with characters, explore spells, and uncover secrets from the wizarding universe. 

## Features

✨ **Meet Wizopedia**  
Wizopedia is your magical talking book that knows everything about Harry Potter characters! Just enter the name of a wizard or witch, and Wizopedia will share enchanting details and fascinating stories. Whether you want to learn about Harry, Hermione, or any other character, Wizopedia has you covered!

📜 **Explore the Spell Archive**  
Dive into the **Spell Archive** to search for spells and uncover the secrets of the wizarding world. From simple charms to complex curses, discover how each spell works and the lore behind them.

🧙‍♂️ **Talk to Your Favorite Wizard**  
Feel free to chat with your favorite wizard! Ask questions, learn about their adventures, and dive deeper into the magic. Whether you want to know about Dumbledore's wisdom or Ron's bravery, the conversation is just a click away.

## Technology

**Wizarding Hub** is powered by the OpenAI API, using advanced system prompting to bring the magic to life. This project is designed and deployed using Streamlit, providing an interactive and user-friendly experience.

## Getting Started

To run the Wizarding Hub locally, clone this repository and install the necessary dependencies:

```bash
git clone https://github.com/noelabu/AIRepublic_CharacterAI.git
cd AIRepublic_CharacterAI
pip install -r requirements.txt
```

### API Key Configuration
To use the OpenAI API, you'll need an API key. Sign up at [OpenAI](https://openai.com) and create an API key. Store your key in an environment variable named `OPENAI_API_KEY`.

```bash
export OPENAI_API_KEY='your-api-key'
```

### Running the Streamlit App
After setting up the API key, you can run the Streamlit app to interact with the tools.

```bash
streamlit run app.py
```

Open your browser and go to `http://localhost:8501` to access the application. You can also access the application [here](https://noelabu-wizard-world.streamlit.app/).
## Contributing

Contributions are welcome! If you have ideas for new features, improvements, or bug fixes, feel free to open an issue or submit a pull request.

## Acknowledgments

- OpenAI for providing the API that powers Wizopedia.
- The Harry Potter community for inspiring this magical experience.