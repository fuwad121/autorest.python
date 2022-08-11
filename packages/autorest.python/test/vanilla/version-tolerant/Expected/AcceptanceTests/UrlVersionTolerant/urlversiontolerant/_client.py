# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from copy import deepcopy
from typing import Any, Optional, TYPE_CHECKING

from azure.core import PipelineClient
from azure.core.rest import HttpRequest, HttpResponse

from ._configuration import AutoRestUrlTestServiceConfiguration
from ._serialization import Deserializer, Serializer
from .operations import PathItemsOperations, PathsOperations, QueriesOperations

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from typing import Dict


class AutoRestUrlTestService:  # pylint: disable=client-accepts-api-version-keyword
    """Test Infrastructure for AutoRest.

    :ivar paths: PathsOperations operations
    :vartype paths: urlversiontolerant.operations.PathsOperations
    :ivar queries: QueriesOperations operations
    :vartype queries: urlversiontolerant.operations.QueriesOperations
    :ivar path_items: PathItemsOperations operations
    :vartype path_items: urlversiontolerant.operations.PathItemsOperations
    :param global_string_path: A string value 'globalItemStringPath' that appears in the path.
     Required.
    :type global_string_path: str
    :param global_string_query: should contain value null. Default value is None.
    :type global_string_query: str
    :keyword endpoint: Service URL. Default value is "http://localhost:3000".
    :paramtype endpoint: str
    """

    def __init__(  # pylint: disable=missing-client-constructor-parameter-credential
        self,
        global_string_path: str,
        global_string_query: Optional[str] = None,
        *,
        endpoint: str = "http://localhost:3000",
        **kwargs: Any
    ) -> None:
        self._config = AutoRestUrlTestServiceConfiguration(
            global_string_path=global_string_path, global_string_query=global_string_query, **kwargs
        )
        self._client = PipelineClient(base_url=endpoint, config=self._config, **kwargs)

        self._serialize = Serializer()
        self._deserialize = Deserializer()
        self._serialize.client_side_validation = False
        self.paths = PathsOperations(self._client, self._config, self._serialize, self._deserialize)
        self.queries = QueriesOperations(self._client, self._config, self._serialize, self._deserialize)
        self.path_items = PathItemsOperations(self._client, self._config, self._serialize, self._deserialize)

    def send_request(self, request: HttpRequest, **kwargs: Any) -> HttpResponse:
        """Runs the network request through the client's chained policies.

        >>> from azure.core.rest import HttpRequest
        >>> request = HttpRequest("GET", "https://www.example.org/")
        <HttpRequest [GET], url: 'https://www.example.org/'>
        >>> response = client.send_request(request)
        <HttpResponse: 200 OK>

        For more information on this code flow, see https://aka.ms/azsdk/dpcodegen/python/send_request

        :param request: The network request you want to make. Required.
        :type request: ~azure.core.rest.HttpRequest
        :keyword bool stream: Whether the response payload will be streamed. Defaults to False.
        :return: The response of your network call. Does not do error handling on your response.
        :rtype: ~azure.core.rest.HttpResponse
        """

        request_copy = deepcopy(request)
        request_copy.url = self._client.format_url(request_copy.url)
        return self._client.send_request(request_copy, **kwargs)

    def close(self):
        # type: () -> None
        self._client.close()

    def __enter__(self):
        # type: () -> AutoRestUrlTestService
        self._client.__enter__()
        return self

    def __exit__(self, *exc_details):
        # type: (Any) -> None
        self._client.__exit__(*exc_details)