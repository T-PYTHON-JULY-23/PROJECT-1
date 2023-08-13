def update_state():
    with open("bill.txt", "r") as file:
        change_word=file.read()
        change_word=change_word.replace("pending", "complete")
        file.close()
    with open("bill.txt", "w") as file:
        file.write(change_word)
        file.close()