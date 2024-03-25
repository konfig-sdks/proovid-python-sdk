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

from proovid_python_sdk.pydantic.e_status import EStatus
from proovid_python_sdk.pydantic.reject_label_type import RejectLabelType

class NaturalPersonFaceVerificationResponse(BaseModel):
    status: typing.Optional[EStatus] = Field(None, alias='status')

    comment: typing.Optional[typing.Optional[str]] = Field(None, alias='comment')

    reject_labels: typing.Optional[typing.Optional[typing.List[RejectLabelType]]] = Field(None, alias='rejectLabels')

    face_match_confidence: typing.Optional[typing.Optional[typing.Union[int, float]]] = Field(None, alias='faceMatchConfidence')

    image_id: typing.Optional[typing.Optional[str]] = Field(None, alias='imageId')

    creation_date: typing.Optional[datetime] = Field(None, alias='creationDate')

    last_updated_date: typing.Optional[datetime] = Field(None, alias='lastUpdatedDate')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
