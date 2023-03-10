from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler

import settings

# from langchain_for_slack_bot_rev2 import LangChainAgent
from chat_gpt_agent import ConversationAgent

SLACK_BOT_TOKEN = settings.SLACK_BOT_TOKEN
SLACK_APP_TOKEN = settings.SLACK_APP_TOKEN

app = App(token=SLACK_BOT_TOKEN)
agent = ConversationAgent()


@app.event("app_mention")
def mention_handler(body, say):
    """
    メンションを受けたメッセージに対して応答する

    Parameters
    ----------
    body : dict
        リクエストボディ
    say : function
        メッセージを送信する関数

    Returns
    -------
    None
    """
    # say("AIが回答を作成中です。しばらくお待ちください。")

    text: str = body["event"]["text"]
    # textから"<@U04M0QRDWUA>"等を削除
    text = text.replace("<@U04MZL9BJ21>", "")
    text = text.replace("<@U04M0QRDWUA>", "")
    try:
        answer = agent.get_answer(text)
    except Exception as e:
        answer = "エラーが発生しました。"

        print(answer)

        # show stack trace
        import traceback

        traceback.print_exc()

        answer += "\n\n"
        answer += traceback.format_exc()

        print(answer)

    say(answer)


# ソケットモードの有効化＆アプリの実行


if __name__ == "__main__":
    handler = SocketModeHandler(app, SLACK_APP_TOKEN)
    handler.start()
