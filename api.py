import openai

def ask_gpt(text):
    openai.api_key = 'your-openai-api-key'

    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=text,
        max_tokens=100
    )

    return response.choices[0].text.strip()

if __name__ == "__main__":
    user_input = "This is a test."
    gpt_response = ask_gpt(user_input)
    print("GPT says: " + gpt_response)
