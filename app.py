import streamlit as st
import time
from textblob import TextBlob
import spacy
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lex_rank import LexRankSummarizer
from sumy.summarizers.lsa import LsaSummarizer

# ============================
# 🌟 PAGE CONFIGURATION
# ============================
st.set_page_config(
    page_title="NLPiffy 3.0",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ============================
# 🎨 CUSTOM CSS DESIGN
# ============================
st.markdown("""
    <style>
        /* Background Gradient */
        .stApp {
            background: linear-gradient(135deg, #0f172a 0%, #1e293b 50%, #3e2723 100%);
            color: #f1f1f1;
        }

        /* Card Style */
        .card {
            background-color: rgba(255, 255, 255, 0.05);
            padding: 25px;
            border-radius: 16px;
            box-shadow: 0 6px 20px rgba(0, 0, 0, 0.4);
            margin-bottom: 25px;
            backdrop-filter: blur(8px);
        }

        /* Title Styling */
        .main-title {
            text-align: center;
            color: #fbbf24;
            font-size: 2.6rem;
            font-weight: 800;
            letter-spacing: 0.6px;
            text-shadow: 0 0 10px rgba(251, 191, 36, 0.6);
        }

        /* Subtitle */
        .sub-title {
            text-align: center;
            color: #d1d5db;
            font-size: 1.2rem;
            margin-bottom: 25px;
            font-weight: 500;
        }

        /* Buttons */
        div.stButton > button {
            background: linear-gradient(90deg, #1e3a8a, #3b82f6);
            color: white;
            border: none;
            border-radius: 10px;
            padding: 0.7rem 1.5rem;
            font-size: 1.05rem;
            transition: all 0.3s ease;
            font-weight: 600;
        }

        div.stButton > button:hover {
            background: linear-gradient(90deg, #3b82f6, #60a5fa);
            transform: translateY(-2px);
            box-shadow: 0 4px 15px rgba(96, 165, 250, 0.5);
        }

        /* Text Input */
        textarea, input, .stTextArea textarea {
            background-color: rgba(255, 255, 255, 0.08) !important;
            color: #f9fafb !important;
            border-radius: 10px !important;
            border: 1.5px solid #8b5e3c !important;
            font-size: 1rem !important;
            font-family: 'Segoe UI', sans-serif !important;
        }

        /* Sidebar styling */
        [data-testid="stSidebar"] {
            background: linear-gradient(180deg, #1e293b, #3e2723);
            color: #f1f1f1;
            font-weight: 500;
        }

        /* Sidebar headings */
        [data-testid="stSidebar"] h1, 
        [data-testid="stSidebar"] h2, 
        [data-testid="stSidebar"] h3 {
            color: #fbbf24;
        }

        /* Footer */
        footer, .reportview-container .main footer {
            color: #d1d5db;
            text-align: center;
            padding-top: 20px;
            font-size: 0.9rem;
        }

        /* Expander */
        .streamlit-expanderHeader {
            font-weight: 600;
            color: #fbbf24 !important;
        }

        /* Radio and Selectbox labels */
        label, .stSelectbox label {
            color: #f1f1f1 !important;
            font-weight: 600 !important;
        }

        /* Tables */
        .stDataFrame, div[data-testid="stDataFrame"] table {
            background-color: rgba(255,255,255,0.05);
            color: #f1f1f1;
            border-radius: 10px;
        }

        /* Metric box text */
        div[data-testid="stMetricValue"] {
            color: #fbbf24;
        }
    </style>
""", unsafe_allow_html=True)



# ============================
# 🧠 TITLE SECTION
# ============================
st.markdown("<h1 class='main-title'>🧠 NLPiffy 3.0</h1>", unsafe_allow_html=True)
st.markdown("<p class='sub-title'>Your Modern Natural Language Processing Playground</p>", unsafe_allow_html=True)
st.markdown("---")

# ============================
# 📘 ABOUT SECTION
# ============================
with st.expander("📘 About this App"):
    st.markdown("""
    Welcome to **NLPiffy 3.0**, an advanced NLP playground built with Streamlit!  
    It helps you perform various Natural Language Processing tasks such as:
    - 🪶 Tokenization & Lemmatization  
    - 🏷️ Named Entity Recognition (NER)  
    - 💬 Sentiment Analysis  
    - 🧾 Text Summarization (LexRank / LSA)

    💡 *Built using SpaCy, TextBlob, and Sumy — ready for Python 3.12+*
    """)

# ============================
# 🧩 SIDEBAR
# ============================
st.sidebar.image("images/Logo.png", width=100)
)
st.sidebar.header("⚙️ Configuration")
feature = st.sidebar.selectbox(
    "Choose an NLP Feature",
    ["Tokenization & Lemmatization", "Named Entity Recognition", "Sentiment Analysis", "Text Summarization"]
)
st.sidebar.info("💡 Tip: Paste a paragraph or an article for better results.")


# ============================
# ✍️ INPUT AREA
# ============================
st.markdown("<div class='card'>", unsafe_allow_html=True)
message = st.text_area("📝 Enter Text to Analyze", height=180, placeholder="Type or paste your text here...")
st.markdown("</div>", unsafe_allow_html=True)

# Load SpaCy model
nlp = spacy.load("en_core_web_sm")

# ============================
# ⚡ PROCESSING SECTION
# ============================
if st.button("✨ Run Analysis"):
    if not message.strip():
        st.warning("⚠️ Please enter some text to analyze!")
    else:
        with st.spinner("Processing your text..."):
            time.sleep(1)
            doc = nlp(message)

            # ============================
            # 🪶 TOKENIZATION & LEMMATIZATION
            # ============================
            if feature == "Tokenization & Lemmatization":
                st.markdown("<h3>🪶 Tokenization & Lemmatization</h3>", unsafe_allow_html=True)
                tokens = [(token.text, token.lemma_) for token in doc]
                st.dataframe(tokens, use_container_width=True)

            # ============================
            # 🏷️ NAMED ENTITY RECOGNITION
            # ============================
            elif feature == "Named Entity Recognition":
                st.markdown("<h3>🏷️ Named Entity Recognition</h3>", unsafe_allow_html=True)
                entities = [(ent.text, ent.label_) for ent in doc.ents]
                st.dataframe(entities, use_container_width=True)
                st.success(f"✅ Total Entities Found: {len(entities)}")

            # ============================
            # 💬 SENTIMENT ANALYSIS
            # ============================
            elif feature == "Sentiment Analysis":
                st.markdown("<h3>💬 Sentiment Analysis</h3>", unsafe_allow_html=True)
                blob = TextBlob(message)
                polarity = blob.sentiment.polarity
                subjectivity = blob.sentiment.subjectivity
                st.metric("Polarity", round(polarity, 3))
                st.metric("Subjectivity", round(subjectivity, 3))
                if polarity > 0:
                    st.success("😊 Positive Sentiment")
                elif polarity < 0:
                    st.error("😔 Negative Sentiment")
                else:
                    st.warning("😐 Neutral Sentiment")

            # ============================
            # 🧾 TEXT SUMMARIZATION
            # ============================
            elif feature == "Text Summarization":
                st.markdown("<h3>🧾 Text Summarization</h3>", unsafe_allow_html=True)
                method = st.radio("Choose a summarizer:", ["LexRank", "LSA"])
                parser = PlaintextParser.from_string(message, Tokenizer("english"))
                if method == "LexRank":
                    summarizer = LexRankSummarizer()
                else:
                    summarizer = LsaSummarizer()
                summary_sentences = summarizer(parser.document, 3)
                summary = " ".join(str(sentence) for sentence in summary_sentences)
                st.success("✅ Summary Generated:")
                st.markdown(f"**{summary}**")

