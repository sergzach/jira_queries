"""
A place to get results mentioned in requestSectionsCustomNamespace.

Use glom-syntax to specify additional selections in SUBMAPs.
"""
from jira_query_types import JiraRequestParameters, ALL_FIELDS
from splitconfigs import apply_config
from settings import *


class RequestSectionsCustomNamespace:
    """
    Place here requests you want to view.
    """
    class Config1:
        REQUESTS = dict(
            TASKS=JiraRequestParameters(
                path='/rest/api/2/search',
                fields=ALL_FIELDS,
                jql='issuetype = "task" and (project = "Time tracker")',
                max_results=5000,
                SUBMAPS=dict(
                    SUMMARY='issues.*.fields.summary',
                    PROJECT_KEY='issues.*.fields.project.key',
                    PROJECT_NAME='issues.*.fields.project.name',
                    ACCOUNT='issues.*.fields.account',
                    ACCOUNT_NAME='issues.*.fields.customfield_10400.name',
                    PROJECT_FIELD='issues.*.fields.customfield_10400'
                ),
            ),
            ACCOUNTS=JiraRequestParameters(
                path='/rest/tempo-accounts/1/account',
                fields=ALL_FIELDS,
                jql=None,
                max_results=5000,
                SUBMAPS=dict(ACCOUNT_NAME='*.name'),
            ),
        )
        ACTIVE_JIRA_CREDENTIAL = JIRA_MY_CREDENTIALS


@apply_config(1)
def debug_point(request_results: dict):
    print('Place breakpoint here.')
