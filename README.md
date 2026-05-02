# start-cloudflare

![Github CI](https://github.com/justmars/start-cloudflare/actions/workflows/ci.yml/badge.svg)

Small Pydantic settings helpers for Cloudflare projects.

`start-cloudflare` centralizes the environment variables and header helpers that Cloudflare API clients tend to repeat: account ID, API version, account email, legacy global API key, Origin CA key, bearer token headers, and account-scoped endpoint URLs.

## Install

```bash
uv add start-cloudflare
```

## Configure

Create a `.env` file or export the variables in your shell:

```dotenv
CF_ACCT_ID=your-account-id
CF_API_VERSION=4
CF_ACCT_EMAIL=you@example.com
CF_GLOBAL_API_KEY=legacy-global-api-key
CF_ORIGIN_CA_KEY=origin-ca-key
```

Only `CF_ACCT_ID` is normally needed for URL construction. Authentication
values are optional until you request the matching header helper.

## Use

```python
from start_cloudflare import CF

cf = CF()

base_url = cf.base
account_url = cf.add_account_endpoint("/zones")
auth_header = CF.set_bearer_auth("api-token")
```

For a default configuration, `base_url` is
`https://api.cloudflare.com/client/v4`, and `account_url` is
`https://api.cloudflare.com/client/v4/accounts/zones`.

## Documentation

See the [full documentation](https://justmars.github.io/start-cloudflare) for
field details, examples, and generated API reference.

## Development

```bash
uv sync
uv run pytest
uv run zensical build
```

To preview the docs locally:

```bash
just docs
```
