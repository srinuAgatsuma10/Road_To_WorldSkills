import json
import os
from datetime import datetime

class TestResultLogger:
    def __init__(self, filename: str):
        self.filename = filename

        # Create file if not exists or empty
        if not os.path.exists(filename) or os.stat(filename).st_size == 0:
            with open(filename, "w") as f:
                json.dump([], f)


    def log(self, test_id: str, status: str, duration_ms: int) -> None:
        with open(self.filename, "r") as f:
            data = json.load(f)

        record = {
            "id": test_id,
            "status": status,
            "duration_ms": duration_ms,
            "timestamp": datetime.now().strftime("%Y-%m-%dT%H:%M:%S")
        }

        data.append(record)

        with open(self.filename, "w") as f:
            json.dump(data, f, indent=2)

    def summary(self) -> None:
        with open(self.filename, "r") as f:
            data = json.load(f)

        total = len(data)
        passed = sum(1 for d in data if d["status"] == "pass")
        failed = sum(1 for d in data if d["status"] == "fail")
        avg = sum(d["duration_ms"] for d in data) // total

        print(f"Total:        {total}")
        print(f"Passed:       {passed}")
        print(f"Failed:       {failed}")
        print(f"Avg duration: {avg} ms")


# Sample calls
logger = TestResultLogger("Logger_results.json")
logger.log("TC-001", "pass", 342)
logger.log("TC-002", "fail", 1201)
logger.log("TC-003", "pass", 88)
logger.log("TC-004", "pass", 450)
logger.log("TC-005", "fail", 3002)
logger.summary()
