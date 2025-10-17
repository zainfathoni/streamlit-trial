"""
STEP 1: Basic Chat Dashboard
============================

🧠 React mental model: Component tree with state
💬 Prompt: "Build a simple Streamlit chat app with a title, message list, and input box"
🐍 Python translation: Sequential Streamlit calls + session_state for persistence

Key concepts:
- State management (like useState) → st.session_state
- Rendering (like JSX) → st.write(), st.columns()
- Interaction (like onClick) → st.button()
"""

import streamlit as st

st.set_page_config(page_title="Chat Dashboard", layout="centered")

# ============================================================================
# HEADER (like <Header title="Chat Dashboard" />)
# ============================================================================
st.title("💬 Chat Dashboard")
st.caption("A simple chat app built with Streamlit")

# ============================================================================
# STATE INITIALIZATION (like useState([]))
# ============================================================================
if "messages" not in st.session_state:
    st.session_state.messages = []

# ============================================================================
# MESSAGE LIST (like <MessageList messages={messages} />)
# ============================================================================
st.write("### Messages")

if st.session_state.messages:
    for i, msg in enumerate(st.session_state.messages):
        st.write(f"**{i+1}.** {msg}")
else:
    st.info("No messages yet. Start the conversation!")

# ============================================================================
# INPUT BOX & SEND BUTTON (like <InputBox onSend={handleSend} />)
# ============================================================================
col1, col2 = st.columns([4, 1])

with col1:
    new_message = st.text_input(
        "Type a message:",
        placeholder="Say something...",
        key="message_input"
    )

with col2:
    if st.button("Send", use_container_width=True):
        if new_message.strip():
            st.session_state.messages.append(new_message)
            st.rerun()  # React component re-renders; Streamlit script re-runs
        else:
            st.warning("Message cannot be empty!")

# ============================================================================
# Footer
# ============================================================================
st.divider()
st.caption(f"Messages in chat: {len(st.session_state.messages)}")
