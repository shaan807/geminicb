import streamlit as st
from google.generativeai import genai

# Create a new Gemini chatgenai
genai.configure(api_key='AIzaSyDhEmTAWAbbRPXE1ulLimH6ljEUFYYCt5M')

# Define the chatgenai's responses
@genai.dialog('hello')
def hello(convo):
    convo.say('Hello! How are you today?')
    convo.next()

@genai.dialog('goodbye')
def goodbye(convo):
    convo.say('Goodbye! It was nice talking to you.')
    convo.next()

@genai.dialog('help')
def help(convo):
    convo.say('I can help you with a variety of tasks, such as getting the weather forecast, finding a nearby restaurant, or playing a game.')
    convo.next()

# Define the Streamlit UI
st.set_page_config(layout="wide")

# Create a sidebar for user settings
st.sidebar.title("User Settings")
avatar = st.sidebar.selectbox("Choose your avatar:", ["cat", "dog", "owl"])
language = st.sidebar.selectbox("Choose your preferred language:", ["English", "Spanish", "French"])
response_style = st.sidebar.selectbox("Choose the chatgenai's response style:", ["Casual", "Formal", "Professional"])

# Create tabs for different sections of the app
tab1, tab2 = st.columns(2)

with tab1:
    st.title("Gemini Chatgenai")
    st.write("Ask me anything and I'll try to help!")

    # Get the user's input
    user_input = st.text_input("Your message:", placeholder="Type your message here...")

    # Send the user's input to the chatgenai
    genai_response = genai.respond(user_input)

    # Display the chatgenai's response
    st.write("Chatgenai:")
    st.markdown(genai_response, unsafe_allow_html=True)

with tab2:
    st.title("Help")
    st.write("Here you can find information on how to use the chatgenai and its features.")
    st.markdown("""
        * **How to ask a question:** Simply type your question or request in the chat box and press enter. The chatgenai will understand your intent and respond accordingly.
        * **Supported languages:** The chatgenai currently supports English, Spanish, and French. You can select your preferred language in the user settings sidebar.
        * **Response styles:** You can choose from three different response styles for the chatgenai: Casual, Formal, and Professional. Select the style that you prefer in the user settings sidebar.
    """)

# Add custom CSS and JavaScript to style the app
custom_css = """
    body {
        background-color: #f0f2f5;
        font-family: 'Helvetica', 'Arial', sans-serif;
    }

    .chat-container {
        display: flex;
        flex-direction: column;
        gap: 1rem;
        padding: 1rem;
        background-color: #fff;
        border-radius:  8px;
        width: 60%;
        margin: 0 auto;
    }

    .user-message {
        background-color: #e5e5e5;
        padding: 1rem;
        border-radius: 8px;
        margin-right: auto;
        max-width: 60%;
    }

    .chatgenai-message {
        background-color: #007bff;
        color: #fff;
        padding: 1rem;
        border-radius: 8px;
        margin-left: auto;
        max-width: 60%;
    }

    .avatar {
        width: 32px;
        height: 32px;
        border-radius: 50%;
        margin-right: 0.5rem;
    }
"""

custom_js = """
    document.querySelectorAll('.chatgenai-message').forEach((message) => {
        // Add an avatar to the chatgenai messages
        const avatar = document.createElement('img');
        avatar.src = 'https://avatars.dicebear.com/api/identicon/' + message.textContent.toLowerCase().replace(/\s/g, '') + '.svg';
        avatar.classList.add('avatar');
        message.insertBefore(avatar, message.firstChild);
    });
"""

st.write('<style>{}</style>'.format(custom_css), unsafe_allow_html=True)
st.write('<script>{}</script>'.format(custom_js), unsafe_allow_html=True)
