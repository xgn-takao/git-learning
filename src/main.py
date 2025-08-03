import logging

# ログ設定
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def hello_world():
    logger.info("Hello World関数が呼ばれました")
    print("Hello, Git World!")

def get_user_name():
    try:
        return input("あなたの名前を入力してください: ")
    except KeyboardInterrupt:
        logger.warning("処理がキャンセルされました")
        print("\n処理がキャンセルされました")
        return None
    except EOFError:
        logger.error("入力エラーが発生しました")
        print("\n入力エラーが発生しました")
        return None

def greet_user():
    name = get_user_name()
    if name:
        logger.info(f"ユーザー {name} に挨拶します")
        print(f"こんにちは、{name}さん!")
    else:
        logger.info("処理が終了されました")
        print("処理を終了します")

if __name__ == "__main__":
    hello_world()
    greet_user()
