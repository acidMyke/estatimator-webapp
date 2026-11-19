from pathlib import Path

from openapi_python_client import generate
from openapi_python_client.config import Config, ConfigFile, MetaType
from openapi_python_client.parser.errors import ErrorLevel

MAILJET_SPEC_URL = (
    "https://artifacts.apis.io/mailjet/openapi/mailjet-send-api-openapi.yml"
)


ROOT = Path(__file__).resolve().parents[2]
SRC_DIR = ROOT / "src"

OPENAPI_DIR = ROOT / "openapi" / "external"
MAILJET_CLIENT_DIR = SRC_DIR / "mailjet_send_client"


def generate_client(
    spec_path: Path,
    output_path: Path,
    project_name: str,
):
    config = Config.from_sources(
        config_file=ConfigFile(
            project_name_override=project_name,
            package_name_override=project_name.replace("-", "_"),
        ),
        meta_type=MetaType.NONE,
        document_source=spec_path,
        file_encoding="utf-8",
        overwrite=True,
        output_path=output_path,
    )

    errors = generate(config=config)
    warnings = [error for error in errors if error.level == ErrorLevel.WARNING]
    failures = [error for error in errors if error.level == ErrorLevel.ERROR]

    for warning in warnings:
        print(f"WARNING: {warning.header}")

    if failures:
        for error in failures:
            print(f"ERROR: {error.header}")
            if error.detail:
                print(error.detail)

        raise RuntimeError(f"Failed to generate client: {project_name}")

    print(f"Generated client: {output_path}")


def main():
    generate_client(
        OPENAPI_DIR / "filtered-mailjet.json",
        MAILJET_CLIENT_DIR,
        "mailjet-send-client",
    )


if __name__ == "__main__":
    main()
