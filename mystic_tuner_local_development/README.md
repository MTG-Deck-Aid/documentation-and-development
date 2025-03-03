# Configuring Local Development Environment

## Prerequisites

- Have Docker Engine installed on your machine.

## From Complete Scratch Steps

1. Clone this repository and all the other repositories that are part of the project. Please clone are the same parent directory. Ex:

   ```
   Mystic Tuner
   ├── documentation-and-development
   ├── frontend
   ├── backend
   ├── database
   ```

2. Navigate to the `documentation-and-development/mystic_tuner_local_development` directory in a
   linux based terminal.

3. `Run python build.py` to build the necessary .env files and then the docker compose file
4. The frontend container takes a while to run but you will see
   "Ready in Xs" when it is ready.

## Using Docker Compose with .env files in place

1. Navigate to the `documentation-and-development/mystic_tuner_local_development` directory in a
   linux based terminal.
2. Run the command: `docker-compose build && docker-compose up`
3. The docker command should complete with no errors and deploy 3 containers: frontend, backend, and database.
4. The frontend container takes a while to run but you will see
   "Ready in Xs" when it is ready.

NOTE: database is WIp
