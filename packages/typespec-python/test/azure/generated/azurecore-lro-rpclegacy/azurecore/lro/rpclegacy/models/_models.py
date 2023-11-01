# coding=utf-8
# pylint: disable=too-many-lines
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) Python Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from typing import Any, List, Mapping, Optional, TYPE_CHECKING, Union, overload

from .. import _model_base
from .._model_base import rest_field

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from .. import models as _models


class Error(_model_base.Model):
    """The error object.

    All required parameters must be populated in order to send to server.

    :ivar code: One of a server-defined set of error codes. Required.
    :vartype code: str
    :ivar message: A human-readable representation of the error. Required.
    :vartype message: str
    :ivar target: The target of the error.
    :vartype target: str
    :ivar details: An array of details about specific errors that led to this reported error.
    :vartype details: list[~azurecore.lro.rpclegacy.models.Error]
    :ivar innererror: An object containing more specific information than the current object about
     the error.
    :vartype innererror: ~azurecore.lro.rpclegacy.models.InnerError
    """

    code: str = rest_field()
    """One of a server-defined set of error codes. Required."""
    message: str = rest_field()
    """A human-readable representation of the error. Required."""
    target: Optional[str] = rest_field()
    """The target of the error."""
    details: Optional[List["_models.Error"]] = rest_field()
    """An array of details about specific errors that led to this reported error."""
    innererror: Optional["_models.InnerError"] = rest_field()
    """An object containing more specific information than the current object about the error."""

    @overload
    def __init__(
        self,
        *,
        code: str,
        message: str,
        target: Optional[str] = None,
        details: Optional[List["_models.Error"]] = None,
        innererror: Optional["_models.InnerError"] = None,
    ):
        ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]):
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:  # pylint: disable=useless-super-delegation
        super().__init__(*args, **kwargs)


class ErrorResponse(_model_base.Model):
    """A response containing error details.

    All required parameters must be populated in order to send to server.

    :ivar error: The error object. Required.
    :vartype error: ~azurecore.lro.rpclegacy.models.Error
    """

    error: "_models.Error" = rest_field()
    """The error object. Required."""

    @overload
    def __init__(
        self,
        *,
        error: "_models.Error",
    ):
        ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]):
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:  # pylint: disable=useless-super-delegation
        super().__init__(*args, **kwargs)


class InnerError(_model_base.Model):
    """An object containing more specific information about the error. As per Microsoft One API
    guidelines -
    https://github.com/Microsoft/api-guidelines/blob/vNext/Guidelines.md#7102-error-condition-responses.

    :ivar code: One of a server-defined set of error codes.
    :vartype code: str
    :ivar innererror: Inner error.
    :vartype innererror: ~azurecore.lro.rpclegacy.models.InnerError
    """

    code: Optional[str] = rest_field()
    """One of a server-defined set of error codes."""
    innererror: Optional["_models.InnerError"] = rest_field()
    """Inner error."""

    @overload
    def __init__(
        self,
        *,
        code: Optional[str] = None,
        innererror: Optional["_models.InnerError"] = None,
    ):
        ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]):
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:  # pylint: disable=useless-super-delegation
        super().__init__(*args, **kwargs)


class JobData(_model_base.Model):
    """Data of the job.

    All required parameters must be populated in order to send to server.

    :ivar comment: Comment. Required.
    :vartype comment: str
    """

    comment: str = rest_field()
    """Comment. Required."""

    @overload
    def __init__(
        self,
        *,
        comment: str,
    ):
        ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]):
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:  # pylint: disable=useless-super-delegation
        super().__init__(*args, **kwargs)


class JobResult(_model_base.Model):
    """Result of the job.

    Readonly variables are only populated by the server, and will be ignored when sending a request.

    All required parameters must be populated in order to send to server.

    :ivar job_id: A processing job identifier. Required.
    :vartype job_id: str
    :ivar comment: Comment. Required.
    :vartype comment: str
    :ivar status: The status of the processing job. Required. Known values are: "notStarted",
     "running", "succeeded", "failed", "canceled", and "partiallyCompleted".
    :vartype status: str or ~azurecore.lro.rpclegacy.models.JobStatus
    :ivar errors: Error objects that describes the error when status is "Failed".
    :vartype errors: list[~azurecore.lro.rpclegacy.models.ErrorResponse]
    :ivar results: The results.
    :vartype results: list[str]
    """

    job_id: str = rest_field(name="jobId", visibility=["read"])
    """A processing job identifier. Required."""
    comment: str = rest_field(visibility=["read"])
    """Comment. Required."""
    status: Union[str, "_models.JobStatus"] = rest_field(visibility=["read"])
    """The status of the processing job. Required. Known values are: \"notStarted\", \"running\",
     \"succeeded\", \"failed\", \"canceled\", and \"partiallyCompleted\"."""
    errors: Optional[List["_models.ErrorResponse"]] = rest_field(visibility=["read"])
    """Error objects that describes the error when status is \"Failed\"."""
    results: Optional[List[str]] = rest_field(visibility=["read"])
    """The results."""
