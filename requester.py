import requests

from jira_query_types import JiraCredentials, JiraRequestParameters


class Requester:
    HEADERS = {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
    }

    def __init__(self, jira_credentials: JiraCredentials):
        self._session = requests.Session()
        self._session.auth = (
            jira_credentials.username,
            jira_credentials.password,
        )
        self._url = jira_credentials.url
        self._session.headers.update(self.HEADERS)

    def get_response_as_json(
        self, jira_request_parameters: JiraRequestParameters
    ):
        return self._session.request(
            method='GET',
            url=self._url + jira_request_parameters.path,
            params={
                'fields': jira_request_parameters.fields,
                'maxResults': jira_request_parameters.max_results,
                'jql': jira_request_parameters.jql,
            },
        ).json()
