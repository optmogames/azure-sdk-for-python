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


class DenyAssignmentPermission(Model):
    """Deny assignment permissions.

    :param actions: Actions to which the deny assignment does not grant
     access.
    :type actions: list[str]
    :param not_actions: Actions to exclude from that the deny assignment does
     not grant access.
    :type not_actions: list[str]
    :param data_actions: Data actions to which the deny assignment does not
     grant access.
    :type data_actions: list[str]
    :param not_data_actions: Data actions to exclude from that the deny
     assignment does not grant access.
    :type not_data_actions: list[str]
    """

    _attribute_map = {
        'actions': {'key': 'actions', 'type': '[str]'},
        'not_actions': {'key': 'notActions', 'type': '[str]'},
        'data_actions': {'key': 'dataActions', 'type': '[str]'},
        'not_data_actions': {'key': 'notDataActions', 'type': '[str]'},
    }

    def __init__(self, **kwargs):
        super(DenyAssignmentPermission, self).__init__(**kwargs)
        self.actions = kwargs.get('actions', None)
        self.not_actions = kwargs.get('not_actions', None)
        self.data_actions = kwargs.get('data_actions', None)
        self.not_data_actions = kwargs.get('not_data_actions', None)
