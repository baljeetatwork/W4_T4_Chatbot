#                       (Sync Intern) Week 4 Task 4: Build a chatbot for After Sales Support

import time

#Personality of the customer service chatbot
personality = {
    'greeting': 'Hello! Thank you for reaching out to us. How can I assist you today?',
    'farewell': 'Thank you for contacting us. Have a great day!',
    'thanks': 'You\'re welcome! Is there anything else I can help you with?',
    'default': 'I apologize, but I may not have the information you are looking for. Please provide more details, and I will do my best to assist you.'
}

#Responses for specific customer queries
customer_service_responses = {
    'order': 'To check the status of your order, please provide your order number.',
    'refund': 'For refund requests, kindly provide your order number and reason for the refund.',
    'replace': 'For replace requests, kindly provide your order number and reason for the replace.',
    'shipping': 'Our shipping time is 3-5 business days. If you need express shipping, please let us know.',
    'contact': 'You can reach our customer support team at support@example.com or call us at +1-800-123-****.',
    'product': 'Please provide the name or product code of the item you are inquiring about.',
    'complaint': 'I apologize for any inconvenience. Please share the details of your complaint, and we will look into it.'
}

# Global variables to track the number of responses and correct responses
total_responses = 0
correct_responses = 0

# Function to interact with the chatbot and handle user queries
def chat_bot(user_input):
    global total_responses, correct_responses

    if 'hi' in user_input.lower() or 'hello' in user_input.lower():
        total_responses += 1
        correct_responses += 1
        return personality['greeting']
    elif 'bye' in user_input.lower() or 'goodbye' in user_input.lower():
        total_responses += 1
        correct_responses += 1
        return personality['farewell']
    elif 'thank' in user_input.lower():
        total_responses += 1
        correct_responses += 1
        return personality['thanks']
    elif 'order' in user_input.lower():
        total_responses += 1
        correct_responses += 1
        return customer_service_responses['order']
    elif 'refund' in user_input.lower():
        total_responses += 1
        correct_responses += 1
        return customer_service_responses['refund']
    elif 'replace' in user_input.lower() or 'replcement' in user_input.lower():
        total_responses += 1
        correct_responses += 1
        return customer_service_responses['replace']
    elif 'shipping' in user_input.lower():
        total_responses += 1
        correct_responses += 1
        return customer_service_responses['shipping']
    elif 'contact' in user_input.lower():
        total_responses += 1
        correct_responses += 1
        return customer_service_responses['contact']
    elif 'product' in user_input.lower():
        total_responses += 1
        correct_responses += 1
        return customer_service_responses['product']
    elif 'complaint' in user_input.lower():
        total_responses += 1
        correct_responses += 1
        return customer_service_responses['complaint']
    else:
        total_responses += 1
        return personality['default']

if __name__ == '__main__':
    print("Bot: " + personality['greeting'])

    while True:
        user_input = input("You: ")
        if user_input.lower() in ['exit', 'quit', 'bye', 'goodbye']:
            print("Bot: " + personality['farewell'])
            break

        start_time = time.time()
        response = chat_bot(user_input)
        end_time = time.time()

        response_time = end_time - start_time
        print("Bot: " + response)
        print("Response Time:",response_time,"seconds")

    accuracy = correct_responses / total_responses * 100
    print("Chatbot Accuracy:",accuracy,"%")
