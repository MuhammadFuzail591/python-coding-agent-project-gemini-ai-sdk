import os
from dotenv import load_dotenv
from google import genai

def main():
   load_dotenv()

   api_key = os.environ.get("GEMINI_API_KEY")
   print(api_key)
   client = genai.Client(api_key=api_key)
   print(client)

   res = client.models.generate_content(
      model="gemini-2.0-flash",
      contents = "Hi there how are you"
   )

   print(res.text)

main()