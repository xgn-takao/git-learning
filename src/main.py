import logging

# ログ設定
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def hello_world():
    logger.info("Hello World関数が呼ばれました")
    print("Hello, Git World!")

def get_user_name():
    return input("あなたの名前を入力してください: ")

def greet_user():
    name = get_user_name()
    logger.info(f"ユーザー {name} に挨拶します")
    print(f"こんにちは、{name}さん!")

if __name__ == "__main__":
    hello_world()
    greet_user()
