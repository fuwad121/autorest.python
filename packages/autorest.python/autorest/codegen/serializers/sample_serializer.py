# pylint: disable=too-many-lines
# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
import logging
from typing import Dict, Any
from jinja2 import Environment

from autorest.codegen.models.credential_types import AzureKeyCredentialType
from autorest.codegen.models.credential_types import TokenCredentialType
from autorest.codegen.models.imports import FileImport, ImportType
from autorest.codegen.models.operation import OperationBase
from autorest.codegen.models.operation_group import OperationGroup
from autorest.codegen.serializers.import_serializer import FileImportSerializer
from ..models import CodeModel

_LOGGER = logging.getLogger(__name__)


class SampleSerializer:
    def __init__(
        self,
        code_model: CodeModel,
        env: Environment,
        operation_group: OperationGroup,
        operation: OperationBase[Any],
        sample: Dict[str, Any],
        file_name: str,
        sample_origin_name: str,
    ) -> None:
        self.code_model = code_model
        self.env = env
        self.operation_group = operation_group
        self.operation = operation
        self.sample = sample
        self.file_name = file_name
        self.sample_origin_name = sample_origin_name

    def _imports(self) -> FileImportSerializer:
        imports = FileImport()
        namespace = (self.code_model.options["package_name"] or "").replace(
            "-", "."
        ) or self.code_model.namespace
        client = self.code_model.clients[0]
        imports.add_submodule_import(namespace, client.name, ImportType.THIRDPARTY)
        credential_type = getattr(client.credential, "type", None)
        if isinstance(credential_type, TokenCredentialType):
            imports.add_submodule_import(
                "azure.identity", "DefaultAzureCredential", ImportType.THIRDPARTY
            )
        elif isinstance(credential_type, AzureKeyCredentialType):
            imports.add_import("os", ImportType.STDLIB)
            imports.add_submodule_import(
                "azure.core.credentials", "AzureKeyCredential", ImportType.THIRDPARTY
            )
        return FileImportSerializer(imports, True)

    def _client_params(self) -> Dict[str, Any]:
        # client params
        special_param = dict()
        credential_type = getattr(self.code_model.clients[0].credential, "type", None)
        if isinstance(credential_type, TokenCredentialType):
            special_param.update({"credential": "DefaultAzureCredential()"})
        elif isinstance(credential_type, AzureKeyCredentialType):
            special_param.update(
                {"credential": 'AzureKeyCredential(key=os.getenv("AZURE_KEY"))'}
            )

        params_positional = [
            p
            for p in self.code_model.clients[0].parameters.positional
            if not (p.optional or p.client_default_value)
        ]
        cls = lambda x: f'"{x}"'
        client_params = {
            p.client_name: special_param.get(
                p.client_name,
                cls(
                    self.sample["parameters"].get(p.rest_api_name)
                    or p.client_name.upper()
                ),
            )
            for p in params_positional
        }

        return client_params

    # prepare operation parameters
    def _operation_params(self) -> Dict[str, Any]:
        params_positional = [
            p
            for p in self.operation.parameters.positional
            if not p.client_default_value
        ]
        cls = lambda x: f'"{x}"' if isinstance(x, str) else str(x)
        failure_info = "fail to find required param named {} in example file {}"
        operation_params = {}
        for param in params_positional:
            name = param.rest_api_name
            param_value = self.sample["parameters"].get(name)
            if not param.optional:
                if not param_value:
                    raise Exception(failure_info.format(name, self.sample_origin_name))
                operation_params[param.client_name] = cls(param_value)
        return operation_params

    def _operation_group_name(self) -> str:
        if self.operation_group.is_mixin:
            return ""
        return f".{self.operation_group.property_name}"

    def _operation_result(self) -> str:
        lro = ".result()"
        paging = "\n    for item in response:\n        print(item)"
        normal_print = "\n    print(response)"
        if self.operation.operation_type == "paging":
            return paging
        if self.operation.operation_type == "lro":
            return lro + normal_print
        if self.operation.operation_type == "lropaging":
            return lro + paging
        return normal_print

    def _operation_name(self) -> str:
        return f".{self.operation.name}"

    def _origin_file(self) -> str:
        name = self.sample.get("x-ms-original-file", "").split("specification")[-1]
        return "specification" + name if name else name

    def serialize(self) -> str:
        return self.env.get_template("sample.py.jinja2").render(
            code_model=self.code_model,
            file_name=self.file_name,
            operation_result=self._operation_result(),
            operation_params=self._operation_params(),
            operation_group_name=self._operation_group_name(),
            operation_name=self._operation_name(),
            imports=self._imports(),
            client_params=self._client_params(),
            origin_file=self._origin_file(),
        )