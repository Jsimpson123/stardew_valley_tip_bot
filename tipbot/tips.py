import random

def generate_tip():
    with open("../tips/stardew_tips.txt", encoding='utf8') as f:
        contents = f.read()
        contents_list = contents.split("\n")
        cleaned_list = []
        for tip in contents_list:
            new = tip.strip("- ")
            cleaned_list.append(new)
        return random.choice(cleaned_list[:-1])