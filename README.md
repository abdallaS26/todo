# todo

## PostgreSQL setup

This app now defaults to PostgreSQL by default. The configured default connection is:

```bash
postgresql+psycopg://postgres:postgres@localhost:5432/todo_db
```

To override the default connection, set the `DATABASE_URL` environment variable before starting the app:

```bash
export DATABASE_URL="postgresql+psycopg://<user>:<password>@localhost:5432/todo_db"
```

Then create the database and tables:

```bash
createdb todo_db
python init_db.py
```

Start the app from the virtual environment:

```bash
source venv/bin/activate
python app.py
```
# todo-app
