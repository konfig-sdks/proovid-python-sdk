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


class ShuftiAddressResultResponse(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            
            
            class issueDate(
                schemas.BoolBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneBoolMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, bool, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'issueDate':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class selectedType(
                schemas.BoolBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneBoolMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, bool, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'selectedType':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class addressDocumentCountry(
                schemas.BoolBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneBoolMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, bool, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'addressDocumentCountry':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class addressDocumentMustNotBeExpired(
                schemas.BoolBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneBoolMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, bool, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'addressDocumentMustNotBeExpired':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            fullAddress = schemas.AnyTypeSchema
            name = schemas.AnyTypeSchema
            
            
            class addressDocumentVisibility(
                schemas.BoolBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneBoolMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, bool, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'addressDocumentVisibility':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class addressDocument(
                schemas.BoolBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneBoolMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, bool, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'addressDocument':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            addressDocumentProof = schemas.AnyTypeSchema
            __annotations__ = {
                "issueDate": issueDate,
                "selectedType": selectedType,
                "addressDocumentCountry": addressDocumentCountry,
                "addressDocumentMustNotBeExpired": addressDocumentMustNotBeExpired,
                "fullAddress": fullAddress,
                "name": name,
                "addressDocumentVisibility": addressDocumentVisibility,
                "addressDocument": addressDocument,
                "addressDocumentProof": addressDocumentProof,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["issueDate"]) -> MetaOapg.properties.issueDate: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["selectedType"]) -> MetaOapg.properties.selectedType: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["addressDocumentCountry"]) -> MetaOapg.properties.addressDocumentCountry: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["addressDocumentMustNotBeExpired"]) -> MetaOapg.properties.addressDocumentMustNotBeExpired: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["fullAddress"]) -> MetaOapg.properties.fullAddress: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["addressDocumentVisibility"]) -> MetaOapg.properties.addressDocumentVisibility: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["addressDocument"]) -> MetaOapg.properties.addressDocument: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["addressDocumentProof"]) -> MetaOapg.properties.addressDocumentProof: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["issueDate", "selectedType", "addressDocumentCountry", "addressDocumentMustNotBeExpired", "fullAddress", "name", "addressDocumentVisibility", "addressDocument", "addressDocumentProof", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["issueDate"]) -> typing.Union[MetaOapg.properties.issueDate, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["selectedType"]) -> typing.Union[MetaOapg.properties.selectedType, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["addressDocumentCountry"]) -> typing.Union[MetaOapg.properties.addressDocumentCountry, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["addressDocumentMustNotBeExpired"]) -> typing.Union[MetaOapg.properties.addressDocumentMustNotBeExpired, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["fullAddress"]) -> typing.Union[MetaOapg.properties.fullAddress, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> typing.Union[MetaOapg.properties.name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["addressDocumentVisibility"]) -> typing.Union[MetaOapg.properties.addressDocumentVisibility, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["addressDocument"]) -> typing.Union[MetaOapg.properties.addressDocument, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["addressDocumentProof"]) -> typing.Union[MetaOapg.properties.addressDocumentProof, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["issueDate", "selectedType", "addressDocumentCountry", "addressDocumentMustNotBeExpired", "fullAddress", "name", "addressDocumentVisibility", "addressDocument", "addressDocumentProof", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        issueDate: typing.Union[MetaOapg.properties.issueDate, None, bool, schemas.Unset] = schemas.unset,
        selectedType: typing.Union[MetaOapg.properties.selectedType, None, bool, schemas.Unset] = schemas.unset,
        addressDocumentCountry: typing.Union[MetaOapg.properties.addressDocumentCountry, None, bool, schemas.Unset] = schemas.unset,
        addressDocumentMustNotBeExpired: typing.Union[MetaOapg.properties.addressDocumentMustNotBeExpired, None, bool, schemas.Unset] = schemas.unset,
        fullAddress: typing.Union[MetaOapg.properties.fullAddress, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, schemas.Unset] = schemas.unset,
        name: typing.Union[MetaOapg.properties.name, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, schemas.Unset] = schemas.unset,
        addressDocumentVisibility: typing.Union[MetaOapg.properties.addressDocumentVisibility, None, bool, schemas.Unset] = schemas.unset,
        addressDocument: typing.Union[MetaOapg.properties.addressDocument, None, bool, schemas.Unset] = schemas.unset,
        addressDocumentProof: typing.Union[MetaOapg.properties.addressDocumentProof, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ShuftiAddressResultResponse':
        return super().__new__(
            cls,
            *args,
            issueDate=issueDate,
            selectedType=selectedType,
            addressDocumentCountry=addressDocumentCountry,
            addressDocumentMustNotBeExpired=addressDocumentMustNotBeExpired,
            fullAddress=fullAddress,
            name=name,
            addressDocumentVisibility=addressDocumentVisibility,
            addressDocument=addressDocument,
            addressDocumentProof=addressDocumentProof,
            _configuration=_configuration,
            **kwargs,
        )
