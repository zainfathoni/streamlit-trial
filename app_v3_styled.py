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

# ============================================================================
# COLOR & STYLE CONSTANTS (like CSS variables or Tailwind color tokens)
# ============================================================================
STYLE_COLORS = {
    "user_bubble": "#DCF8C6",  # WhatsApp-like light green
    "assistant_bubble": "#E8E8E8",  # Light gray
    "user_text": "#000",
    "assistant_text": "#222",
    "timestamp": "#999",
}

STYLE_DIMENSIONS = {
    "bubble_padding": "12px 16px",
    "bubble_border_radius": "16px",
    "bubble_max_width": "70%",
    "timestamp_font_size": "0.75rem",
    "margin_bottom": "12px",
}

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
def render_message(timestamp: str, text: str, role: str = "user") -> None:
    """
    Render a single message bubble with conditional styling (like <MessageBubble /> in React).

    This demonstrates the React concept of conditional rendering based on props:
    className={isUser ? 'user-bubble' : 'assistant-bubble'} → role-based inline CSS

    Args:
        timestamp: Message send time in "HH:MM:SS" format
        text: Message content to display
        role: Message sender ("user" or "assistant") - determines color and alignment

    React equivalent: <MessageBubble text={text} timestamp={timestamp} role={role} />
    """
    # Determine colors and alignment based on role (like role-based className in React)
    is_user = role == "user"
    bubble_color = STYLE_COLORS["user_bubble"] if is_user else STYLE_COLORS["assistant_bubble"]
    text_color = STYLE_COLORS["user_text"] if is_user else STYLE_COLORS["assistant_text"]
    align = "flex-end" if is_user else "flex-start"

    html = f"""
    <div style="
        display: flex;
        justify-content: {align};
        margin-bottom: {STYLE_DIMENSIONS['margin_bottom']};
    ">
        <div style="
            background-color: {bubble_color};
            padding: {STYLE_DIMENSIONS['bubble_padding']};
            border-radius: {STYLE_DIMENSIONS['bubble_border_radius']};
            max-width: {STYLE_DIMENSIONS['bubble_max_width']};
            box-shadow: 0 1px 2px rgba(0,0,0,0.1);
        ">
            <small style="color: {STYLE_COLORS['timestamp']}; font-size: {STYLE_DIMENSIONS['timestamp_font_size']};">
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
col_title, col_role, col_clear = st.columns([3, 1, 1])

with col_title:
    st.write("### Messages")

with col_role:
    demo_role = st.radio(
        "Send as:",
        ["User", "Assistant"],
        horizontal=True,
        label_visibility="collapsed",
        key="demo_role"
    )

with col_clear:
    if st.button("🗑️ Clear", use_container_width=True):
        st.session_state.messages = []
        st.session_state.message_input = ""
        st.rerun()

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
        "Type a message (press Enter to send):",
        placeholder="Say something...",
        key="message_input"
    )

with col2:
    if st.button("Send", use_container_width=True):
        if new_message.strip():
            selected_role = st.session_state.get("demo_role", "User").lower()
            msg_obj = {
                "text": new_message,
                "timestamp": datetime.now().strftime("%H:%M:%S"),
                "role": selected_role
            }
            st.session_state.messages.append(msg_obj)
            st.rerun()
        else:
            st.warning("Message cannot be empty!")

# ============================================================================
# Footer
# ============================================================================
st.caption(f"📊 {len(st.session_state.messages)} message{'s' if len(st.session_state.messages) != 1 else ''}")
