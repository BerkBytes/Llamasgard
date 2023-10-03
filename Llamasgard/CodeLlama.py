import requests

API_URL = "http://127.0.0.1:8000/predict"

def CodeLlama(user, system="""Your name is Code Llama, a state-of-the-art large language model (LLM) specialized in generating and discussing code. As an advanced descendant of Llama 2, you've been trained extensively on code-specific datasets, granting you the capability to generate code, understand natural language related to code, complete code fragments, and assist in debugging. You are proficient in many popular programming languages such as Python, C++, Java, PHP, Typescript, C#, Bash, and more. Keep responses concise and be friendly towards users.""", prefix='' ,max_new_tokens=1024, temperature=0.9, top_p=0.95, repetition_penalty=1.2, top_k=50,num_return_sequences=1):
    data = {
        'user': user,
        'system': system,
        'prefix': prefix,
        'max_new_tokens': max_new_tokens,
        'temperature': temperature,
        'top_p': top_p,
        'repetition_penalty': repetition_penalty,
        'top_k': top_k,
        'num_return_sequences': num_return_sequences,
    }

    response = requests.post(API_URL, json=data)

    if response.status_code == 200:
        return response.json()['response']
    else:
        return f"Error {response.status_code}: {response.text}"
