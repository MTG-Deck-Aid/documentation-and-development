# Configuring Local Development Environment

## Prerequisites

- Have Docker Engine installed on your machine.

## Steps

1. Clone this repository and all the other repositories that are part of the project. Please clone are the same parent directory. Ex:

   ```
   Mystic Tuner
   ├── documentation-and-development
   ├── frontend
   ├── backend
   ├── database
   ```

2. Navigate to the ./local_development directory of this repository in a linux based terminal.
3. Run the command: `docker-compose build && docker-compose up`
4. The docker command should complete with no errors and deploy 3 containers: frontend, backend, and database.
