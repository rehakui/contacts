import json

FILENAME = "contacts.json"

def load():
    try:
        with open(FILENAME, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

def save(contacts):
    with open(FILENAME, "w", encoding="utf-8") as f:
        json.dump(contacts, f, ensure_ascii=False, indent=2)



def add(contacts):
    name = input("名前を入力して下さい: ")
    number = input("数字を入力して下さい: ")
    contacts[name] = number
    save(contacts)
    print(f"{name} を保存しました。")

def list_contacts(contacts):
    if not contacts:
        print("空です。")
    else:
        for nam, num in contacts.items():
            print(f"{nam}: {num}")

def find(contacts):
    find_name = str(input("検索する名前: "))
    find_number = contacts.get(find_name)
    if find_number:
        print(f"{find_name}の数字: {find_number}")
    else:
        print("見つかりませんでした。")

def delete_contacts(contacts):
    delete_name = str(input("削除する名前: "))
    if delete_name in contacts:
        confirm = str(input(f"{delete_name} を本当に削除しますか? (y/n): ")).lower()
        if confirm == "y":
            del contacts[delete_name]
            save(contacts)
            print(f"{delete_name} を削除しました。")
        elif confirm == "n":
            print("キャンセルしました。")
            return
    else:
        print("名前が見つかりません。")
    save(contacts)

def main():
    contacts = load()
    while True:
        user_prompt = str(input("add/find/list/find/delete?: "))
        if user_prompt == "add":
            add(contacts)
        elif user_prompt == "find":
            find(contacts)
        elif user_prompt == "list":
            list_contacts(contacts)
        elif user_prompt == "find":
            find(contacts)
        elif user_prompt == "delete":
            delete_contacts(contacts)
        elif user_prompt == "end":
            break


if __name__ == "__main__":
    main()
