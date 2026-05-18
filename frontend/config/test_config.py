from settings import Config

print("Flask Environment:", Config.FLASK_ENV)
print("Database URI:", Config.SQLALCHEMY_DATABASE_URI)
print("JWT Secret Loaded:", bool(Config.JWT_SECRET_KEY))
print("AWS Region:", Config.AWS_DEFAULT_REGION)
print("Model Path:", Config.MODEL_PATH)