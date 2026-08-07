with open("python_basics/09_files/notes.txt") as file:
    lines = file.readlines()
    searched_attribute = input("What are you looking for? ")

    topic_found = False

    for line in lines:
        if line.strip() == searched_attribute:
            topic_found = True
            break
    if topic_found:
        print("Topic found.")
    else:
        print("Topic not found")
