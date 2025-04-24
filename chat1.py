from openai import OpenAI
client = OpenAI()

# Set the base URL for the OpenAI API
client.api_base = 'https://openai-api.agilearch.tech'

completion = client.chat.completions.create(
    model="gpt-4o", #模型名称
    messages=[
        {
            # 角色设置
            "role": "developer", 
            "content": "你是一个IT技术架构师"},
        {
            # 提示词
            "role": "user",
            "content": "我是一个初级程序员，我想成为一名IT技朼架构师，你有什么建议吗？"
        }
    ]
)

print(completion.choices[0].message)