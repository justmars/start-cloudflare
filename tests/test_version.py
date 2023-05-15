import pathlib

import tomllib

import start_cloudflare


def test_version():
    path = pathlib.Path("pyproject.toml")
    data = tomllib.loads(path.read_text())
    version = data["tool"]["poetry"]["version"]
    assert version == start_cloudflare.__version__
