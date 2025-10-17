"""
LIVE CODING DEMO: Chat Dashboard
=================================

Starting point for the live talk demo.

🧠 React thinking: declarative, composable, state-driven
🐍 Python + Streamlit: idiomatic, runnable, evolving

During the talk, I'll modify this step-by-step:
1. Add timestamps (Step 2)
2. Add styling (Step 3)

Each iteration translates React mental models into Python.
"""

import streamlit as st

st.set_page_config(page_title="Chat Dashboard", layout="centered")

# ============================================================================
# HEADER (like <Header title="Chat Dashboard" />)
# ============================================================================
st.title("💬 Chat Dashboard")
st.caption("A React developer's first Python app")

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
            st.rerun()
        else:
            st.warning("Message cannot be empty!")

# ============================================================================
# Footer
# ============================================================================
st.divider()
st.caption(f"Messages in chat: {len(st.session_state.messages)}")
