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
from pydantic import BaseModel, Field, RootModel, ConfigDict

from proovid_python_sdk.pydantic.add_natural_person_data_save_result import AddNaturalPersonDataSaveResult
from proovid_python_sdk.pydantic.document_images import DocumentImages
from proovid_python_sdk.pydantic.sum_sub_verification_response import SumSubVerificationResponse

class AddNaturalPersonResponse(BaseModel):
    id: typing.Optional[int] = Field(None, alias='id')

    client_reference_id: typing.Optional[typing.Optional[str]] = Field(None, alias='clientReferenceId')

    document_images: typing.Optional[DocumentImages] = Field(None, alias='documentImages')

    data_save_responses: typing.Optional[AddNaturalPersonDataSaveResult] = Field(None, alias='dataSaveResponses')

    verifications: typing.Optional[SumSubVerificationResponse] = Field(None, alias='verifications')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
