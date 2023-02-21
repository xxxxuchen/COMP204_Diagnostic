from typing import Set
from symptoms import Symptoms

class Patient:
    '''The Patient class stores information about a patient '''
    
    def __init__(self, my_patient_ID: int, my_symptoms, my_diagnostic: str) -> None:
        '''
        Initialize the Patient object on which the method is called with
        the integer my_patient_ID, the Symptom object my_symptoms, and the String my_diagnostic
        '''
        self.ID = my_patient_ID
        self.symptoms = my_symptoms
        self.diagnostic = my_diagnostic 
        
    def similarity_to_patients(self, all_patients: list) -> Set[int]:
        """
        Returns a set of the patient Objects with the highest similarity between the symptoms
        of the object self and the symptoms of all the patients stored in the dictionary all_patients.
        """
        highest_sim = -1000000000
        highest_pat = set()
        for p in all_patients:
            sim = self.symptoms.symptom_similarity(p.symptoms)
            if sim == highest_sim:
                highest_pat.add(p)
            elif sim > highest_sim:
                highest_pat.clear()
                highest_sim = sim
                highest_pat.add(p)
        return highest_pat
    
    def getting_diagnostics(self, patient_set : set) -> str:
        """
        Returns a string representing the most frequent diagnostic from the patient_set. 
        """     
        diagnostic_frequencies = {}
        for p in patient_set:
            diag = p.diagnostic
            if diag not in diagnostic_frequencies:
                diagnostic_frequencies[diag] = 1
            else:
                diagnostic_frequencies[diag] += 1
        highest = 0
        highest_diagnostic = ''
        for k in diagnostic_frequencies:
            if diagnostic_frequencies[k] >= highest:
                highest = diagnostic_frequencies[k]
                highest_diagnostic = k
        return highest_diagnostic
    
    def __str__(self) -> str:
        '''
        Returns a String describing the symptom object. 
        '''
        return 'Patient ID= ' + str(self.ID) + '\nSymptoms = ' + str(self.symptoms) + 'Diagnosis:' + str(self.diagnostic)    
    
if __name__ == '__main__':
    p = Patient(56374, Symptoms({"headache","fever"}, {"coughing", "runny_nose","sneezing"}), "meningitis")
    print(p)
    print(str(p))
    sy = Symptoms({"headache","fever"}, {"coughing", "runny_nose","sneezing"})
    
    print(Symptoms)