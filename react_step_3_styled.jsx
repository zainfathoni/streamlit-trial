/**
 * STEP 3: Visual Polish with Styled Bubbles (React Reference)
 * ===========================================================
 *
 * This is how a React developer would add conditional styling and components.
 * Use this as a reference when prompting Claude Code to build app_v3_styled.py
 *
 * React mental model:
 * - Component extraction (MessageBubble component)
 * - Conditional styling (className or inline styles based on props)
 * - Props passing (role determines appearance)
 * - Conditional rendering
 */

import React, { useState } from 'react';
import './ChatDashboard.css'; // Styles below

/**
 * MessageBubble Component
 * =======================
 * A reusable component that renders a single message with styling
 * based on the role (user or assistant).
 *
 * Like a component in Streamlit that we extract to a function (render_message).
 */
function MessageBubble({ timestamp, text, role = 'user' }) {
  // Determine styling based on role
  const isUser = role === 'user';
  const bubbleClass = isUser ? 'bubble bubble--user' : 'bubble bubble--assistant';

  return (
    <div className={`bubble-container ${isUser ? 'bubble-container--right' : 'bubble-container--left'}`}>
      <div className={bubbleClass}>
        <div className="bubble__timestamp">{timestamp}</div>
        <div className="bubble__text">{text}</div>
      </div>
    </div>
  );
}

export default function ChatDashboard() {
  // State: Now include role in each message
  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState('');
  const [demoRole, setDemoRole] = useState('user');

  // Handler: Send message with role
  const handleSend = () => {
    if (input.trim()) {
      const timestamp = new Date().toLocaleTimeString([], {
        hour: '2-digit',
        minute: '2-digit',
        second: '2-digit',
      });

      const newMessage = {
        text: input,
        timestamp: timestamp,
        role: demoRole, // Add role for styling
      };

      setMessages([...messages, newMessage]);
      setInput('');
    }
  };

  // Handler: Clear chat
  const handleClear = () => {
    setMessages([]);
    setInput('');
  };

  // Derived: Reverse for newest-first
  const displayMessages = [...messages].reverse();

  // Render
  return (
    <div className="chat-container">
      {/* Header */}
      <h1>💬 Chat Dashboard</h1>
      <p className="subtitle">With styled message bubbles</p>

      {/* Message list */}
      <div className="messages-section">
        <div className="messages-header">
          <h2>Messages</h2>

          {/* Role toggle for demo */}
          <div className="role-selector">
            <label>Send as:</label>
            <select value={demoRole} onChange={(e) => setDemoRole(e.target.value)}>
              <option value="user">User</option>
              <option value="assistant">Assistant</option>
            </select>
          </div>

          <button onClick={handleClear} className="btn-clear">
            🗑️ Clear
          </button>
        </div>

        {displayMessages.length > 0 ? (
          <div className="messages-list">
            {displayMessages.map((msg, i) => (
              <MessageBubble
                key={i}
                timestamp={msg.timestamp}
                text={msg.text}
                role={msg.role}
              />
            ))}
          </div>
        ) : (
          <div className="empty-state">
            💭 No messages yet. Start the conversation!
          </div>
        )}
      </div>

      {/* Input */}
      <div className="input-section">
        <input
          type="text"
          value={input}
          onChange={(e) => setInput(e.target.value)}
          onKeyPress={(e) => e.key === 'Enter' && handleSend()}
          placeholder="Say something..."
          className="input-box"
        />
        <button onClick={handleSend} className="btn-send">
          Send
        </button>
      </div>

      {/* Footer */}
      <div className="footer">
        <small>📊 {messages.length} message{messages.length !== 1 ? 's' : ''}</small>
      </div>
    </div>
  );
}

/**
 * CSS Styles (ChatDashboard.css)
 * =============================
 * This would normally be in a separate file, but shown here for reference.
 */

/*
.chat-container {
  max-width: 600px;
  margin: 0 auto;
  font-family: sans-serif;
}

.messages-section {
  margin: 20px 0;
  border: 1px solid #e0e0e0;
  border-radius: 8px;
  padding: 16px;
  min-height: 200px;
}

.messages-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 16px;
  gap: 12px;
}

.messages-header h2 {
  margin: 0;
  flex: 1;
}

.role-selector {
  display: flex;
  align-items: center;
  gap: 8px;
}

.role-selector label {
  font-size: 0.9rem;
}

.role-selector select {
  padding: 4px 8px;
  border: 1px solid #ccc;
  border-radius: 4px;
}

.btn-clear {
  padding: 8px 12px;
  background: white;
  border: 1px solid #ccc;
  border-radius: 4px;
  cursor: pointer;
}

.messages-list {
  display: flex;
  flex-direction: column;
  gap: 12px;
}

.bubble-container {
  display: flex;
  margin-bottom: 12px;
}

.bubble-container--right {
  justify-content: flex-end;
}

.bubble-container--left {
  justify-content: flex-start;
}

.bubble {
  max-width: 70%;
  padding: 12px 16px;
  border-radius: 16px;
  box-shadow: 0 1px 2px rgba(0, 0, 0, 0.1);
}

.bubble--user {
  background-color: #DCF8C6;
  color: #000;
}

.bubble--assistant {
  background-color: #E8E8E8;
  color: #222;
}

.bubble__timestamp {
  font-size: 0.75rem;
  color: #999;
  margin-bottom: 4px;
}

.bubble__text {
  line-height: 1.4;
}

.empty-state {
  text-align: center;
  color: #999;
  padding: 40px;
}

.input-section {
  display: flex;
  gap: 8px;
  margin: 16px 0;
}

.input-box {
  flex: 1;
  padding: 8px 12px;
  border: 1px solid #ccc;
  border-radius: 4px;
  font-size: 1rem;
}

.btn-send {
  padding: 8px 16px;
  background: #0066CC;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

.btn-send:hover {
  background: #0052A3;
}

.footer {
  text-align: center;
  padding: 8px;
  color: #666;
}
*/

/**
 * Key React Concepts Enhanced:
 * ============================
 *
 * 1. Component Extraction
 *    React:
 *      function MessageBubble({ timestamp, text, role }) { ... }
 *
 *    Python equivalent (Streamlit):
 *      def render_message(timestamp: str, text: str, role: str = "user") -> None:
 *        ...
 *        st.markdown(html, unsafe_allow_html=True)
 *
 * 2. Conditional Styling (className based on props)
 *    React:
 *      const isUser = role === 'user';
 *      const bubbleClass = isUser ? 'bubble bubble--user' : 'bubble bubble--assistant';
 *      <div className={bubbleClass}>
 *
 *    Python equivalent (Streamlit):
 *      is_user = role == "user"
 *      bubble_color = "#DCF8C6" if is_user else "#E8E8E8"
 *      align = "flex-end" if is_user else "flex-start"
 *      html = f"""<div style="background-color: {bubble_color}; ...">
 *
 * 3. Props Passing
 *    React:
 *      <MessageBubble timestamp={msg.timestamp} text={msg.text} role={msg.role} />
 *
 *    Python:
 *      render_message(msg_obj["timestamp"], msg_obj["text"], msg_obj.get("role", "user"))
 *
 * 4. Conditional Rendering
 *    React:
 *      {displayMessages.length > 0 ? (
 *        <div>...</div>
 *      ) : (
 *        <div>No messages</div>
 *      )}
 *
 *    Python:
 *      if st.session_state.messages:
 *        for msg_obj in reversed(...):
 *          render_message(...)
 *      else:
 *        st.info("💭 No messages yet...")
 *
 * 5. Inline Styles (alternative to className)
 *    React:
 *      const styles = {
 *        backgroundColor: isUser ? '#DCF8C6' : '#E8E8E8',
 *        padding: '12px 16px',
 *      };
 *      <div style={styles}>
 *
 *    Python (Streamlit):
 *      html = f'''<div style="background-color: {bubble_color}; padding: 12px 16px;">
 *
 * 6. Select/Dropdown for Role Toggle
 *    React:
 *      <select value={demoRole} onChange={(e) => setDemoRole(e.target.value)}>
 *        <option value="user">User</option>
 *        <option value="assistant">Assistant</option>
 *      </select>
 *
 *    Python (Streamlit):
 *      demo_role = st.radio("Send as:", ["User", "Assistant"], horizontal=True)
 *
 * Pattern: Component Extraction + Conditional Styling
 * ====================================================
 * The key insight: Extract complex rendering logic into components/functions.
 * Use props to control appearance (conditional styling).
 * This makes code more maintainable and reusable.
 *
 * In React: MessageBubble component with role prop
 * In Python: render_message() function with role parameter
 * Same concept, different syntax.
 */
