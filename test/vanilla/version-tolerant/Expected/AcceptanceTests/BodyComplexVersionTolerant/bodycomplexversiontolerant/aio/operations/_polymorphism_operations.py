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

from ...operations._polymorphism_operations import (
    build_get_complicated_request,
    build_get_composed_with_discriminator_request,
    build_get_composed_without_discriminator_request,
    build_get_dot_syntax_request,
    build_get_valid_request,
    build_put_complicated_request,
    build_put_missing_discriminator_request,
    build_put_valid_missing_required_request,
    build_put_valid_request,
)

T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]


class PolymorphismOperations:
    """PolymorphismOperations async operations.

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
    async def get_valid(self, **kwargs: Any) -> Any:
        """Get complex types that are polymorphic.

        :return: JSON object
        :rtype: Any
        :raises: ~azure.core.exceptions.HttpResponseError

        Example:
            .. code-block:: python

                # response body for status code(s): 200
                response.json() == {
                    "fishtype": "fishtype",
                    "length": "float",
                    "siblings": [
                        "..."
                    ],
                    "species": "str (optional)"
                }
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[Any]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        request = build_get_valid_request(
            template_url=self.get_valid.metadata["url"],
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

    get_valid.metadata = {"url": "/complex/polymorphism/valid"}  # type: ignore

    @distributed_trace_async
    async def put_valid(self, complex_body: Any, **kwargs: Any) -> None:
        """Put complex types that are polymorphic.

        :param complex_body: Please put a salmon that looks like this:
         {
                 'fishtype':'Salmon',
                 'location':'alaska',
                 'iswild':true,
                 'species':'king',
                 'length':1.0,
                 'siblings':[
                   {
                     'fishtype':'Shark',
                     'age':6,
                     'birthday': '2012-01-05T01:00:00Z',
                     'length':20.0,
                     'species':'predator',
                   },
                   {
                     'fishtype':'Sawshark',
                     'age':105,
                     'birthday': '1900-01-05T01:00:00Z',
                     'length':10.0,
                     'picture': new Buffer([255, 255, 255, 255, 254]).toString('base64'),
                     'species':'dangerous',
                   },
                   {
                     'fishtype': 'goblin',
                     'age': 1,
                     'birthday': '2015-08-08T00:00:00Z',
                     'length': 30.0,
                     'species': 'scary',
                     'jawsize': 5
                   }
                 ]
               };.
        :type complex_body: Any
        :return: None
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError

        Example:
            .. code-block:: python

                fishtype = 'Salmon' or 'Shark'

                # JSON input template you can fill out and use as your body input.
                complex_body = {
                    "fishtype": "fishtype",
                    "length": "float",
                    "siblings": [
                        "..."
                    ],
                    "species": "str (optional)"
                }
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[None]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        content_type = kwargs.pop("content_type", "application/json")  # type: Optional[str]

        json = complex_body

        request = build_put_valid_request(
            content_type=content_type,
            json=json,
            template_url=self.put_valid.metadata["url"],
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

    put_valid.metadata = {"url": "/complex/polymorphism/valid"}  # type: ignore

    @distributed_trace_async
    async def get_dot_syntax(self, **kwargs: Any) -> Any:
        """Get complex types that are polymorphic, JSON key contains a dot.

        :return: JSON object
        :rtype: Any
        :raises: ~azure.core.exceptions.HttpResponseError

        Example:
            .. code-block:: python

                # response body for status code(s): 200
                response.json() == {
                    "fish.type": "fish.type",
                    "species": "str (optional)"
                }
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[Any]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        request = build_get_dot_syntax_request(
            template_url=self.get_dot_syntax.metadata["url"],
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

    get_dot_syntax.metadata = {"url": "/complex/polymorphism/dotsyntax"}  # type: ignore

    @distributed_trace_async
    async def get_composed_with_discriminator(self, **kwargs: Any) -> Any:
        """Get complex object composing a polymorphic scalar property and array property with polymorphic
        element type, with discriminator specified. Deserialization must NOT fail and use the
        discriminator type specified on the wire.

        :return: JSON object
        :rtype: Any
        :raises: ~azure.core.exceptions.HttpResponseError

        Example:
            .. code-block:: python

                # response body for status code(s): 200
                response.json() == {
                    "fishes": [
                        {
                            "fish.type": "fish.type",
                            "species": "str (optional)"
                        }
                    ],
                    "salmons": [
                        {
                            "fish.type": "DotSalmon",
                            "iswild": "bool (optional)",
                            "location": "str (optional)",
                            "species": "str (optional)"
                        }
                    ],
                    "sampleFish": {
                        "fish.type": "fish.type",
                        "species": "str (optional)"
                    },
                    "sampleSalmon": {
                        "fish.type": "DotSalmon",
                        "iswild": "bool (optional)",
                        "location": "str (optional)",
                        "species": "str (optional)"
                    }
                }
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[Any]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        request = build_get_composed_with_discriminator_request(
            template_url=self.get_composed_with_discriminator.metadata["url"],
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

    get_composed_with_discriminator.metadata = {"url": "/complex/polymorphism/composedWithDiscriminator"}  # type: ignore

    @distributed_trace_async
    async def get_composed_without_discriminator(self, **kwargs: Any) -> Any:
        """Get complex object composing a polymorphic scalar property and array property with polymorphic
        element type, without discriminator specified on wire. Deserialization must NOT fail and use
        the explicit type of the property.

        :return: JSON object
        :rtype: Any
        :raises: ~azure.core.exceptions.HttpResponseError

        Example:
            .. code-block:: python

                # response body for status code(s): 200
                response.json() == {
                    "fishes": [
                        {
                            "fish.type": "fish.type",
                            "species": "str (optional)"
                        }
                    ],
                    "salmons": [
                        {
                            "fish.type": "DotSalmon",
                            "iswild": "bool (optional)",
                            "location": "str (optional)",
                            "species": "str (optional)"
                        }
                    ],
                    "sampleFish": {
                        "fish.type": "fish.type",
                        "species": "str (optional)"
                    },
                    "sampleSalmon": {
                        "fish.type": "DotSalmon",
                        "iswild": "bool (optional)",
                        "location": "str (optional)",
                        "species": "str (optional)"
                    }
                }
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[Any]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        request = build_get_composed_without_discriminator_request(
            template_url=self.get_composed_without_discriminator.metadata["url"],
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

    get_composed_without_discriminator.metadata = {"url": "/complex/polymorphism/composedWithoutDiscriminator"}  # type: ignore

    @distributed_trace_async
    async def get_complicated(self, **kwargs: Any) -> Any:
        """Get complex types that are polymorphic, but not at the root of the hierarchy; also have
        additional properties.

        :return: JSON object
        :rtype: Any
        :raises: ~azure.core.exceptions.HttpResponseError

        Example:
            .. code-block:: python

                # response body for status code(s): 200
                response.json() == {
                    "fishtype": "salmon",
                    "iswild": "bool (optional)",
                    "length": "float",
                    "location": "str (optional)",
                    "siblings": [
                        {
                            "fishtype": "fishtype",
                            "length": "float",
                            "siblings": [
                                "..."
                            ],
                            "species": "str (optional)"
                        }
                    ],
                    "species": "str (optional)"
                }
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[Any]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        request = build_get_complicated_request(
            template_url=self.get_complicated.metadata["url"],
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

    get_complicated.metadata = {"url": "/complex/polymorphism/complicated"}  # type: ignore

    @distributed_trace_async
    async def put_complicated(self, complex_body: Any, **kwargs: Any) -> None:
        """Put complex types that are polymorphic, but not at the root of the hierarchy; also have
        additional properties.

        :param complex_body:
        :type complex_body: Any
        :return: None
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError

        Example:
            .. code-block:: python

                fishtype = 'SmartSalmon'

                # JSON input template you can fill out and use as your body input.
                complex_body = {
                    "fishtype": "salmon",
                    "iswild": "bool (optional)",
                    "length": "float",
                    "location": "str (optional)",
                    "siblings": [
                        {
                            "fishtype": "fishtype",
                            "length": "float",
                            "siblings": [
                                "..."
                            ],
                            "species": "str (optional)"
                        }
                    ],
                    "species": "str (optional)"
                }
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[None]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        content_type = kwargs.pop("content_type", "application/json")  # type: Optional[str]

        json = complex_body

        request = build_put_complicated_request(
            content_type=content_type,
            json=json,
            template_url=self.put_complicated.metadata["url"],
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

    put_complicated.metadata = {"url": "/complex/polymorphism/complicated"}  # type: ignore

    @distributed_trace_async
    async def put_missing_discriminator(self, complex_body: Any, **kwargs: Any) -> Any:
        """Put complex types that are polymorphic, omitting the discriminator.

        :param complex_body:
        :type complex_body: Any
        :return: JSON object
        :rtype: Any
        :raises: ~azure.core.exceptions.HttpResponseError

        Example:
            .. code-block:: python

                fishtype = 'SmartSalmon'

                # JSON input template you can fill out and use as your body input.
                complex_body = {
                    "fishtype": "salmon",
                    "iswild": "bool (optional)",
                    "length": "float",
                    "location": "str (optional)",
                    "siblings": [
                        {
                            "fishtype": "fishtype",
                            "length": "float",
                            "siblings": [
                                "..."
                            ],
                            "species": "str (optional)"
                        }
                    ],
                    "species": "str (optional)"
                }

                # response body for status code(s): 200
                response.json() == {
                    "fishtype": "salmon",
                    "iswild": "bool (optional)",
                    "length": "float",
                    "location": "str (optional)",
                    "siblings": [
                        {
                            "fishtype": "fishtype",
                            "length": "float",
                            "siblings": [
                                "..."
                            ],
                            "species": "str (optional)"
                        }
                    ],
                    "species": "str (optional)"
                }
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[Any]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        content_type = kwargs.pop("content_type", "application/json")  # type: Optional[str]

        json = complex_body

        request = build_put_missing_discriminator_request(
            content_type=content_type,
            json=json,
            template_url=self.put_missing_discriminator.metadata["url"],
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

    put_missing_discriminator.metadata = {"url": "/complex/polymorphism/missingdiscriminator"}  # type: ignore

    @distributed_trace_async
    async def put_valid_missing_required(self, complex_body: Any, **kwargs: Any) -> None:
        """Put complex types that are polymorphic, attempting to omit required 'birthday' field - the
        request should not be allowed from the client.

        :param complex_body: Please attempt put a sawshark that looks like this, the client should not
         allow this data to be sent:
         {
             "fishtype": "sawshark",
             "species": "snaggle toothed",
             "length": 18.5,
             "age": 2,
             "birthday": "2013-06-01T01:00:00Z",
             "location": "alaska",
             "picture": base64(FF FF FF FF FE),
             "siblings": [
                 {
                     "fishtype": "shark",
                     "species": "predator",
                     "birthday": "2012-01-05T01:00:00Z",
                     "length": 20,
                     "age": 6
                 },
                 {
                     "fishtype": "sawshark",
                     "species": "dangerous",
                     "picture": base64(FF FF FF FF FE),
                     "length": 10,
                     "age": 105
                 }
             ]
         }.
        :type complex_body: Any
        :return: None
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError

        Example:
            .. code-block:: python

                fishtype = 'Salmon' or 'Shark'

                # JSON input template you can fill out and use as your body input.
                complex_body = {
                    "fishtype": "fishtype",
                    "length": "float",
                    "siblings": [
                        "..."
                    ],
                    "species": "str (optional)"
                }
        """
        cls = kwargs.pop("cls", None)  # type: ClsType[None]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))

        content_type = kwargs.pop("content_type", "application/json")  # type: Optional[str]

        json = complex_body

        request = build_put_valid_missing_required_request(
            content_type=content_type,
            json=json,
            template_url=self.put_valid_missing_required.metadata["url"],
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

    put_valid_missing_required.metadata = {"url": "/complex/polymorphism/missingrequired/invalid"}  # type: ignore