import re
import csv

logs = {"2026-04-29 08:12:03 INFO  [AuthService] User login successful for user=priya.sharma",
"2026-04-29 08:14:55 ERROR [PaymentGateway] Timeout reached for user=ravi.kumar",
"2026-04-29 08:17:22 WARN  [SessionManager] Token expiry imminent for user=anita.desai",
"2026-04-29 08:21:10 ERROR [AuthService] Invalid credentials for user=mohit.joshi",
"2026-04-29 08:25:44 INFO  [ReportService] Statement generated for user=kavitha.nair"}

pattern = re.compile(
    r"(?P<date>\d{4}-\d{2}-\d{2})\s+"
    r"(?P<time>\d{2}:\d{2}:\d{2})\s+"
    r"(?P<level>\w+)\s+\[(?P<service>[^\]]+)\].*user=(?P<username>[\w\.]+)"
)

with open("parsed_logs.csv", "w") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["date", "time", "level", "service", "username"])
    for log in logs:
        match = pattern.search(log)
        if match:
            date = match.group("date")
            time = match.group("time")
            level = match.group("level")
            service = match.group("service")
            username = match.group("username")
            writer.writerow([date, time, level, service, username])


