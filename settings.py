"""
Credentials for different users.
"""
import os
from jira_query_types import JiraCredentials


JIRA_DEFAULT_API_USER_CREDENTIALS = JiraCredentials(
    url=os.environ['JIRA_URL'],
    username=os.environ['SYSTEM_JIRA_USERNAME'],
    password=os.environ['SYSTEM_JIRA_PASSWORD'],
)
JIRA_MY_CREDENTIALS = JiraCredentials(
    url=os.environ['JIRA_URL'],
    username=os.environ['SZAKHAROV_JIRA_USERNAME'],
    password=os.environ['SZAKHAROV_JIRA_PASSWORD'],
)
