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

if "demo_role" not in st.session_state:
    st.session_state.demo_role = "user"

# ============================================================================
# COMPONENT: Message Bubble (React: MessageBubble component)
# ============================================================================
def render_message(timestamp: str, text: str, role: str = "user") -> None:
    """Render a styled message bubble with conditional styling based on role."""
    is_user = role == "user"
    bubble_color = "#DCF8C6" if is_user else "#E8E8E8"
    text_color = "#000" if is_user else "#222"
    align = "flex-end" if is_user else "flex-start"

    html = f"""
    <div style="display: flex; justify-content: {align}; margin-bottom: 12px;">
        <div style="
            max-width: 70%;
            background-color: {bubble_color};
            color: {text_color};
            padding: 12px 16px;
            border-radius: 16px;
            box-shadow: 0 1px 2px rgba(0, 0, 0, 0.1);
        ">
            <div style="font-size: 0.75rem; color: #999; margin-bottom: 4px;">
                {timestamp}
            </div>
            <div style="line-height: 1.4;">
                {text}
            </div>
        </div>
    </div>
    """
    st.markdown(html, unsafe_allow_html=True)

# ============================================================================
# UI LAYOUT
# ============================================================================
st.title("💬 Chat Dashboard")
st.write("*A React developer's first Python app*")

# Messages section header with role selector and clear button
col1, col2, col3 = st.columns([0.4, 0.3, 0.3])
with col1:
    st.subheader("Messages")
with col2:
    # Role selector (React: <select> for demoRole)
    st.session_state.demo_role = st.radio(
        "Send as:",
        ["user", "assistant"],
        horizontal=True,
        key="role_select",
        index=0 if st.session_state.demo_role == "user" else 1
    )
with col3:
    if st.button("🗑️ Clear", key="btn_clear"):
        # React equivalent: handleClear()
        st.session_state.messages = []
        st.session_state.input_value = ""
        st.rerun()

# ============================================================================
# MESSAGE LIST RENDERING (React: derived rendering with reverse + component)
# ============================================================================
if st.session_state.messages:
    # Derived rendering: reverse for newest-first (like useMemo)
    for msg_obj in reversed(st.session_state.messages):
        # Use render_message component with role-based styling
        role = msg_obj.get("role", "user")
        render_message(msg_obj["timestamp"], msg_obj["text"], role)
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
        # React equivalent: handleSend() with timestamp and role
        if user_input.strip():
            # Rich state: object with text, timestamp, and role (like React)
            timestamp = datetime.now().strftime("%H:%M:%S")
            message_obj = {
                "text": user_input,
                "timestamp": timestamp,
                "role": st.session_state.demo_role  # Add role for styling
            }
            st.session_state.messages.append(message_obj)
            st.session_state.input_value = ""
            st.rerun()

# ============================================================================
# FOOTER
# ============================================================================
st.divider()
st.caption(f"Messages in chat: {len(st.session_state.messages)}")
