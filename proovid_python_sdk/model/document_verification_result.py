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


class DocumentVerificationResult(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            
            
            class documentValidity(
                schemas.BoolBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneBoolMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, bool, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'documentValidity':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class documentVisibility(
                schemas.BoolBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneBoolMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, bool, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'documentVisibility':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class mustNotBeExpired(
                schemas.BoolBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneBoolMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, bool, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'mustNotBeExpired':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class documentNumber(
                schemas.BoolBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneBoolMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, bool, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'documentNumber':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
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
            
            
            class expiredDate(
                schemas.BoolBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneBoolMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, bool, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'expiredDate':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class dob(
                schemas.BoolBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneBoolMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, bool, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'dob':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class name(
                schemas.BoolBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneBoolMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, bool, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'name':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class documentCountry(
                schemas.BoolBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneBoolMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, bool, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'documentCountry':
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
            
            
            class faceOnDocumentMatched(
                schemas.BoolBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneBoolMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, bool, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'faceOnDocumentMatched':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            __annotations__ = {
                "documentValidity": documentValidity,
                "documentVisibility": documentVisibility,
                "mustNotBeExpired": mustNotBeExpired,
                "documentNumber": documentNumber,
                "issueDate": issueDate,
                "expiredDate": expiredDate,
                "dob": dob,
                "name": name,
                "documentCountry": documentCountry,
                "selectedType": selectedType,
                "faceOnDocumentMatched": faceOnDocumentMatched,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["documentValidity"]) -> MetaOapg.properties.documentValidity: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["documentVisibility"]) -> MetaOapg.properties.documentVisibility: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["mustNotBeExpired"]) -> MetaOapg.properties.mustNotBeExpired: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["documentNumber"]) -> MetaOapg.properties.documentNumber: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["issueDate"]) -> MetaOapg.properties.issueDate: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["expiredDate"]) -> MetaOapg.properties.expiredDate: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["dob"]) -> MetaOapg.properties.dob: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["documentCountry"]) -> MetaOapg.properties.documentCountry: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["selectedType"]) -> MetaOapg.properties.selectedType: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["faceOnDocumentMatched"]) -> MetaOapg.properties.faceOnDocumentMatched: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["documentValidity", "documentVisibility", "mustNotBeExpired", "documentNumber", "issueDate", "expiredDate", "dob", "name", "documentCountry", "selectedType", "faceOnDocumentMatched", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["documentValidity"]) -> typing.Union[MetaOapg.properties.documentValidity, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["documentVisibility"]) -> typing.Union[MetaOapg.properties.documentVisibility, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["mustNotBeExpired"]) -> typing.Union[MetaOapg.properties.mustNotBeExpired, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["documentNumber"]) -> typing.Union[MetaOapg.properties.documentNumber, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["issueDate"]) -> typing.Union[MetaOapg.properties.issueDate, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["expiredDate"]) -> typing.Union[MetaOapg.properties.expiredDate, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["dob"]) -> typing.Union[MetaOapg.properties.dob, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> typing.Union[MetaOapg.properties.name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["documentCountry"]) -> typing.Union[MetaOapg.properties.documentCountry, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["selectedType"]) -> typing.Union[MetaOapg.properties.selectedType, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["faceOnDocumentMatched"]) -> typing.Union[MetaOapg.properties.faceOnDocumentMatched, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["documentValidity", "documentVisibility", "mustNotBeExpired", "documentNumber", "issueDate", "expiredDate", "dob", "name", "documentCountry", "selectedType", "faceOnDocumentMatched", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        documentValidity: typing.Union[MetaOapg.properties.documentValidity, None, bool, schemas.Unset] = schemas.unset,
        documentVisibility: typing.Union[MetaOapg.properties.documentVisibility, None, bool, schemas.Unset] = schemas.unset,
        mustNotBeExpired: typing.Union[MetaOapg.properties.mustNotBeExpired, None, bool, schemas.Unset] = schemas.unset,
        documentNumber: typing.Union[MetaOapg.properties.documentNumber, None, bool, schemas.Unset] = schemas.unset,
        issueDate: typing.Union[MetaOapg.properties.issueDate, None, bool, schemas.Unset] = schemas.unset,
        expiredDate: typing.Union[MetaOapg.properties.expiredDate, None, bool, schemas.Unset] = schemas.unset,
        dob: typing.Union[MetaOapg.properties.dob, None, bool, schemas.Unset] = schemas.unset,
        name: typing.Union[MetaOapg.properties.name, None, bool, schemas.Unset] = schemas.unset,
        documentCountry: typing.Union[MetaOapg.properties.documentCountry, None, bool, schemas.Unset] = schemas.unset,
        selectedType: typing.Union[MetaOapg.properties.selectedType, None, bool, schemas.Unset] = schemas.unset,
        faceOnDocumentMatched: typing.Union[MetaOapg.properties.faceOnDocumentMatched, None, bool, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'DocumentVerificationResult':
        return super().__new__(
            cls,
            *args,
            documentValidity=documentValidity,
            documentVisibility=documentVisibility,
            mustNotBeExpired=mustNotBeExpired,
            documentNumber=documentNumber,
            issueDate=issueDate,
            expiredDate=expiredDate,
            dob=dob,
            name=name,
            documentCountry=documentCountry,
            selectedType=selectedType,
            faceOnDocumentMatched=faceOnDocumentMatched,
            _configuration=_configuration,
            **kwargs,
        )
