def read_private_files(file_paths):
    data = ""
    for file_path in file_paths:
        with open(file_path, "r") as file:
            data += file.read() + "\n"  # Separate data from different files
    return data

# Example usage
file_paths = ["data/database.txt"]
private_data = read_private_files(file_paths)

import openai

# Set up OpenAI API client
openai.api_key = "Enter your openai api key"

def generate_response(user_input, private_data):
    prompt = f"User: {user_input}\nPrivate Data: {private_data}\nBot:"
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=50
    )
    return response.choices[0].text.strip()

# Example usage

print("Bot: What do you want to know?")

while True:
    user_input = input("You: ")
    if user_input.lower() == 'exit':
        break

    response = generate_response(user_input, private_data)
    print("Bot:", response)
