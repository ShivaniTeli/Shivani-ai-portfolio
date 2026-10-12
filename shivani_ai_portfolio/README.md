# Shivani Teli — AI/ML Engineer Portfolio

A Streamlit portfolio focused on AI/ML, Generative AI, RAG, agentic systems, projects and recruiter-facing demos.

## 1. Customize before publishing
In `app.py`, replace:
- `YOUR_GITHUB`
- `YOUR_LINKEDIN`
- `YOUR_EMAIL`

Also review every metric/project statement and keep only claims you can explain in an interview.

## 2. Run locally
```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate

pip install -r requirements.txt
streamlit run app.py
```
Then open the localhost URL Streamlit prints.

## 3. Put it on GitHub
1. Create a new GitHub repository, e.g. `ai-portfolio`.
2. From this folder run:
```bash
git init
git add .
git commit -m "Build AI portfolio"
git branch -M main
git remote add origin https://github.com/YOUR_GITHUB/ai-portfolio.git
git push -u origin main
```

## 4. Deploy on Streamlit Community Cloud
1. Go to https://share.streamlit.io/
2. Sign in with GitHub.
3. Click **Create app** / **New app**.
4. Select your `ai-portfolio` repository and `main` branch.
5. Set the main file path to `app.py`.
6. Deploy.
7. Streamlit gives you a public URL such as `https://your-name-ai-portfolio.streamlit.app`.

That public URL is your deployed portfolio. Add it to your resume and LinkedIn.

## 5. Resume format
```
Portfolio: https://your-name-ai-portfolio.streamlit.app
GitHub:    https://github.com/YOUR_GITHUB
LinkedIn:  https://linkedin.com/in/YOUR_LINKEDIN
```

## Recommended next upgrades
- Add your real project screenshots and architecture diagrams under `assets/`.
- Add a downloadable resume PDF.
- Replace the rule-based AI Lab with a real RAG assistant.
- Add live links to deployed project demos.
- Add LangSmith/observability screenshots where appropriate.
- Use Streamlit Secrets for API keys; never commit secrets to GitHub.
