# chat-app

To run:

### Database:
Start a Postgres instance with Docker, mapping localhost:5000 to 5432 on container
```
docker run --name some-postgres -e POSTGRES_PASSWORD=password -d -p 5000:5432 postgres
```

### Server:
In server directory, start venv (optional), install pip requirements, then run server:
```
pip install -r requirements.txt
```
```
python chat-app-server.py
```

### Client:
In client directory install requirements with:
```
yarn install
```

Then run:
```
yarn expo-electron start
```
