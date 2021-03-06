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


class TextOperationResult(Model):
    """TextOperationResult.

    :param status: Status of the text operation. Possible values include: 'Not
     Started', 'Running', 'Failed', 'Succeeded'
    :type status: str or
     ~azure.cognitiveservices.vision.computervision.models.TextOperationStatusCodes
    :param recognition_result:
    :type recognition_result:
     ~azure.cognitiveservices.vision.computervision.models.RecognitionResult
    """

    _attribute_map = {
        'status': {'key': 'status', 'type': 'TextOperationStatusCodes'},
        'recognition_result': {'key': 'recognitionResult', 'type': 'RecognitionResult'},
    }

    def __init__(self, *, status=None, recognition_result=None, **kwargs) -> None:
        super(TextOperationResult, self).__init__(**kwargs)
        self.status = status
        self.recognition_result = recognition_result
