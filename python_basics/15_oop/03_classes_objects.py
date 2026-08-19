class TestCase:
    def __init__(self, name, duration, status="blocked"):
        self.name = name
        self.duration = duration
        self.status = status

    def __str__(self):
        return f"{self.name} [{self.status}]"


login_test = TestCase(
    name="login_test",
    duration=1.2,
    status="passed",
)

print(login_test)
