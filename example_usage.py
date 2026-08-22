from client import AiAmbientScribeClinicalDocumentationGeneratorClient

def main():
    client = AiAmbientScribeClinicalDocumentationGeneratorClient()
    audio = 'Patient reports fatigue for three weeks and mild shortness of breath...'
    ctx = {'patient_age': 52, 'gender': 'M', 'visit_type': 'follow-up'}
    res = client.transcribe_and_document(audio, ctx, 'primary_care')
    print('Specialty: ' + res['specialty'] + ' | Accuracy: ' + str(res['accuracy_score']) + '%')
    print('Time Saved: ' + str(res['documentation_time_saved_minutes']) + ' minutes')
    print('ICD-10 Codes: ' + str(res['icd10_codes_suggested']))
    note = res['soap_note']
    print('SOAP Note:')
    for section, text in note.items():
        print('  [' + section.upper() + '] ' + text[:80] + '...')

if __name__ == '__main__':
    main()
