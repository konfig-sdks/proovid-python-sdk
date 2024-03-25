import typing_extensions

from proovid_python_sdk.paths import PathValues
from proovid_python_sdk.apis.paths.api_address_address_verification_id import ApiAddressAddressVerificationId
from proovid_python_sdk.apis.paths.api_address_address_verification_id_certificate_pdf import ApiAddressAddressVerificationIdCertificatePdf
from proovid_python_sdk.apis.paths.api_address_verification_by_level import ApiAddressVerificationByLevel
from proovid_python_sdk.apis.paths.api_address_natural_person_elv import ApiAddressNaturalPersonELV
from proovid_python_sdk.apis.paths.api_address_link_response import ApiAddressLinkResponse
from proovid_python_sdk.apis.paths.api_document_document_verification_id import ApiDocumentDocumentVerificationId
from proovid_python_sdk.apis.paths.api_document_document_verification_id_certificate_pdf import ApiDocumentDocumentVerificationIdCertificatePdf
from proovid_python_sdk.apis.paths.api_document_verify_document import ApiDocumentVerifyDocument
from proovid_python_sdk.apis.paths.api_health_status import ApiHealthStatus
from proovid_python_sdk.apis.paths.api_health_version import ApiHealthVersion
from proovid_python_sdk.apis.paths.api_natural_person import ApiNaturalPerson
from proovid_python_sdk.apis.paths.api_natural_person_verify import ApiNaturalPersonVerify
from proovid_python_sdk.apis.paths.api_natural_person_verifyentity import ApiNaturalPersonVerifyentity
from proovid_python_sdk.apis.paths.api_natural_person_natural_person_id_update_documents import ApiNaturalPersonNaturalPersonIdUpdateDocuments
from proovid_python_sdk.apis.paths.api_natural_person_natural_person_id_update_documents_verify import ApiNaturalPersonNaturalPersonIdUpdateDocumentsVerify
from proovid_python_sdk.apis.paths.api_natural_person_natural_person_id_verify import ApiNaturalPersonNaturalPersonIdVerify
from proovid_python_sdk.apis.paths.api_natural_person_natural_person_id_get import ApiNaturalPersonNaturalPersonIdGet
from proovid_python_sdk.apis.paths.api_natural_person_natural_person_id_update_info import ApiNaturalPersonNaturalPersonIdUpdateInfo
from proovid_python_sdk.apis.paths.api_natural_person_verification_record_verification_id import ApiNaturalPersonVerificationRecordVerificationId
from proovid_python_sdk.apis.paths.api_natural_person_natural_person_id_certificate import ApiNaturalPersonNaturalPersonIdCertificate
from proovid_python_sdk.apis.paths.api_natural_person_natural_person_id_delete import ApiNaturalPersonNaturalPersonIdDelete
from proovid_python_sdk.apis.paths.api_natural_person_natural_person_id_verifications import ApiNaturalPersonNaturalPersonIdVerifications
from proovid_python_sdk.apis.paths.api_natural_person_id import ApiNaturalPersonId
from proovid_python_sdk.apis.paths.api_natural_person_reference import ApiNaturalPersonReference
from proovid_python_sdk.apis.paths.api_screening_natural_person import ApiScreeningNaturalPerson
from proovid_python_sdk.apis.paths.api_screening_natural_person_id import ApiScreeningNaturalPersonId
from proovid_python_sdk.apis.paths.api_screening_aml_report_reference import ApiScreeningAmlReportReference

PathToApi = typing_extensions.TypedDict(
    'PathToApi',
    {
        PathValues.API_ADDRESS_ADDRESS_VERIFICATION_ID: ApiAddressAddressVerificationId,
        PathValues.API_ADDRESS_ADDRESS_VERIFICATION_ID_CERTIFICATE_PDF: ApiAddressAddressVerificationIdCertificatePdf,
        PathValues.API_ADDRESS_VERIFICATION_BY_LEVEL: ApiAddressVerificationByLevel,
        PathValues.API_ADDRESS_NATURAL_PERSON_ELV: ApiAddressNaturalPersonELV,
        PathValues.API_ADDRESS_LINK_RESPONSE: ApiAddressLinkResponse,
        PathValues.API_DOCUMENT_DOCUMENT_VERIFICATION_ID: ApiDocumentDocumentVerificationId,
        PathValues.API_DOCUMENT_DOCUMENT_VERIFICATION_ID_CERTIFICATE_PDF: ApiDocumentDocumentVerificationIdCertificatePdf,
        PathValues.API_DOCUMENT_VERIFY_DOCUMENT: ApiDocumentVerifyDocument,
        PathValues.API_HEALTH_STATUS: ApiHealthStatus,
        PathValues.API_HEALTH_VERSION: ApiHealthVersion,
        PathValues.API_NATURAL_PERSON: ApiNaturalPerson,
        PathValues.API_NATURAL_PERSON_VERIFY: ApiNaturalPersonVerify,
        PathValues.API_NATURAL_PERSON_VERIFYENTITY: ApiNaturalPersonVerifyentity,
        PathValues.API_NATURAL_PERSON_NATURAL_PERSON_ID_UPDATE_DOCUMENTS: ApiNaturalPersonNaturalPersonIdUpdateDocuments,
        PathValues.API_NATURAL_PERSON_NATURAL_PERSON_ID_UPDATE_DOCUMENTS_VERIFY: ApiNaturalPersonNaturalPersonIdUpdateDocumentsVerify,
        PathValues.API_NATURAL_PERSON_NATURAL_PERSON_ID_VERIFY: ApiNaturalPersonNaturalPersonIdVerify,
        PathValues.API_NATURAL_PERSON_NATURAL_PERSON_ID_GET: ApiNaturalPersonNaturalPersonIdGet,
        PathValues.API_NATURAL_PERSON_NATURAL_PERSON_ID_UPDATE_INFO: ApiNaturalPersonNaturalPersonIdUpdateInfo,
        PathValues.API_NATURAL_PERSON_VERIFICATION_RECORD_VERIFICATION_ID: ApiNaturalPersonVerificationRecordVerificationId,
        PathValues.API_NATURAL_PERSON_NATURAL_PERSON_ID_CERTIFICATE: ApiNaturalPersonNaturalPersonIdCertificate,
        PathValues.API_NATURAL_PERSON_NATURAL_PERSON_ID_DELETE: ApiNaturalPersonNaturalPersonIdDelete,
        PathValues.API_NATURAL_PERSON_NATURAL_PERSON_ID_VERIFICATIONS: ApiNaturalPersonNaturalPersonIdVerifications,
        PathValues.API_NATURAL_PERSON_ID: ApiNaturalPersonId,
        PathValues.API_NATURAL_PERSON_REFERENCE: ApiNaturalPersonReference,
        PathValues.API_SCREENING_NATURAL_PERSON: ApiScreeningNaturalPerson,
        PathValues.API_SCREENING_NATURAL_PERSON_ID: ApiScreeningNaturalPersonId,
        PathValues.API_SCREENING_AML_REPORT_REFERENCE: ApiScreeningAmlReportReference,
    }
)

path_to_api = PathToApi(
    {
        PathValues.API_ADDRESS_ADDRESS_VERIFICATION_ID: ApiAddressAddressVerificationId,
        PathValues.API_ADDRESS_ADDRESS_VERIFICATION_ID_CERTIFICATE_PDF: ApiAddressAddressVerificationIdCertificatePdf,
        PathValues.API_ADDRESS_VERIFICATION_BY_LEVEL: ApiAddressVerificationByLevel,
        PathValues.API_ADDRESS_NATURAL_PERSON_ELV: ApiAddressNaturalPersonELV,
        PathValues.API_ADDRESS_LINK_RESPONSE: ApiAddressLinkResponse,
        PathValues.API_DOCUMENT_DOCUMENT_VERIFICATION_ID: ApiDocumentDocumentVerificationId,
        PathValues.API_DOCUMENT_DOCUMENT_VERIFICATION_ID_CERTIFICATE_PDF: ApiDocumentDocumentVerificationIdCertificatePdf,
        PathValues.API_DOCUMENT_VERIFY_DOCUMENT: ApiDocumentVerifyDocument,
        PathValues.API_HEALTH_STATUS: ApiHealthStatus,
        PathValues.API_HEALTH_VERSION: ApiHealthVersion,
        PathValues.API_NATURAL_PERSON: ApiNaturalPerson,
        PathValues.API_NATURAL_PERSON_VERIFY: ApiNaturalPersonVerify,
        PathValues.API_NATURAL_PERSON_VERIFYENTITY: ApiNaturalPersonVerifyentity,
        PathValues.API_NATURAL_PERSON_NATURAL_PERSON_ID_UPDATE_DOCUMENTS: ApiNaturalPersonNaturalPersonIdUpdateDocuments,
        PathValues.API_NATURAL_PERSON_NATURAL_PERSON_ID_UPDATE_DOCUMENTS_VERIFY: ApiNaturalPersonNaturalPersonIdUpdateDocumentsVerify,
        PathValues.API_NATURAL_PERSON_NATURAL_PERSON_ID_VERIFY: ApiNaturalPersonNaturalPersonIdVerify,
        PathValues.API_NATURAL_PERSON_NATURAL_PERSON_ID_GET: ApiNaturalPersonNaturalPersonIdGet,
        PathValues.API_NATURAL_PERSON_NATURAL_PERSON_ID_UPDATE_INFO: ApiNaturalPersonNaturalPersonIdUpdateInfo,
        PathValues.API_NATURAL_PERSON_VERIFICATION_RECORD_VERIFICATION_ID: ApiNaturalPersonVerificationRecordVerificationId,
        PathValues.API_NATURAL_PERSON_NATURAL_PERSON_ID_CERTIFICATE: ApiNaturalPersonNaturalPersonIdCertificate,
        PathValues.API_NATURAL_PERSON_NATURAL_PERSON_ID_DELETE: ApiNaturalPersonNaturalPersonIdDelete,
        PathValues.API_NATURAL_PERSON_NATURAL_PERSON_ID_VERIFICATIONS: ApiNaturalPersonNaturalPersonIdVerifications,
        PathValues.API_NATURAL_PERSON_ID: ApiNaturalPersonId,
        PathValues.API_NATURAL_PERSON_REFERENCE: ApiNaturalPersonReference,
        PathValues.API_SCREENING_NATURAL_PERSON: ApiScreeningNaturalPerson,
        PathValues.API_SCREENING_NATURAL_PERSON_ID: ApiScreeningNaturalPersonId,
        PathValues.API_SCREENING_AML_REPORT_REFERENCE: ApiScreeningAmlReportReference,
    }
)
