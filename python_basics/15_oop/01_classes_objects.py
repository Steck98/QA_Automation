class TestCase:
    allowed_statuses = ("passed", "failed", "skipped", "blocked")

    def __init__(self, name, duration, status="blocked") -> None:
        self.name = name
        self.status = status
        self.duration = duration

    def display_result(self):
        print(f"Test: {self.name} | Status: {self.status} | Duration: {self.duration}s")

    def mark_as_passed(self):
        self.status = "passed"

    def change_status(self, new_status):
        if new_status in self.allowed_statuses:
            self.status = new_status
        else:
            print("Invalid status")

    def is_failed(self):
        return self.status == "failed"

    def is_slow(self, limit):
        return self.duration > limit


login_test = TestCase(name="login_test", duration=1.2, status="passed")
payment_test = TestCase(name="payment_test", status="failed", duration=5.8)
registration_test = TestCase(name="registration_test", duration=0)


login_test.display_result()
payment_test.display_result()
registration_test.display_result()
