from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_ignore_empty=True)

    app_name: str = "{{ cookiecutter.project_name }}"
    app_env: str = "development"
    log_level: str = "INFO"

settings = Settings()
