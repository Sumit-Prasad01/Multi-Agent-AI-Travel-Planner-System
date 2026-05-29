# 🌍 AI Travel Planning System using LangGraph

A real-world **Multi-Agent AI Travel Planning System** built using **LangGraph**, **LangChain**, and **Llama 3.3 70B**. The system leverages multiple specialized AI agents that collaborate to automatically plan complete trips, including flights, hotels, itineraries, and final travel recommendations.

---

## 🚀 Overview

Planning a trip often requires searching multiple websites, comparing options, organizing schedules, and creating an itinerary. This project automates the entire process using a collaborative multi-agent architecture powered by Large Language Models (LLMs).

The system uses **4 specialized AI agents** that communicate through **LangGraph workflows** to deliver an end-to-end travel planning experience.

---

## 🏗️ Multi-Agent Architecture

### ✈️ Flight Search Agent
- Searches for available flights.
- Retrieves flight details using AviationStack API.
- Provides departure, arrival, duration, and pricing information.

### 🏨 Hotel Search Agent
- Finds suitable hotel accommodations.
- Compares available options based on user preferences.
- Returns structured hotel recommendations.

### 🗓️ Itinerary Planning Agent
- Creates a day-by-day travel plan.
- Suggests attractions, activities, and schedules.
- Optimizes travel experience based on trip duration.

### 🤖 Final Response Agent
- Aggregates results from all agents.
- Generates a comprehensive travel plan.
- Provides a user-friendly final response.

---

## ✨ Features

- ✈️ Flight Search Agent
- 🏨 Hotel Search Agent
- 🗓️ Itinerary Planning Agent
- 🤖 Final Response Agent
- 🧠 Persistent Memory using PostgreSQL
- 🌐 Real-Time API Integration
- 🔄 Multi-Agent Workflow with LangGraph
- 💬 Natural Language Travel Planning
- 📊 Structured Travel Recommendations
- 💻 Interactive Streamlit Interface

---

## 🛠️ Tech Stack

| Technology | Purpose |
|------------|---------|
| LangGraph | Multi-agent orchestration |
| LangChain | LLM application framework |
| Groq | High-performance inference |
| Llama 3.3 70B | Large Language Model |
| PostgreSQL 16 | Persistent memory storage |
| Docker Compose | Database deployment |
| Streamlit | Web application interface |
| Tavily API | Web search and information retrieval |
| AviationStack API | Flight information retrieval |

---

## 📂 Project Structure

```text
AI_Travel_Planning_System/
│
├── frontend/
│   ├── app.py
│   └── styles.py
│
├── src/
│   ├── tools/
│   │   ├── flight_tool.py
│   │   └── tavily_tool.py
│   │
│   ├── config.py
│   └── __init__.py
│
├── .env
├── docker-compose.yml
├── main.py
├── requirements.txt
├── setup.py
└── README.md
```

---

## ⚙️ Installation

### 1. Clone Repository

```bash
git clone https://github.com/Sumit-Prasad01/Multi-Agent-AI-Travel-Planner-System.git
cd AI-Travel-Planning-System
```

### 2. Create Virtual Environment

```bash
python -m venv .venv
```

Activate:

**Windows**
```bash
.venv\Scripts\activate
```

**Linux / macOS**
```bash
source .venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🐘 PostgreSQL Setup

Start PostgreSQL using Docker Compose:

```bash
docker-compose up -d
```

Verify:

```bash
docker ps
```

---

## 🔑 Environment Variables

Create a `.env` file:

```env
GROQ_API_KEY=your_groq_api_key

TAVILY_API_KEY=your_tavily_api_key

AVIATIONSTACK_API_KEY=your_aviationstack_api_key

DATABASE_URL=postgresql://username:password@localhost:5432/travel_db
```

---

## ▶️ Running the Application

### Start Backend

```bash
python main.py
```

### Launch Streamlit UI

```bash
streamlit run frontend/app.py
```

---

## 🔄 Workflow

```text
User Query
     │
     ▼
Flight Search Agent
     │
     ▼
Hotel Search Agent
     │
     ▼
Itinerary Planning Agent
     │
     ▼
Final Response Agent
     │
     ▼
Complete Travel Plan
```

---

## 🧠 Memory System

The application uses PostgreSQL for:

- Conversation history
- User preferences
- Travel context retention
- Multi-turn interactions

This enables a more personalized travel planning experience.

---

## 📸 Example Query

```text
Plan a 5-day trip to Bali from Kolkata in December.
I need budget-friendly flights and hotels.
```

### Example Output

```text
✓ Recommended Flights

✓ Hotel Suggestions

✓ Day-wise Itinerary

✓ Budget Estimation

✓ Travel Tips
```

---

## 🔮 Future Improvements

- Google Maps Integration
- Weather Forecast Agent
- Budget Optimization Agent
- Restaurant Recommendation Agent
- Visa Requirement Agent
- Multi-City Trip Planning
- RAG-Based Travel Knowledge Base

---

## 👨‍💻 Author

Built using LangGraph and Multi-Agent AI architecture for real-world travel planning automation.

---

## ⭐ If you found this project useful

Give the repository a star and share it with others.
