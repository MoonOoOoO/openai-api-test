import os
import openai

# Set up your OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")


def encode_message(input_message):
    return [{'role': 'user', 'content': f"{input_message}"}]


def chat_with_bot(messages):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # GPT-Turbo 3.5 model
        messages=encode_message(messages),
        stream=True
        # max_tokens=150,  # Maximum length of the response
        # # Higher values make output more random, lower values make it more deterministic
        # temperature=0.6,
        # top_p=1.0,
        # frequency_penalty=0.0,
        # presence_penalty=0.0,
        # stop=["\n"]  # Stop when a newline character is predicted
    )

    for chunk in response:
        if chunk['choices'][0]['delta']:
            print(chunk['choices'][0]['delta']['content'], end="")
    print()


if __name__ == "__main__":
    print("Chatbot: Hi! How can I help you today? (type 'exit' to quit)")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("Chatbot: Goodbye!")
            break
        prompt = f"You: {user_input}\nChatbot:"
        chat_with_bot(user_input)
