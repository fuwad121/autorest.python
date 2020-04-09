# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from typing import TYPE_CHECKING

from azure.core import PipelineClient
from msrest import Deserializer, Serializer

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from typing import Any, Optional

from ._configuration import NonStringEnumsClientConfiguration
from .operations import IntOperations
from .operations import FloatOperations


class NonStringEnumsClient(object):
    """Testing non-string enums.

    :ivar int: IntOperations operations
    :vartype int: nonstringenums.operations.IntOperations
    :ivar float: FloatOperations operations
    :vartype float: nonstringenums.operations.FloatOperations
    :param str base_url: Service URL
    """

    def __init__(
        self,
        base_url=None,  # type: Optional[str]
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        if not base_url:
            base_url = 'http://localhost:3000'
        self._config = NonStringEnumsClientConfiguration(**kwargs)
        self._client = PipelineClient(base_url=base_url, config=self._config, **kwargs)

        client_models = {}
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

        self.int = IntOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.float = FloatOperations(
            self._client, self._config, self._serialize, self._deserialize)

    def close(self):
        # type: () -> None
        self._client.close()

    def __enter__(self):
        # type: () -> NonStringEnumsClient
        self._client.__enter__()
        return self

    def __exit__(self, *exc_details):
        # type: (Any) -> None
        self._client.__exit__(*exc_details)