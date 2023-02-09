import os
import openai
import webbrowser

os.environ["OPENAI_API_KEY"] = "Your OpenAI API key"  # get it from https://platform.openai.com/account/api-keys
openai.api_key = os.getenv("OPENAI_API_KEY")

response = openai.Image.create(
  prompt="inside a black hole",
  n=1,
  size="1024x1024"
)
print(response)
image_url = response['data'][0]['url']
print (image_url)
webbrowser.open_new_tab(image_url)