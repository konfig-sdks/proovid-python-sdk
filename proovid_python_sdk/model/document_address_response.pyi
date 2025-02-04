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


class DocumentAddressResponse(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            
            
            class street(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'street':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class streetNumber(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'streetNumber':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class buildingName(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'buildingName':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class buildingNumber(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'buildingNumber':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class flatNumber(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'flatNumber':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class city(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'city':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class state(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'state':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class zipCode(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'zipCode':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class country(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'country':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            __annotations__ = {
                "street": street,
                "streetNumber": streetNumber,
                "buildingName": buildingName,
                "buildingNumber": buildingNumber,
                "flatNumber": flatNumber,
                "city": city,
                "state": state,
                "zipCode": zipCode,
                "country": country,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["street"]) -> MetaOapg.properties.street: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["streetNumber"]) -> MetaOapg.properties.streetNumber: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["buildingName"]) -> MetaOapg.properties.buildingName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["buildingNumber"]) -> MetaOapg.properties.buildingNumber: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["flatNumber"]) -> MetaOapg.properties.flatNumber: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["city"]) -> MetaOapg.properties.city: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["state"]) -> MetaOapg.properties.state: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["zipCode"]) -> MetaOapg.properties.zipCode: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["country"]) -> MetaOapg.properties.country: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["street", "streetNumber", "buildingName", "buildingNumber", "flatNumber", "city", "state", "zipCode", "country", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["street"]) -> typing.Union[MetaOapg.properties.street, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["streetNumber"]) -> typing.Union[MetaOapg.properties.streetNumber, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["buildingName"]) -> typing.Union[MetaOapg.properties.buildingName, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["buildingNumber"]) -> typing.Union[MetaOapg.properties.buildingNumber, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["flatNumber"]) -> typing.Union[MetaOapg.properties.flatNumber, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["city"]) -> typing.Union[MetaOapg.properties.city, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["state"]) -> typing.Union[MetaOapg.properties.state, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["zipCode"]) -> typing.Union[MetaOapg.properties.zipCode, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["country"]) -> typing.Union[MetaOapg.properties.country, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["street", "streetNumber", "buildingName", "buildingNumber", "flatNumber", "city", "state", "zipCode", "country", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        street: typing.Union[MetaOapg.properties.street, None, str, schemas.Unset] = schemas.unset,
        streetNumber: typing.Union[MetaOapg.properties.streetNumber, None, str, schemas.Unset] = schemas.unset,
        buildingName: typing.Union[MetaOapg.properties.buildingName, None, str, schemas.Unset] = schemas.unset,
        buildingNumber: typing.Union[MetaOapg.properties.buildingNumber, None, str, schemas.Unset] = schemas.unset,
        flatNumber: typing.Union[MetaOapg.properties.flatNumber, None, str, schemas.Unset] = schemas.unset,
        city: typing.Union[MetaOapg.properties.city, None, str, schemas.Unset] = schemas.unset,
        state: typing.Union[MetaOapg.properties.state, None, str, schemas.Unset] = schemas.unset,
        zipCode: typing.Union[MetaOapg.properties.zipCode, None, str, schemas.Unset] = schemas.unset,
        country: typing.Union[MetaOapg.properties.country, None, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'DocumentAddressResponse':
        return super().__new__(
            cls,
            *args,
            street=street,
            streetNumber=streetNumber,
            buildingName=buildingName,
            buildingNumber=buildingNumber,
            flatNumber=flatNumber,
            city=city,
            state=state,
            zipCode=zipCode,
            country=country,
            _configuration=_configuration,
            **kwargs,
        )
