"""
STEP 3: Visual Polish (Styled Chat Bubbles)
============================================

🧠 React mental model: Component styling with conditional classes
💬 Prompt: "Make it look like a chat app with colored message bubbles (user on right/blue, assistant on left/gray)"
🐍 Python translation: st.markdown() with inline HTML/CSS for bubble styling

Key concepts:
- Conditional styling (like className={isUser ? 'user' : 'assistant'}) → inline CSS
- Component layout → st.columns(), st.container()
- Theme awareness → colors that work in light/dark mode
"""

import streamlit as st
from datetime import datetime

st.set_page_config(page_title="Chat Dashboard", layout="centered")

# ============================================================================
# HEADER
# ============================================================================
st.title("💬 Chat Dashboard")
st.caption("With styled message bubbles")

# ============================================================================
# STATE INITIALIZATION
# ============================================================================
if "messages" not in st.session_state:
    st.session_state.messages = []

# ============================================================================
# MESSAGE DISPLAY COMPONENT (with styling)
# ============================================================================
def render_message(timestamp, text, role="user"):
    """
    Render a single message bubble.

    Like a React <MessageBubble /> component with props:
    - timestamp: when message was sent
    - text: message content
    - role: "user" or "assistant" (determines color/alignment)
    """
    # Determine colors and alignment based on role
    is_user = role == "user"
    bubble_color = "#DCF8C6" if is_user else "#E8E8E8"  # WhatsApp-like colors
    text_color = "#000" if is_user else "#222"
    align = "flex-end" if is_user else "flex-start"

    html = f"""
    <div style="
        display: flex;
        justify-content: {align};
        margin-bottom: 12px;
    ">
        <div style="
            background-color: {bubble_color};
            padding: 12px 16px;
            border-radius: 16px;
            max-width: 70%;
            box-shadow: 0 1px 2px rgba(0,0,0,0.1);
        ">
            <small style="color: #999; font-size: 0.75rem;">
                {timestamp}
            </small>
            <div style="color: {text_color}; margin-top: 4px; line-height: 1.4;">
                {text}
            </div>
        </div>
    </div>
    """
    st.markdown(html, unsafe_allow_html=True)

# ============================================================================
# MESSAGE LIST (rendered with bubble styling)
# ============================================================================
st.write("### Messages")

if st.session_state.messages:
    for msg_obj in reversed(st.session_state.messages):
        role = msg_obj.get("role", "user")
        render_message(msg_obj["timestamp"], msg_obj["text"], role)
else:
    st.info("💭 No messages yet. Start the conversation!")

# ============================================================================
# INPUT BOX & SEND BUTTON
# ============================================================================
st.divider()

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
            msg_obj = {
                "text": new_message,
                "timestamp": datetime.now().strftime("%H:%M:%S"),
                "role": "user"
            }
            st.session_state.messages.append(msg_obj)
            st.rerun()
        else:
            st.warning("Message cannot be empty!")

# ============================================================================
# Footer
# ============================================================================
st.caption(f"📊 {len(st.session_state.messages)} message{'s' if len(st.session_state.messages) != 1 else ''}")
