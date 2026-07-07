"""
Architecture

                User
                  │
        ┌─────────┴─────────┐
        │                   │
     Text/File           Image
        │                   │
        ▼                   ▼
     Llama 3           Moondream
        │                   │
        └─────────┬─────────┘
                  ▼
              Response
"""

from ollama import chat

messages = []

print("Chatbot started. Type 'quit' to exit.")

while True:
    user_input = input("You: ")

    if user_input.lower() == "quit":
        print("Goodbye!")
        break

    if not user_input.strip():
        print("Please enter a message.")
        continue

    try:
        messages.append(
            {
                "role": "user",
                "content": user_input
            }
        )

        response = chat(
            model="llama3",
            messages=messages
        )

        assistant_reply = response["message"]["content"]

        print("\nBot:", assistant_reply, "\n")

        messages.append(
            {
                "role": "assistant",
                "content": assistant_reply
            }
        )

    except Exception as e:
        print(f"Error: {e}")