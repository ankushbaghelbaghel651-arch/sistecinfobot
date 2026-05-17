import streamlit as st
import numpy as np

# ── Page config ──────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="SISTec Info Bot",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ── CSS ───────────────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=DM+Mono:wght@400;500&display=swap');

html, body, [class*="css"] {
    font-family: 'DM Sans', sans-serif;
}

.main-header {
    background: linear-gradient(135deg, #0f1b4c 0%, #1a2f7a 50%, #1e40af 100%);
    padding: 2.2rem 2rem;
    border-radius: 18px;
    margin-bottom: 1.5rem;
    text-align: center;
    color: white;
    box-shadow: 0 8px 40px rgba(15,27,76,0.35);
    position: relative;
    overflow: hidden;
}
.main-header::before {
    content: '';
    position: absolute;
    top: -40px; right: -40px;
    width: 180px; height: 180px;
    background: rgba(255,255,255,0.05);
    border-radius: 50%;
}
.main-header::after {
    content: '';
    position: absolute;
    bottom: -60px; left: -20px;
    width: 220px; height: 220px;
    background: rgba(255,255,255,0.04);
    border-radius: 50%;
}
.main-header h1 {
    font-size: 2.4rem;
    font-weight: 700;
    margin: 0;
    letter-spacing: -0.5px;
}
.main-header p {
    font-size: 1rem;
    opacity: 0.8;
    margin: 0.5rem 0 0;
    font-weight: 400;
}

.chat-user {
    background: linear-gradient(135deg, #dbeafe, #eff6ff);
    border-radius: 16px 16px 4px 16px;
    padding: 0.85rem 1.1rem;
    margin: 0.6rem 0 0.6rem auto;
    max-width: 72%;
    color: #1e3a8a;
    font-weight: 500;
    border: 1px solid #bfdbfe;
    line-height: 1.6;
}
.chat-bot {
    background: white;
    border: 1px solid #e2e8f0;
    border-radius: 16px 16px 16px 4px;
    padding: 0.9rem 1.1rem;
    margin: 0.6rem auto 0.6rem 0;
    max-width: 85%;
    color: #1e293b;
    box-shadow: 0 2px 12px rgba(0,0,0,0.06);
    line-height: 1.7;
}
.source-box {
    background: #f8faff;
    border-left: 4px solid #3b82f6;
    border-radius: 0 8px 8px 0;
    padding: 0.7rem 1rem;
    margin-top: 0.5rem;
    font-size: 0.82rem;
    color: #475569;
    font-family: 'DM Mono', monospace;
}
.metric-card {
    background: white;
    border: 1px solid #e2e8f0;
    border-radius: 14px;
    padding: 1rem;
    text-align: center;
    box-shadow: 0 2px 10px rgba(0,0,0,0.04);
    transition: box-shadow 0.2s;
}
.metric-card:hover {
    box-shadow: 0 4px 20px rgba(0,0,0,0.09);
}
.metric-card b {
    font-size: 1.5rem;
    color: #1e40af;
    display: block;
    margin-bottom: 0.2rem;
}
.metric-card small {
    color: #64748b;
    font-size: 0.78rem;
    font-weight: 500;
    text-transform: uppercase;
    letter-spacing: 0.5px;
}
.badge {
    display: inline-block;
    background: #eff6ff;
    color: #1d4ed8;
    border-radius: 20px;
    padding: 0.2rem 0.75rem;
    font-size: 0.75rem;
    font-weight: 600;
    margin: 0.15rem;
    border: 1px solid #bfdbfe;
}
.status-ready {
    display: inline-block;
    background: #dcfce7;
    color: #16a34a;
    border-radius: 20px;
    padding: 0.2rem 0.75rem;
    font-size: 0.75rem;
    font-weight: 600;
    border: 1px solid #bbf7d0;
}
.status-pending {
    display: inline-block;
    background: #fef9c3;
    color: #a16207;
    border-radius: 20px;
    padding: 0.2rem 0.75rem;
    font-size: 0.75rem;
    font-weight: 600;
    border: 1px solid #fef08a;
}
.stButton > button {
    background: linear-gradient(135deg, #1e3a8a, #2563eb) !important;
    color: white !important;
    border: none !important;
    border-radius: 10px !important;
    font-weight: 600 !important;
    padding: 0.5rem 1.5rem !important;
    transition: opacity 0.2s !important;
}
.stButton > button:hover {
    opacity: 0.9 !important;
}
.stTextInput > div > div > input {
    border: 2px solid #e2e8f0 !important;
    border-radius: 10px !important;
    font-family: 'DM Sans', sans-serif !important;
    transition: border-color 0.2s !important;
}
.stTextInput > div > div > input:focus {
    border-color: #3b82f6 !important;
    box-shadow: 0 0 0 3px rgba(59,130,246,0.1) !important;
}
.info-banner {
    background: linear-gradient(135deg, #eff6ff, #f0fdf4);
    border: 1px solid #bfdbfe;
    border-radius: 12px;
    padding: 1rem 1.2rem;
    color: #1e40af;
    font-size: 0.95rem;
}
div[data-testid="stSidebarContent"] {
    background: #f8faff;
}
</style>
""", unsafe_allow_html=True)


# ── Demo knowledge base ───────────────────────────────────────────────────────
DEMO_TEXT = """
[Document: SISTec Overview]
Sagar Institute of Science Technology & Engineering (SISTec) Gandhi Nagar is located in Bhopal, Madhya Pradesh, India.
It is affiliated to Rajiv Gandhi Proudyogiki Vishwavidyalaya (RGPV) and approved by AICTE.
The institute offers undergraduate and postgraduate programs in engineering and technology.
SISTec is known for its modern infrastructure, experienced faculty, and strong industry connections.

[Document: Courses Offered]
SISTec Gandhi Nagar offers the following B.E. programs:
- Computer Science & Engineering (CSE)
- Artificial Intelligence & Data Science (AI & DS)
- Information Technology (IT)
- Electronics & Communication Engineering (ECE)
- Mechanical Engineering (ME)
- Civil Engineering (CE)
Postgraduate: M.Tech in Computer Science
Lateral Entry (LE) admission is available for diploma holders directly into 2nd year B.E.

[Document: Admission Process]
Admissions are conducted through MP DTE (Directorate of Technical Education) via the DTE counselling process.
Students must have passed 12th with PCM (Physics, Chemistry, Mathematics) with minimum 45% marks (40% for SC/ST).
JEE Main score is preferred for admission consideration.
The admission helpline number and portal link are available on the official website www.sistec.ac.in.
Documents required: 10th marksheet, 12th marksheet, character certificate, migration certificate, passport-size photograph, category certificate (if applicable).

[Document: Fees Structure]
The approximate tuition fee for B.E. programs is Rs. 60,000 to Rs. 75,000 per year depending on the branch.
Hostel fee is approximately Rs. 70,000 per year (includes room and mess charges).
Scholarship schemes available:
- MP government fee waiver for eligible SC/ST/OBC students
- Merit scholarships for top-performing students
- Central government scholarship schemes
Fee can be paid online via the college ERP portal.

[Document: Campus and Facilities]
SISTec Gandhi Nagar has a modern, sprawling campus with well-equipped laboratories and a central library.
The campus has high-speed Wi-Fi connectivity throughout.
Sports facilities include a cricket ground, basketball court, volleyball court, and indoor games room.
Hostel facility is available for both boys and girls with 24x7 security and CCTV surveillance.
Other campus amenities: cafeteria, medical room, ATM, stationery shop, transport facility.
The campus is equipped with smart classrooms and audio-visual (AV) halls for seminars and workshops.

[Document: Placement Cell]
The Training & Placement Cell (T&P Cell) at SISTec connects students with top recruiters.
Companies that have visited for campus recruitment include TCS, Infosys, Wipro, Capgemini, Tech Mahindra, HCL, Mphasis, and several startups.
Average package offered is between 3 LPA to 6 LPA. Highest package recorded is 12 LPA.
The placement cell conducts year-round soft skills training, aptitude preparation, mock interviews, and group discussions.
Students can register with the placement portal to track opportunities.

[Document: Events and Student Activities]
SISTec organizes several annual events:
- Utkarsh: The annual cultural festival
- Technical Fest: Includes coding competitions, robotics events, paper presentations
- Sports Week: Inter-college and intra-college competitions
The AI & DS department regularly conducts workshops, hackathons, and coding competitions.
The "Build with RAG: AI Workshop & Competition" was held on 14th–15th May 2026 at the AI & DS AV Hall.
Student clubs include the Coding Club, Robotics Club, Cultural Committee, NSS (National Service Scheme), and the Entrepreneurship Cell.

[Document: Faculty and Administration]
SISTec has a team of highly qualified and experienced faculty members with PhDs and industry experience.
The institute is headed by a Principal and supported by Heads of Departments (HoDs) for each branch.
Faculty members are actively involved in research, publications, and funded projects.
The administrative office handles student records, fee receipts, bonafide certificates, and other official documents.

[Document: Contact Information]
Address: SISTec Gandhi Nagar, Bhopal, Madhya Pradesh - 462036
Website: www.sistec.ac.in
The institute is open Monday to Saturday, 9:00 AM to 5:00 PM.
For admissions enquiry, visit the official website or contact the admission office directly on campus.
For placement enquiries, contact the Training & Placement Cell via the official website.
"""


# ── RAG Pipeline ──────────────────────────────────────────────────────────────
def build_rag_pipeline(api_key: str, doc_texts: list):
    """Build embeddings + FAISS index from documents. Returns (index, chunks, meta)."""
    import google.generativeai as genai
    import faiss

    genai.configure(api_key=api_key)

    chunks, meta = [], []
    for fname, text in doc_texts:
        size, overlap = 500, 80
        words = text.split()
        i = 0
        while i < len(words):
            chunk = " ".join(words[i: i + size])
            chunks.append(chunk)
            meta.append(fname)
            i += size - overlap

    embeddings = []
    for chunk in chunks:
        res = genai.embed_content(
            model="models/text-embedding-004",
            content=chunk,
            task_type="retrieval_document",
        )
        embeddings.append(res["embedding"])

    arr = np.array(embeddings, dtype="float32")
    faiss.normalize_L2(arr)
    index = faiss.IndexFlatIP(arr.shape[1])
    index.add(arr)

    return index, chunks, meta


def retrieve_and_answer(query: str, index, chunks: list, meta: list, api_key: str, top_k: int = 4):
    """Retrieve top-k chunks and generate an answer using Gemini."""
    import google.generativeai as genai
    import faiss

    genai.configure(api_key=api_key)

    # Embed the query
    qres = genai.embed_content(
        model="models/text-embedding-004",
        content=query,
        task_type="retrieval_query",
    )
    qvec = np.array([qres["embedding"]], dtype="float32")
    faiss.normalize_L2(qvec)

    scores, ids = index.search(qvec, top_k)
    retrieved = [
        (chunks[i], meta[i], float(scores[0][j]))
        for j, i in enumerate(ids[0])
        if i >= 0
    ]

    context = "\n\n".join(f"[Source: {m}]\n{c}" for c, m, _ in retrieved)

    prompt = f"""You are SISTec Info Bot, a helpful and friendly assistant for Sagar Institute of Science Technology & Engineering (SISTec), Gandhi Nagar, Bhopal.

Answer ONLY from the provided context below. If the answer is not found in the context, respond with:
"I'm sorry, I don't have information about that in my knowledge base. Please contact the college office directly at www.sistec.ac.in or visit the campus."

Context:
{context}

Question: {query}

Instructions:
- Be concise, accurate, and student-friendly
- Use bullet points when listing multiple items
- Mention the source document when relevant
- Do NOT make up or assume any information not present in the context
- Keep your response focused and helpful"""

    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(prompt)
    return response.text, retrieved


# ── Session state init ────────────────────────────────────────────────────────
if "messages" not in st.session_state:
    st.session_state["messages"] = []
if "rag_ready" not in st.session_state:
    st.session_state["rag_ready"] = False
if "rag_data" not in st.session_state:
    st.session_state["rag_data"] = None
if "prefill" not in st.session_state:
    st.session_state["prefill"] = ""
if "chunk_count" not in st.session_state:
    st.session_state["chunk_count"] = 0
if "doc_count" not in st.session_state:
    st.session_state["doc_count"] = 0


# ── Sidebar ───────────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("## ⚙️ Setup")
    api_key = st.text_input(
        "🔑 Gemini API Key",
        type="password",
        help="Get a free key at aistudio.google.com",
    )

    st.markdown("---")
    st.markdown("### 📂 Upload College Documents")
    uploaded = st.file_uploader(
        "Upload PDFs or TXT files",
        accept_multiple_files=True,
        type=["pdf", "txt"],
        help="Add SISTec prospectus, handbook, event docs, brochures, etc.",
    )

    use_demo = st.checkbox(
        "✅ Use built-in SISTec knowledge base",
        value=True,
        help="Includes pre-loaded SISTec information for immediate use.",
    )

    build_btn = st.button("🚀 Build Knowledge Base", use_container_width=True)

    st.markdown("---")
    st.markdown("### 💡 Sample Questions")
    sample_qs = [
        "What courses does SISTec offer?",
        "What are the hostel facilities?",
        "How to apply for admission?",
        "Tell me about the placement cell",
        "What are the fee details?",
        "What events does SISTec organise?",
        "What are the campus facilities?",
        "How can I contact SISTec?",
    ]
    for q in sample_qs:
        if st.button(q, key=f"sq_{q}", use_container_width=True):
            st.session_state["prefill"] = q

    st.markdown("---")
    st.caption("🛠 Built with RAG · Gemini 1.5 Flash · FAISS · Streamlit")


# ── Main area ─────────────────────────────────────────────────────────────────
st.markdown("""
<div class="main-header">
  <h1>🎓 SISTec Info Bot</h1>
  <p>AI-powered college information assistant · Powered by RAG + Gemini 1.5 Flash</p>
</div>
""", unsafe_allow_html=True)

# Metrics row
col1, col2, col3, col4 = st.columns(4)
with col1:
    total_docs = st.session_state["doc_count"]
    st.markdown(
        f'<div class="metric-card"><b>{total_docs}</b><small>Documents</small></div>',
        unsafe_allow_html=True,
    )
with col2:
    if st.session_state["rag_ready"]:
        kb_status = '<span class="status-ready">✅ Ready</span>'
    else:
        kb_status = '<span class="status-pending">⏳ Pending</span>'
    st.markdown(
        f'<div class="metric-card">{kb_status}<br><small style="margin-top:4px;display:block">KB Status</small></div>',
        unsafe_allow_html=True,
    )
with col3:
    msgs = len(st.session_state["messages"])
    st.markdown(
        f'<div class="metric-card"><b>{msgs}</b><small>Messages</small></div>',
        unsafe_allow_html=True,
    )
with col4:
    chunks = st.session_state["chunk_count"]
    st.markdown(
        f'<div class="metric-card"><b>{chunks}</b><small>Chunks Indexed</small></div>',
        unsafe_allow_html=True,
    )

st.markdown("---")


# ── Build Knowledge Base ──────────────────────────────────────────────────────
if build_btn:
    if not api_key:
        st.error("⚠️ Please enter your Gemini API key in the sidebar first!")
    else:
        doc_texts = []
        if use_demo:
            doc_texts.append(("SISTec_KnowledgeBase.txt", DEMO_TEXT))

        if uploaded:
            for f in uploaded:
                try:
                    if f.name.lower().endswith(".pdf"):
                        try:
                            import pdfplumber
                            with pdfplumber.open(f) as pdf:
                                text = "\n".join(
                                    page.extract_text() or "" for page in pdf.pages
                                )
                        except ImportError:
                            st.warning(
                                f"pdfplumber not installed. Could not read PDF: {f.name}. "
                                "Install with: pip install pdfplumber"
                            )
                            continue
                    else:
                        text = f.read().decode("utf-8", errors="ignore")

                    if text.strip():
                        doc_texts.append((f.name, text))
                    else:
                        st.warning(f"⚠️ {f.name} appears to be empty or unreadable.")
                except Exception as e:
                    st.warning(f"⚠️ Could not read {f.name}: {e}")

        if not doc_texts:
            st.error("❌ No documents to process! Enable the demo KB or upload files.")
        else:
            with st.spinner("🔨 Building knowledge base — chunking & embedding..."):
                try:
                    index, chunks, meta = build_rag_pipeline(api_key, doc_texts)
                    st.session_state["rag_data"] = (index, chunks, meta)
                    st.session_state["rag_ready"] = True
                    st.session_state["messages"] = []
                    st.session_state["chunk_count"] = len(chunks)
                    st.session_state["doc_count"] = len(doc_texts)
                    st.success(
                        f"✅ Knowledge base ready! "
                        f"{len(chunks)} chunks indexed from {len(doc_texts)} document(s)."
                    )
                    st.rerun()
                except Exception as e:
                    st.error(f"❌ Error building knowledge base: {e}")


# ── Chat history display ──────────────────────────────────────────────────────
for msg in st.session_state["messages"]:
    if msg["role"] == "user":
        st.markdown(
            f'<div class="chat-user">🧑‍🎓 {msg["content"]}</div>',
            unsafe_allow_html=True,
        )
    else:
        st.markdown(
            f'<div class="chat-bot">🤖 {msg["content"]}</div>',
            unsafe_allow_html=True,
        )
        if msg.get("sources"):
            with st.expander("📄 View retrieved source chunks"):
                for chunk_text, fname, score in msg["sources"]:
                    preview = chunk_text[:320].replace("<", "&lt;").replace(">", "&gt;")
                    st.markdown(
                        f'<div class="source-box">'
                        f'<span class="badge">📄 {fname}</span> '
                        f'<span class="badge">score: {score:.3f}</span>'
                        f'<br><br>{preview}...'
                        f'</div>',
                        unsafe_allow_html=True,
                    )


# ── Chat input ────────────────────────────────────────────────────────────────
prefill_val = st.session_state.pop("prefill", "")

user_input = st.text_input(
    "Ask anything about SISTec 👇",
    value=prefill_val,
    placeholder="e.g. What B.E. courses are offered at SISTec?",
    key="chat_input",
)

send_col, clear_col, _ = st.columns([1, 1, 4])
with send_col:
    send_btn = st.button("Send 📨", use_container_width=True)
with clear_col:
    clear_btn = st.button("🗑️ Clear", use_container_width=True)

if clear_btn:
    st.session_state["messages"] = []
    st.rerun()

if send_btn and user_input.strip():
    if not st.session_state["rag_ready"]:
        st.warning("⚠️ Please build the knowledge base first using the sidebar!")
    elif not api_key:
        st.warning("⚠️ Please enter your Gemini API key in the sidebar!")
    else:
        st.session_state["messages"].append({"role": "user", "content": user_input})
        index, chunks, meta = st.session_state["rag_data"]

        with st.spinner("🤔 Thinking..."):
            try:
                answer, sources = retrieve_and_answer(
                    user_input, index, chunks, meta, api_key
                )
                st.session_state["messages"].append(
                    {"role": "bot", "content": answer, "sources": sources}
                )
            except Exception as e:
                st.session_state["messages"].append(
                    {
                        "role": "bot",
                        "content": f"❌ An error occurred: {str(e)}\n\nPlease check your API key and try again.",
                        "sources": [],
                    }
                )
        st.rerun()


# ── Welcome state ─────────────────────────────────────────────────────────────
if not st.session_state["rag_ready"]:
    st.markdown("""
    <div class="info-banner">
        👈 <strong>Get started:</strong> Enter your Gemini API key in the sidebar, then click
        <strong>Build Knowledge Base</strong>. The built-in SISTec knowledge base is pre-loaded
        so you can start chatting immediately after building!
    </div>
    """, unsafe_allow_html=True)
