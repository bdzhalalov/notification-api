from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    ENV: str = "development"
    APP_HOST: str = "127.0.0.1"
    APP_PORT: int = "8000"
    LOG_LEVEL: str = "DEBUG"
    MONGO_INITDB_ROOT_USERNAME: str
    MONGO_INITDB_ROOT_PASSWORD: str
    DB_HOST: str
    DB_PORT: int
    DB_NAME: str
    DB_USERNAME: str
    DB_PASSWORD: str

    class Config:
        env_file = ".env"

    #TODO: use Depend instead methods
    def get_db_name(self):
        if self.ENV == "test":
            return self.DB_NAME + "_test"

        return self.DB_NAME

    def get_db_uri(self):

        db_name = self.get_db_name()
        return f'mongodb://{self.DB_USERNAME}:{self.DB_PASSWORD}@{self.DB_HOST}:{self.DB_PORT}/{db_name}?authSource={db_name}'


settings = Settings()
