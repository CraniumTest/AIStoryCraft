import openai
import os

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")  # retrieve OpenAI API key from environment variables

def generate_story(prompt, continuation_length=100):
    openai.api_key = OPENAI_API_KEY

    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=continuation_length,
        n=1,
        stop=None,
        temperature=0.7
    )
    story_continuation = response.choices[0].text.strip()
    return story_continuation
