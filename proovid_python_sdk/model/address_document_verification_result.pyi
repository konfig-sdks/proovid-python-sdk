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


class AddressDocumentVerificationResult(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            
            
            class reference(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'reference':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class documentDate(
                schemas.DateTimeBase,
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                class MetaOapg:
                    format = 'date-time'
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, datetime, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'documentDate':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            documentStatus = schemas.Int32Schema
            
            
            class documentResult(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'documentResult':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            validityPeriod = schemas.Int32Schema
            
            
            class error(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'error':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
        
            @staticmethod
            def additionalInfo() -> typing.Type['ShuftiAddressDataResponse']:
                return ShuftiAddressDataResponse
            __annotations__ = {
                "reference": reference,
                "documentDate": documentDate,
                "documentStatus": documentStatus,
                "documentResult": documentResult,
                "validityPeriod": validityPeriod,
                "error": error,
                "additionalInfo": additionalInfo,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["reference"]) -> MetaOapg.properties.reference: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["documentDate"]) -> MetaOapg.properties.documentDate: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["documentStatus"]) -> MetaOapg.properties.documentStatus: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["documentResult"]) -> MetaOapg.properties.documentResult: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["validityPeriod"]) -> MetaOapg.properties.validityPeriod: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["error"]) -> MetaOapg.properties.error: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["additionalInfo"]) -> 'ShuftiAddressDataResponse': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["reference", "documentDate", "documentStatus", "documentResult", "validityPeriod", "error", "additionalInfo", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["reference"]) -> typing.Union[MetaOapg.properties.reference, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["documentDate"]) -> typing.Union[MetaOapg.properties.documentDate, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["documentStatus"]) -> typing.Union[MetaOapg.properties.documentStatus, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["documentResult"]) -> typing.Union[MetaOapg.properties.documentResult, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["validityPeriod"]) -> typing.Union[MetaOapg.properties.validityPeriod, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["error"]) -> typing.Union[MetaOapg.properties.error, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["additionalInfo"]) -> typing.Union['ShuftiAddressDataResponse', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["reference", "documentDate", "documentStatus", "documentResult", "validityPeriod", "error", "additionalInfo", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        reference: typing.Union[MetaOapg.properties.reference, None, str, schemas.Unset] = schemas.unset,
        documentDate: typing.Union[MetaOapg.properties.documentDate, None, str, datetime, schemas.Unset] = schemas.unset,
        documentStatus: typing.Union[MetaOapg.properties.documentStatus, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        documentResult: typing.Union[MetaOapg.properties.documentResult, None, str, schemas.Unset] = schemas.unset,
        validityPeriod: typing.Union[MetaOapg.properties.validityPeriod, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        error: typing.Union[MetaOapg.properties.error, None, str, schemas.Unset] = schemas.unset,
        additionalInfo: typing.Union['ShuftiAddressDataResponse', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'AddressDocumentVerificationResult':
        return super().__new__(
            cls,
            *args,
            reference=reference,
            documentDate=documentDate,
            documentStatus=documentStatus,
            documentResult=documentResult,
            validityPeriod=validityPeriod,
            error=error,
            additionalInfo=additionalInfo,
            _configuration=_configuration,
            **kwargs,
        )

from proovid_python_sdk.model.shufti_address_data_response import ShuftiAddressDataResponse
