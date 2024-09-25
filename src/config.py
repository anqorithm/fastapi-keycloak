from pydantic_settings import BaseSettings
from pydantic import Field
from keycloak import KeycloakOpenID

class Settings(BaseSettings):
    keycloak_server_url: str = Field(..., env="KEYCLOAK_SERVER_URL")
    keycloak_realm: str = Field(..., env="KEYCLOAK_REALM")
    keycloak_client_id: str = Field(..., env="KEYCLOAK_CLIENT_ID")
    keycloak_client_secret: str = Field(..., env="KEYCLOAK_CLIENT_SECRET")

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()

keycloak_openid = KeycloakOpenID(
    server_url=settings.keycloak_server_url,
    realm_name=settings.keycloak_realm,
    client_id=settings.keycloak_client_id,
    client_secret_key=settings.keycloak_client_secret,
)

def get_openid_config():
    return keycloak_openid.well_known()
