# 🤖 AI Agent Tracing Example

This project shows how **AI agents** work together and how we can use **tracing** to watch everything step by step.  

---

## 🔍 What is Tracing?

**Tracing** is like a diary or log book for the AI.  
It records every step so we can see:  

- 📝 What question was asked  
- 🤖 Which agent answered  
- 🔄 If the question was given to another agent  
- 🛠️ What tools were used  
- ✅ What answer was given  

---

## 🌟 Why Use Tracing?

1. **See the journey** – Understand how the AI solved your question  
2. **Find problems** – Spot where something went wrong  
3. **Learn** – Watch how AI “thinks” and makes choices  
4. **Improve** – Make agents smarter by looking at past steps  

---

## 🧑‍💻 Project Files

- **`agent.py`** → Creates the agents (Assistant + Math Agent) and runs tracing  
- **`tool.py`** → Math tool (for adding numbers)  
- **`config.py`** → Settings for the AI model  

---

## 🚀 How It Works

1. Run the program  
2. Type a question (example: `What is 5 + 3?`)  
3. Assistant Agent decides if it should solve or handoff to Math Agent  
4. Math Agent solves the math problem  
5. Tracing saves all steps (like a movie of the conversation)  
6. Type `exit` to quit  

---

## ✨ Example

User: What is 10 + 5?
Assistant Agent → decides this is math
Assistant Agent → sends question to Math Agent
Math Agent → answers: 15
Tracing → saves every step
---

## 🎓 Learn More

Tracing is used everywhere:  
- 🏥 In hospitals to track patient care  
- 🚗 In self-driving cars to see decisions  
- 🎮 In games to understand player actions  
- 📱 In apps to improve performance  

---

❤️ Made for learning how **AI agents + tracing** work in simple steps!
