# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from enum import Enum
from azure.core import CaseInsensitiveEnumMeta


class ContentType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Content type for upload."""

    #: Content Type 'application/pdf'
    APPLICATION_PDF = "application/pdf"
    #: Content Type 'image/jpeg'
    IMAGE_JPEG = "image/jpeg"
    #: Content Type 'image/png'
    IMAGE_PNG = "image/png"
    #: Content Type 'image/tiff'
    IMAGE_TIFF = "image/tiff"