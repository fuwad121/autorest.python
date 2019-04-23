# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from azure.core import AsyncPipelineClient
from msrest import Serializer, Deserializer

from ._configuration_async import AutoRestHttpInfrastructureTestServiceConfiguration
from msrest.exceptions import HttpOperationError
from .operations_async import HttpFailureOperations
from .operations_async import HttpSuccessOperations
from .operations_async import HttpRedirectsOperations
from .operations_async import HttpClientFailureOperations
from .operations_async import HttpServerFailureOperations
from .operations_async import HttpRetryOperations
from .operations_async import MultipleResponsesOperations
from .. import models


class AutoRestHttpInfrastructureTestService(object):
    """Test Infrastructure for AutoRest


    :ivar http_failure: HttpFailure operations
    :vartype http_failure: httpinfrastructure.aio.operations_async.HttpFailureOperations
    :ivar http_success: HttpSuccess operations
    :vartype http_success: httpinfrastructure.aio.operations_async.HttpSuccessOperations
    :ivar http_redirects: HttpRedirects operations
    :vartype http_redirects: httpinfrastructure.aio.operations_async.HttpRedirectsOperations
    :ivar http_client_failure: HttpClientFailure operations
    :vartype http_client_failure: httpinfrastructure.aio.operations_async.HttpClientFailureOperations
    :ivar http_server_failure: HttpServerFailure operations
    :vartype http_server_failure: httpinfrastructure.aio.operations_async.HttpServerFailureOperations
    :ivar http_retry: HttpRetry operations
    :vartype http_retry: httpinfrastructure.aio.operations_async.HttpRetryOperations
    :ivar multiple_responses: MultipleResponses operations
    :vartype multiple_responses: httpinfrastructure.aio.operations_async.MultipleResponsesOperations

    :param str base_url: Service URL
    """

    def __init__(
            self, base_url=None, config=None, **kwargs):

        if not base_url:
            base_url = 'http://localhost:3000'
        self._config = config or AutoRestHttpInfrastructureTestServiceConfiguration(**kwargs)
        self._client = AsyncPipelineClient(base_url=base_url, config=self._config, **kwargs)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self.api_version = '1.0.0'
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

        self.http_failure = HttpFailureOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.http_success = HttpSuccessOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.http_redirects = HttpRedirectsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.http_client_failure = HttpClientFailureOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.http_server_failure = HttpServerFailureOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.http_retry = HttpRetryOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.multiple_responses = MultipleResponsesOperations(
            self._client, self._config, self._serialize, self._deserialize)

    async def __aenter__(self):
        await self._client.__aenter__()
        return self
    async def __aexit__(self, *exc_details):
        await self._client.__aexit__(*exc_details)
