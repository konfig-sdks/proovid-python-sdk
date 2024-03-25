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

from proovid_python_sdk.pydantic.add_natural_person_info_request import AddNaturalPersonInfoRequest
from proovid_python_sdk.pydantic.natural_person_documents_request import NaturalPersonDocumentsRequest

class AddNaturalPersonRequest(BaseModel):
    info: typing.Optional[AddNaturalPersonInfoRequest] = Field(None, alias='info')

    client_reference_id: typing.Optional[typing.Optional[str]] = Field(None, alias='clientReferenceId')

    documents: typing.Optional[NaturalPersonDocumentsRequest] = Field(None, alias='documents')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
