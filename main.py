"""
Отправка запросов к JIRA.

* Для дальнейшей проверки - изменять нужно данные в файле debug_point.py.
* Чтобы добавить новые credentials для Jira, изменяйте settings.py
"""
from collections import defaultdict

from glom import glom

from jira_query_types import JiraCredentials, JiraRequestParameters
from debug_point import debug_point, RequestSectionsCustomNamespace
from requester import Requester


class MainNamespace:
    @classmethod
    def main(cls):
        request_results = {}
        jira_requester = Requester(
            RequestSectionsCustomNamespace.ACTIVE_JIRA_CREDENTIAL
        )
        structure_for_intersections = defaultdict(lambda: [])
        for (
            request_name,
            request_parameters,
        ) in RequestSectionsCustomNamespace.REQUESTS.items():
            # Request results.
            json_response = jira_requester.get_response_as_json(
                request_parameters
            )
            request_results.update({request_name: json_response})
            if request_parameters.SUBMAPS:
                for (
                    submap_name,
                    submap_value,
                ) in request_parameters.SUBMAPS.items():
                    request_results.update(
                        {
                            f'{request_name}_{submap_name}': glom(
                                json_response, submap_value
                            )
                        }
                    )
                    structure_for_intersections[submap_name].append(
                        request_name
                    )
        # Create information about intersections.
        for (
            submap_name,
            request_names,
        ) in structure_for_intersections.items():
            if len(request_names) >= 2:
                result_intersection = None
                for i_request_name, request_name in enumerate(request_names):
                    cur_intersection_value = request_results[
                        f'{request_name}_{submap_name}'
                    ]
                    if i_request_name == 0:
                        result_intersection = set(cur_intersection_value)
                    else:
                        result_intersection &= set(cur_intersection_value)
                request_results[
                    f'INTERSECTION_{submap_name}'
                ] = result_intersection

        debug_point(request_results)


if __name__ == '__main__':
    MainNamespace.main()
