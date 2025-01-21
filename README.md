# Wiki style web app
This is a wiki style web application.

## Running with docker
To run it with docker simply run
```sh
docker compose up --build
```
Then navigate to the application at http://localhost.

## Running in development
To run it locally you need to install `poetry`, you then need to install the requirements with `poetry install`.

Inside the `wiki` folder run:
```sh
poetry run python -m app
```
You can then navigate to the application at http://127.0.0.1:5000.

Adding/removing/updating documents locally will alter the `app.db` file. To reset this file, delete `app.db` and run:
```sh
cat app.sql | sqlite3 app.db
```
