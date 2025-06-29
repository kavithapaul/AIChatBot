# AIChatBot

A Python-based AI chatbot using OpenAI's GPT-3.5-turbo model. This chatbot provides conversational AI capabilities with memory of the conversation history.

## Features

- 🤖 Powered by OpenAI GPT-3.5-turbo
- 💬 Maintains conversation history during the session
- 🔄 Clear conversation history command
- 🛡️ Error handling and user-friendly interface
- 💰 Uses OpenAI's free tier (new accounts get $5 credit)

## Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/kavithapaul/AIChatBot.git
cd AIChatBot
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Get OpenAI API Key
1. Go to [OpenAI API Keys](https://platform.openai.com/api-keys)
2. Sign up for a free account (gets $5 credit)
3. Create a new API key
4. Copy the API key

### 4. Configure Environment
```bash
cp .env.example .env
```
Edit the `.env` file and add your OpenAI API key:
```
OPENAI_API_KEY=your_actual_api_key_here
```

### 5. Run the Chatbot
```bash
python chatbot.py
```

## Usage

- Type your messages and press Enter to chat
- Type `clear` to clear conversation history
- Type `quit`, `exit`, or `bye` to exit the chatbot

## Example Conversation

```
🤖 AI ChatBot - Type 'quit' to exit, 'clear' to clear history
==================================================

👤 You: Hello! How are you today?
🤖 Bot: Hello! I'm doing great, thank you for asking! I'm here and ready to help you with any questions or just have a friendly conversation. How are you doing today?

👤 You: Can you help me with Python programming?
🤖 Bot: Absolutely! I'd be happy to help you with Python programming. Whether you need help with basic syntax, debugging code, understanding concepts, or working on specific projects, I'm here to assist. What specific Python topic or problem would you like help with?
```

## Cost Information

- **Free Tier**: New OpenAI accounts receive $5 in free credits
- **Cost**: GPT-3.5-turbo costs approximately $0.002 per 1K tokens
- **Estimation**: $5 credit = ~2.5 million tokens = thousands of conversations
- **Monitoring**: Check usage at [OpenAI Usage Dashboard](https://platform.openai.com/usage)

## Customization

You can modify the chatbot by editing `chatbot.py`:

- **Change AI personality**: Modify the system message in `get_response()`
- **Adjust response length**: Change `max_tokens` parameter
- **Modify creativity**: Adjust `temperature` (0.0 = focused, 1.0 = creative)
- **Switch models**: Change `model` to `gpt-4` (costs more) or other available models

## Troubleshooting

### Common Issues

1. **"Please set your OPENAI_API_KEY"**
   - Make sure you created the `.env` file
   - Verify your API key is correct in the `.env` file

2. **"You exceeded your current quota"**
   - Your free credits are exhausted
   - Add billing information to your OpenAI account

3. **"Invalid API key"**
   - Double-check your API key is copied correctly
   - Ensure no extra spaces in the `.env` file

## Security Notes

- Never commit your `.env` file to version control
- Keep your API key private and secure
- The `.env.example` file is safe to commit (contains no real keys)

## Contributing

Feel free to fork this repository and submit pull requests for improvements!

## License

This project is open source and available under the MIT License.
