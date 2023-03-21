import os
import openai


def main():

    starting_prompt = """
    I want you to become my Prompt Creator. Your goal is to help me craft the best possible prompt for my needs. 
    The prompt will be used by you, ChatGPT. You will follow the following process: 
    1. Your first response will be to ask me what the prompt should be about. I will provide my answer, 
    but we will need to improve it through continual iterations by going through the next steps. 
    2. Based on my input, you will generate 3 sections. 
    a) Revised prompt (provide your rewritten prompt. it should be clear, concise, and easily understood by you), 
    b) Suggestions (provide suggestions on what details to include in the prompt to improve it), and 
    c) Questions (ask any relevant questions pertaining to what additional information is needed from me to improve 
    the prompt). 
    3. We will continue this iterative process with me providing additional information to you and you updating the 
    prompt in the Revised prompt section until it's complete.
    """

    # Set up the OpenAI API key
    openai.api_key = os.environ["OPENAI_API_KEY"]

    # Define campaign inputs as constants
    objective = "generate awareness of the brand in the target audience"
    brand = "Ricola"
    product = "ricola sweets, candies and mint candies to heal sore throat or throat ache, breath mints"
    target_audience = "swiss population, any age any sex"

    # Define a function to get the response from the OpenAI GPT-3 chat
    def get_response(prompt):
        openai_response = openai.Completion.create(
            engine="davinci",
            prompt=prompt,
            temperature=1,
            max_tokens=50,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )

        return openai_response.choices[0].text.strip()

    # Generate marketing campaign message
    message_prompt = f"Generate a marketing campaign message for {product} by {brand} that targets {target_audience} and aims to {objective}."
    message_response = get_response(message_prompt)

    # Generate slogan
    slogan_prompt = f"Create a slogan for {product} by {brand} that helps to promote the campaign and increase brand awareness."
    slogan_response = get_response(slogan_prompt)

    print('------------------------------------------------------------------------------------')
    print(f"\nMarketing campaign message for {product} by {brand}:\n\n{message_response}\n")
    print(f"Slogan for {product} by {brand}: {slogan_response}\n")


if __name__ == "__main__":
    main()
