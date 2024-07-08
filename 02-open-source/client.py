from openai import OpenAI


client = OpenAI(
    base_url='http://localhost:11434/v1/',
    api_key='ollama',
)

if __name__ == '__main__':
    prompt = "What's the formula for energy?"

    response = client.chat.completions.create(
        model='gemma:2b',
        temperature=0.0,
        messages=[{"role": "user", "content": prompt}]
    )
    answer = response.choices[0].message.content
    print(answer)
    print(f"Number of completion_tokens: {response.usage.completion_tokens}")