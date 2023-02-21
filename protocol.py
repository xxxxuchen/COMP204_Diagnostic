from patient import Patient
from symptoms import Symptoms

class Protocol:
    '''The Protocol class stores information about the diagnosis procedure'''
    
    def __init__(self, target_patient, list_patients) -> None:
        '''
        Initialize the Protocol object on which the method is called with
        the target_patient on which the protocol will be performed having
        as reference the list of patients list_patients
        '''
        self.patient = target_patient
        self.my_patients = list_patients
        
    def protocol(self) -> str:
        '''Return the diagnostic for self.patient based on the list of self.my_patients
        '''
        similiar_patients = self.patient.similarity_to_patients(self.my_patients)
        diagnostic = self.patient.getting_diagnostics(similiar_patients)
        return diagnostic    
        
if __name__=="__main__":
    # all patients variable is a list of Patient instances
    all_patients = [Patient(56374, Symptoms({"headache","fever"}, {"coughing", "runny_nose","sneezing"}), "meningitis"),
                    Patient(45437, Symptoms({"coughing", "runny_nose"},{"headache","fever"}), "cold"),
                    Patient(16372, Symptoms({"coughing", "sore_throat"},{"fever"}), "cold"),
                    Patient(54324, Symptoms({"vomiting", "coughing","stomach_pain"},{"fever"}), "food_poisoning"),
                    Patient(73454, Symptoms({"coughing", "runny_nose"},{"headache","fever"}), "cold"),
                    Patient(35249, Symptoms({"sore_throat", "coughing","fever"},{"stomach_pain", "runny_nose"}), "pharyngitis"),
                    Patient(44274, Symptoms({"fever", "headache"},{"stomach_pain", "runny_nose","sore_throat", "coughing",}), "meningitis"),
                    Patient(74821, Symptoms({"vomiting", "fever"},{"headache"}), "food_poisoning"),
                    Patient(94231, Symptoms({"stomach_pain", "fever","sore_throat","coughing","headache"},{"vomiting"}), "unknown")]
    
    # diagnose Jaspal
    jaspal = Patient(2, Symptoms({'headache'},{'sneezing'}), 'unknown')
    p = Protocol(jaspal, all_patients)
    print(f'Diagnosis for jaspal: {p.protocol()}')

    # diagnose Yang 
    #yang = Patient(3, Symptoms({"coughing", "runny_nose", "sneezing"},{"headache","fever"}), 'unknown')
    #p = Protocol(yang, all_patients)
    #print(f'Diagnosis for yang: {p.protocol()}')
    