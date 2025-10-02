from operator import contains

contacts = {}

is_start = True

while is_start:
    def add():
        name = input("名前を入力して下さい: ")
        number = input("数字を入力して下さい: ")
        contacts[name] = number

    def find():
        find_name = input("名前を検索して下さい: ")
        find_number = contacts.get(find_name)
        if find_number:
            print(f"{find_name}の数字: {find_number}")
        else:
            print("見つかりませんでした。")

    def list():
        if not contacts:
            print("空です。")
        else:
            for nam, num in contacts.items():
                print(f"{nam}: {num}")

    user_prompt = str(input("add/find/list?: "))
    if user_prompt == "add":
        add()
    elif user_prompt == "find":
        find()
    elif user_prompt == "list":
        list()
    elif user_prompt == "end":
        is_start = False

