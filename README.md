# api-pagination-lint

**Portfolio Brief.** Check list API specs for pagination, limits, and ordering guarantees.

## Problem

List endpoints break clients when pagination is vague. This CLI reviews API notes for missing limits and cursor semantics.

## Solution

`api-pagination-lint` accepts API list endpoint notes or OpenAPI snippets in text, JSON, JSONL, or CSV form.

## Why It Matters

```bash
python -m pip install -e ".[dev]"
api-pagination-lint examples/sample.txt
api-pagination-lint examples/sample.txt --json --fail-on medium
```

## How To Run

| Rule | Severity | Meaning |
|---|---:|---|
| `no-pagination` | high | list endpoint lacks pagination |
| `missing-limit` | medium | limit is missing |
| `undefined-order` | low | result ordering is undefined |

## Quality

```bash
ruff check .
pytest
python -m api_pagination_lint --help
```

License: MIT

### Example Input

```text
GET /users returns all users pagination none limit missing order undefined
```

### Architecture

`cli.py` reads files, `core.py` evaluates records, and `rules.py` keeps the api-pagination-lint policy surface explicit.
