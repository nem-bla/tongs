from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI()

# origin, target, text
def send_prompt(origin, target, prompt):

    completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a language translator named Tongs. You will receive the origin language, target language, and prompt to be translated. You will reply only with the translation of the prompt."},
        {"role": "user", "content": f"{origin} to {target}: {prompt}"}
    ]
    )
    return completion.choices[0].message.content

def main():
    print('Welcome to the Tongs language translator')
    origin = input('Select an origin language: ')
    target = input('Select a target language: ')
    prompt = input('Enter the text to be translated: ')

    response = send_prompt(origin, target, prompt)
    print(f'Translated Text: {response}')

main()





