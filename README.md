# API Pagination Lint

![API Pagination Lint cover](assets/readme-cover.svg)

> Check list API specs for pagination, limits, and ordering guarantees

![stack](https://img.shields.io/badge/stack-Python-16a34a?style=flat-square) ![python](https://img.shields.io/badge/python-3.11-dc2626?style=flat-square) ![license](https://img.shields.io/badge/license-MIT-7c3aed?style=flat-square) ![ci](https://img.shields.io/badge/ci-GitHub%20Actions-0891b2?style=flat-square)

## At a glance

| Area | Detail |
| --- | --- |
| Focus | API operations |
| Command | `api-pagination-lint` |
| Formats | text, JSON, JSONL, CSV |
| Output | Markdown table or JSON |

## What it checks

| Rule | Severity | What it catches |
| --- | --- | --- |
| `no-pagination` | high | list endpoint lacks pagination |
| `missing-limit` | medium | limit is missing |
| `undefined-order` | low | result ordering is undefined |

## Try it locally

```bash
python -m pip install -e ".[dev]"
api-pagination-lint examples/sample.txt
api-pagination-lint examples/sample.txt --json --fail-on medium
```

## Notes from the code

`rules.py` keeps the project policy explicit, while `core.py` handles parsing and report rendering. The CLI stays thin on purpose so the checks are easy to test.

## Verify

```bash
python -m pip install -e ".[dev]"
ruff check .
pytest
python -m api_pagination_lint --help
```
