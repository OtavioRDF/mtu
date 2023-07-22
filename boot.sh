#!/usr/bin/env sh
alembic upgrade head
python -m jobs.consumer &
uvicorn --host 0.0.0.0 --port 8000 app.main:app 