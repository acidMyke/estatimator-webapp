from application.core.settings.base import BaseAppSettings


class DatasourceSettings(BaseAppSettings):
    # TODO: add OneMap token
    # TODO: add data.gov.sg token
    # TODO: add URA token
    pass


datasource_settings = DatasourceSettings()  # pyright: ignore[reportCallIssue]
