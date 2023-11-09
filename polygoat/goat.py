import openai
from openai import OpenAI
import os

client = OpenAI(api_key=os.environ['OPENAI_API_KEY'], )

system = "You are an alien from Alpha Centauri B"
#assistant = "I am a chatbot"
#user = "Where are you from?"


def chat(user_input, system_input):

  user_input = user_input
  #assistant_input = assistant_input
  system_input = system_input
  
  completion = client.chat.completions.create(
      model="gpt-3.5-turbo",
      messages=[
          {
              "role": "system",
              "content": system_input
          },
           # {
           #   "role": "assistant", "content": assistant_input
           # },
          {
              "role": "user",
              "content": user_input
          }
      ],
      max_tokens=64)
  return print(completion.choices[0].message)
