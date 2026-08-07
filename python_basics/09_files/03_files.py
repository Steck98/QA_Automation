# Napisz program, który:

# Otworzy plik w trybie:
# "a"
# Dopisze na końcu:
# SQL
# API
# Docker
# Zamknie plik.
# Otworzy go ponownie.
# Wyświetli całą zawartość.

with open("python_basics/09_files/notes.txt", "a") as file:
    file.write("\nSQL")
    file.write("\nAPI")
    file.write("\nDocker")
with open("python_basics/09_files/notes.txt") as file:
    print(file.read())
