# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import functools
from typing import Any, Callable, Dict, Generic, Optional, TypeVar
import warnings

from azure.core.exceptions import (
    ClientAuthenticationError,
    HttpResponseError,
    ResourceExistsError,
    ResourceNotFoundError,
    map_error,
)
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import AsyncHttpResponse
from azure.core.rest import HttpRequest
from azure.core.tracing.decorator_async import distributed_trace_async

from ...operations._enum_operations import (
    build_get_not_expandable_request,
    build_get_referenced_constant_request,
    build_get_referenced_request,
    build_put_not_expandable_request,
    build_put_referenced_constant_request,
    build_put_referenced_request,
)

T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]


class EnumOperations:
    """EnumOperations async operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    """

    def __init__(self, client, config, serializer, deserializer) -> None:
        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self._config = config

    @distributed_trace_async
    async def get_not_expandable(self, **kwargs: Any) -> str:
        """Get enum value 'red color' from enumeration of 'red color', 'green-color', 'blue_color'.

        :return: str. Possible values are: "red color", "green-color", and "blue_color".
        :rtype: str
        :raises: ~azure.core.exceptions.HttpResponseError

        Example:
            .. code-block:: python

                # response body for status code(s): 200
                response.json() == "str (optional)"
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[str]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        request = build_get_not_expandable_request(
            template_url=self.get_not_expandable.metadata["url"],
        )
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client.send_request(
            request, stream=False, _return_pipeline_response=True, **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if response.content:
            deserialized = response.json()
        else:
            deserialized = None

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get_not_expandable.metadata = {"url": "/string/enum/notExpandable"}  # type: ignore

    @distributed_trace_async
    async def put_not_expandable(self, string_body: str, **kwargs: Any) -> None:
        """Sends value 'red color' from enumeration of 'red color', 'green-color', 'blue_color'.

        :param string_body: string body. Possible values are: "red color", "green-color", and
         "blue_color".
        :type string_body: str
        :return: None
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[None]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        content_type = kwargs.pop("content_type", "application/json")  # type: Optional[str]

        json = string_body

        request = build_put_not_expandable_request(
            content_type=content_type,
            json=json,
            template_url=self.put_not_expandable.metadata["url"],
        )
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client.send_request(
            request, stream=False, _return_pipeline_response=True, **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
            return cls(pipeline_response, None, {})

    put_not_expandable.metadata = {"url": "/string/enum/notExpandable"}  # type: ignore

    @distributed_trace_async
    async def get_referenced(self, **kwargs: Any) -> str:
        """Get enum value 'red color' from enumeration of 'red color', 'green-color', 'blue_color'.

        :return: str. Possible values are: "red color", "green-color", and "blue_color".
        :rtype: str
        :raises: ~azure.core.exceptions.HttpResponseError

        Example:
            .. code-block:: python

                # response body for status code(s): 200
                response.json() == "str (optional)"
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[str]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        request = build_get_referenced_request(
            template_url=self.get_referenced.metadata["url"],
        )
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client.send_request(
            request, stream=False, _return_pipeline_response=True, **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if response.content:
            deserialized = response.json()
        else:
            deserialized = None

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get_referenced.metadata = {"url": "/string/enum/Referenced"}  # type: ignore

    @distributed_trace_async
    async def put_referenced(self, enum_string_body: str, **kwargs: Any) -> None:
        """Sends value 'red color' from enumeration of 'red color', 'green-color', 'blue_color'.

        :param enum_string_body: enum string body. Possible values are: "red color", "green-color", and
         "blue_color".
        :type enum_string_body: str
        :return: None
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[None]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        content_type = kwargs.pop("content_type", "application/json")  # type: Optional[str]

        json = enum_string_body

        request = build_put_referenced_request(
            content_type=content_type,
            json=json,
            template_url=self.put_referenced.metadata["url"],
        )
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client.send_request(
            request, stream=False, _return_pipeline_response=True, **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
            return cls(pipeline_response, None, {})

    put_referenced.metadata = {"url": "/string/enum/Referenced"}  # type: ignore

    @distributed_trace_async
    async def get_referenced_constant(self, **kwargs: Any) -> Any:
        """Get value 'green-color' from the constant.

        :return: JSON object
        :rtype: Any
        :raises: ~azure.core.exceptions.HttpResponseError

        Example:
            .. code-block:: python

                # response body for status code(s): 200
                response.json() == {
                    "ColorConstant": "str",
                    "field1": "str (optional)"
                }
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[Any]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        request = build_get_referenced_constant_request(
            template_url=self.get_referenced_constant.metadata["url"],
        )
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client.send_request(
            request, stream=False, _return_pipeline_response=True, **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if response.content:
            deserialized = response.json()
        else:
            deserialized = None

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get_referenced_constant.metadata = {"url": "/string/enum/ReferencedConstant"}  # type: ignore

    @distributed_trace_async
    async def put_referenced_constant(self, enum_string_body: Any, **kwargs: Any) -> None:
        """Sends value 'green-color' from a constant.

        :param enum_string_body: enum string body.
        :type enum_string_body: Any
        :return: None
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError

        Example:
            .. code-block:: python

                # JSON input template you can fill out and use as your body input.
                enum_string_body = {
                    "ColorConstant": "str",
                    "field1": "str (optional)"
                }
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[None]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        content_type = kwargs.pop("content_type", "application/json")  # type: Optional[str]

        json = enum_string_body

        request = build_put_referenced_constant_request(
            content_type=content_type,
            json=json,
            template_url=self.put_referenced_constant.metadata["url"],
        )
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client.send_request(
            request, stream=False, _return_pipeline_response=True, **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
            return cls(pipeline_response, None, {})

    put_referenced_constant.metadata = {"url": "/string/enum/ReferencedConstant"}  # type: ignore