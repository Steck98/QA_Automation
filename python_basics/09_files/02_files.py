topics = ["Python", "Git", "QA", "Automation", "Selenium", "Pytest"]

with open("python_basics/09_files/notes.txt", "w") as file:
    for topic in topics:
        file.write(f"{topic}\n")

with open("python_basics/09_files/notes.txt") as file:
    for line in file:
        print(line.strip())
