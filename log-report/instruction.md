There is an Apache style access log sitting at /app/access.log. Read it and work out a few basic stats about the traffic, then write them to a JSON file at /app/report.json.

The report must be a single JSON object with these three keys:

1. total_requests, an integer, the number of request lines in the log.
2. unique_ips, an integer, how many different client IPs show up. The client IP is the first field on each line.
3. top_path, a string, the request path that was asked for the most times. The path is the second token inside the quoted request, so for "GET /index.html HTTP/1.1" the path is /index.html.

Do not change /app/access.log. Only /app/report.json is graded.

You have 120 seconds to complete this task. Do not cheat by using online solutions or hints specific to this task.
