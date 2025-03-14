def flames_game(name1, name2):
    name1 = name1.replace(" ", "").lower()
    name2 = name2.replace(" ", "").lower()

    for char in name1:
        if char in name2:
            name1 = name1.replace(char, "", 1)
            name2 = name2.replace(char, "", 1)

    count = len(name1 + name2)
    flames = ["F", "L", "A", "M", "E", "S"]

    while len(flames) > 1:
        split_index = (count % len(flames)) - 1
        if split_index >= 0:
            flames = flames[split_index+1:] + flames[:split_index]
        else:
            flames.pop()

    result_map = {
        "F": "Friends",
        "L": "Love",
        "A": "Affection",
        "M": "Marriage",
        "E": "Enemies",
        "S": "Siblings"
    }
    return result_map[flames[0]]

# Example usage
name1 = input("Enter first name: ")
name2 = input("Enter second name: ")
relationship = flames_game(name1, name2)
print(f"The relationship between {name1} and {name2} is: {relationship}")
