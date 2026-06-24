import streamlit as st
import random
import streamlit.components.v1 as components

st.set_page_config(page_title="Phonics Quest", page_icon="🔤", layout="centered")

QUESTIONS = [
    {
        "phonogram": "sh",
        "sound_text": "shhh",
        "question": "Which word has the /sh/ sound?",
        "options": ["ship", "sip", "chip", "sit"],
        "answer": "ship",
        "explanation": "'sh' makes the /sh/ sound, as in ship."
    },
    {
        "phonogram": "ch",
        "sound_text": "ch",
        "question": "Which word has the /ch/ sound?",
        "options": ["shop", "chat", "thin", "ship"],
        "answer": "chat",
        "explanation": "'ch' makes the /ch/ sound, as in chat."
    },
    {
        "phonogram": "ai",
        "sound_text": "ay",
        "question": "Which word has the /ai/ sound?",
        "options": ["rain", "run", "red", "rock"],
        "answer": "rain",
        "explanation": "'ai' usually makes the long /a/ sound, as in rain."
    },
    {
        "phonogram": "ee",
        "sound_text": "ee",
        "question": "Which word has the /ee/ sound?",
        "options": ["bed", "bee", "big", "bad"],
        "answer": "bee",
        "explanation": "'ee' makes the long /e/ sound, as in bee."
    },
    {
        "phonogram": "igh",
        "sound_text": "eye",
        "question": "You see the word 'light'. Which phonogram helps you read it?",
        "options": ["igh", "sh", "ch", "oo"],
        "answer": "igh",
        "explanation": "'igh' makes the long /i/ sound, as in light."
    },
    {
        "phonogram": "oo",
        "sound_text": "oo",
        "question": "You see the word 'moon'. Which sound do the letters 'oo' make?",
        "options": ["long /oo/", "/sh/", "/ai/", "short /a/"],
        "answer": "long /oo/",
        "explanation": "'oo' makes the long /oo/ sound, as in moon."
    },
    {
        "phonogram": "th",
        "sound_text": "th",
        "question": "Which word has the /th/ sound?",
        "options": ["then", "ship", "chip", "sing"],
        "answer": "then",
        "explanation": "'th' makes the /th/ sound, as in then."
    }
]


def speak_button(text, label):
    components.html(
        f"""
        <button onclick="speakText()" style="
            background-color:#ffcc4d;
            border:none;
            padding:10px 18px;
            border-radius:12px;
            font-size:18px;
            cursor:pointer;">
            🔊 {label}
        </button>

        <script>
        function speakText() {{
            const msg = new SpeechSynthesisUtterance("{text}");
            msg.lang = "en-US";
            msg.rate = 0.7;
            msg.pitch = 1.1;
            window.speechSynthesis.speak(msg);
        }}
        </script>
        """,
        height=60
    )


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
st.write("Listen to the phonogram sound. Then choose the correct answer!")

col1, col2, col3 = st.columns(3)
col1.metric("Score", st.session_state.score)
col2.metric("Best Score", st.session_state.best_score)
col3.metric("Questions", st.session_state.total_questions)

st.divider()

q = st.session_state.question

st.subheader(f"🎧 Phonogram: {q['phonogram']}")
speak_button(q["sound_text"], "Hear the sound")

st.subheader("🎯 Challenge")
st.write(q["question"])

answer = st.radio(
    "Choose one answer:",
    q["options"],
    index=None,
    disabled=st.session_state.answered
)

if st.button("Submit Answer", disabled=st.session_state.answered or answer is None):
    st.session_state.answered = True
    st.session_state.total_questions += 1

    if answer == q["answer"]:
        st.success("✅ Correct!")
        st.balloons()
        st.session_state.score += 10
        st.session_state.best_score = max(
            st.session_state.best_score,
            st.session_state.score
        )
    else:
        st.error(f"❌ Incorrect. The answer is '{q['answer']}'.")

    st.info("💡 " + q["explanation"])

if st.session_state.answered:
    if st.button("Next Question"):
        new_question()
        st.rerun()

st.divider()

if st.button("🔄 Restart Game"):
    st.session_state.score = 0
    st.session_state.total_questions = 0
    new_question()
    st.rerun()

st.caption("⭐ Listen, choose, learn and beat your best score!")
