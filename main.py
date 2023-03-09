import openai
import os


def chatbot():

    # Set up the OpenAI API key
    openai.api_key = os.environ["OPENAI_API_KEY"]

    # Define a function to get the response from the OpenAI GPT-3 chat
    def get_response(prompt):

        openai_response = openai.Completion.create(
            engine="davinci",
            prompt=prompt,
            temperature=0.001,
            max_tokens=50,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )

        return openai_response.choices[0].text.strip()

    print("Hi! I'm a simple chatbot. You can start chatting with me by typing your message.\n")

    # Start the chat loop
    while True:
        user_message = input("You: ")
        response = get_response(user_message)

        print("Chatbot:", response)


if __name__ == "__main__":
    chatbot()

