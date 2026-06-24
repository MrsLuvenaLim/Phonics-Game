import streamlit as st
import random

st.set_page_config(
    page_title="Phonics Quest",
    page_icon="🔤",
    layout="centered"
)

QUESTIONS = [
    {
        "question": "Which word has the /sh/ sound?",
        "options": ["ship", "sip", "chip", "sit"],
        "answer": "ship",
        "explanation": "'sh' makes the /sh/ sound."
    },
    {
        "question": "Which word has the /ch/ sound?",
        "options": ["shop", "chat", "thin", "ship"],
        "answer": "chat",
        "explanation": "'ch' makes the /ch/ sound."
    },
    {
        "question": "Which word has the long /a/ sound?",
        "options": ["cap", "cake", "cat", "back"],
        "answer": "cake",
        "explanation": "The magic 'e' helps make the long /a/ sound."
    },
    {
        "question": "Which word has the /ee/ sound?",
        "options": ["bed", "bee", "big", "bad"],
        "answer": "bee",
        "explanation": "'ee' makes the long /e/ sound."
    },
    {
        "question": "Which word has the /ai/ sound?",
        "options": ["rain", "run", "red", "rock"],
        "answer": "rain",
        "explanation": "'ai' usually makes the long /a/ sound."
    },
    {
        "question": "You see the word 'light'. Which phonogram helps you read it?",
        "options": ["igh", "sh", "ch", "oo"],
        "answer": "igh",
        "explanation": "'igh' makes the long /i/ sound."
    },
    {
        "question": "You see the word 'moon'. Which sound do the letters 'oo' make?",
        "options": ["long /oo/", "/sh/", "/ai/", "short /a/"],
        "answer": "long /oo/",
        "explanation": "'oo' makes the long /oo/ sound."
    },
    {
        "question": "Which word has the /th/ sound?",
        "options": ["then", "ship", "chip", "sing"],
        "answer": "then",
        "explanation": "'th' makes the /th/ sound."
    }
]


def new_question():
    st.session_state.question = random.choice(QUESTIONS)
    st.session_state.answered = False


if "score" not in st.session_state:
    st.session_state.score = 0

if "best_score" not in st.session_state:
    st.session_state.best_score = 0

if "total_questions" not in st.session_state:
    st.session_state.total_questions = 0

if "question" not in st.session_state:
    new_question()

st.title("🔤 Phonics Quest")
st.write("Learn phonics, earn points and beat your best score!")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Score", st.session_state.score)

with col2:
    st.metric("Best Score", st.session_state.best_score)

with col3:
    st.metric("Questions", st.session_state.total_questions)

st.divider()

q = st.session_state.question

st.subheader("🎯 Challenge")
st.write(q["question"])

answer = st.radio(
    "Choose one answer:",
    q["options"],
    index=None,
    disabled=st.session_state.get("answered", False)
)

if st.button("Submit Answer", disabled=st.session_state.get("answered", False)):

    st.session_state.answered = True
    st.session_state.total_questions += 1

    if answer == q["answer"]:
        st.success("✅ Correct!")
        st.balloons()
        st.session_state.score += 10

        if st.session_state.score > st.session_state.best_score:
            st.session_state.best_score = st.session_state.score

    else:
        st.error(f"❌ Incorrect. The answer is '{q['answer']}'.")

    st.info("💡 " + q["explanation"])

if st.session_state.get("answered", False):

    if st.button("Next Question"):
        new_question()
        st.rerun()

st.divider()

if st.button("🔄 Restart Game"):
    st.session_state.score = 0
    st.session_state.total_questions = 0
    new_question()
    st.rerun()

st.markdown("---")
st.caption("⭐ Challenge yourself and beat your highest score!")
