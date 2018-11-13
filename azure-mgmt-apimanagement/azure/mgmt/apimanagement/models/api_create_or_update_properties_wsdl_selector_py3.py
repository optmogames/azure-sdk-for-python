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


class ApiCreateOrUpdatePropertiesWsdlSelector(Model):
    """Criteria to limit import of WSDL to a subset of the document.

    :param wsdl_service_name: Name of service to import from WSDL
    :type wsdl_service_name: str
    :param wsdl_endpoint_name: Name of endpoint(port) to import from WSDL
    :type wsdl_endpoint_name: str
    """

    _attribute_map = {
        'wsdl_service_name': {'key': 'wsdlServiceName', 'type': 'str'},
        'wsdl_endpoint_name': {'key': 'wsdlEndpointName', 'type': 'str'},
    }

    def __init__(self, *, wsdl_service_name: str=None, wsdl_endpoint_name: str=None, **kwargs) -> None:
        super(ApiCreateOrUpdatePropertiesWsdlSelector, self).__init__(**kwargs)
        self.wsdl_service_name = wsdl_service_name
        self.wsdl_endpoint_name = wsdl_endpoint_name