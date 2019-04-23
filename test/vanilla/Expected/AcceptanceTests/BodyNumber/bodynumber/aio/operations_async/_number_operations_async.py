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

from ... import models


class NumberOperations:
    """NumberOperations async operations.

    You should not instantiate directly this class, but create a Client instance that will create it for you and attach it as attribute.

    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    """

    models = models

    def __init__(self, client, config, serializer, deserializer) -> None:

        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer

        self._config = config

    async def get_null(
            self, *, raw=False, **kwargs):
        """Get null Number value.

        :param bool raw: returns the direct response alongside the
         deserialized response
        :return: float or ClientRawResponse if raw=true
        :rtype: float or ~msrest.pipeline.ClientRawResponse
        :raises: :class:`ErrorException<bodynumber.models.ErrorException>`
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
        pipeline_response = await self._client._pipeline.run(request)
        response = pipeline_response.http_response.internal_response

        if response.status_code not in [200]:
            raise models.ErrorException(self._deserialize, response)

        deserialized = None
        if response.status_code == 200:
            deserialized = self._deserialize('float', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    get_null.metadata = {'url': '/number/null'}

    async def get_invalid_float(
            self, *, raw=False, **kwargs):
        """Get invalid float Number value.

        :param bool raw: returns the direct response alongside the
         deserialized response
        :return: float or ClientRawResponse if raw=true
        :rtype: float or ~msrest.pipeline.ClientRawResponse
        :raises: :class:`ErrorException<bodynumber.models.ErrorException>`
        """
        # Construct URL
        url = self.get_invalid_float.metadata['url']

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
        pipeline_response = await self._client._pipeline.run(request)
        response = pipeline_response.http_response.internal_response

        if response.status_code not in [200]:
            raise models.ErrorException(self._deserialize, response)

        deserialized = None
        if response.status_code == 200:
            deserialized = self._deserialize('float', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    get_invalid_float.metadata = {'url': '/number/invalidfloat'}

    async def get_invalid_double(
            self, *, raw=False, **kwargs):
        """Get invalid double Number value.

        :param bool raw: returns the direct response alongside the
         deserialized response
        :return: float or ClientRawResponse if raw=true
        :rtype: float or ~msrest.pipeline.ClientRawResponse
        :raises: :class:`ErrorException<bodynumber.models.ErrorException>`
        """
        # Construct URL
        url = self.get_invalid_double.metadata['url']

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
        pipeline_response = await self._client._pipeline.run(request)
        response = pipeline_response.http_response.internal_response

        if response.status_code not in [200]:
            raise models.ErrorException(self._deserialize, response)

        deserialized = None
        if response.status_code == 200:
            deserialized = self._deserialize('float', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    get_invalid_double.metadata = {'url': '/number/invaliddouble'}

    async def get_invalid_decimal(
            self, *, raw=False, **kwargs):
        """Get invalid decimal Number value.

        :param bool raw: returns the direct response alongside the
         deserialized response
        :return: decimal.Decimal or ClientRawResponse if raw=true
        :rtype: decimal.Decimal or ~msrest.pipeline.ClientRawResponse
        :raises: :class:`ErrorException<bodynumber.models.ErrorException>`
        """
        # Construct URL
        url = self.get_invalid_decimal.metadata['url']

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
        pipeline_response = await self._client._pipeline.run(request)
        response = pipeline_response.http_response.internal_response

        if response.status_code not in [200]:
            raise models.ErrorException(self._deserialize, response)

        deserialized = None
        if response.status_code == 200:
            deserialized = self._deserialize('decimal', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    get_invalid_decimal.metadata = {'url': '/number/invaliddecimal'}

    async def put_big_float(
            self, number_body, *, raw=False, **kwargs):
        """Put big float value 3.402823e+20.

        :param number_body:
        :type number_body: float
        :param bool raw: returns the direct response alongside the
         deserialized response
        :return: None or ClientRawResponse if raw=true
        :rtype: None or ~msrest.pipeline.ClientRawResponse
        :raises: :class:`ErrorException<bodynumber.models.ErrorException>`
        """
        # Construct URL
        url = self.put_big_float.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        headers = kwargs.get('headers')
        if headers:
            header_parameters.update(headers)

        # Construct body
        body_content = self._serialize.body(number_body, 'float')

        # Construct and send request
        request = self._client.put(url, query_parameters, header_parameters, body_content)
        pipeline_response = await self._client._pipeline.run(request)
        response = pipeline_response.http_response.internal_response

        if response.status_code not in [200]:
            raise models.ErrorException(self._deserialize, response)

        if raw:
            client_raw_response = ClientRawResponse(None, response)
            return client_raw_response
    put_big_float.metadata = {'url': '/number/big/float/3.402823e+20'}

    async def get_big_float(
            self, *, raw=False, **kwargs):
        """Get big float value 3.402823e+20.

        :param bool raw: returns the direct response alongside the
         deserialized response
        :return: float or ClientRawResponse if raw=true
        :rtype: float or ~msrest.pipeline.ClientRawResponse
        :raises: :class:`ErrorException<bodynumber.models.ErrorException>`
        """
        # Construct URL
        url = self.get_big_float.metadata['url']

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
        pipeline_response = await self._client._pipeline.run(request)
        response = pipeline_response.http_response.internal_response

        if response.status_code not in [200]:
            raise models.ErrorException(self._deserialize, response)

        deserialized = None
        if response.status_code == 200:
            deserialized = self._deserialize('float', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    get_big_float.metadata = {'url': '/number/big/float/3.402823e+20'}

    async def put_big_double(
            self, number_body, *, raw=False, **kwargs):
        """Put big double value 2.5976931e+101.

        :param number_body:
        :type number_body: float
        :param bool raw: returns the direct response alongside the
         deserialized response
        :return: None or ClientRawResponse if raw=true
        :rtype: None or ~msrest.pipeline.ClientRawResponse
        :raises: :class:`ErrorException<bodynumber.models.ErrorException>`
        """
        # Construct URL
        url = self.put_big_double.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        headers = kwargs.get('headers')
        if headers:
            header_parameters.update(headers)

        # Construct body
        body_content = self._serialize.body(number_body, 'float')

        # Construct and send request
        request = self._client.put(url, query_parameters, header_parameters, body_content)
        pipeline_response = await self._client._pipeline.run(request)
        response = pipeline_response.http_response.internal_response

        if response.status_code not in [200]:
            raise models.ErrorException(self._deserialize, response)

        if raw:
            client_raw_response = ClientRawResponse(None, response)
            return client_raw_response
    put_big_double.metadata = {'url': '/number/big/double/2.5976931e+101'}

    async def get_big_double(
            self, *, raw=False, **kwargs):
        """Get big double value 2.5976931e+101.

        :param bool raw: returns the direct response alongside the
         deserialized response
        :return: float or ClientRawResponse if raw=true
        :rtype: float or ~msrest.pipeline.ClientRawResponse
        :raises: :class:`ErrorException<bodynumber.models.ErrorException>`
        """
        # Construct URL
        url = self.get_big_double.metadata['url']

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
        pipeline_response = await self._client._pipeline.run(request)
        response = pipeline_response.http_response.internal_response

        if response.status_code not in [200]:
            raise models.ErrorException(self._deserialize, response)

        deserialized = None
        if response.status_code == 200:
            deserialized = self._deserialize('float', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    get_big_double.metadata = {'url': '/number/big/double/2.5976931e+101'}

    async def put_big_double_positive_decimal(
            self, *, raw=False, **kwargs):
        """Put big double value 99999999.99.

        :param bool raw: returns the direct response alongside the
         deserialized response
        :return: None or ClientRawResponse if raw=true
        :rtype: None or ~msrest.pipeline.ClientRawResponse
        :raises: :class:`ErrorException<bodynumber.models.ErrorException>`
        """
        number_body = 99999999.99

        # Construct URL
        url = self.put_big_double_positive_decimal.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        headers = kwargs.get('headers')
        if headers:
            header_parameters.update(headers)

        # Construct body
        body_content = self._serialize.body(number_body, 'float')

        # Construct and send request
        request = self._client.put(url, query_parameters, header_parameters, body_content)
        pipeline_response = await self._client._pipeline.run(request)
        response = pipeline_response.http_response.internal_response

        if response.status_code not in [200]:
            raise models.ErrorException(self._deserialize, response)

        if raw:
            client_raw_response = ClientRawResponse(None, response)
            return client_raw_response
    put_big_double_positive_decimal.metadata = {'url': '/number/big/double/99999999.99'}

    async def get_big_double_positive_decimal(
            self, *, raw=False, **kwargs):
        """Get big double value 99999999.99.

        :param bool raw: returns the direct response alongside the
         deserialized response
        :return: float or ClientRawResponse if raw=true
        :rtype: float or ~msrest.pipeline.ClientRawResponse
        :raises: :class:`ErrorException<bodynumber.models.ErrorException>`
        """
        # Construct URL
        url = self.get_big_double_positive_decimal.metadata['url']

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
        pipeline_response = await self._client._pipeline.run(request)
        response = pipeline_response.http_response.internal_response

        if response.status_code not in [200]:
            raise models.ErrorException(self._deserialize, response)

        deserialized = None
        if response.status_code == 200:
            deserialized = self._deserialize('float', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    get_big_double_positive_decimal.metadata = {'url': '/number/big/double/99999999.99'}

    async def put_big_double_negative_decimal(
            self, *, raw=False, **kwargs):
        """Put big double value -99999999.99.

        :param bool raw: returns the direct response alongside the
         deserialized response
        :return: None or ClientRawResponse if raw=true
        :rtype: None or ~msrest.pipeline.ClientRawResponse
        :raises: :class:`ErrorException<bodynumber.models.ErrorException>`
        """
        number_body = -99999999.99

        # Construct URL
        url = self.put_big_double_negative_decimal.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        headers = kwargs.get('headers')
        if headers:
            header_parameters.update(headers)

        # Construct body
        body_content = self._serialize.body(number_body, 'float')

        # Construct and send request
        request = self._client.put(url, query_parameters, header_parameters, body_content)
        pipeline_response = await self._client._pipeline.run(request)
        response = pipeline_response.http_response.internal_response

        if response.status_code not in [200]:
            raise models.ErrorException(self._deserialize, response)

        if raw:
            client_raw_response = ClientRawResponse(None, response)
            return client_raw_response
    put_big_double_negative_decimal.metadata = {'url': '/number/big/double/-99999999.99'}

    async def get_big_double_negative_decimal(
            self, *, raw=False, **kwargs):
        """Get big double value -99999999.99.

        :param bool raw: returns the direct response alongside the
         deserialized response
        :return: float or ClientRawResponse if raw=true
        :rtype: float or ~msrest.pipeline.ClientRawResponse
        :raises: :class:`ErrorException<bodynumber.models.ErrorException>`
        """
        # Construct URL
        url = self.get_big_double_negative_decimal.metadata['url']

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
        pipeline_response = await self._client._pipeline.run(request)
        response = pipeline_response.http_response.internal_response

        if response.status_code not in [200]:
            raise models.ErrorException(self._deserialize, response)

        deserialized = None
        if response.status_code == 200:
            deserialized = self._deserialize('float', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    get_big_double_negative_decimal.metadata = {'url': '/number/big/double/-99999999.99'}

    async def put_big_decimal(
            self, number_body, *, raw=False, **kwargs):
        """Put big decimal value 2.5976931e+101.

        :param number_body:
        :type number_body: decimal.Decimal
        :param bool raw: returns the direct response alongside the
         deserialized response
        :return: None or ClientRawResponse if raw=true
        :rtype: None or ~msrest.pipeline.ClientRawResponse
        :raises: :class:`ErrorException<bodynumber.models.ErrorException>`
        """
        # Construct URL
        url = self.put_big_decimal.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        headers = kwargs.get('headers')
        if headers:
            header_parameters.update(headers)

        # Construct body
        body_content = self._serialize.body(number_body, 'decimal')

        # Construct and send request
        request = self._client.put(url, query_parameters, header_parameters, body_content)
        pipeline_response = await self._client._pipeline.run(request)
        response = pipeline_response.http_response.internal_response

        if response.status_code not in [200]:
            raise models.ErrorException(self._deserialize, response)

        if raw:
            client_raw_response = ClientRawResponse(None, response)
            return client_raw_response
    put_big_decimal.metadata = {'url': '/number/big/decimal/2.5976931e+101'}

    async def get_big_decimal(
            self, *, raw=False, **kwargs):
        """Get big decimal value 2.5976931e+101.

        :param bool raw: returns the direct response alongside the
         deserialized response
        :return: decimal.Decimal or ClientRawResponse if raw=true
        :rtype: decimal.Decimal or ~msrest.pipeline.ClientRawResponse
        :raises: :class:`ErrorException<bodynumber.models.ErrorException>`
        """
        # Construct URL
        url = self.get_big_decimal.metadata['url']

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
        pipeline_response = await self._client._pipeline.run(request)
        response = pipeline_response.http_response.internal_response

        if response.status_code not in [200]:
            raise models.ErrorException(self._deserialize, response)

        deserialized = None
        if response.status_code == 200:
            deserialized = self._deserialize('decimal', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    get_big_decimal.metadata = {'url': '/number/big/decimal/2.5976931e+101'}

    async def put_big_decimal_positive_decimal(
            self, *, raw=False, **kwargs):
        """Put big decimal value 99999999.99.

        :param bool raw: returns the direct response alongside the
         deserialized response
        :return: None or ClientRawResponse if raw=true
        :rtype: None or ~msrest.pipeline.ClientRawResponse
        :raises: :class:`ErrorException<bodynumber.models.ErrorException>`
        """
        number_body = Decimal(99999999.99)

        # Construct URL
        url = self.put_big_decimal_positive_decimal.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        headers = kwargs.get('headers')
        if headers:
            header_parameters.update(headers)

        # Construct body
        body_content = self._serialize.body(number_body, 'decimal')

        # Construct and send request
        request = self._client.put(url, query_parameters, header_parameters, body_content)
        pipeline_response = await self._client._pipeline.run(request)
        response = pipeline_response.http_response.internal_response

        if response.status_code not in [200]:
            raise models.ErrorException(self._deserialize, response)

        if raw:
            client_raw_response = ClientRawResponse(None, response)
            return client_raw_response
    put_big_decimal_positive_decimal.metadata = {'url': '/number/big/decimal/99999999.99'}

    async def get_big_decimal_positive_decimal(
            self, *, raw=False, **kwargs):
        """Get big decimal value 99999999.99.

        :param bool raw: returns the direct response alongside the
         deserialized response
        :return: decimal.Decimal or ClientRawResponse if raw=true
        :rtype: decimal.Decimal or ~msrest.pipeline.ClientRawResponse
        :raises: :class:`ErrorException<bodynumber.models.ErrorException>`
        """
        # Construct URL
        url = self.get_big_decimal_positive_decimal.metadata['url']

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
        pipeline_response = await self._client._pipeline.run(request)
        response = pipeline_response.http_response.internal_response

        if response.status_code not in [200]:
            raise models.ErrorException(self._deserialize, response)

        deserialized = None
        if response.status_code == 200:
            deserialized = self._deserialize('decimal', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    get_big_decimal_positive_decimal.metadata = {'url': '/number/big/decimal/99999999.99'}

    async def put_big_decimal_negative_decimal(
            self, *, raw=False, **kwargs):
        """Put big decimal value -99999999.99.

        :param bool raw: returns the direct response alongside the
         deserialized response
        :return: None or ClientRawResponse if raw=true
        :rtype: None or ~msrest.pipeline.ClientRawResponse
        :raises: :class:`ErrorException<bodynumber.models.ErrorException>`
        """
        number_body = Decimal(-99999999.99)

        # Construct URL
        url = self.put_big_decimal_negative_decimal.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        headers = kwargs.get('headers')
        if headers:
            header_parameters.update(headers)

        # Construct body
        body_content = self._serialize.body(number_body, 'decimal')

        # Construct and send request
        request = self._client.put(url, query_parameters, header_parameters, body_content)
        pipeline_response = await self._client._pipeline.run(request)
        response = pipeline_response.http_response.internal_response

        if response.status_code not in [200]:
            raise models.ErrorException(self._deserialize, response)

        if raw:
            client_raw_response = ClientRawResponse(None, response)
            return client_raw_response
    put_big_decimal_negative_decimal.metadata = {'url': '/number/big/decimal/-99999999.99'}

    async def get_big_decimal_negative_decimal(
            self, *, raw=False, **kwargs):
        """Get big decimal value -99999999.99.

        :param bool raw: returns the direct response alongside the
         deserialized response
        :return: decimal.Decimal or ClientRawResponse if raw=true
        :rtype: decimal.Decimal or ~msrest.pipeline.ClientRawResponse
        :raises: :class:`ErrorException<bodynumber.models.ErrorException>`
        """
        # Construct URL
        url = self.get_big_decimal_negative_decimal.metadata['url']

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
        pipeline_response = await self._client._pipeline.run(request)
        response = pipeline_response.http_response.internal_response

        if response.status_code not in [200]:
            raise models.ErrorException(self._deserialize, response)

        deserialized = None
        if response.status_code == 200:
            deserialized = self._deserialize('decimal', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    get_big_decimal_negative_decimal.metadata = {'url': '/number/big/decimal/-99999999.99'}

    async def put_small_float(
            self, number_body, *, raw=False, **kwargs):
        """Put small float value 3.402823e-20.

        :param number_body:
        :type number_body: float
        :param bool raw: returns the direct response alongside the
         deserialized response
        :return: None or ClientRawResponse if raw=true
        :rtype: None or ~msrest.pipeline.ClientRawResponse
        :raises: :class:`ErrorException<bodynumber.models.ErrorException>`
        """
        # Construct URL
        url = self.put_small_float.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        headers = kwargs.get('headers')
        if headers:
            header_parameters.update(headers)

        # Construct body
        body_content = self._serialize.body(number_body, 'float')

        # Construct and send request
        request = self._client.put(url, query_parameters, header_parameters, body_content)
        pipeline_response = await self._client._pipeline.run(request)
        response = pipeline_response.http_response.internal_response

        if response.status_code not in [200]:
            raise models.ErrorException(self._deserialize, response)

        if raw:
            client_raw_response = ClientRawResponse(None, response)
            return client_raw_response
    put_small_float.metadata = {'url': '/number/small/float/3.402823e-20'}

    async def get_small_float(
            self, *, raw=False, **kwargs):
        """Get big double value 3.402823e-20.

        :param bool raw: returns the direct response alongside the
         deserialized response
        :return: float or ClientRawResponse if raw=true
        :rtype: float or ~msrest.pipeline.ClientRawResponse
        :raises: :class:`ErrorException<bodynumber.models.ErrorException>`
        """
        # Construct URL
        url = self.get_small_float.metadata['url']

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
        pipeline_response = await self._client._pipeline.run(request)
        response = pipeline_response.http_response.internal_response

        if response.status_code not in [200]:
            raise models.ErrorException(self._deserialize, response)

        deserialized = None
        if response.status_code == 200:
            deserialized = self._deserialize('float', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    get_small_float.metadata = {'url': '/number/small/float/3.402823e-20'}

    async def put_small_double(
            self, number_body, *, raw=False, **kwargs):
        """Put small double value 2.5976931e-101.

        :param number_body:
        :type number_body: float
        :param bool raw: returns the direct response alongside the
         deserialized response
        :return: None or ClientRawResponse if raw=true
        :rtype: None or ~msrest.pipeline.ClientRawResponse
        :raises: :class:`ErrorException<bodynumber.models.ErrorException>`
        """
        # Construct URL
        url = self.put_small_double.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        headers = kwargs.get('headers')
        if headers:
            header_parameters.update(headers)

        # Construct body
        body_content = self._serialize.body(number_body, 'float')

        # Construct and send request
        request = self._client.put(url, query_parameters, header_parameters, body_content)
        pipeline_response = await self._client._pipeline.run(request)
        response = pipeline_response.http_response.internal_response

        if response.status_code not in [200]:
            raise models.ErrorException(self._deserialize, response)

        if raw:
            client_raw_response = ClientRawResponse(None, response)
            return client_raw_response
    put_small_double.metadata = {'url': '/number/small/double/2.5976931e-101'}

    async def get_small_double(
            self, *, raw=False, **kwargs):
        """Get big double value 2.5976931e-101.

        :param bool raw: returns the direct response alongside the
         deserialized response
        :return: float or ClientRawResponse if raw=true
        :rtype: float or ~msrest.pipeline.ClientRawResponse
        :raises: :class:`ErrorException<bodynumber.models.ErrorException>`
        """
        # Construct URL
        url = self.get_small_double.metadata['url']

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
        pipeline_response = await self._client._pipeline.run(request)
        response = pipeline_response.http_response.internal_response

        if response.status_code not in [200]:
            raise models.ErrorException(self._deserialize, response)

        deserialized = None
        if response.status_code == 200:
            deserialized = self._deserialize('float', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    get_small_double.metadata = {'url': '/number/small/double/2.5976931e-101'}

    async def put_small_decimal(
            self, number_body, *, raw=False, **kwargs):
        """Put small decimal value 2.5976931e-101.

        :param number_body:
        :type number_body: decimal.Decimal
        :param bool raw: returns the direct response alongside the
         deserialized response
        :return: None or ClientRawResponse if raw=true
        :rtype: None or ~msrest.pipeline.ClientRawResponse
        :raises: :class:`ErrorException<bodynumber.models.ErrorException>`
        """
        # Construct URL
        url = self.put_small_decimal.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        headers = kwargs.get('headers')
        if headers:
            header_parameters.update(headers)

        # Construct body
        body_content = self._serialize.body(number_body, 'decimal')

        # Construct and send request
        request = self._client.put(url, query_parameters, header_parameters, body_content)
        pipeline_response = await self._client._pipeline.run(request)
        response = pipeline_response.http_response.internal_response

        if response.status_code not in [200]:
            raise models.ErrorException(self._deserialize, response)

        if raw:
            client_raw_response = ClientRawResponse(None, response)
            return client_raw_response
    put_small_decimal.metadata = {'url': '/number/small/decimal/2.5976931e-101'}

    async def get_small_decimal(
            self, *, raw=False, **kwargs):
        """Get small decimal value 2.5976931e-101.

        :param bool raw: returns the direct response alongside the
         deserialized response
        :return: decimal.Decimal or ClientRawResponse if raw=true
        :rtype: decimal.Decimal or ~msrest.pipeline.ClientRawResponse
        :raises: :class:`ErrorException<bodynumber.models.ErrorException>`
        """
        # Construct URL
        url = self.get_small_decimal.metadata['url']

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
        pipeline_response = await self._client._pipeline.run(request)
        response = pipeline_response.http_response.internal_response

        if response.status_code not in [200]:
            raise models.ErrorException(self._deserialize, response)

        deserialized = None
        if response.status_code == 200:
            deserialized = self._deserialize('decimal', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    get_small_decimal.metadata = {'url': '/number/small/decimal/2.5976931e-101'}
