import pandas as pd
from openai_chatgpt_example import start_chat


def summarize_news(csv_file="news.csv"):
    news = pd.read_csv(csv_file)

    # records = news.to_dict(orient="records")

    # for record in records[:5]:
    #     print(record)

    groups = news.groupby("topic_id")
    summarize_list = list()
    for gid, group in groups:
        # print(group)
        temp = list(group["title"])
        message = "\n".join(temp)
        summarize_str = start_chat(message)
        summarize_list.append(summarize_str)
        # print(summarize_str)
        # print(test)
        # print(list(group["title"]))
        # break

    return summarize_list


if __name__ == "__main__":
    test_news = summarize_news()
    for test_new in test_news:
        print(test_new)
