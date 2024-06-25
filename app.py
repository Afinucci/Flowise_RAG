import streamlit as st
import streamlit.components.v1 as components

# Path to the logo image (local file in the same directory)
#logo_path = "logo.png"

# Display the logo
#st.image(logo_path, width=200)

# Title of the Streamlit app
st.title("Chatbot Integration in Streamlit")

# HTML and JavaScript code for the chatbot
chatbot_html = """
<flowise-fullchatbot></flowise-fullchatbot>
<script type="module">
    import Chatbot from "https://cdn.jsdelivr.net/npm/flowise-embed/dist/web.js"
    Chatbot.initFull({
        chatflowid: "0d1ff924-ed2b-438b-a467-420726ebe6a1",
        apiHost: "http://localhost:3000",
    })
</script>
"""

# Embed the chatbot HTML and JavaScript code
components.html(chatbot_html, height=800, width=1000)

# Add any additional Streamlit elements below
st.write("This is a sample Streamlit app with an embedded chatbot.")