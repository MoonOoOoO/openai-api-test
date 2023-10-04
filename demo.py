import os
import openai

openai.api_key = os.getenv('OPENAI_API_KEY')
res = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "user", "content": "你好"},
    ]
)

# 2 token 1 个字
# 输入 0.03 usd 10000字
# 输出 0.04 usd 10000字

# 输入2.2毛钱1w字
# 输出2.9毛钱1w字

if __name__ == '__main__':
    print(res['choices'][0]['message']['content'])
