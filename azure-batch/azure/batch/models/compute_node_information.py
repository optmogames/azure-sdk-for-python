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


class ComputeNodeInformation(Model):
    """Information about the compute node on which a task ran.

    :param affinity_id: An identifier for the compute node on which the task
     ran, which can be passed when adding a task to request that the task be
     scheduled on this compute node.
    :type affinity_id: str
    :param node_url: The URL of the node on which the task ran. .
    :type node_url: str
    :param pool_id: The ID of the pool on which the task ran.
    :type pool_id: str
    :param node_id: The ID of the node on which the task ran.
    :type node_id: str
    :param task_root_directory: The root directory of the task on the compute
     node.
    :type task_root_directory: str
    :param task_root_directory_url: The URL to the root directory of the task
     on the compute node.
    :type task_root_directory_url: str
    """

    _attribute_map = {
        'affinity_id': {'key': 'affinityId', 'type': 'str'},
        'node_url': {'key': 'nodeUrl', 'type': 'str'},
        'pool_id': {'key': 'poolId', 'type': 'str'},
        'node_id': {'key': 'nodeId', 'type': 'str'},
        'task_root_directory': {'key': 'taskRootDirectory', 'type': 'str'},
        'task_root_directory_url': {'key': 'taskRootDirectoryUrl', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(ComputeNodeInformation, self).__init__(**kwargs)
        self.affinity_id = kwargs.get('affinity_id', None)
        self.node_url = kwargs.get('node_url', None)
        self.pool_id = kwargs.get('pool_id', None)
        self.node_id = kwargs.get('node_id', None)
        self.task_root_directory = kwargs.get('task_root_directory', None)
        self.task_root_directory_url = kwargs.get('task_root_directory_url', None)
