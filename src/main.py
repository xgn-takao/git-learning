def hello_world():
    print("Hello, Git World!")

def get_user_name():
    return input("あなたの名前を入力してください: ")

def greet_user():
    name = get_user_name()
    print(f"こんにちは、{name}さん!")

if __name__ == "__main__":
    hello_world()
    greet_user()
