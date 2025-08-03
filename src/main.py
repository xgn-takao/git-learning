def hello_world():
    print("Hello, Git World!")

def get_user_name():
    try:
        return input("あなたの名前を入力してください: ")
    except KeyboardInterrupt:
        print("\n処理がキャンセルされました")
        return None
    except EOFError:
        print("\n入力エラーが発生しました")
        return None

def greet_user():
    name = get_user_name()
    if name:
        print(f"こんにちは、{name}さん!")
    else:
        print("処理を終了します")

if __name__ == "__main__":
    hello_world()
    greet_user()
