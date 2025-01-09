from openai import OpenAI
client = OpenAI()


def start_chat(user_message, rpg_setting="你是一個中立且專業的記者,幫我把新聞摘錄成30字以內的一句話"):
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


# return_str = start_chat("3時間點低溫僅8度！強烈大陸冷氣團來襲 高山有望降雪")
# print(return_str)
