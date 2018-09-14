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


class AzureTimeSeriesData(Model):
    """AzureTimeSeriesData.

    :param dim_values: Gets or sets dimension values
    :type dim_values: list[str]
    :param min: Gets or sets Min value
    :type min: float
    :param max: Gets or sets Max value
    :type max: float
    :param sum: Gets or sets Sum value
    :type sum: float
    :param count: Gets or sets Count value
    :type count: int
    """

    _attribute_map = {
        'dim_values': {'key': 'dimValues', 'type': '[str]'},
        'min': {'key': 'min', 'type': 'float'},
        'max': {'key': 'max', 'type': 'float'},
        'sum': {'key': 'sum', 'type': 'float'},
        'count': {'key': 'count', 'type': 'int'},
    }

    def __init__(self, *, dim_values=None, min: float=None, max: float=None, sum: float=None, count: int=None, **kwargs) -> None:
        super(AzureTimeSeriesData, self).__init__(**kwargs)
        self.dim_values = dim_values
        self.min = min
        self.max = max
        self.sum = sum
        self.count = count
