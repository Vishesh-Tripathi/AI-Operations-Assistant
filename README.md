# 🧠 AI Operations Assistant

An **AI Operations Assistant** that accepts natural-language tasks, plans execution steps, calls real external APIs, and validates results using a **multi-agent architecture**.

This project demonstrates **agent-based reasoning**, **LLM orchestration (Groq)**, and **real API integrations**, built as part of a GenAI / AI Ops Intern assignment.

---

## ✨ Features

- **Planner Agent** – Converts user intent into a structured JSON plan  
- **Executor Agent** – Executes steps and calls external APIs  
- **Verifier Agent** – Validates results and produces final structured output  
- **Real APIs Integrated**
  - 🌦️ OpenWeather API (Weather data)
  - 🧑‍💻 GitHub Search API (Repositories)
  - 📰 News API (Latest news)(https://newsapi.org/)
- **Retry on API failure**
- **Graceful fallback when partial data is available**
- **Runs locally with FastAPI + Swagger UI**

---

## 🏗️ Architecture

```
User Input
↓
Planner Agent (LLM → JSON Plan)
↓
Executor Agent (Calls APIs)
↓
Verifier Agent (LLM → Final Output)
```

Each agent has a **clear responsibility**, enabling modularity and fault tolerance.

---

## 📁 Project Structure

```
ai_ops_assistant/
├── agents/
│   ├── planner.py
│   ├── executor.py
│   └── verifier.py
│
├── tools/
│   ├── weather_tool.py
│   ├── github_tool.py
│   ├── news_tool.py
│   └── retry.py
│
├── llm/
│   └── llm_client.py
│
├── main.py
├── requirements.txt
├── .env.example
└── README.md
```

---

## 🔧 Setup Instructions

### 1️⃣ Clone the Repository
```bash
git clone <your-repo-url>
cd ai_ops_assistant
```

---

### 2️⃣ Create Virtual Environment (Optional but Recommended)

```bash
python -m venv venv
venv\Scripts\activate   # Windows
```

---

### 3️⃣ Install Dependencies

```bash
python -m pip install -r requirements.txt
```

---

### 4️⃣ Configure Environment Variables

Create a `.env` file using `.env.example` as reference:

```env
GROQ_API_KEY=your_groq_api_key
WEATHER_API_KEY=your_openweather_api_key
NEWS_API_KEY=your_newsapi_key
```

---

## ▶️ How to Run the Application

Start the FastAPI server:

```bash
python -m uvicorn main:app --reload
```

You should see:

```
Uvicorn running on http://127.0.0.1:8000
```

---

## 🧪 Using Swagger UI (IMPORTANT)

Swagger UI provides an interactive interface to test the assistant.

### 🔗 Open Swagger UI

```
http://127.0.0.1:8000/docs

```
---

### ▶️ Run a Task

1. Go to **POST /run**
2. Click **Try it out**
3. Enter a task, for example:

```json
{
  "task": "Get current weather in Delhi and list 20 AI repositories on GitHub"
}
```

4. Click **Execute**

---

## 📤 Example Output

```json
{
  "summary": "Current weather in Delhi and list of 20 AI repositories on GitHub",
  "data": {
    "weather": {
      "city": "Delhi",
      "temperature": 14.05,
      "condition": "mist"
    },
    "repositories": [
      {
        "name": "vercel/ai",
        "stars": 21512,
        "url": "https://github.com/vercel/ai"
      }
    ]
  }
}
```

---

## 🛠️ Error Handling

### 🔁 Retry on API Failure

* External API calls include retry logic
* Handles transient network or rate-limit failures

### 🧯 Graceful Fallback

* If one API fails, successful results are preserved
* Errors are reported clearly in the final response
* System never crashes due to partial failures

---

## 🚀 Improvements With More Time

* **Caching API responses** (Redis / in-memory)
* **Cost tracking per LLM request**
* **Parallel tool execution** for faster responses
* Automatic re-planning on failed steps

---

## 🤖 LLM Provider

This project uses **Groq (LLaMA-3.x)** for:

* Fast inference
* Structured JSON outputs
* Low-latency agent reasoning

---

## ✅ Summary

This project demonstrates:

* Agent-based system design
* Real-world API orchestration
* Fault-tolerant AI workflows
* Production-ready AI Ops patterns

---

## 📌 Notes

* The system runs fully **locally**
* No monolithic prompts are used
* Each agent operates independently

---

## 👨‍💻 Author

Built by **Vishesh Tripathi**
AI Ops / Full-Stack Developer
