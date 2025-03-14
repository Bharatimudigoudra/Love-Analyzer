def love_calculator(name1, name2): 
    name1 = name1.lower()
    name2 = name2.lower()
    
    combined_names = name1 + name2
    true_count = sum(combined_names.count(letter) for letter in "true")
    love_count = sum(combined_names.count(letter) for letter in "love")

    love_score = int(str(true_count) + str(love_count)) % 101  # Ensuring percentage stays within 0-100

    print(f"💖 Love Score for {name1.capitalize()} & {name2.capitalize()}: {love_score}% 💖")

name1 = input("Enter first name: ").strip()
name2 = input("Enter second name: ").strip()
love_calculator(name1, name2)
