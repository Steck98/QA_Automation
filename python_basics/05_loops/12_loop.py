# Firma zatrudnia 15 nowych pracowników.

# Program ma wypisać identyfikatory:

# EMP-001
# EMP-002
# EMP-003
# ...
# EMP-015
# Wymagania
# użyj for,
# użyj range(),
# nie wpisuj numerów ręcznie.
i = 0
for worker in range(15):
    i += 1
    print(f"EMP-{i:02}")
