from openai import OpenAI
client = OpenAI()


def start_chat(user_message, rpg_setting="你是一個公正的記者,幫我把新聞摘錄成30字以內的一句話"):
    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": rpg_setting},
            {
                "role": "user",
                "content": user_message
            }
        ]
    )

    return completion.choices[0].message.content
