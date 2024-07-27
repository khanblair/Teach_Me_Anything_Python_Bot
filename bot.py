import json
import os
import random

class SimpleBot:
    def __init__(self, data_file='bot_data.json'):
        self.data_file = data_file
        self.data = self.load_data()

    def load_data(self):
        if os.path.exists(self.data_file):
            with open(self.data_file, 'r') as file:
                return json.load(file)
        return {}

    def save_data(self):
        with open(self.data_file, 'w') as file:
            json.dump(self.data, file, indent=4)

    def add_data(self, question, answer):
        self.data[question.lower()] = answer
        self.save_data()
        print("Thanks, I have learned something new today!")

    def get_answer(self, question):
        question = question.lower()
        if question in self.data:
            if random.random() < 0.6:  # 60% chance of correct answer
                return self.data[question]
            else:
                return "I'm not sure about that."
        else:
            return "Teach me"

    def remove_data(self, key):
        if key in self.data:
            del self.data[key]
            self.save_data()
            print(f"Data removed: {key}")
        else:
            print(f"Key not found: {key}")

    def list_data(self):
        for key, value in self.data.items():
            print(f"{key}: {value}")

def main():
    bot = SimpleBot()
    
    while True:
        user_input = input("You: ").strip()[:100]
        
        if user_input.lower() == 'quit':
            print("Goodbye!")
            break
        
        response = bot.get_answer(user_input)
        print("Bot:", response)
        
        if response == "Teach me":
            answer = input("Teach me the answer: ").strip()
            bot.add_data(user_input, answer)

if __name__ == "__main__":
    main()