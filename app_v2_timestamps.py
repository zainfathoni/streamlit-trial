"""
STEP 2: Add Interactivity (Timestamps & Ordering)
==================================================

🧠 React mental model: State with enriched data, derived rendering
💬 Prompt: "Add timestamps to messages and show the newest messages first"
🐍 Python translation: Store structured data, manipulate with reversed()

Key concepts:
- Rich state (like useState with objects) → dict in session_state
- Derived rendering (like useMemo) → reversed() loop
- Temporal data (like Date.now()) → datetime.now()
"""

import streamlit as st
from datetime import datetime

st.set_page_config(page_title="Chat Dashboard", layout="centered")

# ============================================================================
# HEADER
# ============================================================================
st.title("💬 Chat Dashboard")
st.caption("With timestamps and newest-first ordering")

# ============================================================================
# STATE INITIALIZATION (now storing structured data)
# ============================================================================
if "messages" not in st.session_state:
    st.session_state.messages = []

# ============================================================================
# MESSAGE LIST (newest first, with timestamps)
# ============================================================================
st.write("### Messages")

if st.session_state.messages:
    # Reverse to show newest first (like React with array.reverse())
    for msg_obj in reversed(st.session_state.messages):
        timestamp = msg_obj["timestamp"]
        text = msg_obj["text"]
        st.write(f"**{timestamp}** — {text}")
else:
    st.info("No messages yet. Start the conversation!")

# ============================================================================
# INPUT BOX & SEND BUTTON (now captures timestamp)
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
            # Create message object with timestamp
            msg_obj = {
                "text": new_message,
                "timestamp": datetime.now().strftime("%H:%M:%S")
            }
            st.session_state.messages.append(msg_obj)
            st.rerun()
        else:
            st.warning("Message cannot be empty!")

# ============================================================================
# Footer
# ============================================================================
st.divider()
st.caption(f"Messages in chat: {len(st.session_state.messages)}")
