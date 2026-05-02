---
icon: lucide/rocket
---

# start-cloudflare

Pydantic settings helpers for building small Cloudflare API clients.

The package keeps Cloudflare account configuration in one `BaseSettings` class and provides small helpers for request headers and account-scoped endpoint URLs.

## Install

```bash
uv add start-cloudflare
```

## Configuration

`CF` reads from environment variables and from a local `.env` file.

```dotenv
CF_ACCT_ID=your-account-id
CF_API_VERSION=4
CF_ACCT_EMAIL=you@example.com
CF_GLOBAL_API_KEY=legacy-global-api-key
CF_ORIGIN_CA_KEY=origin-ca-key
```

| Environment variable | Field | Notes |
| --- | --- | --- |
| `CF_ACCT_ID` | `account_id` | Cloudflare account ID used for account endpoints. |
| `CF_API_VERSION` | `version` | API version used in `https://api.cloudflare.com/client/v{version}`. Defaults to `4`. |
| `CF_ACCT_EMAIL` | `email` | Account email used with legacy key authentication. |
| `CF_GLOBAL_API_KEY` | `global_api_key` | Legacy global API key. Prefer API tokens for new integrations. |
| `CF_ORIGIN_CA_KEY` | `origin_ca_key` | Origin CA key for certificate workflows. |

!!! note "Cloudflare authentication"

    Cloudflare recommends API tokens for new integrations. Use
    `CF.set_bearer_auth(token)` to build an `Authorization: Bearer ...` header.
    The global API key helpers are kept for older integrations that still need
    `X-Auth-Email` and `X-Auth-Key`.

## Quickstart

```python
from start_cloudflare import CF

cf = CF()

headers = CF.set_bearer_auth("api-token")
endpoint = cf.add_account_endpoint("/zones")
```

With the default API version, `endpoint` resolves to:

```text
https://api.cloudflare.com/client/v4/accounts/zones
```

## Common Patterns

### Bearer token

```python
headers = CF.set_bearer_auth("api-token")
```

### Legacy global API key

```python
cf = CF()
headers = {
    **cf.head_email,
    **cf.head_auth_key,
}
```

### Account endpoint

```python
cf = CF()
url = cf.add_account_endpoint("/workers/scripts")
```

The path must start with `/`.

## Reference

See the [API reference](reference.md) for generated details on exported
constants, security keys, and settings fields.
