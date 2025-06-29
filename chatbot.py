import os
import openai
from dotenv import load_dotenv

load_dotenv()

class AIChatBot:
    def __init__(self):
        self.api_key = os.getenv('OPENAI_API_KEY')
        self.client = None
        self.conversation_history = []
    
    def _get_client(self):
        if self.client is None:
            if not self.api_key:
                raise ValueError("OpenAI API key not found. Please set OPENAI_API_KEY environment variable.")
            self.client = openai.OpenAI(api_key=self.api_key)
        return self.client
    
    def get_response(self, user_input):
        try:
            self.conversation_history.append({"role": "user", "content": user_input})
            
            client = self._get_client()
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a helpful AI assistant. Be friendly and conversational."},
                    *self.conversation_history
                ],
                max_tokens=150,
                temperature=0.7
            )
            
            bot_response = response.choices[0].message.content
            self.conversation_history.append({"role": "assistant", "content": bot_response})
            
            return bot_response
            
        except Exception as e:
            return f"Sorry, I encountered an error: {str(e)}"
    
    def clear_history(self):
        self.conversation_history = []
        print("Conversation history cleared!")

def main():
    print("🤖 AI ChatBot - Type 'quit' to exit, 'clear' to clear history")
    print("=" * 50)
    
    if not os.getenv('OPENAI_API_KEY'):
        print("❌ Error: Please set your OPENAI_API_KEY in the .env file")
        print("1. Copy .env.example to .env")
        print("2. Add your OpenAI API key to the .env file")
        return
    
    chatbot = AIChatBot()
    
    while True:
        user_input = input("\n👤 You: ").strip()
        
        if user_input.lower() in ['quit', 'exit', 'bye']:
            print("👋 Goodbye! Thanks for chatting!")
            break
        elif user_input.lower() == 'clear':
            chatbot.clear_history()
            continue
        elif not user_input:
            continue
        
        print("🤖 Bot: ", end="")
        response = chatbot.get_response(user_input)
        print(response)

if __name__ == "__main__":
    main()
