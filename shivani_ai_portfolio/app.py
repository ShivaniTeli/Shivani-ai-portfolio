import base64
from pathlib import Path
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Shivani Teli | AI/ML Engineer",
    page_icon="✦",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# -------------------------------------------------------------------
# EDIT THESE LINKS
# -------------------------------------------------------------------
GITHUB_URL = "https://github.com/ShivaniTeli"
LINKEDIN_URL = "https://www.linkedin.com/in/shivani-t-600413136/"
EMAIL = "shivaiteli57@gmail.com"
RESUME_PATH = "assets/Shivani_Resume.pdf"

# Convert the local resume to a browser-downloadable link so it can use
# the exact same premium HTML button styling as the other hero buttons.
resume_file = Path(RESUME_PATH)
if resume_file.exists():
    resume_b64 = base64.b64encode(resume_file.read_bytes()).decode("utf-8")
    RESUME_URL = f"data:application/pdf;base64,{resume_b64}"
else:
    RESUME_URL = "#"

# -------------------------------------------------------------------
# GLOBAL STYLES
# Medium slate theme + cyan/purple glow + glassmorphism + transitions
# -------------------------------------------------------------------
st.markdown(
    r"""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=Space+Grotesk:wght@500;600;700&display=swap');

:root {
    --bg: #4B4A43;
    --bg-2: #55544C;
    --panel: rgba(242, 240, 233, 0.16);
    --panel-strong: rgba(89, 87, 78, 0.72);
    --border: rgba(244, 241, 232, 0.30);
    --text: #F4F1E8;
    --muted: #D8D3C7;
    --cyan: #D7D0BF;
    --cyan-2: #F1EBDD;
    --purple: #B8AD98;
    --purple-2: #E4DCCB;
    --shadow: 0 18px 50px rgba(27, 27, 24, 0.20);
}

html { scroll-behavior: smooth; }

.stApp {
    background:
        radial-gradient(circle at 12% 15%, rgba(101,230,243,.13), transparent 28%),
        radial-gradient(circle at 88% 22%, rgba(194,156,255,.14), transparent 30%),
        linear-gradient(135deg, var(--bg) 0%, var(--bg-2) 48%, #615F55 100%);
    color: var(--text);
    font-family: "Inter", sans-serif;
}

[data-testid="stHeader"] { background: transparent; }
[data-testid="stToolbar"] { right: 1rem; }
#MainMenu, footer { visibility: hidden; }

.block-container {
    max-width: 1240px;
    padding-top: 1.5rem;
    padding-bottom: 5rem;
}

h1, h2, h3 {
    font-family: "Space Grotesk", sans-serif !important;
    color: var(--text) !important;
    letter-spacing: -0.025em;
}

p, li, label, .stMarkdown { color: var(--text); }

a { text-decoration: none !important; }

.nav-shell {
    position: sticky;
    top: .7rem;
    z-index: 999;
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: .78rem 1rem;
    margin-bottom: 1.4rem;
    border: 1px solid var(--border);
    background: rgba(73, 72, 65, .82);
    backdrop-filter: blur(18px);
    -webkit-backdrop-filter: blur(18px);
    border-radius: 18px;
    box-shadow: var(--shadow);
}
.brand {
    font-family: "Space Grotesk", sans-serif;
    font-weight: 800;
    letter-spacing: .08em;
    color: white;
}
.brand span { color: var(--cyan); }
.nav-links a {
    color: var(--muted) !important;
    margin-left: 1rem;
    font-size: .9rem;
    transition: .25s ease;
}
.nav-links a:hover { color: white !important; text-shadow: 0 0 18px rgba(101,230,243,.65); }

.hero {
    position: relative;
    overflow: hidden;
    min-height: 600px;
    border: 1px solid var(--border);
    border-radius: 30px;
    padding: clamp(2rem, 5vw, 4.6rem);
    background:
        linear-gradient(120deg, rgba(77,76,69,.94), rgba(94,92,82,.80)),
        radial-gradient(circle at 78% 30%, rgba(101,230,243,.12), transparent 35%);
    box-shadow: var(--shadow);
    isolation: isolate;
}
.hero::before {
    content: "";
    position: absolute;
    inset: 0;
    opacity: .18;
    background-image:
        linear-gradient(rgba(255,255,255,.08) 1px, transparent 1px),
        linear-gradient(90deg, rgba(255,255,255,.08) 1px, transparent 1px);
    background-size: 42px 42px;
    mask-image: linear-gradient(to bottom, black, transparent 90%);
    z-index: -2;
}
.hero-glow {
    position:absolute;
    width: 320px; height:320px;
    border-radius:50%;
    filter: blur(70px);
    opacity:.23;
    animation: floatGlow 8s ease-in-out infinite alternate;
    z-index:-1;
}
.glow-a { right:5%; top:4%; background:var(--cyan); }
.glow-b { right:24%; bottom:-12%; background:var(--purple); animation-delay:-3s; }
@keyframes floatGlow {
    from { transform: translate3d(-15px,-10px,0) scale(.9); }
    to { transform: translate3d(22px,18px,0) scale(1.12); }
}

.eyebrow {
    display:inline-flex;
    align-items:center;
    gap:.5rem;
    padding:.42rem .7rem;
    border-radius:999px;
    border:1px solid rgba(101,230,243,.28);
    background:rgba(101,230,243,.08);
    color:var(--cyan-2);
    font-size:.78rem;
    font-weight:700;
    letter-spacing:.12em;
}
.pulse-dot {
    width:8px; height:8px; border-radius:50%;
    background:var(--cyan);
    box-shadow:0 0 16px var(--cyan);
    animation:pulse 1.8s infinite;
}
@keyframes pulse {
    0%,100% { transform:scale(.75); opacity:.6; }
    50% { transform:scale(1.2); opacity:1; }
}

.hero-title {
    font-family:"Space Grotesk", sans-serif;
    font-size:clamp(2.35rem, 5vw, 4.65rem);
    line-height:.95;
    font-weight:800;
    max-width:820px;
    margin:1.4rem 0 1rem;
    letter-spacing:-.055em;
}
.gradient-text {
    background:linear-gradient(90deg, #ffffff 5%, var(--cyan-2) 48%, var(--purple-2) 92%);
    -webkit-background-clip:text;
    -webkit-text-fill-color:transparent;
    background-clip:text;
}
.hero-copy {
    max-width:720px;
    color:var(--muted);
    font-size:1.08rem;
    line-height:1.8;
}
.type-line {
    margin-top:1rem;
    color:#edf7ff;
    font-family:"Space Grotesk",sans-serif;
    font-weight:600;
}
.type-line .type {
    color:var(--cyan-2);
}
.type::after {
    content:"";
    animation: roles 10s infinite;
}
@keyframes roles {
    0%,18% { content:"AI/ML Engineer"; }
    22%,42% { content:"Generative AI Developer"; }
    46%,66% { content:"RAG & LLM Builder"; }
    70%,86% { content:"Agentic AI Engineer"; }
    90%,100% { content:"Production AI Builder"; }
}

.hero-actions { display:flex; flex-wrap:wrap; gap:.8rem; margin-top:1.7rem; }
.btn {
    display:inline-block;
    padding:.82rem 1.15rem;
    border-radius:13px;
    font-weight:700;
    transition:transform .25s ease, box-shadow .25s ease, border-color .25s ease;
}
.btn-primary {
    color:#272722 !important;
    background:linear-gradient(100deg,#F0ECE2,#D8D0BF);
    box-shadow:0 10px 30px rgba(101,230,243,.18);
}
.btn-secondary {
    color:white !important;
    border:1px solid var(--border);
    background:rgba(255,255,255,.06);
}
.btn:hover { transform:translateY(-3px); box-shadow:0 14px 35px rgba(20,31,50,.25); }

.floating-chip {
    position:absolute;
    padding:.48rem .72rem;
    border:1px solid rgba(255,255,255,.15);
    border-radius:999px;
    background:rgba(94,91,81,.62);
    backdrop-filter:blur(10px);
    font-size:.76rem;
    color:#eef8ff;
    animation:chipFloat 5s ease-in-out infinite;
}
.c1 { right:8%; top:18%; }
.c2 { right:20%; top:34%; animation-delay:-1.2s; }
.c3 { right:7%; top:51%; animation-delay:-2.1s; }
.c4 { right:24%; top:67%; animation-delay:-3.1s; }
@keyframes chipFloat {
    0%,100% { transform:translateY(0); }
    50% { transform:translateY(-10px); }
}

.section-wrap {
    padding:5.5rem 0 1rem;
    animation:fadeUp .7s ease both;
}
@keyframes fadeUp {
    from { opacity:0; transform:translateY(24px); }
    to { opacity:1; transform:translateY(0); }
}
.section-kicker {
    color:var(--cyan-2);
    font-size:.75rem;
    font-weight:800;
    letter-spacing:.15em;
    text-transform:uppercase;
}
.section-title {
    font-size:clamp(2rem,4vw,3.2rem);
    margin:.35rem 0 .6rem;
}
.section-sub { color:var(--muted); max-width:760px; line-height:1.75; }

.glass-card {
    height:100%;
    border:1px solid var(--border);
    border-radius:22px;
    padding:1.35rem;
    background:linear-gradient(145deg, rgba(242,240,233,.16), rgba(117,112,99,.28));
    backdrop-filter:blur(16px);
    -webkit-backdrop-filter:blur(16px);
    box-shadow:0 14px 38px rgba(20,31,50,.14);
    transition:transform .3s ease, border-color .3s ease, box-shadow .3s ease;
}
.glass-card:hover {
    transform:translateY(-7px);
    border-color:rgba(101,230,243,.45);
    box-shadow:0 20px 48px rgba(20,31,50,.24), 0 0 26px rgba(101,230,243,.08);
}
.card-num {
    font-family:"Space Grotesk",sans-serif;
    font-size:.8rem;
    color:var(--cyan-2);
    letter-spacing:.12em;
}
.card-title { font-size:1.3rem; font-weight:800; margin:.7rem 0; }
.card-copy { color:var(--muted); line-height:1.7; min-height:100px; }
.tags { display:flex; flex-wrap:wrap; gap:.4rem; margin-top:1rem; }
.tag {
    padding:.32rem .55rem;
    border-radius:8px;
    font-size:.72rem;
    color:#f5fbff;
    background:rgba(255,255,255,.075);
    border:1px solid rgba(255,255,255,.10);
}

.metric {
    text-align:center;
    padding:1.4rem .8rem;
    border:1px solid var(--border);
    border-radius:20px;
    background:rgba(242,240,233,.13);
    transition:.25s ease;
}
.metric:hover { transform:scale(1.025); background:rgba(103,124,154,.38); }
.metric strong {
    display:block;
    font-family:"Space Grotesk",sans-serif;
    font-size:2rem;
    color:white;
}
.metric span { color:var(--muted); font-size:.85rem; }

.skill-box {
    border-left:2px solid rgba(101,230,243,.55);
    padding:.3rem 0 .3rem 1rem;
    margin:.55rem 0;
}
.skill-box b { color:white; }
.skill-box span { color:var(--muted); }

.timeline-item {
    position:relative;
    margin-left:1rem;
    padding:0 0 2rem 2rem;
    border-left:1px solid rgba(199,212,231,.26);
}
.timeline-item::before {
    content:"";
    position:absolute;
    width:12px;height:12px;border-radius:50%;
    left:-6.5px;top:5px;
    background:var(--cyan);
    box-shadow:0 0 18px rgba(101,230,243,.65);
}
.timeline-year { color:var(--cyan-2); font-size:.8rem; font-weight:800; }
.timeline-title { font-weight:800; font-size:1.08rem; margin:.2rem 0; }
.timeline-copy { color:var(--muted); line-height:1.65; }

.ai-lab {
    border:1px solid rgba(194,156,255,.25);
    background:
        radial-gradient(circle at 88% 12%, rgba(194,156,255,.11), transparent 28%),
        rgba(77,96,127,.38);
    padding:1.4rem;
    border-radius:24px;
}
.status-row {
    display:flex; gap:.65rem; flex-wrap:wrap; margin:.7rem 0 1.2rem;
}
.status-pill {
    border:1px solid var(--border);
    background:rgba(255,255,255,.06);
    border-radius:999px;
    padding:.35rem .6rem;
    font-size:.72rem;
    color:var(--muted);
}
.status-pill::before { content:"●"; color:var(--cyan); margin-right:.4rem; }

div[data-testid="stTextInput"] input {
    background:rgba(74,72,65,.62) !important;
    border:1px solid rgba(220,238,255,.18) !important;
    color:white !important;
    border-radius:14px !important;
}
div[data-testid="stTextInput"] input:focus {
    border-color:rgba(101,230,243,.55) !important;
    box-shadow:0 0 0 2px rgba(101,230,243,.08) !important;
}
.stButton > button {
    border:1px solid rgba(101,230,243,.30);
    border-radius:12px;
    background:linear-gradient(100deg, rgba(101,230,243,.92), rgba(194,156,255,.90));
    color:#203047;
    font-weight:800;
    transition:.25s ease;
}
.stButton > button:hover { transform:translateY(-2px); border-color:white; color:#203047; }

.contact-card {
    text-align:center;
    padding:3rem 1.2rem;
    border:1px solid var(--border);
    border-radius:28px;
    background:linear-gradient(135deg,rgba(101,230,243,.08),rgba(194,156,255,.10));
}
.contact-links { display:flex; justify-content:center; flex-wrap:wrap; gap:.7rem; margin-top:1.2rem; }

.small-note { color:var(--muted); font-size:.78rem; }
hr { border-color:rgba(255,255,255,.10) !important; }

@media (max-width: 780px) {
    .nav-links { display:none; }
    .hero { min-height:660px; padding:2rem 1.25rem; }
    .hero-title { font-size:2.65rem; }
    .floating-chip { opacity:.58; font-size:.64rem; }
    .c1 { top:72%; left:7%; right:auto; }
    .c2 { top:79%; left:36%; right:auto; }
    .c3 { top:86%; left:12%; right:auto; }
    .c4 { display:none; }
    .section-wrap { padding-top:4rem; }
}

/* Warm editorial visual-only overrides */
.glass-card {
    background: rgba(239, 235, 225, 0.94) !important;
    border-color: rgba(255,255,255,.38) !important;
}
.glass-card .card-title, .glass-card b { color: #1D1D1A !important; }
.glass-card .card-copy, .glass-card .skill-box span { color: #555149 !important; }
.glass-card .card-num { color: #6E685D !important; }
.glass-card .tag {
    color: #35332E !important;
    background: rgba(77,74,66,.08) !important;
    border-color: rgba(77,74,66,.12) !important;
}
.metric { background: rgba(241,237,227,.92) !important; }
.metric strong { color: #1E1E1A !important; }
.metric span { color: #5D594F !important; }

</style>
""",
    unsafe_allow_html=True,
)

# -------------------------------------------------------------------
# NAVIGATION
# -------------------------------------------------------------------
st.markdown(
    f"""
<div class="nav-shell">
  <div class="brand">SHIVANI<span> TELI</span></div>
  <div class="nav-links">
    <a href="#about">About</a>
    <a href="#skills">Skills</a>
    <a href="#projects">Projects</a>
    <a href="#experience">Experience</a>
    <a href="#certifications">Credentials</a>
    <a href="#contact">Contact</a>
  </div>
</div>
""",
    unsafe_allow_html=True,
)

# -------------------------------------------------------------------
# HERO
# -------------------------------------------------------------------
st.markdown(
    f"""
<div class="hero">
  <div class="hero-glow glow-a"></div>
  <div class="hero-glow glow-b"></div>

  <div class="eyebrow"><span class="pulse-dot"></span> BUILDING PRODUCTION AI SYSTEMS</div>

  <div class="hero-title">
    Hi, I'm <span class="gradient-text">Shivani Teli.</span><br>
    I build intelligent AI systems.
  </div>

  <div class="hero-copy">
    AI/ML Engineer focused on Machine Learning, Generative AI, RAG, LLM applications
    and agentic workflows — from data and architecture to APIs, deployment and monitoring.
  </div>

  <div class="type-line">Engineering as: <span class="type"></span></div>

  <div class="hero-actions">
    <a class="btn btn-primary" href="#projects">Explore Projects ↓</a>
    <a class="btn btn-secondary" href="{RESUME_URL}" download="Shivani_Resume.pdf">Download Resume ↓</a>
    <a class="btn btn-secondary" href="{GITHUB_URL}" target="_blank">GitHub ↗</a>
    <a class="btn btn-secondary" href="{LINKEDIN_URL}" target="_blank">LinkedIn ↗</a>
  </div>

  <div class="floating-chip c1">✦ RAG</div>
  <div class="floating-chip c2">◉ LLM</div>
  <div class="floating-chip c3">⌁ LangGraph</div>
  <div class="floating-chip c4">◇ AI Agents</div>
</div>
""",
    unsafe_allow_html=True,
)

# -------------------------------------------------------------------
# ANIMATED NEURAL NETWORK
# -------------------------------------------------------------------
components.html(
    r"""
<div id="network-wrap">
  <canvas id="neuralCanvas"></canvas>
  <div class="network-label">LIVE AI NETWORK • RAG • AGENTS • ML</div>
</div>
<style>
html,body{margin:0;background:transparent;overflow:hidden}
#network-wrap{
  height:260px; position:relative; overflow:hidden; border-radius:24px;
  border:1px solid rgba(225,240,255,.15);
  background:linear-gradient(135deg,rgba(92,113,143,.26),rgba(70,91,122,.22));
}
#neuralCanvas{width:100%;height:100%;display:block}
.network-label{
  position:absolute;left:18px;bottom:14px;color:#d9e8f7;
  font:700 11px Inter,Arial;letter-spacing:.14em;opacity:.8
}
</style>
<script>
const canvas=document.getElementById("neuralCanvas");
const ctx=canvas.getContext("2d");
let W,H,dpr;
let nodes=[];
function resize(){
  dpr=window.devicePixelRatio||1;
  W=canvas.clientWidth; H=canvas.clientHeight;
  canvas.width=W*dpr; canvas.height=H*dpr;
  ctx.setTransform(dpr,0,0,dpr,0,0);
  const count=Math.max(24,Math.floor(W/42));
  nodes=Array.from({length:count},()=>({
    x:Math.random()*W,y:Math.random()*H,
    vx:(Math.random()-.5)*.34,vy:(Math.random()-.5)*.34,
    r:1.5+Math.random()*2.3
  }));
}
function draw(){
  ctx.clearRect(0,0,W,H);
  for(let i=0;i<nodes.length;i++){
    const a=nodes[i];
    a.x+=a.vx;a.y+=a.vy;
    if(a.x<0||a.x>W)a.vx*=-1;
    if(a.y<0||a.y>H)a.vy*=-1;
    for(let j=i+1;j<nodes.length;j++){
      const b=nodes[j],dx=a.x-b.x,dy=a.y-b.y,d=Math.hypot(dx,dy);
      if(d<125){
        const alpha=(1-d/125)*.28;
        ctx.strokeStyle=`rgba(159,231,244,${alpha})`;
        ctx.lineWidth=.7;
        ctx.beginPath();ctx.moveTo(a.x,a.y);ctx.lineTo(b.x,b.y);ctx.stroke();
      }
    }
  }
  nodes.forEach((n,i)=>{
    ctx.beginPath();ctx.arc(n.x,n.y,n.r,0,Math.PI*2);
    ctx.fillStyle=i%4===0?"rgba(210,181,255,.95)":"rgba(118,235,246,.95)";
    ctx.shadowBlur=13;ctx.shadowColor=i%4===0?"#c29cff":"#65e6f3";
    ctx.fill();ctx.shadowBlur=0;
  });
  requestAnimationFrame(draw);
}
window.addEventListener("resize",resize);resize();draw();
</script>
""",
    height=280,
)

# -------------------------------------------------------------------
# ABOUT + METRICS
# -------------------------------------------------------------------
st.markdown('<div id="about" class="section-wrap"><div class="section-kicker">01 / About</div><h2 class="section-title">Engineering experience. AI-first direction.</h2><p class="section-sub">I combine software engineering, data pipelines and production debugging experience with machine learning and modern Generative AI. My focus is building systems that can be explained, evaluated, deployed and monitored — not only notebooks.</p></div>', unsafe_allow_html=True)

m1, m2, m3, m4 = st.columns(4)
with m1:
    st.markdown('<div class="metric"><strong>4+</strong><span>Years Engineering Experience</span></div>', unsafe_allow_html=True)
with m2:
    st.markdown('<div class="metric"><strong>10K+</strong><span>Audio Sessions Analyzed</span></div>', unsafe_allow_html=True)
with m3:
    st.markdown('<div class="metric"><strong>30%</strong><span>Debugging Time Improvement</span></div>', unsafe_allow_html=True)
with m4:
    st.markdown('<div class="metric"><strong>3+</strong><span>End-to-End AI Projects</span></div>', unsafe_allow_html=True)

# -------------------------------------------------------------------
# SKILLS
# -------------------------------------------------------------------
st.markdown('<div id="skills" class="section-wrap"><div class="section-kicker">02 / Skills</div><h2 class="section-title">My AI engineering toolkit.</h2><p class="section-sub">A practical stack spanning data, ML, GenAI, backend engineering, cloud and production observability.</p></div>', unsafe_allow_html=True)

s1, s2, s3, s4 = st.columns(4)
skill_groups = [
    ("AI / ML", "Scikit-learn · XGBoost · Random Forest · NLP · Anomaly Detection · Model Evaluation"),
    ("Generative AI", "LLMs · RAG · Embeddings · Prompt Engineering · LangChain · LangGraph · AI Agents"),
    ("Backend / Data", "Python · SQL · Pandas · FastAPI · Flask · REST APIs · ETL · Microservices"),
    ("Cloud / MLOps", "AWS · Azure · Docker · GitHub · CI/CD · LangSmith · Application Monitoring"),
]
for col, (title, items) in zip([s1, s2, s3, s4], skill_groups):
    with col:
        st.markdown(f'<div class="glass-card"><div class="card-title">{title}</div><div class="skill-box"><span>{items}</span></div></div>', unsafe_allow_html=True)

# -------------------------------------------------------------------
# PROJECTS
# -------------------------------------------------------------------
st.markdown('<div id="projects" class="section-wrap"><div class="section-kicker">03 / Featured Work</div><h2 class="section-title">Systems I can build end-to-end.</h2><p class="section-sub">Each project is framed around the problem, architecture, implementation and production considerations recruiters and interviewers care about.</p></div>', unsafe_allow_html=True)

projects = [
    (
        "01 / MULTIMODAL AI",
        "AI Compliance Auditor",
        "A multimodal compliance workflow that processes video, extracts transcript/OCR information, orchestrates analysis with LangGraph and uses RAG to cross-reference content against compliance rules.",
        ["Azure Video Indexer", "LangGraph", "RAG", "Azure AI Search", "OpenAI", "LangSmith"],
    ),
    (
        "02 / GENERATIVE AI",
        "Enterprise HR RAG Assistant",
        "An enterprise knowledge assistant designed to answer HR policy questions from internal documents using chunking, embeddings, vector retrieval, grounded generation, security controls and evaluation.",
        ["Python", "FastAPI", "LangChain", "Embeddings", "Vector DB", "RAG"],
    ),
    (
        "03 / MACHINE LEARNING",
        "Zebra Device Compatibility ML",
        "A machine-learning workflow for identifying device compatibility patterns across keyboard/scanner streams, helping reduce avoidable test failures and improve validation efficiency.",
        ["Python", "XGBoost", "Pandas", "Feature Engineering", "Classification"],
    ),
]

cols = st.columns(3)
for col, (num, title, copy, tags) in zip(cols, projects):
    tag_html = "".join(f'<span class="tag">{t}</span>' for t in tags)
    with col:
        st.markdown(
            f'<div class="glass-card"><div class="card-num">{num}</div><div class="card-title">{title}</div><div class="card-copy">{copy}</div><div class="tags">{tag_html}</div></div>',
            unsafe_allow_html=True,
        )

# -------------------------------------------------------------------
# EXPERIENCE
# -------------------------------------------------------------------
st.markdown('<div id="experience" class="section-wrap"><div class="section-kicker">04 / Experience</div><h2 class="section-title">Software engineering foundation. Applied AI evolution.</h2><p class="section-sub">My experience combines production software engineering with hands-on Data Science, Machine Learning and Generative AI development.</p></div>', unsafe_allow_html=True)

st.markdown(
    """
<div class="timeline-item">
  <div class="timeline-year">LEARNBAY · DATA SCIENCE & GENERATIVE AI</div>
  <div class="timeline-title">AI / ML Project Experience</div>
  <div class="timeline-copy">Built hands-on Data Science, Machine Learning and Generative AI projects covering data preprocessing, feature engineering, model training and evaluation, RAG, LLM applications, embeddings, vector retrieval, LangChain/LangGraph workflows and cloud-based AI solutions.</div>
</div>
<div class="timeline-item">
  <div class="timeline-year">PERSISTENT SYSTEMS · ZEBRA TECHNOLOGIES</div>
  <div class="timeline-title">Software / Data Engineering</div>
  <div class="timeline-copy">Worked across Android framework/application development and data-driven performance analysis. Built Python/AWS ETL workflows for large-scale audio-session analytics and worked on device-stream compatibility use cases.</div>
</div>
<div class="timeline-item">
  <div class="timeline-year">HARMAN · INTEL PROJECTS</div>
  <div class="timeline-title">Framework Development & Validation Automation</div>
  <div class="timeline-copy">Built Python automation around CTS/GTS/VTS validation, log analysis and debugging workflows, improving regression detection and reducing manual debugging effort.</div>
</div>
""",
    unsafe_allow_html=True,
)

# -------------------------------------------------------------------
# CERTIFICATIONS
# -------------------------------------------------------------------
st.markdown('<div id="certifications" class="section-wrap"><div class="section-kicker">05 / Credentials</div><h2 class="section-title">Certifications & advanced learning.</h2><p class="section-sub">Formal learning that complements my production engineering experience and hands-on AI/ML projects.</p></div>', unsafe_allow_html=True)

c1, c2 = st.columns(2)
with c1:
    st.markdown(
        """<div class="glass-card">
        <div class="card-num">IBM</div>
        <div class="card-title">IBM Data Science Professional Certificate</div>
        <div class="card-copy">Professional Data Science training covering Python, SQL, data analysis, visualization, machine learning and applied data-science workflows.</div>
        <div class="tags"><span class="tag">Data Science</span><span class="tag">Python</span><span class="tag">SQL</span><span class="tag">Machine Learning</span></div>
        </div>""",
        unsafe_allow_html=True,
    )
with c2:
    st.markdown(
        """<div class="glass-card">
        <div class="card-num">IIT GUWAHATI · LEARNBAY</div>
        <div class="card-title">Advanced Data Science & Generative AI Program</div>
        <div class="card-copy">Advanced learning in Data Science and Generative AI, including machine learning, LLMs, RAG, prompt engineering, AI agents and production-oriented AI development.</div>
        <div class="tags"><span class="tag">Generative AI</span><span class="tag">LLMs</span><span class="tag">RAG</span><span class="tag">AI Agents</span></div>
        </div>""",
        unsafe_allow_html=True,
    )

# -------------------------------------------------------------------
# CONTACT
# -------------------------------------------------------------------
st.markdown(
    f"""
<div id="contact" class="section-wrap">
  <div class="contact-card">
    <div class="section-kicker">06 / Contact</div>
    <h2 class="section-title">Let's build something intelligent.</h2>
    <p class="section-sub" style="margin:0 auto;">Open to AI/ML Engineering, Data Science and Generative AI opportunities.</p>
    <div class="contact-links">
      <a class="btn btn-primary" href="{LINKEDIN_URL}" target="_blank">LinkedIn ↗</a>
      <a class="btn btn-secondary" href="{GITHUB_URL}" target="_blank">GitHub ↗</a>
      <a class="btn btn-secondary" href="mailto:{EMAIL}">Email ↗</a>
    </div>
  </div>
</div>
""",
    unsafe_allow_html=True,
)

