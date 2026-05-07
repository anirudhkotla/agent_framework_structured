import os
from dotenv import load_dotenv
from mistralai.client import Mistral


load_dotenv()

api_key = os.getenv("MISTRAL_API_KEY")

client = Mistral(api_key=api_key)


async def generate_response(context, message):

    prompt = f"""
    Context:
    {context}

    User:
    {message}
    """

    response = client.chat.complete(
        model="mistral-small-latest",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content