import streamlit as st

from ui import inject_css, render_header, render_room_output, render_empty_state
from student_logic import craft_room_story

st.set_page_config(
    page_title="AI Room Story Crafter",
    page_icon="🏰",
    layout="centered",
)

inject_css()
render_header()

if "room_data" not in st.session_state:
    st.session_state.room_data = None

room_name = st.text_input("Room Name", placeholder="e.g. Hall of Fractured Hours")
theme = st.text_input("Theme", placeholder="e.g. ancient crystal vault")
mood = st.selectbox(
    "Mood",
    ["Mysterious", "Magical", "Dark", "Ancient", "Dreamlike"],
)

generate_clicked = st.button("Craft Room Story", use_container_width=True)

if generate_clicked:
    if room_name.strip() and theme.strip():
        st.session_state.room_data = craft_room_story(
            room_name=room_name.strip(),
            theme=theme.strip(),
            mood=mood,
        )
    else:
        st.session_state.room_data = None
        st.warning("Please enter both Room Name and Theme.")

room_data = st.session_state.room_data

if room_data:
    render_room_output(room_data)
else:
    render_empty_state()