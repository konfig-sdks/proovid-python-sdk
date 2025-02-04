# coding: utf-8

"""
    Proovid Electronic Verification

    Proovid API is a RESTful application that specializes in electronic verification (Proof of address and Proof of Identity) by employing an advanced risk-tiered approacch in combination with a smart Risk assessment system. <a href='docs/PROOVid_ELV.pdf' target='_blank'>More information</a> 

    The version of the OpenAPI document: v1
    Contact: info@proovid.com
    Created by: http://www.proovid.com
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from proovid_python_sdk import schemas  # noqa: F401


class DocumentVerificationResponse(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            id = schemas.Int64Schema
            systemId = schemas.Int32Schema
            status = schemas.Int32Schema
        
            @staticmethod
            def documentData() -> typing.Type['DocumentVerificationData']:
                return DocumentVerificationData
        
            @staticmethod
            def documentResult() -> typing.Type['DocumentVerificationResult']:
                return DocumentVerificationResult
            
            
            class declinedReason(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'declinedReason':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class declinedCodeProovid(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'declinedCodeProovid':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            __annotations__ = {
                "id": id,
                "systemId": systemId,
                "status": status,
                "documentData": documentData,
                "documentResult": documentResult,
                "declinedReason": declinedReason,
                "declinedCodeProovid": declinedCodeProovid,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["systemId"]) -> MetaOapg.properties.systemId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["status"]) -> MetaOapg.properties.status: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["documentData"]) -> 'DocumentVerificationData': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["documentResult"]) -> 'DocumentVerificationResult': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["declinedReason"]) -> MetaOapg.properties.declinedReason: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["declinedCodeProovid"]) -> MetaOapg.properties.declinedCodeProovid: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["id", "systemId", "status", "documentData", "documentResult", "declinedReason", "declinedCodeProovid", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["systemId"]) -> typing.Union[MetaOapg.properties.systemId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["status"]) -> typing.Union[MetaOapg.properties.status, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["documentData"]) -> typing.Union['DocumentVerificationData', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["documentResult"]) -> typing.Union['DocumentVerificationResult', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["declinedReason"]) -> typing.Union[MetaOapg.properties.declinedReason, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["declinedCodeProovid"]) -> typing.Union[MetaOapg.properties.declinedCodeProovid, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["id", "systemId", "status", "documentData", "documentResult", "declinedReason", "declinedCodeProovid", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        id: typing.Union[MetaOapg.properties.id, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        systemId: typing.Union[MetaOapg.properties.systemId, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        status: typing.Union[MetaOapg.properties.status, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        documentData: typing.Union['DocumentVerificationData', schemas.Unset] = schemas.unset,
        documentResult: typing.Union['DocumentVerificationResult', schemas.Unset] = schemas.unset,
        declinedReason: typing.Union[MetaOapg.properties.declinedReason, None, str, schemas.Unset] = schemas.unset,
        declinedCodeProovid: typing.Union[MetaOapg.properties.declinedCodeProovid, None, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'DocumentVerificationResponse':
        return super().__new__(
            cls,
            *args,
            id=id,
            systemId=systemId,
            status=status,
            documentData=documentData,
            documentResult=documentResult,
            declinedReason=declinedReason,
            declinedCodeProovid=declinedCodeProovid,
            _configuration=_configuration,
            **kwargs,
        )

from proovid_python_sdk.model.document_verification_data import DocumentVerificationData
from proovid_python_sdk.model.document_verification_result import DocumentVerificationResult
