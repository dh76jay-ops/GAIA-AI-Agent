 GAIA AI Agent

![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python)
![HuggingFace](https://img.shields.io/badge/HuggingFace-smolagents-orange?logo=huggingface)
![LLM](https://img.shields.io/badge/LLM-Qwen2.5--72B-purple)
![License](https://img.shields.io/badge/License-MIT-green)

> Autonomous AI Agent capable of solving complex, multi-step reasoning tasks using RAG and real-time web search — inspired by the GAIA benchmark.

---

 What It Does

This agent doesn't just answer questions — it **thinks step by step**, searches the web for real-time information, and combines reasoning with retrieval to give accurate answers.

-  "Real-time web search" using DuckDuckGo
-  "Multi-step reasoning" powered by Qwen2.5-72B LLM
-  "RAG pipeline" for context-aware, accurate responses
-  "Modular tool-use workflow" — decides when to search vs. reason internally
-  "Benchmarked" against GAIA benchmark scenarios

---

 Demo

**Question asked:** *"Who invented the telephone?"*

```
--- Question 1 ---
Q: Who invented the telephone?

- Executing parsed code:
  final_answer("Alexander Graham Bell")

Final answer: Alexander Graham Bell

[Step 5: Duration 197.15s | Input tokens: 14,374 | Output tokens: 628]
```

The agent used "5 reasoning steps", searched the web, analyzed results, and returned the correct answer autonomously.

---

 Tech Stack

| Tool | Purpose |
|------|---------|
| Python | Core language |
| smolagents | Agent framework |
| Qwen2.5-72B | Large Language Model |
| HuggingFace Inference API | LLM hosting |
| DuckDuckGo Search Tool | Real-time web search |
| RAG Pipeline | Context-aware retrieval |

---

 Installation & Setup

 1. Clone the repository
```bash
git clone https://github.com/dh76jay-ops/GAIA-AI-Agent.git
cd GAIA-AI-Agent
```

 2. Install dependencies
```bash
pip install smolagents huggingface_hub duckduckgo-search
```

 3. Set your HuggingFace API token
Create a `.env` file:
```
HF_TOKEN=your_huggingface_token_here
```
Get your free token at: https://huggingface.co/settings/tokens

 4. Run the agent
Open `real_ai_agent.ipynb` in Jupyter Notebook and run all cells.

---

## Example Questions to Try

```python
questions = [
    "Who invented the telephone?",
    "What is the most in-demand AI skill for freshers in India?",
    "What is the capital of France and what is it famous for?",
    "Who founded HuggingFace and what is their most popular model?"
]
```

---

 How It Works

```
User Question
      ↓
Agent receives question
      ↓
Decides: Search web OR use internal reasoning?
      ↓
[If search needed] → DuckDuckGo fetches real-time results
      ↓
RAG pipeline provides context to LLM
      ↓
Qwen2.5-72B reasons over results
      ↓
Final Answer returned
```

---

 Key Highlights

- Benchmark: Tested on GAIA benchmark-inspired tasks
- Accuracy: Successfully answers multi-step real-world questions
- Model: Qwen2.5-72B (72 billion parameter LLM)
- Reasoning steps: Up to 5+ steps per query

---

 Certificate

Built as part of the **HuggingFace AI Agents Course 2026**

![HuggingFace](https://img.shields.io/badge/HuggingFace-AI%20Agents%20Course%202026-yellow?logo=huggingface)

---

 Author

Dhananjay Bopche
-  [LinkedIn](https://linkedin.com/in/dhananjay-bopche)
-  [GitHub](https://github.com/dh76jay-ops)
- 🤗 [HuggingFace](https://huggingface.co/dh76jay-dev)

---

" If you found this useful, please star the repo! "
