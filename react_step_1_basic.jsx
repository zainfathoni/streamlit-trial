/**
 * STEP 1: Basic Chat Dashboard (React Reference)
 * ===============================================
 *
 * This is how a React developer would build this.
 * Use this as a reference when prompting Claude Code to build app_v1_basic.py
 *
 * React mental model:
 * - useState for state management (messages array)
 * - Functional component with render
 * - onClick handlers for interactivity
 * - Conditional rendering for empty state
 * - Auto-clearing input after send (typical UX pattern)
 */

import React, { useState } from 'react';

export default function ChatDashboard() {
  // State management (like st.session_state in Streamlit)
  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState('');

  // Handler: Send message
  const handleSend = () => {
    if (input.trim()) {
      setMessages([...messages, input]);
      setInput(''); // Clear input after send
    }
  };

  // Handler: Clear chat
  const handleClear = () => {
    setMessages([]);
    setInput('');
  };

  // Render
  return (
    <div className="chat-container">
      {/* Header component */}
      <h1>💬 Chat Dashboard</h1>
      <p className="subtitle">A React developer's first Python app</p>

      {/* Message list component */}
      <div className="messages-section">
        <div className="messages-header">
          <h2>Messages</h2>
          <button onClick={handleClear} className="btn-clear">
            🗑️ Clear
          </button>
        </div>

        {messages.length > 0 ? (
          <ul className="messages-list">
            {messages.map((msg, i) => (
              <li key={i}>
                <strong>{i + 1}.</strong> {msg}
              </li>
            ))}
          </ul>
        ) : (
          <div className="empty-state">
            💭 No messages yet. Start the conversation!
          </div>
        )}
      </div>

      {/* Input box component */}
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
        <small>Messages in chat: {messages.length}</small>
      </div>
    </div>
  );
}

/**
 * Key React Concepts Used:
 * ========================
 *
 * 1. useState([])
 *    → Python equivalent: if "messages" not in st.session_state: st.session_state.messages = []
 *    → Persistent state across re-renders
 *
 * 2. setMessages([...messages, input])
 *    → Python equivalent: st.session_state.messages.append(new_message)
 *    → Updating state triggers re-render
 *
 * 3. setInput('') after send
 *    → Python equivalent: Input clears automatically on Streamlit rerun (with key)
 *    → UX pattern: clear input after action
 *
 * 4. messages.map((msg, i) => ...)
 *    → Python equivalent: for i, msg in enumerate(st.session_state.messages)
 *    → Rendering lists
 *
 * 5. onKeyPress event + onClick
 *    → Python equivalent: st.text_input() (supports Enter) + st.button()
 *    → User interactivity
 *
 * 6. Conditional rendering (ternary)
 *    → Python equivalent: if/else with st.info()
 *    → Show empty state or list based on data
 *
 * 7. onClick handler
 *    → Python equivalent: st.button() + st.rerun()
 *    → Trigger actions
 */
