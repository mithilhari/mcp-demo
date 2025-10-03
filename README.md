# Simple Model Context Protocol Demo

This repository contains a simple Python implementation of a **Model Context Protocol**.

## 📖 Protocol Overview

The protocol is designed to standardize the input for a conversational AI model. It uses a list of dictionaries (JSON) where each dictionary represents a message and has two key fields:

1.  **`role`**: (`system`, `user`, or `assistant`)
2.  **`content`**: The text of the message.

This structure allows the model to maintain **conversation history (context)** and interpret **system instructions**.

## 🚀 How to Run

1.  **Clone the repository:**
    ```bash
    git clone [YOUR-REPO-URL]
    cd simple-model-context-app
    ```
2.  **Execute the script:**
    ```bash
    python model_context_protocol.py
    ```

## 📜 Example Output

The script will print the context as it's built up, demonstrating how the conversation history is maintained:

```json
{
  "role": "system",
  "content": "You are a helpful and witty assistant who loves to use emojis."
}
...
{
  "role": "user",
  "content": "What's the capital of France?"
},
{
  "role": "assistant",
  "content": "That's easy! It's Paris. 🇫🇷"
}
...
