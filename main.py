import os
import openai

def main():

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
