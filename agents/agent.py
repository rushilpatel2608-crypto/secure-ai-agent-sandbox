import os
import subprocess
import datetime

WORKSPACE = "/workspace"
REPOS = f"{WORKSPACE}/repos"
BUILDS = f"{WORKSPACE}/builds"
LOGS = f"{WORKSPACE}/logs"


def log(message):
    now = datetime.datetime.now().isoformat()
    with open(f"{LOGS}/agent.log", "a") as f:
        f.write(f"[{now}] {message}\n")


def run(cmd):
    log(f"RUN: {cmd}")
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    log(result.stdout)
    log(result.stderr)
    return result.stdout


def create_project(name):
    path = f"{REPOS}/{name}"
    os.makedirs(path, exist_ok=True)

    main_file = f"{path}/main.py"

    with open(main_file, "w") as f:
        f.write("""
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def hello():
    return {"message": "hello world"}
""")

    log(f"Created project {name}")


def list_projects():
    return os.listdir(REPOS)


def main():
    print("Agent ready")

    while True:
        cmd = input("agent> ")

        if cmd.startswith("create-project"):
            name = cmd.split()[1]
            create_project(name)

        elif cmd == "list-projects":
            print(list_projects())

        elif cmd.startswith("run"):
            run(cmd[4:])

        elif cmd == "exit":
            break


if __name__ == "__main__":
    main()
