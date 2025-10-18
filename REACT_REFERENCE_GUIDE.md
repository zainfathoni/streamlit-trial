# React Reference Guide for Live Demo

This guide explains how to use the React reference files during your live talk.

---

## Overview

**The Flow:**
1. 🧠 Show React code (reference files)
2. 💬 Describe the React mental model to audience
3. 🤖 Ask Claude Code to translate to Python
4. 🐍 Point out React↔Python mappings in the result

---

## The Three Steps

### Step 1: Basic Chat Dashboard

**File:** `react_step_1_basic.jsx`

**What it shows:**
- State management with `useState([])`
- Rendering lists with `.map()`
- Event handlers with `onClick`
- Input with `onKeyPress` for Enter key

**When to use it:**
1. During intro: Show audience the React code
2. Say: "This is how I think—as a React developer"
3. Prompt Claude Code: "Look at this React code. Translate it to Python/Streamlit for app.py"
4. After Claude generates code, highlight the mappings:

| React | Python |
|-------|--------|
| `useState([])` | `if "messages" not in st.session_state:` |
| `messages.map()` | `for msg in st.session_state.messages:` |
| `onClick + onKeyPress` | `st.button() + st.text_input()` |
| `setMessages([...])` | `st.session_state.messages.append()` |

**Key insight:** "The pattern is identical—only the syntax changed"

---

### Step 2: Add Timestamps

**File:** `react_step_2_timestamps.jsx`

**What it shows:**
- Rich state objects: `{ text, timestamp }`
- Derived rendering: `[...messages].reverse().map()`
- Temporal data: `new Date().toLocaleTimeString()`
- Accessing object properties: `msg.timestamp`

**When to use it:**
1. After Step 1, say: "Now let's enrich the state"
2. Show `react_step_2_timestamps.jsx` to audience
3. Prompt Claude Code: "I want to add timestamps. Look at this React code—same structure, but now with objects instead of strings"
4. Highlight mappings:

| React | Python |
|-------|--------|
| `{ text, timestamp }` object | dict with `"text"` and `"timestamp"` keys |
| `new Date().toLocaleTimeString()` | `datetime.now().strftime("%H:%M:%S")` |
| `[...arr].reverse().map()` | `reversed(st.session_state.messages)` in for loop |
| `msg.timestamp` | `msg_obj["timestamp"]` |

**Key insight:** "State enrichment is the same pattern in both languages"

---

### Step 3: Visual Polish

**File:** `react_step_3_styled.jsx`

**What it shows:**
- Component extraction: `<MessageBubble />`
- Conditional styling: `isUser ? 'class1' : 'class2'`
- Props passing: `role={msg.role}`
- CSS-in-JS or inline styles

**When to use it:**
1. After Step 2, say: "Now let's make it look nice"
2. Show `react_step_3_styled.jsx` to audience
3. Point out the `MessageBubble` component
4. Prompt Claude Code: "Extract the message rendering into a function. Use conditional styling for user vs. assistant"
5. Highlight mappings:

| React | Python |
|-------|--------|
| `function MessageBubble({ props })` | `def render_message(args) -> None:` |
| `className={isUser ? 'user' : 'assistant'}` | `color = "#DCF8C6" if is_user else "#E8E8E8"` |
| `<select onChange>` | `st.radio()` |
| JSX component props | Function parameters |

**Key insight:** "Component thinking works the same way in Python"

---

## Example Prompts for Claude Code

### Step 1 Prompt
```
"Look at the React code in react_step_1_basic.jsx.

I want to build the same thing in Python/Streamlit:
- useState([]) for state management → st.session_state
- messages.map() for rendering → for loop
- onClick handlers → st.button() + st.rerun()
- Input with Enter key → st.text_input() with key

Build this into app.py. Include a Clear button to reset the chat."
```

### Step 2 Prompt
```
"Now I want to enrich the state like in react_step_2_timestamps.jsx:
- Store messages as objects with {text, timestamp}
- Use reversed() to show newest-first
- Format timestamps as HH:MM:SS

Modify app.py to include these changes."
```

### Step 3 Prompt
```
"Looking at react_step_3_styled.jsx, I want:
- Extract message rendering into a render_message() function
- Add conditional styling: green bubbles for user, gray for assistant
- Add a role toggle (User/Assistant radio buttons)
- Use st.markdown() with inline CSS for the bubbles

Update app.py or show app_v3_styled.py."
```

---

## Talking Points

After each step, emphasize these patterns:

### Universal Patterns
- **State Management:** Both React and Python need to store data
  - React: `useState`
  - Python: `st.session_state`
  - **Concept:** Same everywhere (Redux, Vue, Flutter...)

- **Rendering Lists:** Both React and Python iterate and display
  - React: `.map()`
  - Python: `for` loop
  - **Concept:** The pattern is universal

- **Interactivity:** Both React and Python handle events
  - React: `onClick`, `onChange`, `onKeyPress`
  - Python: `st.button()`, `st.text_input()`
  - **Concept:** Event-driven reactivity is the same

- **Component Thinking:** Both React and Python can extract reusable pieces
  - React: Components with props
  - Python: Functions with parameters
  - **Concept:** Modularity is universal

---

## Not Just Translation

This isn't syntax translation—it's **pattern translation**.

The React files show:
- How you *think* (patterns, mental models)
- What you *intend* (state, rendering, interaction)

Python shows:
- How those thoughts become *code* in a new runtime
- Same intent, different implementation

**The key insight:** If you understand the React pattern, any language becomes just "different syntax for the same idea."

---

## For Your Reference

**Files in this repo:**
- `app.py` — Blank starting point for live coding
- `react_step_1_basic.jsx` — Reference: basic chat
- `react_step_2_timestamps.jsx` — Reference: rich state
- `react_step_3_styled.jsx` — Reference: components & styling
- `app_v1_basic.py` — Python result of Step 1
- `app_v2_timestamps.py` — Python result of Step 2
- `app_v3_styled.py` — Python result of Step 3

**Flow during talk:**
1. Show React code
2. Describe intent
3. Ask Claude Code to build Python
4. Show Python result
5. Highlight the mappings
6. Repeat for Steps 2 & 3

---

## Timing

- **Setup:** 30 seconds (explain the approach)
- **Step 1:** 4–5 minutes (live code or show result)
- **Step 2:** 2–3 minutes (show backup + point out patterns)
- **Step 3:** 2–3 minutes (show final result + toggle demo)
- **Total:** ~12–15 minutes for full demo

**Escape hatches:** If anything breaks, jump to the backup `.py` files. They're already tested.

---

Happy presenting! 🚀
