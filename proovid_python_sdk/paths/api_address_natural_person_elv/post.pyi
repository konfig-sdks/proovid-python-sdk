# coding: utf-8

"""
    Proovid Electronic Verification

    Proovid API is a RESTful application that specializes in electronic verification (Proof of address and Proof of Identity) by employing an advanced risk-tiered approacch in combination with a smart Risk assessment system. <a href='docs/PROOVid_ELV.pdf' target='_blank'>More information</a> 

    The version of the OpenAPI document: v1
    Contact: info@proovid.com
    Created by: http://www.proovid.com
"""

from dataclasses import dataclass
import typing_extensions
import urllib3
from pydantic import RootModel
from proovid_python_sdk.request_before_hook import request_before_hook
import json
from urllib3._collections import HTTPHeaderDict

from proovid_python_sdk.api_response import AsyncGeneratorResponse
from proovid_python_sdk import api_client, exceptions
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

from proovid_python_sdk.model.natural_person_elv_request import NaturalPersonELVRequest as NaturalPersonELVRequestSchema
from proovid_python_sdk.model.address_verification_result import AddressVerificationResult as AddressVerificationResultSchema

from proovid_python_sdk.type.address_verification_result import AddressVerificationResult
from proovid_python_sdk.type.natural_person_elv_request import NaturalPersonELVRequest

from ...api_client import Dictionary
from proovid_python_sdk.pydantic.natural_person_elv_request import NaturalPersonELVRequest as NaturalPersonELVRequestPydantic
from proovid_python_sdk.pydantic.address_verification_result import AddressVerificationResult as AddressVerificationResultPydantic

# body param
SchemaForRequestBodyApplicationJson = NaturalPersonELVRequestSchema
SchemaForRequestBodyTextJson = NaturalPersonELVRequestSchema
SchemaForRequestBodyApplicationJsonPatchjson = NaturalPersonELVRequestSchema
SchemaForRequestBodyApplicationJson = NaturalPersonELVRequestSchema


request_body_natural_person_elv_request = api_client.RequestBody(
    content={
        'application/json': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationJson),
        'text/json': api_client.MediaType(
            schema=SchemaForRequestBodyTextJson),
        'application/json-patch+json': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationJsonPatchjson),
        'application/*+json': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationJson),
    },
)
SchemaFor200ResponseBodyApplicationJson = AddressVerificationResultSchema
SchemaFor200ResponseBodyTextJson = AddressVerificationResultSchema
SchemaFor200ResponseBodyTextPlain = AddressVerificationResultSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: AddressVerificationResult


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: AddressVerificationResult


_response_for_200 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor200,
    response_cls_async=ApiResponseFor200Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor200ResponseBodyApplicationJson),
        'text/json': api_client.MediaType(
            schema=SchemaFor200ResponseBodyTextJson),
        'text/plain': api_client.MediaType(
            schema=SchemaFor200ResponseBodyTextPlain),
    },
)
_all_accept_content_types = (
    'application/json',
    'text/json',
    'text/plain',
)


class BaseApi(api_client.Api):

    def _create_natural_person_elv_mapped_args(
        self,
        natural_person_index_id: typing.Optional[int] = None,
        street: typing.Optional[typing.Optional[str]] = None,
        street_number: typing.Optional[typing.Optional[str]] = None,
        unit: typing.Optional[typing.Optional[str]] = None,
        zip_code: typing.Optional[typing.Optional[str]] = None,
        city: typing.Optional[typing.Optional[str]] = None,
        district: typing.Optional[typing.Optional[str]] = None,
        region: typing.Optional[typing.Optional[str]] = None,
        country: typing.Optional[typing.Optional[str]] = None,
        email: typing.Optional[typing.Optional[str]] = None,
        mobile: typing.Optional[typing.Optional[str]] = None,
        full_address: typing.Optional[typing.Optional[str]] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _body = {}
        if natural_person_index_id is not None:
            _body["naturalPersonIndexId"] = natural_person_index_id
        if street is not None:
            _body["street"] = street
        if street_number is not None:
            _body["streetNumber"] = street_number
        if unit is not None:
            _body["unit"] = unit
        if zip_code is not None:
            _body["zipCode"] = zip_code
        if city is not None:
            _body["city"] = city
        if district is not None:
            _body["district"] = district
        if region is not None:
            _body["region"] = region
        if country is not None:
            _body["country"] = country
        if email is not None:
            _body["email"] = email
        if mobile is not None:
            _body["mobile"] = mobile
        if full_address is not None:
            _body["fullAddress"] = full_address
        args.body = _body
        return args

    async def _acreate_natural_person_elv_oapg(
        self,
        body: typing.Any = None,
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        content_type: str = 'application/json',
        stream: bool = False,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        """
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        used_path = path.value
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'post'.upper()
        _headers.add('Content-Type', content_type)
    
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/api/Address/NaturalPersonELV',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        if body is not schemas.unset:
            serialized_data = request_body_natural_person_elv_request.serialize(body, content_type)
            if 'fields' in serialized_data:
                _fields = serialized_data['fields']
            elif 'body' in serialized_data:
                _body = serialized_data['body']
    
        response = await self.api_client.async_call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            fields=_fields,
            serialized_body=_body,
            body=body,
            auth_settings=_auth,
            timeout=timeout,
            **kwargs
        )
    
        if stream:
            if not 200 <= response.http_response.status <= 299:
                body = (await response.http_response.content.read()).decode("utf-8")
                raise exceptions.ApiStreamingException(
                    status=response.http_response.status,
                    reason=response.http_response.reason,
                    body=body,
                )
    
            async def stream_iterator():
                """
                iterates over response.http_response.content and closes connection once iteration has finished
                """
                async for line in response.http_response.content:
                    if line == b'\r\n':
                        continue
                    yield line
                response.http_response.close()
                await response.session.close()
            return AsyncGeneratorResponse(
                content=stream_iterator(),
                headers=response.http_response.headers,
                status=response.http_response.status,
                response=response.http_response
            )
    
        response_for_status = _status_code_to_response.get(str(response.http_response.status))
        if response_for_status:
            api_response = await response_for_status.deserialize_async(
                                                    response,
                                                    self.api_client.configuration,
                                                    skip_deserialization=skip_deserialization
                                                )
        else:
            # If response data is JSON then deserialize for SDK consumer convenience
            is_json = api_client.JSONDetector._content_type_is_json(response.http_response.headers.get('Content-Type', ''))
            api_response = api_client.ApiResponseWithoutDeserializationAsync(
                body=await response.http_response.json() if is_json else await response.http_response.text(),
                response=response.http_response,
                round_trip_time=response.round_trip_time,
                status=response.http_response.status,
                headers=response.http_response.headers,
            )
    
        if not 200 <= api_response.status <= 299:
            raise exceptions.ApiException(api_response=api_response)
    
        # cleanup session / response
        response.http_response.close()
        await response.session.close()
    
        return api_response


    def _create_natural_person_elv_oapg(
        self,
        body: typing.Any = None,
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        content_type: str = 'application/json',
        stream: bool = False,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        """
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        used_path = path.value
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'post'.upper()
        _headers.add('Content-Type', content_type)
    
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/api/Address/NaturalPersonELV',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        if body is not schemas.unset:
            serialized_data = request_body_natural_person_elv_request.serialize(body, content_type)
            if 'fields' in serialized_data:
                _fields = serialized_data['fields']
            elif 'body' in serialized_data:
                _body = serialized_data['body']
    
        response = self.api_client.call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            fields=_fields,
            serialized_body=_body,
            body=body,
            auth_settings=_auth,
            timeout=timeout,
        )
    
        response_for_status = _status_code_to_response.get(str(response.http_response.status))
        if response_for_status:
            api_response = response_for_status.deserialize(
                                                    response,
                                                    self.api_client.configuration,
                                                    skip_deserialization=skip_deserialization
                                                )
        else:
            # If response data is JSON then deserialize for SDK consumer convenience
            is_json = api_client.JSONDetector._content_type_is_json(response.http_response.headers.get('Content-Type', ''))
            api_response = api_client.ApiResponseWithoutDeserialization(
                body=json.loads(response.http_response.data) if is_json else response.http_response.data,
                response=response.http_response,
                round_trip_time=response.round_trip_time,
                status=response.http_response.status,
                headers=response.http_response.headers,
            )
    
        if not 200 <= api_response.status <= 299:
            raise exceptions.ApiException(api_response=api_response)
    
        return api_response


class CreateNaturalPersonElvRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def acreate_natural_person_elv(
        self,
        natural_person_index_id: typing.Optional[int] = None,
        street: typing.Optional[typing.Optional[str]] = None,
        street_number: typing.Optional[typing.Optional[str]] = None,
        unit: typing.Optional[typing.Optional[str]] = None,
        zip_code: typing.Optional[typing.Optional[str]] = None,
        city: typing.Optional[typing.Optional[str]] = None,
        district: typing.Optional[typing.Optional[str]] = None,
        region: typing.Optional[typing.Optional[str]] = None,
        country: typing.Optional[typing.Optional[str]] = None,
        email: typing.Optional[typing.Optional[str]] = None,
        mobile: typing.Optional[typing.Optional[str]] = None,
        full_address: typing.Optional[typing.Optional[str]] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._create_natural_person_elv_mapped_args(
            natural_person_index_id=natural_person_index_id,
            street=street,
            street_number=street_number,
            unit=unit,
            zip_code=zip_code,
            city=city,
            district=district,
            region=region,
            country=country,
            email=email,
            mobile=mobile,
            full_address=full_address,
        )
        return await self._acreate_natural_person_elv_oapg(
            body=args.body,
            **kwargs,
        )
    
    def create_natural_person_elv(
        self,
        natural_person_index_id: typing.Optional[int] = None,
        street: typing.Optional[typing.Optional[str]] = None,
        street_number: typing.Optional[typing.Optional[str]] = None,
        unit: typing.Optional[typing.Optional[str]] = None,
        zip_code: typing.Optional[typing.Optional[str]] = None,
        city: typing.Optional[typing.Optional[str]] = None,
        district: typing.Optional[typing.Optional[str]] = None,
        region: typing.Optional[typing.Optional[str]] = None,
        country: typing.Optional[typing.Optional[str]] = None,
        email: typing.Optional[typing.Optional[str]] = None,
        mobile: typing.Optional[typing.Optional[str]] = None,
        full_address: typing.Optional[typing.Optional[str]] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._create_natural_person_elv_mapped_args(
            natural_person_index_id=natural_person_index_id,
            street=street,
            street_number=street_number,
            unit=unit,
            zip_code=zip_code,
            city=city,
            district=district,
            region=region,
            country=country,
            email=email,
            mobile=mobile,
            full_address=full_address,
        )
        return self._create_natural_person_elv_oapg(
            body=args.body,
        )

class CreateNaturalPersonElv(BaseApi):

    async def acreate_natural_person_elv(
        self,
        natural_person_index_id: typing.Optional[int] = None,
        street: typing.Optional[typing.Optional[str]] = None,
        street_number: typing.Optional[typing.Optional[str]] = None,
        unit: typing.Optional[typing.Optional[str]] = None,
        zip_code: typing.Optional[typing.Optional[str]] = None,
        city: typing.Optional[typing.Optional[str]] = None,
        district: typing.Optional[typing.Optional[str]] = None,
        region: typing.Optional[typing.Optional[str]] = None,
        country: typing.Optional[typing.Optional[str]] = None,
        email: typing.Optional[typing.Optional[str]] = None,
        mobile: typing.Optional[typing.Optional[str]] = None,
        full_address: typing.Optional[typing.Optional[str]] = None,
        validate: bool = False,
        **kwargs,
    ) -> AddressVerificationResultPydantic:
        raw_response = await self.raw.acreate_natural_person_elv(
            natural_person_index_id=natural_person_index_id,
            street=street,
            street_number=street_number,
            unit=unit,
            zip_code=zip_code,
            city=city,
            district=district,
            region=region,
            country=country,
            email=email,
            mobile=mobile,
            full_address=full_address,
            **kwargs,
        )
        if validate:
            return AddressVerificationResultPydantic(**raw_response.body)
        return api_client.construct_model_instance(AddressVerificationResultPydantic, raw_response.body)
    
    
    def create_natural_person_elv(
        self,
        natural_person_index_id: typing.Optional[int] = None,
        street: typing.Optional[typing.Optional[str]] = None,
        street_number: typing.Optional[typing.Optional[str]] = None,
        unit: typing.Optional[typing.Optional[str]] = None,
        zip_code: typing.Optional[typing.Optional[str]] = None,
        city: typing.Optional[typing.Optional[str]] = None,
        district: typing.Optional[typing.Optional[str]] = None,
        region: typing.Optional[typing.Optional[str]] = None,
        country: typing.Optional[typing.Optional[str]] = None,
        email: typing.Optional[typing.Optional[str]] = None,
        mobile: typing.Optional[typing.Optional[str]] = None,
        full_address: typing.Optional[typing.Optional[str]] = None,
        validate: bool = False,
    ) -> AddressVerificationResultPydantic:
        raw_response = self.raw.create_natural_person_elv(
            natural_person_index_id=natural_person_index_id,
            street=street,
            street_number=street_number,
            unit=unit,
            zip_code=zip_code,
            city=city,
            district=district,
            region=region,
            country=country,
            email=email,
            mobile=mobile,
            full_address=full_address,
        )
        if validate:
            return AddressVerificationResultPydantic(**raw_response.body)
        return api_client.construct_model_instance(AddressVerificationResultPydantic, raw_response.body)


class ApiForpost(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def apost(
        self,
        natural_person_index_id: typing.Optional[int] = None,
        street: typing.Optional[typing.Optional[str]] = None,
        street_number: typing.Optional[typing.Optional[str]] = None,
        unit: typing.Optional[typing.Optional[str]] = None,
        zip_code: typing.Optional[typing.Optional[str]] = None,
        city: typing.Optional[typing.Optional[str]] = None,
        district: typing.Optional[typing.Optional[str]] = None,
        region: typing.Optional[typing.Optional[str]] = None,
        country: typing.Optional[typing.Optional[str]] = None,
        email: typing.Optional[typing.Optional[str]] = None,
        mobile: typing.Optional[typing.Optional[str]] = None,
        full_address: typing.Optional[typing.Optional[str]] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._create_natural_person_elv_mapped_args(
            natural_person_index_id=natural_person_index_id,
            street=street,
            street_number=street_number,
            unit=unit,
            zip_code=zip_code,
            city=city,
            district=district,
            region=region,
            country=country,
            email=email,
            mobile=mobile,
            full_address=full_address,
        )
        return await self._acreate_natural_person_elv_oapg(
            body=args.body,
            **kwargs,
        )
    
    def post(
        self,
        natural_person_index_id: typing.Optional[int] = None,
        street: typing.Optional[typing.Optional[str]] = None,
        street_number: typing.Optional[typing.Optional[str]] = None,
        unit: typing.Optional[typing.Optional[str]] = None,
        zip_code: typing.Optional[typing.Optional[str]] = None,
        city: typing.Optional[typing.Optional[str]] = None,
        district: typing.Optional[typing.Optional[str]] = None,
        region: typing.Optional[typing.Optional[str]] = None,
        country: typing.Optional[typing.Optional[str]] = None,
        email: typing.Optional[typing.Optional[str]] = None,
        mobile: typing.Optional[typing.Optional[str]] = None,
        full_address: typing.Optional[typing.Optional[str]] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._create_natural_person_elv_mapped_args(
            natural_person_index_id=natural_person_index_id,
            street=street,
            street_number=street_number,
            unit=unit,
            zip_code=zip_code,
            city=city,
            district=district,
            region=region,
            country=country,
            email=email,
            mobile=mobile,
            full_address=full_address,
        )
        return self._create_natural_person_elv_oapg(
            body=args.body,
        )

