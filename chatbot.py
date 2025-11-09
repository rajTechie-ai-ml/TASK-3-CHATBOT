import sys

def get_chatbot_response(user_input):
    """
    Analyzes the user's input and returns a predefined, rule-based response.
    
    Key concept: Uses if-elif structure to match input patterns.
    """
    # Convert input to lowercase for case-insensitive matching
    normalized_input = user_input.lower().strip()

    # Rule 1: Greetings
    if "hello" in normalized_input or "hi" in normalized_input:
        return "👋 Hi there! How can I help you today?"

    # Rule 2: Inquiry about well-being
    elif "how are you" in normalized_input or "how are u" in normalized_input:
        return "🤖 I'm fine, thank you! I'm a simple program, but always ready to chat."

    # Rule 3: Exit/Goodbye
    elif "bye" in normalized_input or "goodbye" in normalized_input or "exit" in normalized_input:
        return "👋 Goodbye! Have a great day."

    # Default Rule: If no match is found
    else:
        return "🤔 I only understand basic phrases like 'hello', 'how are you', or 'bye'. Try one of those!"

def start_chatbot():
    """
    The main function that runs the chat loop.
    
    Key concepts: Uses a while loop for continuous conversation and input/output.
    """
    print("--- Simple Rule-Based Chatbot ---")
    print("Type 'bye' or 'exit' to end the conversation.")
    print("-" * 35)

    # Main conversational loop (while True)
    while True:
        try:
            # Get user input (Input/Output)
            user_input = input("You: ")
            
            # Get the determined response
            response = get_chatbot_response(user_input)
            
            # Print the chatbot's output (Input/Output)
            print(f"Bot: {response}")
            
            # Check for termination condition
            if "Goodbye!" in response:
                break # Exit the while loop
                
        except EOFError:
            # Handles unexpected termination (like Ctrl+D)
            print("\nBot: Session terminated. Goodbye!")
            sys.exit(0)
        except Exception as e:
            print(f"An error occurred: {e}")
            break


# Start the application
if __name__ == "__main__":
    start_chatbot()

