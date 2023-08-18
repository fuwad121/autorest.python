# pylint: disable=too-many-lines
# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import sys
from typing import Any, Callable, Dict, Optional, TypeVar

from msrest import Serializer

from azure.core.exceptions import (
    ClientAuthenticationError,
    HttpResponseError,
    ResourceExistsError,
    ResourceNotFoundError,
    ResourceNotModifiedError,
    map_error,
)
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import HttpResponse
from azure.core.rest import HttpRequest
from azure.core.tracing.decorator import distributed_trace
from azure.core.utils import case_insensitive_dict

from .. import models as _models
from .._vendor import _convert_request

if sys.version_info >= (3, 8):
    from typing import Literal  # pylint: disable=no-name-in-module, ungrouped-imports
else:
    from typing_extensions import Literal  # type: ignore  # pylint: disable=ungrouped-imports
T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]

_SERIALIZER = Serializer()


def build_post_required_request(
    path: str, *, custom_header: Optional[str] = None, query: int = 30, **kwargs: Any
) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = kwargs.pop("template_url", "/parameterGrouping/postRequired/{path}")
    path_format_arguments = {
        "path": _SERIALIZER.url("path", path, "str"),
    }

    _url: str = _url.format(**path_format_arguments)  # type: ignore

    # Construct parameters
    if query is not None:
        _params["query"] = _SERIALIZER.query("query", query, "int")

    # Construct headers
    if custom_header is not None:
        _headers["customHeader"] = _SERIALIZER.header("custom_header", custom_header, "str")
    if content_type is not None:
        _headers["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="POST", url=_url, params=_params, headers=_headers, **kwargs)


def build_post_optional_request(*, custom_header: Optional[str] = None, query: int = 30, **kwargs: Any) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = kwargs.pop("template_url", "/parameterGrouping/postOptional")

    # Construct parameters
    if query is not None:
        _params["query"] = _SERIALIZER.query("query", query, "int")

    # Construct headers
    if custom_header is not None:
        _headers["customHeader"] = _SERIALIZER.header("custom_header", custom_header, "str")
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="POST", url=_url, params=_params, headers=_headers, **kwargs)


def build_post_reserved_words_request(
    *, from_parameter: Optional[str] = None, accept_parameter: Optional[str] = None, **kwargs: Any
) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = kwargs.pop("template_url", "/parameterGrouping/postReservedWords")

    # Construct parameters
    if from_parameter is not None:
        _params["from"] = _SERIALIZER.query("from_parameter", from_parameter, "str")
    if accept_parameter is not None:
        _params["accept"] = _SERIALIZER.query("accept_parameter", accept_parameter, "str")

    # Construct headers
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="POST", url=_url, params=_params, headers=_headers, **kwargs)


def build_post_multi_param_groups_request(
    *,
    header_one: Optional[str] = None,
    query_one: int = 30,
    header_two: Optional[str] = None,
    query_two: int = 30,
    **kwargs: Any
) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = kwargs.pop("template_url", "/parameterGrouping/postMultipleParameterGroups")

    # Construct parameters
    if query_one is not None:
        _params["query-one"] = _SERIALIZER.query("query_one", query_one, "int")
    if query_two is not None:
        _params["query-two"] = _SERIALIZER.query("query_two", query_two, "int")

    # Construct headers
    if header_one is not None:
        _headers["header-one"] = _SERIALIZER.header("header_one", header_one, "str")
    if header_two is not None:
        _headers["header-two"] = _SERIALIZER.header("header_two", header_two, "str")
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="POST", url=_url, params=_params, headers=_headers, **kwargs)


def build_post_shared_parameter_group_object_request(  # pylint: disable=name-too-long
    *, header_one: Optional[str] = None, query_one: int = 30, **kwargs: Any
) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = kwargs.pop("template_url", "/parameterGrouping/sharedParameterGroupObject")

    # Construct parameters
    if query_one is not None:
        _params["query-one"] = _SERIALIZER.query("query_one", query_one, "int")

    # Construct headers
    if header_one is not None:
        _headers["header-one"] = _SERIALIZER.header("header_one", header_one, "str")
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="POST", url=_url, params=_params, headers=_headers, **kwargs)


def build_group_with_constant_request(
    *, grouped_constant: Literal["foo"] = "foo", grouped_parameter: Optional[str] = None, **kwargs: Any
) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})

    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = kwargs.pop("template_url", "/parameterGrouping/groupWithConstant")

    # Construct headers
    if grouped_constant is not None:
        _headers["groupedConstant"] = _SERIALIZER.header("grouped_constant", grouped_constant, "str")
    if grouped_parameter is not None:
        _headers["groupedParameter"] = _SERIALIZER.header("grouped_parameter", grouped_parameter, "str")
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="PUT", url=_url, headers=_headers, **kwargs)


class ParameterGroupingOperations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~azureparametergrouping.AutoRestParameterGroupingTestService`'s
        :attr:`parameter_grouping` attribute.
    """

    models = _models

    def __init__(self, *args, **kwargs):
        input_args = list(args)
        self._client = input_args.pop(0) if input_args else kwargs.pop("client")
        self._config = input_args.pop(0) if input_args else kwargs.pop("config")
        self._serialize = input_args.pop(0) if input_args else kwargs.pop("serializer")
        self._deserialize = input_args.pop(0) if input_args else kwargs.pop("deserializer")

    @distributed_trace
    def post_required(  # pylint: disable=inconsistent-return-statements
        self,
        parameter_grouping_post_required_parameters: _models.ParameterGroupingPostRequiredParameters,
        **kwargs: Any
    ) -> None:
        """Post a bunch of required parameters grouped.

        :param parameter_grouping_post_required_parameters: Parameter group. Required.
        :type parameter_grouping_post_required_parameters:
         ~azureparametergrouping.models.ParameterGroupingPostRequiredParameters
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None or the result of cls(response)
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = kwargs.pop("params", {}) or {}

        content_type: str = kwargs.pop("content_type", _headers.pop("Content-Type", "application/json"))
        cls: ClsType[None] = kwargs.pop("cls", None)

        _custom_header = None
        _query = None
        _path = None
        _body = None
        if parameter_grouping_post_required_parameters is not None:
            _body = parameter_grouping_post_required_parameters.body
            _custom_header = parameter_grouping_post_required_parameters.custom_header
            _path = parameter_grouping_post_required_parameters.path
            _query = parameter_grouping_post_required_parameters.query
        _json = self._serialize.body(_body, "int")

        request = build_post_required_request(
            path=_path,
            custom_header=_custom_header,
            query=_query,
            content_type=content_type,
            json=_json,
            template_url=self.post_required.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        _stream = False
        pipeline_response: PipelineResponse = self._client._pipeline.run(  # pylint: disable=protected-access
            request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, pipeline_response)
            raise HttpResponseError(response=response, model=error)

        if cls:
            return cls(pipeline_response, None, {})

    post_required.metadata = {"url": "/parameterGrouping/postRequired/{path}"}

    @distributed_trace
    def post_optional(  # pylint: disable=inconsistent-return-statements
        self,
        parameter_grouping_post_optional_parameters: Optional[_models.ParameterGroupingPostOptionalParameters] = None,
        **kwargs: Any
    ) -> None:
        """Post a bunch of optional parameters grouped.

        :param parameter_grouping_post_optional_parameters: Parameter group. Default value is None.
        :type parameter_grouping_post_optional_parameters:
         ~azureparametergrouping.models.ParameterGroupingPostOptionalParameters
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None or the result of cls(response)
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
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

        _custom_header = None
        _query = None
        if parameter_grouping_post_optional_parameters is not None:
            _custom_header = parameter_grouping_post_optional_parameters.custom_header
            _query = parameter_grouping_post_optional_parameters.query

        request = build_post_optional_request(
            custom_header=_custom_header,
            query=_query,  # type: ignore
            template_url=self.post_optional.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        _stream = False
        pipeline_response: PipelineResponse = self._client._pipeline.run(  # pylint: disable=protected-access
            request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, pipeline_response)
            raise HttpResponseError(response=response, model=error)

        if cls:
            return cls(pipeline_response, None, {})

    post_optional.metadata = {"url": "/parameterGrouping/postOptional"}

    @distributed_trace
    def post_reserved_words(  # pylint: disable=inconsistent-return-statements
        self,
        parameter_grouping_post_reserved_words_parameters: Optional[
            _models.ParameterGroupingPostReservedWordsParameters
        ] = None,
        **kwargs: Any
    ) -> None:
        """Post a grouped parameters with reserved words.

        :param parameter_grouping_post_reserved_words_parameters: Parameter group. Default value is
         None.
        :type parameter_grouping_post_reserved_words_parameters:
         ~azureparametergrouping.models.ParameterGroupingPostReservedWordsParameters
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None or the result of cls(response)
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
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

        _from_parameter = None
        _accept_parameter = None
        if parameter_grouping_post_reserved_words_parameters is not None:
            _accept_parameter = parameter_grouping_post_reserved_words_parameters.accept
            _from_parameter = parameter_grouping_post_reserved_words_parameters.from_property

        request = build_post_reserved_words_request(
            from_parameter=_from_parameter,
            accept_parameter=_accept_parameter,
            template_url=self.post_reserved_words.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        _stream = False
        pipeline_response: PipelineResponse = self._client._pipeline.run(  # pylint: disable=protected-access
            request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, pipeline_response)
            raise HttpResponseError(response=response, model=error)

        if cls:
            return cls(pipeline_response, None, {})

    post_reserved_words.metadata = {"url": "/parameterGrouping/postReservedWords"}

    @distributed_trace
    def post_multi_param_groups(  # pylint: disable=inconsistent-return-statements
        self,
        first_parameter_group: Optional[_models.FirstParameterGroup] = None,
        parameter_grouping_post_multi_param_groups_second_param_group: Optional[
            _models.ParameterGroupingPostMultiParamGroupsSecondParamGroup
        ] = None,
        **kwargs: Any
    ) -> None:
        """Post parameters from multiple different parameter groups.

        :param first_parameter_group: Parameter group. Default value is None.
        :type first_parameter_group: ~azureparametergrouping.models.FirstParameterGroup
        :param parameter_grouping_post_multi_param_groups_second_param_group: Parameter group. Default
         value is None.
        :type parameter_grouping_post_multi_param_groups_second_param_group:
         ~azureparametergrouping.models.ParameterGroupingPostMultiParamGroupsSecondParamGroup
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None or the result of cls(response)
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
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

        _header_one = None
        _query_one = None
        _header_two = None
        _query_two = None
        if first_parameter_group is not None:
            _header_one = first_parameter_group.header_one
            _query_one = first_parameter_group.query_one
        if parameter_grouping_post_multi_param_groups_second_param_group is not None:
            _header_two = parameter_grouping_post_multi_param_groups_second_param_group.header_two
            _query_two = parameter_grouping_post_multi_param_groups_second_param_group.query_two

        request = build_post_multi_param_groups_request(
            header_one=_header_one,
            query_one=_query_one,  # type: ignore
            header_two=_header_two,
            query_two=_query_two,  # type: ignore
            template_url=self.post_multi_param_groups.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        _stream = False
        pipeline_response: PipelineResponse = self._client._pipeline.run(  # pylint: disable=protected-access
            request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, pipeline_response)
            raise HttpResponseError(response=response, model=error)

        if cls:
            return cls(pipeline_response, None, {})

    post_multi_param_groups.metadata = {"url": "/parameterGrouping/postMultipleParameterGroups"}

    @distributed_trace
    def post_shared_parameter_group_object(  # pylint: disable=inconsistent-return-statements
        self, first_parameter_group: Optional[_models.FirstParameterGroup] = None, **kwargs: Any
    ) -> None:
        """Post parameters with a shared parameter group object.

        :param first_parameter_group: Parameter group. Default value is None.
        :type first_parameter_group: ~azureparametergrouping.models.FirstParameterGroup
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None or the result of cls(response)
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
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

        _header_one = None
        _query_one = None
        if first_parameter_group is not None:
            _header_one = first_parameter_group.header_one
            _query_one = first_parameter_group.query_one

        request = build_post_shared_parameter_group_object_request(
            header_one=_header_one,
            query_one=_query_one,  # type: ignore
            template_url=self.post_shared_parameter_group_object.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        _stream = False
        pipeline_response: PipelineResponse = self._client._pipeline.run(  # pylint: disable=protected-access
            request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, pipeline_response)
            raise HttpResponseError(response=response, model=error)

        if cls:
            return cls(pipeline_response, None, {})

    post_shared_parameter_group_object.metadata = {"url": "/parameterGrouping/sharedParameterGroupObject"}

    @distributed_trace
    def group_with_constant(  # pylint: disable=inconsistent-return-statements
        self, grouper: Optional[_models.Grouper] = None, **kwargs: Any
    ) -> None:
        """Parameter group with a constant. Pass in 'foo' for groupedConstant and 'bar' for
        groupedParameter.

        :param grouper: Parameter group. Default value is None.
        :type grouper: ~azureparametergrouping.models.Grouper
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None or the result of cls(response)
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
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

        _grouped_constant = None
        _grouped_parameter = None
        if grouper is not None:
            _grouped_constant = grouper.grouped_constant
            _grouped_parameter = grouper.grouped_parameter

        request = build_group_with_constant_request(
            grouped_constant=_grouped_constant,  # type: ignore
            grouped_parameter=_grouped_parameter,
            template_url=self.group_with_constant.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        _stream = False
        pipeline_response: PipelineResponse = self._client._pipeline.run(  # pylint: disable=protected-access
            request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.Error, pipeline_response)
            raise HttpResponseError(response=response, model=error)

        if cls:
            return cls(pipeline_response, None, {})

    group_with_constant.metadata = {"url": "/parameterGrouping/groupWithConstant"}
