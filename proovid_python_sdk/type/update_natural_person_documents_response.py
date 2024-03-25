# coding: utf-8

"""
    Proovid Electronic Verification

    Proovid API is a RESTful application that specializes in electronic verification (Proof of address and Proof of Identity) by employing an advanced risk-tiered approacch in combination with a smart Risk assessment system. <a href='docs/PROOVid_ELV.pdf' target='_blank'>More information</a> 

    The version of the OpenAPI document: v1
    Contact: info@proovid.com
    Created by: http://www.proovid.com
"""

from datetime import datetime, date
import typing
from enum import Enum
from typing_extensions import TypedDict, Literal, TYPE_CHECKING

from proovid_python_sdk.type.document_images import DocumentImages
from proovid_python_sdk.type.sum_sub_verification_response import SumSubVerificationResponse
from proovid_python_sdk.type.update_natural_person_documents_data_save_result import UpdateNaturalPersonDocumentsDataSaveResult

class RequiredUpdateNaturalPersonDocumentsResponse(TypedDict):
    pass

class OptionalUpdateNaturalPersonDocumentsResponse(TypedDict, total=False):
    id: int

    clientReferenceId: typing.Optional[str]

    dataSaveResponses: UpdateNaturalPersonDocumentsDataSaveResult

    verification: SumSubVerificationResponse

    documentImages: DocumentImages

class UpdateNaturalPersonDocumentsResponse(RequiredUpdateNaturalPersonDocumentsResponse, OptionalUpdateNaturalPersonDocumentsResponse):
    pass
