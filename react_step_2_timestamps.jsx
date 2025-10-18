/**
 * STEP 2: Add Timestamps & Newest-First Ordering (React Reference)
 * ================================================================
 *
 * This is how a React developer would enhance the chat with timestamps.
 * Use this as a reference when prompting Claude Code to build app_v2_timestamps.py
 *
 * React mental model:
 * - Rich state: objects instead of strings
 * - useState with structured data
 * - Derived rendering: reverse before render (like useMemo)
 * - Temporal data: Date.now() or new Date()
 * - Mapping over objects with properties
 */

import React, { useState } from 'react';

export default function ChatDashboard() {
  // State: Now storing objects instead of strings
  // Each message has { text, timestamp }
  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState('');

  // Handler: Send message with timestamp
  const handleSend = () => {
    if (input.trim()) {
      const timestamp = new Date().toLocaleTimeString([], {
        hour: '2-digit',
        minute: '2-digit',
        second: '2-digit',
      });

      const newMessage = {
        text: input,
        timestamp: timestamp, // Add timestamp property
      };

      setMessages([...messages, newMessage]);
      setInput(''); // Clear input
    }
  };

  // Handler: Clear chat
  const handleClear = () => {
    setMessages([]);
    setInput('');
  };

  // Derived rendering: Reverse messages to show newest first
  // (like useMemo or derived state)
  const displayMessages = [...messages].reverse();

  // Render
  return (
    <div className="chat-container">
      {/* Header */}
      <h1>💬 Chat Dashboard</h1>
      <p className="subtitle">With timestamps and newest-first ordering</p>

      {/* Message list */}
      <div className="messages-section">
        <div className="messages-header">
          <h2>Messages</h2>
          <button onClick={handleClear} className="btn-clear">
            🗑️ Clear
          </button>
        </div>

        {displayMessages.length > 0 ? (
          <ul className="messages-list">
            {displayMessages.map((msg, i) => (
              <li key={i}>
                <strong>{msg.timestamp}</strong> — {msg.text}
              </li>
            ))}
          </ul>
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
        <small>Messages in chat: {messages.length}</small>
      </div>
    </div>
  );
}

/**
 * Key React Concepts Enhanced:
 * ============================
 *
 * 1. Rich State Objects (before: string[], now: {text, timestamp}[])
 *    React:
 *      const [messages, setMessages] = useState([]);
 *      const newMessage = { text: input, timestamp: new Date().toLocaleTimeString() };
 *      setMessages([...messages, newMessage]);
 *
 *    Python equivalent (Streamlit):
 *      if "messages" not in st.session_state:
 *        st.session_state.messages = []
 *      msg_obj = {
 *        "text": new_message,
 *        "timestamp": datetime.now().strftime("%H:%M:%S")
 *      }
 *      st.session_state.messages.append(msg_obj)
 *
 * 2. Derived Rendering with reverse()
 *    React:
 *      const displayMessages = [...messages].reverse();
 *      displayMessages.map(msg => ...)
 *
 *    Python equivalent (Streamlit):
 *      for msg_obj in reversed(st.session_state.messages):
 *        st.write(f"**{msg_obj['timestamp']}** — {msg_obj['text']}")
 *
 * 3. Accessing Object Properties
 *    React:
 *      {msg.timestamp} — {msg.text}
 *
 *    Python:
 *      f"{msg_obj['timestamp']} — {msg_obj['text']}"
 *
 * 4. Temporal Data (Date handling)
 *    React:
 *      new Date().toLocaleTimeString()
 *
 *    Python:
 *      from datetime import datetime
 *      datetime.now().strftime("%H:%M:%S")
 *
 * 5. Array Methods
 *    React:
 *      [...messages].reverse() — creates copy and reverses
 *      messages.map(msg => ...)
 *
 *    Python:
 *      reversed(st.session_state.messages) — iterator
 *      for msg in ...
 *
 * Pattern: State Enrichment
 * ==========================
 * The key insight here: We're enriching our state structure.
 * In React, we started with useState([]) for strings.
 * Now we're using useState([]) for objects.
 *
 * The pattern is the same—we're just making the data richer.
 * This is fundamental to both React and Python thinking.
 */
