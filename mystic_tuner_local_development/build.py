"""
Guides the developer through the process of building the mystic tuner system
Helps the developer make the necessary .env files then calls docker compose in a detached terminal
"""

import os
import subprocess
import sys
from dotenv import load_dotenv

# Keys with -DONE-TERMINAL are set in the env and used in the docker compose
frontend_env_vars = {
    "AUTH0_SECRET-DONE-TERMINAL": "",
    "APP_BASE_URL": "http://localhost:3000",
    "AUTH0_DOMAIN": "",
    "AUTH0_CLIENT_ID": "",
    "AUTH0_CLIENT_SECRET": "",
}

backend_env_vars = {
    "AUTH0_CLIENT_ID": "",
    "AUTH0_CLIENT_SECRET": "",
    "AUTH0_DOMAIN": "",
}


def generate_node_key():
    """
    Generates a new node key for the .env files
    """
    node_key = os.urandom(32).hex()
    with open("../../backend/Mystic_Tuner_Backend/.env", "a") as f:
        f.write(f"AUTH0_SECRET='{node_key}'\n")
    return node_key


def build():
    """
    Builds the .env files in the correct system locations
    """
    # Create the .env files
    with open("../../frontend/mystic_tuner_frontend/.env", "w") as f:
        for key, value in frontend_env_vars.items():
            if key.endswith("-DONE-TERMINAL"):
                continue
            f.write(f"{key}='{value}'\n")

    with open("../../backend/Mystic_Tuner_Backend/.env", "w") as f:
        for key, value in backend_env_vars.items():
            if key.endswith("-DONE-TERMINAL"):
                continue
            f.write(f"{key}='{value}'\n")


def validate_git():
    """
    Validates that the git repositories are present
    They should all be in the same directory heirarchy

       ```
       Mystic Tuner
       ├── documentation-and-development
       ├── frontend
       ├── backend
       ├── database
       ```
    """
    repos = ["documentation-and-development", "frontend", "backend", "database"]
    # Get the folders up two levels, then change back to the documentation-and-development folder
    for i in range(2):
        os.chdir("..")
    folders = os.listdir()
    os.chdir("./documentation-and-development")
    os.chdir("./mystic_tuner_local_development")

    for repo in repos:
        if repo not in folders:
            print(
                f"ERROR: ensure that you have correctly cloned the {repo} repository as per the README in documentation-and-development"
            )
            sys.exit(1)


def cli():
    """
    Gets the user input for the .env files
    """
    validate_git()
    allowed_overwrite = input(
        "This will overwrite the current .env files. Are you sure you want to continue? (y/n): "
    )

    if allowed_overwrite.lower() != "y" and allowed_overwrite.lower() != "yes":
        print("Exiting...")
        sys.exit(0)

    print("Please enter the following values for the frontend .env file:")
    for key, value in frontend_env_vars.items():
        if key.endswith("-DONE-TERMINAL"):
            continue
        elif value:
            frontend_env_vars[key] = value
        else:
            frontend_env_vars[key] = input(f"{key}: ")

    print("Please enter the following values for the backend .env file:")
    for key, value in backend_env_vars.items():
        if key.endswith("-DONE-TERMINAL"):
            continue
        elif key in frontend_env_vars:
            backend_env_vars[key] = frontend_env_vars[key]
        elif value:
            backend_env_vars[key] = value
        else:
            backend_env_vars[key] = input(f"{key}: ")


if __name__ == "__main__":
    cli()
    build()
    # Handle the pesky AUTH0_SECRET-DONE-TERMINAL
    generate_node_key()
    subprocess.Popen(["docker-compose", "up"], shell=True)
    sys.exit(0)
