from sqlalchemy import inspect

from config.database import engine

inspector = inspect(engine)

tables = inspector.get_table_names()

print("\nAvailable Tables:\n")

for table in tables:
    print(f" {table}")