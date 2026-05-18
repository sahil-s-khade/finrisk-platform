from sqlalchemy import text

from config.database import engine

try:
    with engine.connect() as connection:
        result = connection.execute(text("SELECT version();"))

        print("\n✅ Database connection successful!\n")

        for row in result:
            print("PostgreSQL Version:")
            print(row[0])

except Exception as e:
    print("\n Database connection failed!\n")
    print(e)