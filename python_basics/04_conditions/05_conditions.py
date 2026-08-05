# Gracz może wejść do miasta, jeżeli:

# ma przepustkę (has_pass),
# lub jest strażnikiem (is_guard).

has_pass = False
is_guard = True

if has_pass or is_guard:
    print("Access granted.")
else:
    print("Access denied.")
