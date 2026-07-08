# log-report

A small Terminal-Bench 2 (Harbor) task. The agent reads an Apache style access log at /app/access.log and writes a JSON summary to /app/report.json with three keys: total_requests, unique_ips and top_path.

## Task layout

The task lives under log-report/ (task.toml, instruction.md, environment/, solution/, tests/).

## Run it

From this folder, with Docker running and Harbor installed:

    harbor run -p log-report -a oracle    # reference solution, reward 1
    harbor run -p log-report --agent nop  # does nothing, reward 0

## How grading works

After the agent stops, tests/test.sh runs pytest and writes reward.txt (1 or 0) and ctrf.json to /logs/verifier/. tests/test_outputs.py opens /app/report.json and checks the three values against the known log (total_requests 6, unique_ips 3, top_path /index.html), one test per value.
