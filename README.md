# log-report

Small Harbor task for Terminal-Bench 2. The agent reads an access log at /app/access.log and writes a summary to /app/report.json with three keys, total_requests, unique_ips and top_path.

The task files are under log-report/ (task.toml, instruction.md, environment/, solution/, tests/).

To run it you need Docker running and Harbor installed:

    harbor run -p log-report -a oracle     # reference solution, reward 1
    harbor run -p log-report --agent nop   # does nothing, reward 0

Grading runs after the agent stops. tests/test.sh runs pytest and writes reward.txt and ctrf.json to /logs/verifier/. The tests open /app/report.json and check the three values against the log (6, 3, /index.html), one test each.
