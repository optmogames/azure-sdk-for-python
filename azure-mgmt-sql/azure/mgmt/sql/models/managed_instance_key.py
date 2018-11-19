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

from .proxy_resource import ProxyResource


class ManagedInstanceKey(ProxyResource):
    """A managed instance key.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar id: Resource ID.
    :vartype id: str
    :ivar name: Resource name.
    :vartype name: str
    :ivar type: Resource type.
    :vartype type: str
    :ivar kind: Kind of encryption protector. This is metadata used for the
     Azure portal experience.
    :vartype kind: str
    :param server_key_type: Required. The key type like 'ServiceManaged',
     'AzureKeyVault'. Possible values include: 'ServiceManaged',
     'AzureKeyVault'
    :type server_key_type: str or ~azure.mgmt.sql.models.ServerKeyType
    :param uri: The URI of the key. If the ServerKeyType is AzureKeyVault,
     then the URI is required.
    :type uri: str
    :ivar thumbprint: Thumbprint of the key.
    :vartype thumbprint: str
    :ivar creation_date: The key creation date.
    :vartype creation_date: datetime
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'kind': {'readonly': True},
        'server_key_type': {'required': True},
        'thumbprint': {'readonly': True},
        'creation_date': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'kind': {'key': 'kind', 'type': 'str'},
        'server_key_type': {'key': 'properties.serverKeyType', 'type': 'str'},
        'uri': {'key': 'properties.uri', 'type': 'str'},
        'thumbprint': {'key': 'properties.thumbprint', 'type': 'str'},
        'creation_date': {'key': 'properties.creationDate', 'type': 'iso-8601'},
    }

    def __init__(self, **kwargs):
        super(ManagedInstanceKey, self).__init__(**kwargs)
        self.kind = None
        self.server_key_type = kwargs.get('server_key_type', None)
        self.uri = kwargs.get('uri', None)
        self.thumbprint = None
        self.creation_date = None
