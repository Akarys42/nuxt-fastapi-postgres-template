#!/usr/bin/env bash
set -e

if [ -v RUN_MIGRATIONS ]; then
  echo Running migrations
  python -m alembic upgrade head
  echo Migrations complete starting application
fi

if [ -v USE_RELOADER ]; then
  extra_args=--reload
fi

uvicorn app.main:app --host 0.0.0.0 $extra_args
