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

from msrest.pipeline import ClientRawResponse

from .. import models


class DictionaryOperations(object):
    """DictionaryOperations operations.

    You should not instantiate directly this class, but create a Client instance that will create it for you and attach it as attribute.

    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    """

    models = models

    def __init__(self, client, config, serializer, deserializer):

        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer

        self._config = config

    def get_valid(
            self, raw=False, **kwargs):
        """Get complex types with dictionary property.

        :param bool raw: returns the direct response alongside the
         deserialized response
        :return: DictionaryWrapper or ClientRawResponse if raw=true
        :rtype: ~bodycomplex.models.DictionaryWrapper or
         ~msrest.pipeline.ClientRawResponse
        :raises: :class:`ErrorException<bodycomplex.models.ErrorException>`
        """
        # Construct URL
        url = self.get_valid.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'
        headers = kwargs.get('headers')
        if headers:
            header_parameters.update(headers)

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request)
        response = pipeline_response.http_response.internal_response

        if response.status_code not in [200]:
            raise models.ErrorException(self._deserialize, response)

        deserialized = None
        if response.status_code == 200:
            deserialized = self._deserialize('DictionaryWrapper', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    get_valid.metadata = {'url': '/complex/dictionary/typed/valid'}

    def put_valid(
            self, default_program=None, raw=False, **kwargs):
        """Put complex types with dictionary property.

        :param default_program:
        :type default_program: dict[str, str]
        :param bool raw: returns the direct response alongside the
         deserialized response
        :return: None or ClientRawResponse if raw=true
        :rtype: None or ~msrest.pipeline.ClientRawResponse
        :raises: :class:`ErrorException<bodycomplex.models.ErrorException>`
        """
        complex_body = models.DictionaryWrapper(default_program=default_program)

        # Construct URL
        url = self.put_valid.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        headers = kwargs.get('headers')
        if headers:
            header_parameters.update(headers)

        # Construct body
        body_content = self._serialize.body(complex_body, 'DictionaryWrapper')

        # Construct and send request
        request = self._client.put(url, query_parameters, header_parameters, body_content)
        pipeline_response = self._client._pipeline.run(request)
        response = pipeline_response.http_response.internal_response

        if response.status_code not in [200]:
            raise models.ErrorException(self._deserialize, response)

        if raw:
            client_raw_response = ClientRawResponse(None, response)
            return client_raw_response
    put_valid.metadata = {'url': '/complex/dictionary/typed/valid'}

    def get_empty(
            self, raw=False, **kwargs):
        """Get complex types with dictionary property which is empty.

        :param bool raw: returns the direct response alongside the
         deserialized response
        :return: DictionaryWrapper or ClientRawResponse if raw=true
        :rtype: ~bodycomplex.models.DictionaryWrapper or
         ~msrest.pipeline.ClientRawResponse
        :raises: :class:`ErrorException<bodycomplex.models.ErrorException>`
        """
        # Construct URL
        url = self.get_empty.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'
        headers = kwargs.get('headers')
        if headers:
            header_parameters.update(headers)

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request)
        response = pipeline_response.http_response.internal_response

        if response.status_code not in [200]:
            raise models.ErrorException(self._deserialize, response)

        deserialized = None
        if response.status_code == 200:
            deserialized = self._deserialize('DictionaryWrapper', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    get_empty.metadata = {'url': '/complex/dictionary/typed/empty'}

    def put_empty(
            self, default_program=None, raw=False, **kwargs):
        """Put complex types with dictionary property which is empty.

        :param default_program:
        :type default_program: dict[str, str]
        :param bool raw: returns the direct response alongside the
         deserialized response
        :return: None or ClientRawResponse if raw=true
        :rtype: None or ~msrest.pipeline.ClientRawResponse
        :raises: :class:`ErrorException<bodycomplex.models.ErrorException>`
        """
        complex_body = models.DictionaryWrapper(default_program=default_program)

        # Construct URL
        url = self.put_empty.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        headers = kwargs.get('headers')
        if headers:
            header_parameters.update(headers)

        # Construct body
        body_content = self._serialize.body(complex_body, 'DictionaryWrapper')

        # Construct and send request
        request = self._client.put(url, query_parameters, header_parameters, body_content)
        pipeline_response = self._client._pipeline.run(request)
        response = pipeline_response.http_response.internal_response

        if response.status_code not in [200]:
            raise models.ErrorException(self._deserialize, response)

        if raw:
            client_raw_response = ClientRawResponse(None, response)
            return client_raw_response
    put_empty.metadata = {'url': '/complex/dictionary/typed/empty'}

    def get_null(
            self, raw=False, **kwargs):
        """Get complex types with dictionary property which is null.

        :param bool raw: returns the direct response alongside the
         deserialized response
        :return: DictionaryWrapper or ClientRawResponse if raw=true
        :rtype: ~bodycomplex.models.DictionaryWrapper or
         ~msrest.pipeline.ClientRawResponse
        :raises: :class:`ErrorException<bodycomplex.models.ErrorException>`
        """
        # Construct URL
        url = self.get_null.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'
        headers = kwargs.get('headers')
        if headers:
            header_parameters.update(headers)

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request)
        response = pipeline_response.http_response.internal_response

        if response.status_code not in [200]:
            raise models.ErrorException(self._deserialize, response)

        deserialized = None
        if response.status_code == 200:
            deserialized = self._deserialize('DictionaryWrapper', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    get_null.metadata = {'url': '/complex/dictionary/typed/null'}

    def get_not_provided(
            self, raw=False, **kwargs):
        """Get complex types with dictionary property while server doesn't provide
        a response payload.

        :param bool raw: returns the direct response alongside the
         deserialized response
        :return: DictionaryWrapper or ClientRawResponse if raw=true
        :rtype: ~bodycomplex.models.DictionaryWrapper or
         ~msrest.pipeline.ClientRawResponse
        :raises: :class:`ErrorException<bodycomplex.models.ErrorException>`
        """
        # Construct URL
        url = self.get_not_provided.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'
        headers = kwargs.get('headers')
        if headers:
            header_parameters.update(headers)

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request)
        response = pipeline_response.http_response.internal_response

        if response.status_code not in [200]:
            raise models.ErrorException(self._deserialize, response)

        deserialized = None
        if response.status_code == 200:
            deserialized = self._deserialize('DictionaryWrapper', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    get_not_provided.metadata = {'url': '/complex/dictionary/typed/notprovided'}
