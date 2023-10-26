# pylint: disable=too-many-lines
# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Unbranded Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Unbranded (R) Python Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import datetime
from typing import Any, Callable, Dict, Optional, TypeVar
import uuid

from corehttp.exceptions import (
    ClientAuthenticationError,
    HttpResponseError,
    ResourceExistsError,
    ResourceNotFoundError,
    ResourceNotModifiedError,
    map_error,
)
from corehttp.rest import HttpRequest, HttpResponse
from corehttp.runtime.pipeline import PipelineResponse
from corehttp.utils import case_insensitive_dict

from .._serialization import Serializer
from .._vendor import RepeatabilityClientMixinABC

T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]

_SERIALIZER = Serializer()
_SERIALIZER.client_side_validation = False


def build_repeatability_immediate_success_request(**kwargs: Any) -> HttpRequest:  # pylint: disable=name-too-long
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})

    # Construct URL
    _url = "/special-headers/repeatability/immediateSuccess"

    # Construct headers
    if "Repeatability-Request-ID" not in _headers:
        _headers["Repeatability-Request-ID"] = str(uuid.uuid4())
    if "Repeatability-First-Sent" not in _headers:
        _headers["Repeatability-First-Sent"] = _SERIALIZER.serialize_data(datetime.datetime.now(), "rfc-1123")

    return HttpRequest(method="POST", url=_url, headers=_headers, **kwargs)


class RepeatabilityClientOperationsMixin(RepeatabilityClientMixinABC):
    def immediate_success(self, **kwargs: Any) -> None:  # pylint: disable=inconsistent-return-statements
        """Check we recognize Repeatability-Request-ID and Repeatability-First-Sent.

        :keyword bool stream: Whether to stream the response of this operation. Defaults to False. You
         will have to context manage the returned stream.
        :return: None
        :rtype: None
        :raises ~corehttp.exceptions.HttpResponseError:
        """
        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = kwargs.pop("params", {}) or {}

        cls: ClsType[None] = kwargs.pop("cls", None)

        _request = build_repeatability_immediate_success_request(
            headers=_headers,
            params=_params,
        )
        _request.url = self._client.format_url(_request.url)

        _stream = kwargs.pop("stream", False)
        pipeline_response: PipelineResponse = self._client.pipeline.run(  # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [204]:
            if _stream:
                response.read()  # Load the body in memory and close the socket
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        response_headers = {}
        response_headers["Repeatability-Result"] = self._deserialize(
            "str", response.headers.get("Repeatability-Result")
        )

        if cls:
            return cls(pipeline_response, None, response_headers)  # type: ignore
