# 🤖 SAFE.AGENT — Your AI's Mechanic

> **We monitor your machine learning models in real-time, detect data drift instantly, and trigger automatic retraining before your business logic fails.**

---

## 📸 Screenshots

### 🏠 Landing Page
<img width="1600" height="799" alt="WhatsApp Image 2026-04-30 at 2 07 17 PM" src="https://github.com/user-attachments/assets/c7742b68-db35-48f4-b282-594ef5bcafa4" />
*A clean, minimal hero page introducing Safe Agent — "Your AI's Mechanic." Deploy SafeAgent with a single click.*

---

### 📊 Self-Auditing Monitor Dashboard
<img width="1600" height="779" alt="WhatsApp Image 2026-04-30 at 2 07 03 PM" src="https://github.com/user-attachments/assets/7e10656d-24b1-42ec-99e6-815056bfa18e" />
*The main monitoring dashboard showing real-time system health. Displays Risk Score (0 = PASS), Average Confidence (94.2%), Estimated Accuracy (91.0%), Data Processed (1,204 records), Detected Issues panel, and a live Confidence Trend chart. Sensitivity is configurable (Medium/Standard shown). Scenario injection buttons (Healthy / Risky Drift) allow instant simulation.*

---

### 📤 System Injection (Upload Page)
<img width="1600" height="777" alt="WhatsApp Image 2026-04-30 at 2 07 35 PM" src="https://github.com/user-attachments/assets/628da918-8163-4fb7-81ae-8e024d4ce95a" />
*The "System Injection" page (Step 01) — upload your trained AI Model (.joblib or .pkl) and Reference Data (CSV dataset for baseline). Hit "Run System Audit" to deploy monitoring.*

---

## 🚀 What is Safe Agent?

**Safe Agent** is a web-based AI model monitoring and self-healing dashboard built with **Python + Flask**. It autonomously watches your deployed machine learning models, detects degradation, and repairs them — without human intervention.

---

## ✨ Features

| Feature | Description |
|---|---|
| 🔍 **Live Health Monitoring** | Continuous audit of model confidence, data drift, and prediction bias |
| 🧠 **AI Explanation** | Google Gemini generates plain-English audit summaries |
| ⚡ **Auto-Repair** | Autonomously retrains RandomForest classifier on clean reference data |
| 📈 **Confidence Trend** | Real-time Chart.js visualization of prediction confidence over time |
| 🎯 **Scenario Injection** | Simulate Healthy or Risky (Drift) traffic instantly |
| 🔧 **Sensitivity Config** | Low / Medium / High audit sensitivity multiplier |
| 🔐 **Secure Auth** | PBKDF2-SHA256 hashed passwords + session management |
| 📥 **Artifact Download** | Download repaired model (.pkl) and cleaned dataset (.csv) |

---

## 🛠️ Tech Stack

```
Backend     → Python 3.x, Flask
ML Engine   → Scikit-learn, Pandas, NumPy, Joblib
AI Layer    → Google Gemini API (gemini-2.5-flash-lite)
Database    → SQLAlchemy + SQLite
Frontend    → HTML5, CSS3, Bootstrap 5, Chart.js
Security    → Werkzeug (PBKDF2-SHA256), python-dotenv
Version Ctrl→ Git
```

---

## 📋 How It Works

```
1. Upload Model (.pkl) + Dataset (.csv)
        ↓
2. System runs batch predictions → logs to predictions.csv
        ↓
3. Self-Audit Agent runs 3-step pipeline:
   ├── Step 1: Confidence Health Check (avg confidence < 0.6 → flag)
   ├── Step 2: Z-Score Drift Detection (deviation > 2.0 → flag)
   └── Step 3: Label Bias Analysis (>80% or <5% positive → flag)
        ↓
4. Risk Score computed → Status: PASS / WARNING / CRITICAL
        ↓
5. Google Gemini generates plain-English explanation
        ↓
6. (If CRITICAL) → Auto-Repair: retrain RandomForest on clean data
        ↓
7. Download repaired model for deployment
```

---

## ⚙️ Installation

```bash
# 1. Clone the repository
git clone https://github.com/uttam/safe-agent.git
cd safe-agent

# 2. Create virtual environment
python -m venv venv
source venv/bin/activate        # Linux/macOS
venv\Scripts\activate           # Windows

# 3. Install dependencies
pip install -r requirements.txt

# 4. Configure environment
echo "GEMINI_API_KEY=your_gemini_api_key_here" > .env

# 5. Run the application
python app.py

# 6. Open in browser
# Navigate to http://localhost:5000
```

---

## 📁 Project Structure

```
safe-agent/
│
├── app.py                      # Flask application (all routes)
├── logger.py                   # CSV prediction logger
├── generate_traffic.py         # Traffic simulator (Healthy/Risky/Mixed)
│
├── agent/
│   └── self_audit_agent.py     # 3-step audit pipeline + risk scoring
│
├── mcp_tools/
│   ├── tools.py                # Drift detection & health analysis
│   └── repair_kit.py           # Autonomous RandomForest retraining
│
├── rag/
│   └── gemini_explainer.py     # Google Gemini RAG explanation layer
│
├── templates/                  # Jinja2 HTML templates
│   ├── index.html              # Landing page
│   ├── login.html
│   ├── register.html
│   ├── upload.html             # System Injection page
│   └── dashboard.html          # Main monitoring dashboard
│
├── data/
│   └── predictions.csv         # Prediction log (auto-created)
│
├── models/                     # Model artifacts
│   ├── reference_data.csv      # Healthy baseline
│   ├── repaired_model.pkl      # Auto-repair output
│   └── repaired_data.csv       # Cleaned training data
│
├── sample/                     # Demo models and data
│   ├── healthy_model.pkl
│   ├── bad_model_drift.pkl
│   ├── healthy_data.csv
│   └── bad_data_drift.csv
│
├── .env                        # API keys (not committed)
├── requirements.txt
└── README.md
```

---

## 📊 Dashboard Status Explained

| Status | Risk Score | Meaning |
|---|---|---|
| ✅ **PASS** | 0 – 10 | Model healthy, no action needed |
| ⚠️ **WARNING** | 11 – 40 | Minor issues, monitor closely |
| 🚨 **CRITICAL** | > 40 | Significant degradation, Auto-Repair recommended |

---

## 🔬 Audit Sensitivity Modes

| Mode | Multiplier | Use Case |
|---|---|---|
| Low | 0.5× | Development / low-stakes environments |
| **Medium (Standard)** | **1.0×** | **Default — balanced monitoring** |
| High | 1.5× | Production / high-stakes environments |

---

## 🧪 Scenario Injection

- **✅ Healthy** — Injects 30 records from reference distribution → should produce PASS
- **🚨 Risky (Drift)** — Injects drifted data + degraded model predictions → should produce CRITICAL

---

## 🔐 Security

- Passwords hashed with **PBKDF2-SHA256** (Werkzeug)
- API keys stored in **`.env`** file (never in source code)
- File uploads sanitized with **`secure_filename()`**
- All database queries via **SQLAlchemy ORM** (no raw SQL)

---

## 🔮 Future Enhancements

- [ ] Real-time streaming monitoring (Kafka / Redis Streams)
- [ ] Multi-model comparison dashboard
- [ ] Email / Slack alerting on CRITICAL status
- [ ] Advanced drift detection (KS test, PSI, MMD)
- [ ] SHAP-based feature importance visualization
- [ ] Docker + Docker Compose deployment
- [ ] REST API for CI/CD pipeline integration
- [ ] Local LLM support via Ollama

---

## 👨‍💻 Author

**Uttam Tripathi**
Roll No: 1220258280
Bachelor of Computer Applications (Data Science & Artificial Intelligence)
Babu Banarasi Das University, Lucknow
Academic Session 2025–26

---

## 📄 License

This project is developed for academic purposes under Babu Banarasi Das University.

---

> *"Safe Agent — because your AI deserves a mechanic."* 🔧
