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


class DocumentImages(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            
            
            class idDocumentId(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'idDocumentId':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class additionalIdDocumentId(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'additionalIdDocumentId':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class faceId(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'faceId':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class addressId(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'addressId':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            __annotations__ = {
                "idDocumentId": idDocumentId,
                "additionalIdDocumentId": additionalIdDocumentId,
                "faceId": faceId,
                "addressId": addressId,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["idDocumentId"]) -> MetaOapg.properties.idDocumentId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["additionalIdDocumentId"]) -> MetaOapg.properties.additionalIdDocumentId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["faceId"]) -> MetaOapg.properties.faceId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["addressId"]) -> MetaOapg.properties.addressId: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["idDocumentId", "additionalIdDocumentId", "faceId", "addressId", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["idDocumentId"]) -> typing.Union[MetaOapg.properties.idDocumentId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["additionalIdDocumentId"]) -> typing.Union[MetaOapg.properties.additionalIdDocumentId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["faceId"]) -> typing.Union[MetaOapg.properties.faceId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["addressId"]) -> typing.Union[MetaOapg.properties.addressId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["idDocumentId", "additionalIdDocumentId", "faceId", "addressId", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        idDocumentId: typing.Union[MetaOapg.properties.idDocumentId, None, str, schemas.Unset] = schemas.unset,
        additionalIdDocumentId: typing.Union[MetaOapg.properties.additionalIdDocumentId, None, str, schemas.Unset] = schemas.unset,
        faceId: typing.Union[MetaOapg.properties.faceId, None, str, schemas.Unset] = schemas.unset,
        addressId: typing.Union[MetaOapg.properties.addressId, None, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'DocumentImages':
        return super().__new__(
            cls,
            *args,
            idDocumentId=idDocumentId,
            additionalIdDocumentId=additionalIdDocumentId,
            faceId=faceId,
            addressId=addressId,
            _configuration=_configuration,
            **kwargs,
        )
