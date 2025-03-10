Heroku Dynos check for certian files to determine the type of application being deployed.
Below are some notes from the Heroku documentation that I found useful.

# Backend

For the python backend, the `requirements.txt` is critical and must be up to data.

Running local command (if we get to it):
`cat Procfile.windows`
`web: python manage.py runserver %PORT%`

`heroku local --port 5006 -f Procfile.windows`

Add Free addons like:

Papertrail (for logging)
`heroku addons:create papertrail:choklad`
`heroku create` to create a new app with the Procfile
`heroku ps` to check the status of the dynos
`heroku ps:scale web=0` to scale down the dynos this will stop the app
`heroku open` to open the app in the browser
`heroku ps:scale web=1` to scale up the dynos this will start the app
`heroku run bash` to run bash on the dyno as a one-off dyno
`heroku addons` to see the addons and their assiocated costs

For Postgres addon follow: https://devcenter.heroku.com/articles/getting-started-with-python#provision-and-use-a-database

Heroku CLI -->
`heroku addons:create heroku-postgresql:essential-0`

requirement.txt -->
psycopg[c]; sys_platform == "linux"
psycopg[binary]; sys_platform != "linux"

Procfile -->
`release: ./manage.py migrate --no-input`

Local Postgres -->
`heroku pg:psql`

# Frontend

/my-heroku-app
├── frontend/ # Frontend repo (React, Vue, etc.)
│ ├── .env
│ ├── package.json
│ ├── src/
│ ├── public/
│ ├── ...
│
├── backend/ # Backend repo (Django)
│ ├── .env
│ ├── manage.py # Python (Django)
│ ├── ...
├── database/ # Postgres SQL repo
│ ├── database_creation_script.sql # Database creation script
|
├── documentation-and-development/ # Deployment-related files
│ ├── Procfile # Heroku Procfile (custom location)
│ ├── other files (optional)
|
├── documentation-and-development/ # Deployment-related files
│ ├── Procfile # Heroku Procfile (custom location)
│ ├── other files (optional)
