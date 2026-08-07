# Masz plik:

# notes.txt

# Napisz program, który:

# Otworzy plik.
# Przejdzie po nim:
# for line in file:
# Wypisze każdą linię bez \n.


with open("python_basics/09_files/notes.txt") as file:
    for line in file:
        print(line.strip())
