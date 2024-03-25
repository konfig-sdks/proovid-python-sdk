operation_parameter_map = {
    '/api/Address/NaturalPersonELV-POST': {
        'parameters': [
            {
                'name': 'naturalPersonIndexId'
            },
            {
                'name': 'street'
            },
            {
                'name': 'streetNumber'
            },
            {
                'name': 'unit'
            },
            {
                'name': 'zipCode'
            },
            {
                'name': 'city'
            },
            {
                'name': 'district'
            },
            {
                'name': 'region'
            },
            {
                'name': 'country'
            },
            {
                'name': 'email'
            },
            {
                'name': 'mobile'
            },
            {
                'name': 'fullAddress'
            },
        ]
    },
    '/api/Address/LinkResponse-POST': {
        'parameters': [
            {
                'name': 'link'
            },
            {
                'name': 'coords'
            },
        ]
    },
    '/api/Address/AddressVerification/{id}-GET': {
        'parameters': [
            {
                'name': 'id'
            },
        ]
    },
    '/api/Address/AddressVerification/{id}-DELETE': {
        'parameters': [
            {
                'name': 'id'
            },
        ]
    },
    '/api/Address/VerificationByLevel-POST': {
        'parameters': [
            {
                'name': 'referenceId'
            },
            {
                'name': 'email'
            },
            {
                'name': 'naturalPersonId'
            },
            {
                'name': 'naturalPersonIndexId'
            },
            {
                'name': 'name'
            },
            {
                'name': 'surname'
            },
            {
                'name': 'mobilePhone'
            },
            {
                'name': 'language'
            },
            {
                'name': 'verificationLevel'
            },
            {
                'name': 'document'
            },
            {
                'name': 'street'
            },
            {
                'name': 'streetNumber'
            },
            {
                'name': 'unit'
            },
            {
                'name': 'district'
            },
            {
                'name': 'city'
            },
            {
                'name': 'region'
            },
            {
                'name': 'zipCode'
            },
            {
                'name': 'country'
            },
            {
                'name': 'fullAddress'
            },
            {
                'name': 'skipDocumentComparison'
            },
            {
                'name': 'validityPeriod'
            },
        ]
    },
    '/api/Address/AddressVerification/{id}/certificate.pdf-GET': {
        'parameters': [
            {
                'name': 'id'
            },
        ]
    },
    '/api/Document/DocumentVerification/{id}/certificate.pdf-GET': {
        'parameters': [
            {
                'name': 'id'
            },
        ]
    },
    '/api/Document/DocumentVerification/{id}-DELETE': {
        'parameters': [
            {
                'name': 'id'
            },
        ]
    },
    '/api/Document/DocumentVerification/{id}-GET': {
        'parameters': [
            {
                'name': 'id'
            },
        ]
    },
    '/api/Document/VerifyDocument-POST': {
        'parameters': [
            {
                'name': 'email'
            },
            {
                'name': 'country'
            },
            {
                'name': 'document'
            },
            {
                'name': 'additionalDocument'
            },
            {
                'name': 'face'
            },
            {
                'name': 'documentType'
            },
            {
                'name': 'naturalPersonId'
            },
        ]
    },
    '/api/Health/Version-GET': {
        'parameters': [
        ]
    },
    '/api/Health/Status-GET': {
        'parameters': [
        ]
    },
    '/api/NaturalPerson-POST': {
        'parameters': [
            {
                'name': 'info'
            },
            {
                'name': 'clientReferenceId'
            },
            {
                'name': 'documents'
            },
        ]
    },
    '/api/NaturalPerson/{id}-DELETE': {
        'parameters': [
            {
                'name': 'id'
            },
        ]
    },
    '/api/NaturalPerson/{id}-GET': {
        'parameters': [
            {
                'name': 'id'
            },
        ]
    },
    '/api/NaturalPerson/{reference}-GET': {
        'parameters': [
            {
                'name': 'reference'
            },
        ]
    },
    '/api/NaturalPerson/{naturalPersonId}/certificate-GET': {
        'parameters': [
            {
                'name': 'naturalPersonId'
            },
        ]
    },
    '/api/NaturalPerson/{naturalPersonId}/get-GET': {
        'parameters': [
            {
                'name': 'naturalPersonId'
            },
        ]
    },
    '/api/NaturalPerson/verificationRecord/{verificationId}-GET': {
        'parameters': [
            {
                'name': 'verificationId'
            },
        ]
    },
    '/api/NaturalPerson/{naturalPersonId}/verifications-GET': {
        'parameters': [
            {
                'name': 'naturalPersonId'
            },
        ]
    },
    '/api/NaturalPerson/{naturalPersonId}/delete-DELETE': {
        'parameters': [
            {
                'name': 'naturalPersonId'
            },
        ]
    },
    '/api/NaturalPerson/{naturalPersonId}/updateDocuments-POST': {
        'parameters': [
            {
                'name': 'naturalPersonId'
            },
            {
                'name': 'idDocument'
            },
            {
                'name': 'addressDocument'
            },
        ]
    },
    '/api/NaturalPerson/{naturalPersonId}/updateInfo-POST': {
        'parameters': [
            {
                'name': 'naturalPersonId'
            },
            {
                'name': 'clientReferenceId'
            },
            {
                'name': 'taxId'
            },
            {
                'name': 'firstName'
            },
            {
                'name': 'lastName'
            },
            {
                'name': 'middleName'
            },
            {
                'name': 'legalName'
            },
            {
                'name': 'dateOfBirth'
            },
            {
                'name': 'gender'
            },
            {
                'name': 'countryBirth'
            },
            {
                'name': 'countryResidence'
            },
            {
                'name': 'countryMainBusiness'
            },
            {
                'name': 'nationality'
            },
            {
                'name': 'email'
            },
            {
                'name': 'emailTwo'
            },
            {
                'name': 'mobilePhone'
            },
            {
                'name': 'mobilePhoneTwo'
            },
            {
                'name': 'automaticallyUpdateNPRisk'
            },
            {
                'name': 'riskLevel'
            },
            {
                'name': 'riskLevelJustification'
            },
            {
                'name': 'isFlagged'
            },
            {
                'name': 'comments'
            },
            {
                'name': 'economicProfile'
            },
        ]
    },
    '/api/NaturalPerson/verify-POST': {
        'parameters': [
            {
                'name': 'info'
            },
            {
                'name': 'clientReferenceId'
            },
            {
                'name': 'documents'
            },
        ]
    },
    '/api/NaturalPerson/{naturalPersonId}/verify-POST': {
        'parameters': [
            {
                'name': 'naturalPersonId'
            },
        ]
    },
    '/api/NaturalPerson/{naturalPersonId}/updateDocuments/verify-POST': {
        'parameters': [
            {
                'name': 'naturalPersonId'
            },
            {
                'name': 'idDocument'
            },
            {
                'name': 'addressDocument'
            },
        ]
    },
    '/api/NaturalPerson/verifyentity-POST': {
        'parameters': [
            {
                'name': 'info'
            },
            {
                'name': 'clientReferenceId'
            },
            {
                'name': 'documents'
            },
        ]
    },
    '/api/Screening/AmlReport/{reference}-GET': {
        'parameters': [
            {
                'name': 'reference'
            },
        ]
    },
    '/api/Screening/NaturalPerson/{id}-GET': {
        'parameters': [
            {
                'name': 'id'
            },
        ]
    },
    '/api/Screening/NaturalPerson/{id}-DELETE': {
        'parameters': [
            {
                'name': 'id'
            },
        ]
    },
    '/api/Screening/NaturalPerson-POST': {
        'parameters': [
            {
                'name': 'naturalPersonId'
            },
            {
                'name': 'firstName'
            },
            {
                'name': 'middleName'
            },
            {
                'name': 'lastName'
            },
            {
                'name': 'dob'
            },
            {
                'name': 'partialMatch'
            },
            {
                'name': 'document'
            },
            {
                'name': 'documentType'
            },
        ]
    },
};