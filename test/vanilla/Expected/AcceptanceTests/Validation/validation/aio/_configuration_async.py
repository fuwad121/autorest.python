# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from azure.core.configuration import Configuration
from azure.core.pipeline import policies

from .._version import VERSION


class AutoRestValidationTestConfiguration(Configuration):
    """Configuration for AutoRestValidationTest
    Note that all parameters used to create this instance are saved as instance
    attributes.

    :param subscription_id: Subscription ID.
    :type subscription_id: str
    """

    def __init__(self, subscription_id, **kwargs):
        if subscription_id is None:
            raise ValueError("Parameter 'subscription_id' must not be None.")
        super(AutoRestValidationTestConfiguration, self).__init__(**kwargs)

        self.subscription_id = subscription_id
        self.api_version = "1.0.0"
        self._configure(**kwargs)
        self.user_agent_policy.add_user_agent('azsdk-python-autorestvalidationtest/{}'.format(VERSION))

    def _configure(self, **kwargs):
        self.user_agent_policy = kwargs.get('user_agent_policy') or policies.UserAgentPolicy(**kwargs)
        self.headers_policy = kwargs.get('headers_policy') or policies.HeadersPolicy(**kwargs)
        self.proxy_policy = kwargs.get('proxy_policy') or policies.ProxyPolicy(**kwargs)
        self.logging_policy = kwargs.get('logging_policy') or policies.NetworkTraceLoggingPolicy(**kwargs)
        self.retry_policy = kwargs.get('retry_policy') or policies.AsyncRetryPolicy(**kwargs)
        self.custom_hook_policy = kwargs.get('custom_hook_policy') or policies.CustomHookPolicy(**kwargs)
        self.redirect_policy = kwargs.get('redirect_policy') or policies.AsyncRedirectPolicy(**kwargs)
        self.authentication_policy = kwargs.get('authentication_policy')
