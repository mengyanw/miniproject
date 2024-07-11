# Dashboard 

## Quick setup
```
git clone https://github.com/mengyanw/miniproject # or
unzip miniproject.zip
cd miniproject

# Set environment variable
cd backend
touch .env
vi .env
# .env file should look like this
API = https://api.blinkfire.com/developer/api/v1/posts
TOKEN = <your api token>

# Populate the db and get the app running
docker compose up
```
## Tools used
Frontend: Vue 3 + Vite + antd
Backend: Django + PostgresSQL

