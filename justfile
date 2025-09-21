set dotenv-load

# prepare to commit
prep:
  pre-commit run --all-files

# serve docs
docs:
  mkdocs serve

# create .env file from example
dumpenv:
  op inject -i env.example -o .env

# upload to pypi
publish:
  uv build && \
  uv publish --token $PYPI_TOKEN
