# Testing & Demo Checklist

A comprehensive guide for testing the chat dashboard demo before your live talk and troubleshooting common issues.

---

## Pre-Talk Setup Checklist ✅

Run through this 15-20 minutes before your talk to ensure everything works.

### Environment Setup
- [ ] Python environment activated and dependencies installed (`pip install -r requirements.txt`)
- [ ] All four Python files exist and are readable:
  - [ ] `app.py` (live coding starting point)
  - [ ] `app_v1_basic.py` (Step 1: Basic chat)
  - [ ] `app_v2_timestamps.py` (Step 2: With timestamps)
  - [ ] `app_v3_styled.py` (Step 3: Styled bubbles)
- [ ] `.streamlit/config.toml` exists and has correct settings
- [ ] No uncommitted changes in git (clean working directory)

### Individual Version Testing
Test each version to ensure all features work before the talk:

#### `app.py` (Live Coding Point)
- [ ] Run: `streamlit run app.py`
- [ ] Input box is visible and focused
- [ ] Send button responsive to clicks
- [ ] After sending, input box clears
- [ ] "Clear" button appears and resets chat
- [ ] Message counter in footer updates correctly
- [ ] No errors in terminal or browser console
- [ ] Clean restart: refresh page, chat is empty

#### `app_v1_basic.py` (Step 1)
- [ ] Run: `streamlit run app_v1_basic.py`
- [ ] Same features as app.py work correctly
- [ ] Message numbering works (1, 2, 3...)
- [ ] Code comments are clear about React mappings

#### `app_v2_timestamps.py` (Step 2)
- [ ] Run: `streamlit run app_v2_timestamps.py`
- [ ] Timestamps display in "HH:MM:SS" format
- [ ] Messages appear **newest first** (bottom to top reading)
- [ ] Clear button works and resets timestamps
- [ ] Input clears after each send
- [ ] No time skips or format errors

#### `app_v3_styled.py` (Step 3)
- [ ] Run: `streamlit run app_v3_styled.py`
- [ ] Message bubbles render correctly (not broken HTML)
- [ ] User messages appear **right-aligned** in light green (#DCF8C6)
- [ ] Assistant messages appear **left-aligned** in light gray (#E8E8E8)
- [ ] Role toggle appears (User/Assistant radio buttons)
- [ ] Toggle works: sending as "Assistant" produces left-aligned gray bubbles
- [ ] Toggle works: sending as "User" produces right-aligned green bubbles
- [ ] Bubbles scale nicely on different screen sizes
- [ ] Timestamps display in bubbles above text
- [ ] Clear button removes all messages and bubble styling

### Display & Projection Testing
- [ ] Light theme is visible on projector (test with `.streamlit/config.toml` settings)
- [ ] Text size is readable from audience distance (zoom in browser if needed: Cmd/Ctrl + Plus)
- [ ] Colors are distinguishable (especially the bubble colors)
- [ ] Sidebars don't interfere with main content
- [ ] No flashing or flickering when sending messages

---

## Common Issues & Solutions

### Issue: Input box doesn't clear after sending
**Solution:** The `value` parameter and `message_input` session state key must match. Check:
```python
# Should have both:
new_message = st.text_input(..., key="message_input", value=st.session_state.get("message_input", ""))
st.session_state.message_input = ""  # After append
```

### Issue: "Clear" button not appearing
**Solution:** Check that columns are created correctly:
```python
col_title, col_clear = st.columns([4, 1])
with col_title:
    st.write("### Messages")
with col_clear:
    if st.button("🗑️ Clear", ...):
```

### Issue: Messages appear in wrong order (oldest first instead of newest first)
**Solution:** Ensure v2 and v3 use `reversed()`:
```python
for msg_obj in reversed(st.session_state.messages):  # ← reversed() is critical
```

### Issue: Role toggle not working in v3
**Solution:** Check the radio button key and role assignment:
```python
demo_role = st.radio("Send as:", ["User", "Assistant"], key="demo_role", ...)
selected_role = st.session_state.get("demo_role", "User").lower()  # ← .lower() converts to lowercase
```

### Issue: Bubble colors wrong or not rendering
**Solution:** Verify colors in `STYLE_COLORS` and check for typos:
```python
STYLE_COLORS = {
    "user_bubble": "#DCF8C6",      # ← Light green (WhatsApp-like)
    "assistant_bubble": "#E8E8E8",  # ← Light gray
    ...
}
```

### Issue: Streamlit not hot-reloading changes
**Solution:**
- Make sure `toolbarMode = "developer"` in `.streamlit/config.toml`
- Or manually refresh the browser (Cmd/Ctrl + R)
- Or restart Streamlit: Ctrl+C, then `streamlit run app.py`

### Issue: Port 8501 already in use
**Solution:**
- Find process: `lsof -i :8501`
- Kill it: `kill -9 <PID>`
- Or use different port: `streamlit run app.py --server.port 8502`

### Issue: Messages not persisting across reruns
**Solution:** Verify session state initialization:
```python
if "messages" not in st.session_state:
    st.session_state.messages = []
```
This MUST come before any message operations.

---

## Live Demo Flow Checklist

During the talk, follow this sequence:

### Before Demo Starts
- [ ] All three apps (.py files) are visible in terminal/editor
- [ ] Browser is open to `localhost:8501`
- [ ] Demo role is set to "User" (for consistency)
- [ ] Chat is empty (press Clear button)
- [ ] Zoom level is 120-150% for visibility

### Step 1: Show `app.py`
- [ ] Demo sending a message
- [ ] Highlight the input clearing
- [ ] Point out React mapping in comments
- [ ] Ask: "What React concepts do you see?" (useState, onClick, rerun)

### Step 2: Switch to `app_v2_timestamps.py`
- [ ] Either live-edit or switch files (suggest switch for safety)
- [ ] Send 2-3 messages with ~5 second gaps
- [ ] Point out newest-first ordering
- [ ] Highlight: "This is `reversed()` — like `array.reverse()` in React"
- [ ] Clear and repeat if time allows

### Step 3: Switch to `app_v3_styled.py`
- [ ] Send one message as "User" (green, right)
- [ ] Toggle to "Assistant" and send reply (gray, left)
- [ ] Send one more as "User" (creates conversation)
- [ ] Point out: "This is conditional styling—`className={isUser ? 'user' : 'assistant'}`"
- [ ] Show the `render_message()` function as component extraction example

### During Q&A
- [ ] Chat is available to re-demonstrate
- [ ] Clear button is ready to reset state
- [ ] Can quickly jump between versions if someone asks "What if we..."

---

## Post-Demo Checklist

After your talk:
- [ ] Commit any demo messages or state changes to git
- [ ] Restore all `.py` files to clean state (reset chat)
- [ ] Back up any variations you created live
- [ ] Note any audience questions for future improvements

---

## Browser Console Debugging

If something breaks, check the browser console:

1. **Open DevTools:** Cmd+Option+I (Mac) or F12 (Windows/Linux)
2. **Check Console tab** for JavaScript errors
3. **Check Network tab** for Streamlit API failures
4. **Look for Streamlit logs** in terminal where you ran `streamlit run`

### Common Terminal Output to Watch For

```bash
# Good signs:
Watchdog reloading app after code changes
Script run successfully

# Bad signs:
FileNotFoundError: No such file or directory
IndentationError: expected an indented block
KeyError: 'message_input'
```

---

## Performance Notes

- **First load:** May take 3-5 seconds (Streamlit caching)
- **After rerun:** Should be instant (< 1 second)
- **Input lag:** Shouldn't have any; if Streamlit is slow, restart it
- **Memory:** All messages stored in `st.session_state` (fine for demo, grows with each message)

---

## Accessibility Checklist

For inclusive demos:
- [ ] Text is large enough (zoom to 120%+)
- [ ] Colors are distinguishable (not just color-blind safe, but readable on projection)
- [ ] Speak as you code (narrate what you're doing)
- [ ] Pause for questions (don't rush through steps)

---

## Tips for a Smooth Demo

1. **Know your escape routes:** If code breaks, immediately switch to a working backup version
2. **Repeat don't improvise:** Use the same message text multiple times for consistency
3. **Explain before showing:** Describe what you'll demonstrate, then show it, then explain what happened
4. **Leave 2 minutes buffer:** Don't fill the entire allocated time; save room for unexpected issues
5. **Have a backup browser tab:** Open all three versions in separate tabs, ready to switch

---

## Resources

- **Streamlit Docs:** https://docs.streamlit.io
- **Talk Slides:** See `think-in-js-code-in-python.md` in the parent repo
- **Claude Code Docs:** https://docs.claude.com
- **Project README:** `README.md`

Good luck with your demo! 🚀
