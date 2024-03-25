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

from proovid_python_sdk.pydantic.base_response import BaseResponse
from proovid_python_sdk.pydantic.string_base_response import StringBaseResponse

class UpdateNaturalPersonDocumentsDataSaveResult(BaseModel):
    id_document_saved: typing.Optional[BaseResponse] = Field(None, alias='idDocumentSaved')

    face_saved: typing.Optional[BaseResponse] = Field(None, alias='faceSaved')

    liveness_check_u_r_l: typing.Optional[StringBaseResponse] = Field(None, alias='livenessCheckURL')

    address_document_saved: typing.Optional[BaseResponse] = Field(None, alias='addressDocumentSaved')

    verification_started: typing.Optional[BaseResponse] = Field(None, alias='verificationStarted')

    all_succeeded: typing.Optional[bool] = Field(None, alias='allSucceeded')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
