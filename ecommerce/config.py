import os

APP_ENV = os.getenv("APP_ENV", "development")
DATABASE_USERNAME = os.getenv("DATABASE_USERNAME", "homestead")
DATABASE_PASSWORD = os.getenv("DATABASE_PASSWORD", "secret")
DATABASE_HOST = os.getenv("DATABASE_HOST", "localhost")
DATABASE_NAME = os.getenv("DATABASE_NAME", "ecommerce")
TEST_DATABASE_NAME = os.getenv("DATABASE_NAME", "ecommerce")
