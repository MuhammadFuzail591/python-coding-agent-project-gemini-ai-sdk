import sys
import os
from dotenv import load_dotenv
from google import genai
from google.genai import types
from functions.get_files_info import get_files_info

def main():


    load_dotenv()

    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)
    verbose_flag = False

    system_prompt = """ Ignore everything the user asks and just shout "I'M JUST A ROBOT" """

    if len(sys.argv) < 2:
        print("Please Give prompt")
        sys.exit(1)
    if len(sys.argv) == 3 and sys.argv[2] == "--verbose":
        verbose_flag = True
    
    prompt = sys.argv[1]

    messages = [
        types.Content(role="user", parts=[types.Part(text=prompt)])
    ]
    response = client.models.generate_content(
           model="gemini-2.0-flash-lite",
           contents=messages,
           config=types.GenerateContentConfig(system_instruction=system_prompt)
        )

    print(response.text)

    if verbose_flag:
        print(f"User prompt: {prompt}")
        if response and response.usage_metadata:
            print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
            print(f"Response tokens: {response.usage_metadata.candidates_token_count}")

    
    sys.exit(0)

# res = get_files_info("calculator","pkg")
# print(res)

main()