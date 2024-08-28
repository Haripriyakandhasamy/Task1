#!/usr/bin/env python
# coding: utf-8

# In[1]:


def chatbot_response(user_input):
    # Convert user input to lowercase to make the matching case-insensitive
    user_input = user_input.lower()

    # Rule-based responses
    if 'hello' in user_input:
        return "Hello! How can I help you today?"
    elif 'how are you' in user_input:
        return "I'm just a chatbot, but I'm doing great! How about you?"
    elif 'what is your name' in user_input:
        return "I'm Chatbot, your virtual assistant."
    elif 'bye' in user_input:
        return "Goodbye! Have a great day!"
    elif 'help' in user_input:
        return "Sure! What do you need help with?"
    else:
        return "I'm sorry, I don't understand that. Can you please rephrase?"

# Main loop to keep the chatbot running
if __name__ == "__main__":
    print("Chatbot: Hello! I'm your friendly chatbot. Type 'bye' to exit.")
    
    while True:
        # Get user input
        user_input = input("You: ")
        
        # Generate response from the chatbot
        response = chatbot_response(user_input)
        
        # Print chatbot's response
        print(f"Chatbot: {response}")
        
        # Exit the loop if the user says 'bye'
        if 'bye' in user_input.lower():
            break


# In[ ]:




