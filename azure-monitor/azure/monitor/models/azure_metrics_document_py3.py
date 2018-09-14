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

from msrest.serialization import Model


class AzureMetricsDocument(Model):
    """AzureMetricsDocument.

    :param time: Gets or sets Time property (in ISO 8601 format)
    :type time: str
    :param data:
    :type data: ~azure.monitor.models.AzureMetricsData
    """

    _attribute_map = {
        'time': {'key': 'time', 'type': 'str'},
        'data': {'key': 'data', 'type': 'AzureMetricsData'},
    }

    def __init__(self, *, time: str=None, data=None, **kwargs) -> None:
        super(AzureMetricsDocument, self).__init__(**kwargs)
        self.time = time
        self.data = data
