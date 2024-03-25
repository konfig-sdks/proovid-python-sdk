# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from proovid_python_sdk.apis.path_to_api import path_to_api

import enum


class PathValues(str, enum.Enum):
    API_ADDRESS_ADDRESS_VERIFICATION_ID = "/api/Address/AddressVerification/{id}"
    API_ADDRESS_ADDRESS_VERIFICATION_ID_CERTIFICATE_PDF = "/api/Address/AddressVerification/{id}/certificate.pdf"
    API_ADDRESS_VERIFICATION_BY_LEVEL = "/api/Address/VerificationByLevel"
    API_ADDRESS_NATURAL_PERSON_ELV = "/api/Address/NaturalPersonELV"
    API_ADDRESS_LINK_RESPONSE = "/api/Address/LinkResponse"
    API_DOCUMENT_DOCUMENT_VERIFICATION_ID = "/api/Document/DocumentVerification/{id}"
    API_DOCUMENT_DOCUMENT_VERIFICATION_ID_CERTIFICATE_PDF = "/api/Document/DocumentVerification/{id}/certificate.pdf"
    API_DOCUMENT_VERIFY_DOCUMENT = "/api/Document/VerifyDocument"
    API_HEALTH_STATUS = "/api/Health/Status"
    API_HEALTH_VERSION = "/api/Health/Version"
    API_NATURAL_PERSON = "/api/NaturalPerson"
    API_NATURAL_PERSON_VERIFY = "/api/NaturalPerson/verify"
    API_NATURAL_PERSON_VERIFYENTITY = "/api/NaturalPerson/verifyentity"
    API_NATURAL_PERSON_NATURAL_PERSON_ID_UPDATE_DOCUMENTS = "/api/NaturalPerson/{naturalPersonId}/updateDocuments"
    API_NATURAL_PERSON_NATURAL_PERSON_ID_UPDATE_DOCUMENTS_VERIFY = "/api/NaturalPerson/{naturalPersonId}/updateDocuments/verify"
    API_NATURAL_PERSON_NATURAL_PERSON_ID_VERIFY = "/api/NaturalPerson/{naturalPersonId}/verify"
    API_NATURAL_PERSON_NATURAL_PERSON_ID_GET = "/api/NaturalPerson/{naturalPersonId}/get"
    API_NATURAL_PERSON_NATURAL_PERSON_ID_UPDATE_INFO = "/api/NaturalPerson/{naturalPersonId}/updateInfo"
    API_NATURAL_PERSON_VERIFICATION_RECORD_VERIFICATION_ID = "/api/NaturalPerson/verificationRecord/{verificationId}"
    API_NATURAL_PERSON_NATURAL_PERSON_ID_CERTIFICATE = "/api/NaturalPerson/{naturalPersonId}/certificate"
    API_NATURAL_PERSON_NATURAL_PERSON_ID_DELETE = "/api/NaturalPerson/{naturalPersonId}/delete"
    API_NATURAL_PERSON_NATURAL_PERSON_ID_VERIFICATIONS = "/api/NaturalPerson/{naturalPersonId}/verifications"
    API_NATURAL_PERSON_ID = "/api/NaturalPerson/{id}"
    API_NATURAL_PERSON_REFERENCE = "/api/NaturalPerson/{reference}"
    API_SCREENING_NATURAL_PERSON = "/api/Screening/NaturalPerson"
    API_SCREENING_NATURAL_PERSON_ID = "/api/Screening/NaturalPerson/{id}"
    API_SCREENING_AML_REPORT_REFERENCE = "/api/Screening/AmlReport/{reference}"
