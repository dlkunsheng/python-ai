import ollama

# Generate text
response = ollama.generate(model="deepseek-r1:1.5b", prompt="Why is the sky blue?")
print(response)

# Chat with the model
messages = [
    {"role": "user", "content": "Why is the sky blue?"}
]
response = ollama.chat(model="deepseek-r1:1.5b", messages=messages)
print(response)

# Stream responses
for chunk in ollama.chat(model="deepseek-r1:1.5b", messages=messages, stream=True):
    print(chunk, end="")