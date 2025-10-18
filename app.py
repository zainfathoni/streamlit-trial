"""
LIVE CODING DEMO: Chat Dashboard
=================================

Starting point for the live talk demo.
Start with this blank template and build up during the talk:

🧠 React thinking: declarative, composable, state-driven
🐍 Python + Streamlit: idiomatic, runnable, evolving

During the talk, you'll modify this step-by-step:
1. Add messages state and display
2. Add input box and send button
3. Add timestamps (Step 2)
4. Add styling (Step 3)

Each iteration translates React mental models into Python.
"""

import streamlit as st
from datetime import datetime

st.set_page_config(page_title="Chat Dashboard", layout="centered")

# ============================================================================
# STATE MANAGEMENT (React: useState)
# ============================================================================
# Initialize session state — persists across reruns
if "messages" not in st.session_state:
    st.session_state.messages = []

if "input_value" not in st.session_state:
    st.session_state.input_value = ""

# ============================================================================
# UI LAYOUT
# ============================================================================
st.title("💬 Chat Dashboard")
st.write("*A React developer's first Python app*")

# Messages section header with clear button
col1, col2 = st.columns([0.8, 0.2])
with col1:
    st.subheader("Messages")
with col2:
    if st.button("🗑️ Clear", key="btn_clear"):
        # React equivalent: handleClear()
        st.session_state.messages = []
        st.session_state.input_value = ""
        st.rerun()

# ============================================================================
# MESSAGE LIST RENDERING (React: derived rendering with reverse)
# ============================================================================
if st.session_state.messages:
    # Derived rendering: reverse for newest-first (like useMemo)
    for msg_obj in reversed(st.session_state.messages):
        st.write(f"**{msg_obj['timestamp']}** — {msg_obj['text']}")
else:
    # Empty state (React: ternary operator)
    st.info("💭 No messages yet. Start the conversation!")

# ============================================================================
# INPUT SECTION (React: onChange + onClick handlers)
# ============================================================================
col1, col2 = st.columns([0.8, 0.2])
with col1:
    # Text input with key for state management
    user_input = st.text_input(
        "Say something...",
        value=st.session_state.input_value,
        key="user_input",
        label_visibility="collapsed"
    )
with col2:
    # Send button
    if st.button("Send", key="btn_send"):
        # React equivalent: handleSend() with timestamp
        if user_input.strip():
            # Rich state: object with text and timestamp (like React)
            timestamp = datetime.now().strftime("%H:%M:%S")
            message_obj = {
                "text": user_input,
                "timestamp": timestamp
            }
            st.session_state.messages.append(message_obj)
            st.session_state.input_value = ""
            st.rerun()

# ============================================================================
# FOOTER
# ============================================================================
st.divider()
st.caption(f"Messages in chat: {len(st.session_state.messages)}")
