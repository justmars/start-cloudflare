import os
from pathlib import Path

import pytest
from dotenv import dotenv_values


@pytest.fixture
def cf_env():
    def cf_env(name: str, default: str | int | None = None):
        if name in os.environ:
            return os.environ[name]
        if Path(".env").exists():
            return dotenv_values(".env").get(name, default)
        return default

    return cf_env
