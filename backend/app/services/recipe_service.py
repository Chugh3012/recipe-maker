from openai import OpenAI

openai_client = OpenAI()

def generate_recipe(ingredients):
    try:
        response = openai_client.chat.completions.create(
            model="gpt-3.5-turbo-1106",
            response_format={ "type": "json_object" },
            messages=[
                {"role": "system", "content": "You are a helpful assistant which generates recipes given ingredients in JSON format"},
                {"role": "user", "content": "Ingredients: " + ingredients},
            ]
        )
        return response.choices[0].message.content # type: ignore
    except Exception as e:
        return str(e)