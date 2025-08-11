import random
import datetime
import requests
import wikipedia

class TaskAgent:
    def __init__(self):
        self.name = "Task Assistant AI Agent"

    def process_request(self, query):
        query_lower = query.lower()

        if "time" in query_lower:
            return self.tell_time()
        elif "joke" in query_lower:
            return self.tell_joke()
        elif "weather" in query_lower:
            return self.get_weather()
        elif any(word in query_lower for word in ["add", "plus", "sum", "+"]):
            return self.simple_math(query_lower)
        else:
            return self.search_wikipedia(query)

    def tell_time(self):
        now = datetime.datetime.now()
        return f"The current time is {now.strftime('%H:%M:%S')}."

    def tell_joke(self):
        jokes = [
            "Why don’t skeletons fight each other? They don’t have the guts.",
            "Why did the computer go to the doctor? Because it caught a virus.",
            "Why was the math book sad? It had too many problems."
        ]
        return random.choice(jokes)

    def get_weather(self):
        city = "Bengaluru"
        api_key = "YOUR_API_KEY"  # Replace with your OpenWeatherMap API key
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
        
        try:
            response = requests.get(url)
            data = response.json()
            temp = data["main"]["temp"]
            description = data["weather"][0]["description"]
            return f"The weather in {city} is {temp}°C with {description}."
        except:
            return "Weather service not available right now."

    def simple_math(self, query):
        try:
            numbers = [int(s) for s in query.split() if s.isdigit()]
            return f"The sum is {sum(numbers)}."
        except:
            return "I couldn't do the math. Please try again."

    def search_wikipedia(self, query):
        try:
            summary = wikipedia.summary(query, sentences=2)
            return summary
        except wikipedia.exceptions.DisambiguationError as e:
            return f"Your query was too broad. Try something more specific, like: {e.options[:3]}"
        except wikipedia.exceptions.PageError:
            return "I couldn't find anything on that topic."
        except:
            return "Wikipedia search is unavailable right now."

if __name__ == "__main__":
    agent = TaskAgent()
    print(f"🤖 {agent.name} is ready!")

    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            print("Agent: Goodbye!")
            break
        response = agent.process_request(user_input)
        print(f"Agent: {response}")
