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


class PolicyAssignment(Model):
    """The policy definition.

    :param display_name: The display name of the policy assignment.
    :type display_name: str
    :param policy_definition_id: The ID of the policy definition.
    :type policy_definition_id: str
    :param scope: The scope for the policy assignment.
    :type scope: str
    :param id: The ID of the policy assignment.
    :type id: str
    :param type: The type of the policy assignment.
    :type type: str
    :param name: The name of the policy assignment.
    :type name: str
    """

    _attribute_map = {
        'display_name': {'key': 'properties.displayName', 'type': 'str'},
        'policy_definition_id': {'key': 'properties.policyDefinitionId', 'type': 'str'},
        'scope': {'key': 'properties.scope', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
    }

    def __init__(self, display_name=None, policy_definition_id=None, scope=None, id=None, type=None, name=None):
        self.display_name = display_name
        self.policy_definition_id = policy_definition_id
        self.scope = scope
        self.id = id
        self.type = type
        self.name = name
