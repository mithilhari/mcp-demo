import json
from typing import List, Dict

# Define the Protocol as a List of Message Dictionaries
ContextProtocol = List[Dict[str, str]]

def initialize_context(system_instruction: str) -> ContextProtocol:
    """Initializes the context with a system-level instruction."""
    return [
        {"role": "system", "content": system_instruction}
    ]

def add_user_message(context: ContextProtocol, message: str) -> ContextProtocol:
    """Adds a new user message to the context."""
    context.append({"role": "user", "content": message})
    return context

def add_assistant_response(context: ContextProtocol, response: str) -> ContextProtocol:
    """Adds the assistant's (model's) response to the context."""
    context.append({"role": "assistant", "content": response})
    return context

def serialize_context(context: ContextProtocol) -> str:
    """Converts the context object into a JSON string for API transmission."""
    # Use indent=2 for readability when printing/debugging
    return json.dumps(context, indent=2)

# --- Example Usage ---
if __name__ == "__main__":
    # 1. Initialize the context with a "System" instruction
    initial_prompt = "You are a helpful and witty assistant who loves to use emojis."
    chat_context = initialize_context(initial_prompt)
    print("--- Initial Context ---")
    print(serialize_context(chat_context))

    # 2. Add a user query
    chat_context = add_user_message(chat_context, "What's the capital of France?")

    # 3. Simulate an assistant response
    assistant_reply = "That's easy! It's Paris. 🇫🇷"
    chat_context = add_assistant_response(chat_context, assistant_reply)

    # 4. Add another turn
    chat_context = add_user_message(chat_context, "And what about the one for Japan?")
    assistant_reply_2 = "That would be Tokyo! 🗼"
    chat_context = add_assistant_response(chat_context, assistant_reply_2)

    # 5. Final Context Ready for API Call
    final_json = serialize_context(chat_context)
    print("\n--- Final Serialized Context (Ready for API) ---")
    print(final_json)
