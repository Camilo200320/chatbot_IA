from schemas.chat_schemas import InputMessage
from openai import OpenAI

client = OpenAI(
  base_url="https://openrouter.ai/api/v1",
  api_key="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",
)

def generate_response(data_in: InputMessage):
    message = data_in.message 

    try:
        completion = client.chat.completions.create(
        model="openai/gpt-oss-20b:free",
        messages=[
                {     
                    "role": "system",
                    "content": "Eres un asistente que siempre responde en español de forma clara y breve"
                },
                {
                    "role": "user",
                    "content": message
                }
                ]
        )

        print("Respuesta del modelo ", completion.choices[0].message.content)
        response = completion.choices[0].message.content
    except Exception as e:
        print(f"Error generating response: {e}")
        response = "Sorry, I couldn´t generate a response at this time."

    return response

