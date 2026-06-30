from __future__ import annotations

from api_pagination_lint.models import Rule

PROJECT_NAME = 'api-pagination-lint'
SUMMARY = 'Check list API specs for pagination, limits, and ordering guarantees.'
SAMPLE_RISK = 'GET /users returns all users pagination none limit missing order undefined'
SAMPLE_CLEAN = 'GET /users cursor pagination limit max 100 order created_at desc'
TEXT_FIELDS = ("text", "content", "description", "summary", "body", "notes", "message")
SUBJECT_FIELDS = ("id", "name", "path", "endpoint", "service", "job", "route", "event")

RULES = (
    Rule(
        code='no-pagination',
        severity='high',
        pattern='\\bpagination\\s*(none|missing|null)\\b|returns all',
        message='list endpoint lacks pagination',
        recommendation='Add cursor or page-based pagination.',
    ),
    Rule(
        code='missing-limit',
        severity='medium',
        pattern='\\blimit\\s*(missing|none|null)\\b',
        message='limit is missing',
        recommendation='Declare default and maximum page sizes.',
    ),
    Rule(
        code='undefined-order',
        severity='low',
        pattern='\\border\\s*(undefined|missing|none)\\b',
        message='result ordering is undefined',
        recommendation='Document stable sort order.',
    ),
)
