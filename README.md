<div align="left">

[![Visit Proovid](./header.png)](https://www.proovid.com&#x2F;)

# Proovid<a id="proovid"></a>

Proovid API is a RESTful application that specializes in electronic verification (Proof of address and Proof of Identity) by employing an advanced risk-tiered approacch in combination with a smart Risk assessment system. <a href='docs/PROOVid_ELV.pdf' target='_blank'>More information</a> 


</div>

## Table of Contents<a id="table-of-contents"></a>

<!-- toc -->

- [Requirements](#requirements)
- [Installation](#installation)
- [Getting Started](#getting-started)
- [Async](#async)
- [Raw HTTP Response](#raw-http-response)
- [Reference](#reference)
  * [`proovid.address.create_natural_person_elv`](#proovidaddresscreate_natural_person_elv)
  * [`proovid.address.link_response`](#proovidaddresslink_response)
  * [`proovid.address.verify_by_id`](#proovidaddressverify_by_id)
  * [`proovid.address.verify_by_id_0`](#proovidaddressverify_by_id_0)
  * [`proovid.address.verify_by_level`](#proovidaddressverify_by_level)
  * [`proovid.address.verify_certificate_pdf`](#proovidaddressverify_certificate_pdf)
  * [`proovid.document.get_certificate`](#prooviddocumentget_certificate)
  * [`proovid.document.verify_deletion`](#prooviddocumentverify_deletion)
  * [`proovid.document.verify_status`](#prooviddocumentverify_status)
  * [`proovid.document.verify_status_0`](#prooviddocumentverify_status_0)
  * [`proovid.health.get_version`](#proovidhealthget_version)
  * [`proovid.health.status_check`](#proovidhealthstatus_check)
  * [`proovid.natural_person.create_or_update`](#proovidnatural_personcreate_or_update)
  * [`proovid.natural_person.delete_by_id`](#proovidnatural_persondelete_by_id)
  * [`proovid.natural_person.get_by_id`](#proovidnatural_personget_by_id)
  * [`proovid.natural_person.get_by_id_0`](#proovidnatural_personget_by_id_0)
  * [`proovid.natural_person.get_certificate`](#proovidnatural_personget_certificate)
  * [`proovid.natural_person.get_details`](#proovidnatural_personget_details)
  * [`proovid.natural_person.get_verification_record`](#proovidnatural_personget_verification_record)
  * [`proovid.natural_person.get_verifications`](#proovidnatural_personget_verifications)
  * [`proovid.natural_person.remove_by_id`](#proovidnatural_personremove_by_id)
  * [`proovid.natural_person.update_documents`](#proovidnatural_personupdate_documents)
  * [`proovid.natural_person.update_information`](#proovidnatural_personupdate_information)
  * [`proovid.natural_person.verify_details`](#proovidnatural_personverify_details)
  * [`proovid.natural_person.verify_details_0`](#proovidnatural_personverify_details_0)
  * [`proovid.natural_person.verify_documents`](#proovidnatural_personverify_documents)
  * [`proovid.natural_person.verify_entity`](#proovidnatural_personverify_entity)
  * [`proovid.screening.get_aml_report`](#proovidscreeningget_aml_report)
  * [`proovid.screening.get_natural_person_by_id`](#proovidscreeningget_natural_person_by_id)
  * [`proovid.screening.remove_natural_person`](#proovidscreeningremove_natural_person)
  * [`proovid.screening.submit_natural_person_screening`](#proovidscreeningsubmit_natural_person_screening)

<!-- tocstop -->

## Requirements<a id="requirements"></a>

Python >=3.7

## Installation<a id="installation"></a>
<div align="center">
  <a href="https://konfigthis.com/sdk-sign-up?company=PROOViD&language=Python">
    <img src="https://raw.githubusercontent.com/konfig-dev/brand-assets/HEAD/cta-images/python-cta.png" width="70%">
  </a>
</div>

## Getting Started<a id="getting-started"></a>

```python
from pprint import pprint
from proovid_python_sdk import ProoViD, ApiException

proovid = ProoViD(
    bearer="YOUR_API_KEY",
)

try:
    create_natural_person_elv_response = proovid.address.create_natural_person_elv(
        natural_person_index_id=1,
        street="string_example",
        street_number="string_example",
        unit="string_example",
        zip_code="string_example",
        city="string_example",
        district="string_example",
        region="string_example",
        country="string_example",
        email="string_example",
        mobile="string_example",
        full_address="string_example",
    )
    print(create_natural_person_elv_response)
except ApiException as e:
    print("Exception when calling AddressApi.create_natural_person_elv: %s\n" % e)
    pprint(e.body)
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```

## Async<a id="async"></a>

`async` support is available by prepending `a` to any method.

```python
import asyncio
from pprint import pprint
from proovid_python_sdk import ProoViD, ApiException

proovid = ProoViD(
    bearer="YOUR_API_KEY",
)


async def main():
    try:
        create_natural_person_elv_response = (
            await proovid.address.acreate_natural_person_elv(
                natural_person_index_id=1,
                street="string_example",
                street_number="string_example",
                unit="string_example",
                zip_code="string_example",
                city="string_example",
                district="string_example",
                region="string_example",
                country="string_example",
                email="string_example",
                mobile="string_example",
                full_address="string_example",
            )
        )
        print(create_natural_person_elv_response)
    except ApiException as e:
        print("Exception when calling AddressApi.create_natural_person_elv: %s\n" % e)
        pprint(e.body)
        pprint(e.headers)
        pprint(e.status)
        pprint(e.reason)
        pprint(e.round_trip_time)


asyncio.run(main())
```

## Raw HTTP Response<a id="raw-http-response"></a>

To access raw HTTP response values, use the `.raw` namespace.

```python
from pprint import pprint
from proovid_python_sdk import ProoViD, ApiException

proovid = ProoViD(
    bearer="YOUR_API_KEY",
)

try:
    create_natural_person_elv_response = proovid.address.raw.create_natural_person_elv(
        natural_person_index_id=1,
        street="string_example",
        street_number="string_example",
        unit="string_example",
        zip_code="string_example",
        city="string_example",
        district="string_example",
        region="string_example",
        country="string_example",
        email="string_example",
        mobile="string_example",
        full_address="string_example",
    )
    pprint(create_natural_person_elv_response.body)
    pprint(create_natural_person_elv_response.body["id"])
    pprint(create_natural_person_elv_response.body["reference"])
    pprint(create_natural_person_elv_response.body["status"])
    pprint(create_natural_person_elv_response.body["verification_level"])
    pprint(create_natural_person_elv_response.body["levels"])
    pprint(create_natural_person_elv_response.body["document_verification"])
    pprint(create_natural_person_elv_response.body["user_verification_url"])
    pprint(create_natural_person_elv_response.body["qr_code"])
    pprint(create_natural_person_elv_response.body["creation_time"])
    pprint(create_natural_person_elv_response.body["error"])
    pprint(create_natural_person_elv_response.headers)
    pprint(create_natural_person_elv_response.status)
    pprint(create_natural_person_elv_response.round_trip_time)
except ApiException as e:
    print("Exception when calling AddressApi.create_natural_person_elv: %s\n" % e)
    pprint(e.body)
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```


## Reference<a id="reference"></a>
### `proovid.address.create_natural_person_elv`<a id="proovidaddresscreate_natural_person_elv"></a>



#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_natural_person_elv_response = proovid.address.create_natural_person_elv(
    natural_person_index_id=1,
    street="string_example",
    street_number="string_example",
    unit="string_example",
    zip_code="string_example",
    city="string_example",
    district="string_example",
    region="string_example",
    country="string_example",
    email="string_example",
    mobile="string_example",
    full_address="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### natural_person_index_id: `int`<a id="natural_person_index_id-int"></a>

##### street: `Optional[str]`<a id="street-optionalstr"></a>

##### street_number: `Optional[str]`<a id="street_number-optionalstr"></a>

##### unit: `Optional[str]`<a id="unit-optionalstr"></a>

##### zip_code: `Optional[str]`<a id="zip_code-optionalstr"></a>

##### city: `Optional[str]`<a id="city-optionalstr"></a>

##### district: `Optional[str]`<a id="district-optionalstr"></a>

##### region: `Optional[str]`<a id="region-optionalstr"></a>

##### country: `Optional[str]`<a id="country-optionalstr"></a>

##### email: `Optional[str]`<a id="email-optionalstr"></a>

##### mobile: `Optional[str]`<a id="mobile-optionalstr"></a>

##### full_address: `Optional[str]`<a id="full_address-optionalstr"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`NaturalPersonELVRequest`](./proovid_python_sdk/type/natural_person_elv_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`AddressVerificationResult`](./proovid_python_sdk/pydantic/address_verification_result.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/Address/NaturalPersonELV` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `proovid.address.link_response`<a id="proovidaddresslink_response"></a>



#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
proovid.address.link_response(
    link="string_example",
    coords=[{}],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### link: `Optional[str]`<a id="link-optionalstr"></a>

##### coords: List[`GpsLocation`]<a id="coords-listgpslocation"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`InfoGps`](./proovid_python_sdk/type/info_gps.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/Address/LinkResponse` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `proovid.address.verify_by_id`<a id="proovidaddressverify_by_id"></a>



#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
verify_by_id_response = proovid.address.verify_by_id(
    id=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `int`<a id="id-int"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`AddressVerificationResult`](./proovid_python_sdk/pydantic/address_verification_result.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/Address/AddressVerification/{id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `proovid.address.verify_by_id_0`<a id="proovidaddressverify_by_id_0"></a>



#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
verify_by_id_0_response = proovid.address.verify_by_id_0(
    id=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `int`<a id="id-int"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`AddressVerificationDeleteResult`](./proovid_python_sdk/pydantic/address_verification_delete_result.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/Address/AddressVerification/{id}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `proovid.address.verify_by_level`<a id="proovidaddressverify_by_level"></a>



#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
verify_by_level_response = proovid.address.verify_by_level(
    reference_id="string_example",
    email="string_example",
    natural_person_id=1,
    natural_person_index_id=1,
    name="string_example",
    surname="string_example",
    mobile_phone="string_example",
    language="string_example",
    verification_level=1,
    document="string_example",
    street="string_example",
    street_number="string_example",
    unit="string_example",
    district="string_example",
    city="string_example",
    region="string_example",
    zip_code="string_example",
    country="string_example",
    full_address="string_example",
    skip_document_comparison=True,
    validity_period=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### reference_id: `Optional[str]`<a id="reference_id-optionalstr"></a>

##### email: `Optional[str]`<a id="email-optionalstr"></a>

##### natural_person_id: `Optional[int]`<a id="natural_person_id-optionalint"></a>

##### natural_person_index_id: `Optional[int]`<a id="natural_person_index_id-optionalint"></a>

##### name: `Optional[str]`<a id="name-optionalstr"></a>

##### surname: `Optional[str]`<a id="surname-optionalstr"></a>

##### mobile_phone: `Optional[str]`<a id="mobile_phone-optionalstr"></a>

##### language: `Optional[str]`<a id="language-optionalstr"></a>

##### verification_level: `int`<a id="verification_level-int"></a>

##### document: `Optional[str]`<a id="document-optionalstr"></a>

##### street: `Optional[str]`<a id="street-optionalstr"></a>

##### street_number: `Optional[str]`<a id="street_number-optionalstr"></a>

##### unit: `Optional[str]`<a id="unit-optionalstr"></a>

##### district: `Optional[str]`<a id="district-optionalstr"></a>

##### city: `Optional[str]`<a id="city-optionalstr"></a>

##### region: `Optional[str]`<a id="region-optionalstr"></a>

##### zip_code: `Optional[str]`<a id="zip_code-optionalstr"></a>

##### country: `Optional[str]`<a id="country-optionalstr"></a>

##### full_address: `Optional[str]`<a id="full_address-optionalstr"></a>

##### skip_document_comparison: `bool`<a id="skip_document_comparison-bool"></a>

##### validity_period: `int`<a id="validity_period-int"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`AddressRequest`](./proovid_python_sdk/type/address_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`AddressVerificationResult`](./proovid_python_sdk/pydantic/address_verification_result.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/Address/VerificationByLevel` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `proovid.address.verify_certificate_pdf`<a id="proovidaddressverify_certificate_pdf"></a>



#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
verify_certificate_pdf_response = proovid.address.verify_certificate_pdf(
    id=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `int`<a id="id-int"></a>

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/Address/AddressVerification/{id}/certificate.pdf` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `proovid.document.get_certificate`<a id="prooviddocumentget_certificate"></a>



#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_certificate_response = proovid.document.get_certificate(
    id=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `int`<a id="id-int"></a>

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/Document/DocumentVerification/{id}/certificate.pdf` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `proovid.document.verify_deletion`<a id="prooviddocumentverify_deletion"></a>



#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
verify_deletion_response = proovid.document.verify_deletion(
    id=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `int`<a id="id-int"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`DeleteDocumentVerificationResponse`](./proovid_python_sdk/pydantic/delete_document_verification_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/Document/DocumentVerification/{id}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `proovid.document.verify_status`<a id="prooviddocumentverify_status"></a>



#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
verify_status_response = proovid.document.verify_status(
    id=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `int`<a id="id-int"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`DocumentVerificationResponse`](./proovid_python_sdk/pydantic/document_verification_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/Document/DocumentVerification/{id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `proovid.document.verify_status_0`<a id="prooviddocumentverify_status_0"></a>



#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
verify_status_0_response = proovid.document.verify_status_0(
    email="string_example",
    country="string_example",
    document="string_example",
    additional_document="string_example",
    face="string_example",
    document_type="string_example",
    natural_person_id=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### email: `Optional[str]`<a id="email-optionalstr"></a>

##### country: `Optional[str]`<a id="country-optionalstr"></a>

##### document: `Optional[str]`<a id="document-optionalstr"></a>

##### additional_document: `Optional[str]`<a id="additional_document-optionalstr"></a>

##### face: `Optional[str]`<a id="face-optionalstr"></a>

##### document_type: `Optional[str]`<a id="document_type-optionalstr"></a>

##### natural_person_id: `Optional[int]`<a id="natural_person_id-optionalint"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`DocumentVerificationRequest`](./proovid_python_sdk/type/document_verification_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`DocumentVerificationResponse`](./proovid_python_sdk/pydantic/document_verification_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/Document/VerifyDocument` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `proovid.health.get_version`<a id="proovidhealthget_version"></a>



#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
proovid.health.get_version()
```

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/Health/Version` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `proovid.health.status_check`<a id="proovidhealthstatus_check"></a>



#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
proovid.health.status_check()
```

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/Health/Status` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `proovid.natural_person.create_or_update`<a id="proovidnatural_personcreate_or_update"></a>



#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_or_update_response = proovid.natural_person.create_or_update(
    info={},
    client_reference_id="string_example",
    documents={},
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### info: [`AddNaturalPersonInfoRequest`](./proovid_python_sdk/type/add_natural_person_info_request.py)<a id="info-addnaturalpersoninforequestproovid_python_sdktypeadd_natural_person_info_requestpy"></a>


##### client_reference_id: `Optional[str]`<a id="client_reference_id-optionalstr"></a>

##### documents: [`NaturalPersonDocumentsRequest`](./proovid_python_sdk/type/natural_person_documents_request.py)<a id="documents-naturalpersondocumentsrequestproovid_python_sdktypenatural_person_documents_requestpy"></a>


#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`AddNaturalPersonRequest`](./proovid_python_sdk/type/add_natural_person_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`AddNaturalPersonResponseBaseResponse`](./proovid_python_sdk/pydantic/add_natural_person_response_base_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/NaturalPerson` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `proovid.natural_person.delete_by_id`<a id="proovidnatural_persondelete_by_id"></a>



#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
delete_by_id_response = proovid.natural_person.delete_by_id(
    id=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `int`<a id="id-int"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`DeleteAmlReport`](./proovid_python_sdk/pydantic/delete_aml_report.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/NaturalPerson/{id}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `proovid.natural_person.get_by_id`<a id="proovidnatural_personget_by_id"></a>



#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_by_id_response = proovid.natural_person.get_by_id(
    id=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `int`<a id="id-int"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`AmlReport`](./proovid_python_sdk/pydantic/aml_report.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/NaturalPerson/{id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `proovid.natural_person.get_by_id_0`<a id="proovidnatural_personget_by_id_0"></a>



#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_by_id_0_response = proovid.natural_person.get_by_id_0(
    reference="reference_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### reference: `str`<a id="reference-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`AmlReport`](./proovid_python_sdk/pydantic/aml_report.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/NaturalPerson/{reference}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `proovid.natural_person.get_certificate`<a id="proovidnatural_personget_certificate"></a>



#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_certificate_response = proovid.natural_person.get_certificate(
    natural_person_id=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### natural_person_id: `int`<a id="natural_person_id-int"></a>

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/NaturalPerson/{naturalPersonId}/certificate` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `proovid.natural_person.get_details`<a id="proovidnatural_personget_details"></a>



#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_details_response = proovid.natural_person.get_details(
    natural_person_id=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### natural_person_id: `int`<a id="natural_person_id-int"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`NaturalPersonResponseBaseResponse`](./proovid_python_sdk/pydantic/natural_person_response_base_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/NaturalPerson/{naturalPersonId}/get` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `proovid.natural_person.get_verification_record`<a id="proovidnatural_personget_verification_record"></a>



#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_verification_record_response = proovid.natural_person.get_verification_record(
    verification_id=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### verification_id: `int`<a id="verification_id-int"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`NaturalPersonInfoResponseBaseResponse`](./proovid_python_sdk/pydantic/natural_person_info_response_base_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/NaturalPerson/verificationRecord/{verificationId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `proovid.natural_person.get_verifications`<a id="proovidnatural_personget_verifications"></a>



#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_verifications_response = proovid.natural_person.get_verifications(
    natural_person_id=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### natural_person_id: `int`<a id="natural_person_id-int"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`SumSubVerificationResponseListBaseResponse`](./proovid_python_sdk/pydantic/sum_sub_verification_response_list_base_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/NaturalPerson/{naturalPersonId}/verifications` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `proovid.natural_person.remove_by_id`<a id="proovidnatural_personremove_by_id"></a>



#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
remove_by_id_response = proovid.natural_person.remove_by_id(
    natural_person_id=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### natural_person_id: `int`<a id="natural_person_id-int"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`BaseResponse`](./proovid_python_sdk/pydantic/base_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/NaturalPerson/{naturalPersonId}/delete` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `proovid.natural_person.update_documents`<a id="proovidnatural_personupdate_documents"></a>



#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_documents_response = proovid.natural_person.update_documents(
    natural_person_id=1,
    id_document={
        "document_type": 0,
    },
    address_document={},
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### natural_person_id: `int`<a id="natural_person_id-int"></a>

##### id_document: [`NaturalPersonIdDocumentRequest`](./proovid_python_sdk/type/natural_person_id_document_request.py)<a id="id_document-naturalpersoniddocumentrequestproovid_python_sdktypenatural_person_id_document_requestpy"></a>


##### address_document: [`NaturalPersonDocumentRequest`](./proovid_python_sdk/type/natural_person_document_request.py)<a id="address_document-naturalpersondocumentrequestproovid_python_sdktypenatural_person_document_requestpy"></a>


#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`NaturalPersonDocumentsRequest`](./proovid_python_sdk/type/natural_person_documents_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`UpdateNaturalPersonDocumentsResponseBaseResponse`](./proovid_python_sdk/pydantic/update_natural_person_documents_response_base_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/NaturalPerson/{naturalPersonId}/updateDocuments` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `proovid.natural_person.update_information`<a id="proovidnatural_personupdate_information"></a>



#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_information_response = proovid.natural_person.update_information(
    natural_person_id=1,
    client_reference_id="string_example",
    tax_id="string_example",
    first_name="string_example",
    last_name="string_example",
    middle_name="string_example",
    legal_name="string_example",
    date_of_birth="1970-01-01T00:00:00.00Z",
    gender=0,
    country_birth="string_example",
    country_residence="string_example",
    country_main_business="string_example",
    nationality="string_example",
    email="string_example",
    email_two="string_example",
    mobile_phone="string_example",
    mobile_phone_two="string_example",
    automatically_update_np_risk=True,
    risk_level=0,
    risk_level_justification="string_example",
    is_flagged=True,
    comments="string_example",
    economic_profile={
        "size_of_annual_income": 0,
        "main_source_of_income": 0,
        "size_of_wealth": 0,
        "source_of_wealth": 0,
        "anticipated_account_turn_over": 0,
    },
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### natural_person_id: `int`<a id="natural_person_id-int"></a>

##### client_reference_id: `Optional[str]`<a id="client_reference_id-optionalstr"></a>

##### tax_id: `Optional[str]`<a id="tax_id-optionalstr"></a>

##### first_name: `Optional[str]`<a id="first_name-optionalstr"></a>

##### last_name: `Optional[str]`<a id="last_name-optionalstr"></a>

##### middle_name: `Optional[str]`<a id="middle_name-optionalstr"></a>

##### legal_name: `Optional[str]`<a id="legal_name-optionalstr"></a>

##### date_of_birth: `Optional[datetime]`<a id="date_of_birth-optionaldatetime"></a>

##### gender: [`EGender`](./proovid_python_sdk/type/e_gender.py)<a id="gender-egenderproovid_python_sdktypee_genderpy"></a>

##### country_birth: `Optional[str]`<a id="country_birth-optionalstr"></a>

##### country_residence: `Optional[str]`<a id="country_residence-optionalstr"></a>

##### country_main_business: `Optional[str]`<a id="country_main_business-optionalstr"></a>

##### nationality: `Optional[str]`<a id="nationality-optionalstr"></a>

##### email: `Optional[str]`<a id="email-optionalstr"></a>

##### email_two: `Optional[str]`<a id="email_two-optionalstr"></a>

##### mobile_phone: `Optional[str]`<a id="mobile_phone-optionalstr"></a>

##### mobile_phone_two: `Optional[str]`<a id="mobile_phone_two-optionalstr"></a>

##### automatically_update_np_risk: `Optional[bool]`<a id="automatically_update_np_risk-optionalbool"></a>

##### risk_level: [`EScore`](./proovid_python_sdk/type/e_score.py)<a id="risk_level-escoreproovid_python_sdktypee_scorepy"></a>

##### risk_level_justification: `Optional[str]`<a id="risk_level_justification-optionalstr"></a>

##### is_flagged: `bool`<a id="is_flagged-bool"></a>

##### comments: `Optional[str]`<a id="comments-optionalstr"></a>

##### economic_profile: [`UpdateNaturalPersonEconomicProfileRequest`](./proovid_python_sdk/type/update_natural_person_economic_profile_request.py)<a id="economic_profile-updatenaturalpersoneconomicprofilerequestproovid_python_sdktypeupdate_natural_person_economic_profile_requestpy"></a>


#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`UpdateNaturalPersonInfoRequest`](./proovid_python_sdk/type/update_natural_person_info_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`NaturalPersonInfoResponseBaseResponse`](./proovid_python_sdk/pydantic/natural_person_info_response_base_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/NaturalPerson/{naturalPersonId}/updateInfo` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `proovid.natural_person.verify_details`<a id="proovidnatural_personverify_details"></a>



#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
verify_details_response = proovid.natural_person.verify_details(
    info={},
    client_reference_id="string_example",
    documents={},
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### info: [`AddNaturalPersonInfoRequest`](./proovid_python_sdk/type/add_natural_person_info_request.py)<a id="info-addnaturalpersoninforequestproovid_python_sdktypeadd_natural_person_info_requestpy"></a>


##### client_reference_id: `Optional[str]`<a id="client_reference_id-optionalstr"></a>

##### documents: [`NaturalPersonDocumentsRequest`](./proovid_python_sdk/type/natural_person_documents_request.py)<a id="documents-naturalpersondocumentsrequestproovid_python_sdktypenatural_person_documents_requestpy"></a>


#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`AddNaturalPersonRequest`](./proovid_python_sdk/type/add_natural_person_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`AddNaturalPersonResponseBaseResponse`](./proovid_python_sdk/pydantic/add_natural_person_response_base_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/NaturalPerson/verify` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `proovid.natural_person.verify_details_0`<a id="proovidnatural_personverify_details_0"></a>



#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
verify_details_0_response = proovid.natural_person.verify_details_0(
    natural_person_id=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### natural_person_id: `int`<a id="natural_person_id-int"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`SumSubVerificationResponseBaseResponse`](./proovid_python_sdk/pydantic/sum_sub_verification_response_base_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/NaturalPerson/{naturalPersonId}/verify` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `proovid.natural_person.verify_documents`<a id="proovidnatural_personverify_documents"></a>



#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
verify_documents_response = proovid.natural_person.verify_documents(
    natural_person_id=1,
    id_document={
        "document_type": 0,
    },
    address_document={},
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### natural_person_id: `int`<a id="natural_person_id-int"></a>

##### id_document: [`NaturalPersonIdDocumentRequest`](./proovid_python_sdk/type/natural_person_id_document_request.py)<a id="id_document-naturalpersoniddocumentrequestproovid_python_sdktypenatural_person_id_document_requestpy"></a>


##### address_document: [`NaturalPersonDocumentRequest`](./proovid_python_sdk/type/natural_person_document_request.py)<a id="address_document-naturalpersondocumentrequestproovid_python_sdktypenatural_person_document_requestpy"></a>


#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`NaturalPersonDocumentsRequest`](./proovid_python_sdk/type/natural_person_documents_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`UpdateNaturalPersonDocumentsResponseBaseResponse`](./proovid_python_sdk/pydantic/update_natural_person_documents_response_base_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/NaturalPerson/{naturalPersonId}/updateDocuments/verify` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `proovid.natural_person.verify_entity`<a id="proovidnatural_personverify_entity"></a>



#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
verify_entity_response = proovid.natural_person.verify_entity(
    info={},
    client_reference_id="string_example",
    documents={},
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### info: [`AddNaturalPersonInfoRequest`](./proovid_python_sdk/type/add_natural_person_info_request.py)<a id="info-addnaturalpersoninforequestproovid_python_sdktypeadd_natural_person_info_requestpy"></a>


##### client_reference_id: `Optional[str]`<a id="client_reference_id-optionalstr"></a>

##### documents: [`NaturalPersonDocumentsRequest`](./proovid_python_sdk/type/natural_person_documents_request.py)<a id="documents-naturalpersondocumentsrequestproovid_python_sdktypenatural_person_documents_requestpy"></a>


#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`AddNaturalPersonRequest`](./proovid_python_sdk/type/add_natural_person_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`AddNaturalPersonResponseBaseResponse`](./proovid_python_sdk/pydantic/add_natural_person_response_base_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/NaturalPerson/verifyentity` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `proovid.screening.get_aml_report`<a id="proovidscreeningget_aml_report"></a>



#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_aml_report_response = proovid.screening.get_aml_report(
    reference="reference_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### reference: `str`<a id="reference-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`AmlReport`](./proovid_python_sdk/pydantic/aml_report.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/Screening/AmlReport/{reference}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `proovid.screening.get_natural_person_by_id`<a id="proovidscreeningget_natural_person_by_id"></a>



#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_natural_person_by_id_response = proovid.screening.get_natural_person_by_id(
    id=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `int`<a id="id-int"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`AmlReport`](./proovid_python_sdk/pydantic/aml_report.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/Screening/NaturalPerson/{id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `proovid.screening.remove_natural_person`<a id="proovidscreeningremove_natural_person"></a>



#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
remove_natural_person_response = proovid.screening.remove_natural_person(
    id=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `int`<a id="id-int"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`DeleteAmlReport`](./proovid_python_sdk/pydantic/delete_aml_report.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/Screening/NaturalPerson/{id}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `proovid.screening.submit_natural_person_screening`<a id="proovidscreeningsubmit_natural_person_screening"></a>



#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
submit_natural_person_screening_response = (
    proovid.screening.submit_natural_person_screening(
        natural_person_id=1,
        first_name="string_example",
        middle_name="string_example",
        last_name="string_example",
        dob="1970-01-01T00:00:00.00Z",
        partial_match="string_example",
        document="string_example",
        document_type="string_example",
    )
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### natural_person_id: `Optional[int]`<a id="natural_person_id-optionalint"></a>

##### first_name: `Optional[str]`<a id="first_name-optionalstr"></a>

##### middle_name: `Optional[str]`<a id="middle_name-optionalstr"></a>

##### last_name: `Optional[str]`<a id="last_name-optionalstr"></a>

##### dob: `datetime`<a id="dob-datetime"></a>

##### partial_match: `Optional[str]`<a id="partial_match-optionalstr"></a>

##### document: `Optional[str]`<a id="document-optionalstr"></a>

##### document_type: `Optional[str]`<a id="document_type-optionalstr"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`NaturalPersonRequest`](./proovid_python_sdk/type/natural_person_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`AmlReport`](./proovid_python_sdk/pydantic/aml_report.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/Screening/NaturalPerson` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---


## Author<a id="author"></a>
This Python package is automatically generated by [Konfig](https://konfigthis.com)
