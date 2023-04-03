import os

DATABASE_URL = os.getenv("DATABASE_URL", None)
if DATABASE_URL is None:
    raise RuntimeError("DATABASE_URL environment variable is not set.")
