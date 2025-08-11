# 🤖 AI Agent Task Assistant

A simple multi-capability AI Agent built in Python that can:
- Tell the current time ⏰
- Tell jokes 😄
- Get live weather updates ☁️
- Perform basic math ➕
- Search Wikipedia for quick knowledge 📚

This project demonstrates the basics of **AI agent decision-making** — the agent decides which “skill” to use based on the user’s query.

---

## 🚀 Features

- **Multi-Tool Agent**: Switches between time, joke, weather, math, and Wikipedia search
- **Live Data**: Fetches current weather using the OpenWeatherMap API
- **Knowledge Search**: Uses Wikipedia API for general questions
- **Extensible**: Easily add new capabilities

---

## 📂 Project Structure
```bash
AI-Agent-Task-Assistant/
│
├── ai_agent.py # Main Python script
├── README.md # Project documentation
└── screenshots/ # Example output screenshots
```

---

## 🛠️ Example interaction
```bash
## Example interaction

🤖 Task Assistant AI Agent is ready!
You: tell me a joke
Agent: Why don’t skeletons fight each other? They don’t have the guts.

You: what is machine learning
Agent: Machine learning is a field of computer science that gives computers the ability to learn without being explicitly programmed...

You: 5 + 10
Agent: The sum is 15.
```

## 💡 How It Works
The agent:

Takes user input

Checks for keywords (e.g., "time", "joke", "weather", "add")

Routes the request to the correct method

Returns the output to the user

If the query doesn’t match a tool, it defaults to Wikipedia search.

## 📌 Future Improvements
Add a translation feature 🌐

Integrate ChatGPT API for open-ended queries 🤖

Add multi-step reasoning capabilities 🔄

## 📄 License
This project is licensed under the MIT License.

## 👨‍💻 Author
Suraj Korishetti
[LinkedIn](https://www.linkedin.com/in/suraj-korishetti-333a44258/)


