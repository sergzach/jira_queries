"""
A module with custom Jira types.
"""
from typing import NamedTuple, Optional

ALL_FIELDS = '*all'


class JiraCredentials(NamedTuple):
    url: str
    username: str
    password: str


class JiraRequestParameters(NamedTuple):
    path: str
    fields: str = None
    jql: Optional[str] = None
    max_results: int = None
    SUBMAPS: Optional[dict] = None
