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


class EventsExceptionInfo(Model):
    """The exception info.

    :param severity_level: The severity level of the exception
    :type severity_level: int
    :param problem_id: The problem ID of the exception
    :type problem_id: str
    :param handled_at: Indicates where the exception was handled at
    :type handled_at: str
    :param assembly: The assembly which threw the exception
    :type assembly: str
    :param method: The method that threw the exception
    :type method: str
    :param message: The message of the exception
    :type message: str
    :param type: The type of the exception
    :type type: str
    :param outer_type: The outer type of the exception
    :type outer_type: str
    :param outer_method: The outer method of the exception
    :type outer_method: str
    :param outer_assembly: The outer assmebly of the exception
    :type outer_assembly: str
    :param outer_message: The outer message of the exception
    :type outer_message: str
    :param innermost_type: The inner most type of the exception
    :type innermost_type: str
    :param innermost_message: The inner most message of the exception
    :type innermost_message: str
    :param innermost_method: The inner most method of the exception
    :type innermost_method: str
    :param innermost_assembly: The inner most assembly of the exception
    :type innermost_assembly: str
    :param details: The details of the exception
    :type details:
     list[~azure.applicationinsights.models.EventsExceptionDetail]
    """

    _attribute_map = {
        'severity_level': {'key': 'severityLevel', 'type': 'int'},
        'problem_id': {'key': 'problemId', 'type': 'str'},
        'handled_at': {'key': 'handledAt', 'type': 'str'},
        'assembly': {'key': 'assembly', 'type': 'str'},
        'method': {'key': 'method', 'type': 'str'},
        'message': {'key': 'message', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'outer_type': {'key': 'outerType', 'type': 'str'},
        'outer_method': {'key': 'outerMethod', 'type': 'str'},
        'outer_assembly': {'key': 'outerAssembly', 'type': 'str'},
        'outer_message': {'key': 'outerMessage', 'type': 'str'},
        'innermost_type': {'key': 'innermostType', 'type': 'str'},
        'innermost_message': {'key': 'innermostMessage', 'type': 'str'},
        'innermost_method': {'key': 'innermostMethod', 'type': 'str'},
        'innermost_assembly': {'key': 'innermostAssembly', 'type': 'str'},
        'details': {'key': 'details', 'type': '[EventsExceptionDetail]'},
    }

    def __init__(self, *, severity_level: int=None, problem_id: str=None, handled_at: str=None, assembly: str=None, method: str=None, message: str=None, type: str=None, outer_type: str=None, outer_method: str=None, outer_assembly: str=None, outer_message: str=None, innermost_type: str=None, innermost_message: str=None, innermost_method: str=None, innermost_assembly: str=None, details=None, **kwargs) -> None:
        super(EventsExceptionInfo, self).__init__(**kwargs)
        self.severity_level = severity_level
        self.problem_id = problem_id
        self.handled_at = handled_at
        self.assembly = assembly
        self.method = method
        self.message = message
        self.type = type
        self.outer_type = outer_type
        self.outer_method = outer_method
        self.outer_assembly = outer_assembly
        self.outer_message = outer_message
        self.innermost_type = innermost_type
        self.innermost_message = innermost_message
        self.innermost_method = innermost_method
        self.innermost_assembly = innermost_assembly
        self.details = details
