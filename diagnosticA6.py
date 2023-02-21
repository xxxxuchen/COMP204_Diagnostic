from typing import Tuple, Set, Dict

### Comments on this implementation:
### - This program is a little bit complicated and hard to follow since data 
###   and code pertaining to different concepts were intermingled

def symptom_similarity(symptoms_A: Tuple[Set], symptoms_B: Tuple[Set]) -> int:
    """
    Returns the similarity between symptoms_A and symptoms_B. symptoms_A and 
    symptoms_B are tuples of a set of symptoms present and a set of symptoms absent.
    The similarity measure is computed by the following equations:
    present_present + absent_absent - present_absent - absent_present
    where:
    present_present is the number of symptoms present in both patients
    absent_absent is the number of symptoms absent in both patients
    present_absent is the number of symptoms present in patientA and absent in patientB
    absent_present is the number of symptoms absent in patientA and present
    in patientB
    >>>symptom_similarity(yang, maria)
    1
    """
    present_present = len(symptoms_A[0].intersection(symptoms_B[0]))
    absent_absent = len(symptoms_A[1].intersection(symptoms_B[1]))
    present_absent = len(symptoms_A[0].intersection(symptoms_B[1]))
    absent_present= len(symptoms_A[1].intersection(symptoms_B[0]))
    return  present_present + absent_absent - present_absent - absent_present

### Regarding symptoms:
### - Data: symptoms present and absent were stored in a tuple and the programmer
###   needs to remember that the first element of the tuple corresponds to the
###   symptoms that are present and the second element of the tuple corresponds to 
###   the symptoms that are absent.
### - Code: symptom_similarity function

def similarity_to_patients(my_symptoms: Tuple[Set], all_patients: Dict[str, Tuple[Set]]) -> Set[int]:
    """
    Returns a set of the patient IDs with the highest similarity between my_symptoms
    (which is a tuple of symptoms present and absent) and the symptoms of
    all the patients stored in the dictionary all_patients.
    >>>similarity_to_patients(yang, all_patients_symptoms)
    {45437, 73454}
     """
    highest_sim = -1000000000
    highest_pat = set()
    for patient_id, symptoms in all_patients.items():
        sim = symptom_similarity(my_symptoms, symptoms)
        if sim == highest_sim:
            highest_pat.add(patient_id)
        elif sim > highest_sim:
            highest_pat.clear()
            highest_sim = sim
            highest_pat.add(patient_id)
    return highest_pat

def getting_diagnostics(patient_set : Set[int], diagnostic_by_patient: Dict[int, str]) -> str:
    """
    Returns a string representing the most frequent diagnostic from 
    the set of diagnostics (stored in the dictionary diagnostic_by_patient)
    of the patient_set (that is a set of ID patients with high similar symptoms)
    >>> getting_diagnostics({45437, 73454}, all_patients_diagnostics)
    'cold'
    """     
    diagnostic_frequencies = {}
    for ID in patient_set:
        diag = diagnostic_by_patient[ID]
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

def protocol(my_symptoms: Tuple[Set], all_patients_symptoms: Dict[str, Tuple[Set]], all_patients_diagnostics: Dict[int, str]) -> str:
    '''
    Return the diagnostic for my_symptoms based on the dictionary of patients
    symptoms (all_patients_symptoms) and the dictionary of patients diagnostics (all_patients_diagnostics).
    >>>protocol(yang, all_patients_symptoms, all_patients_diagnostics)
    'cold'
    '''
    similiar_patients = similarity_to_patients(my_symptoms, all_patients_symptoms)
    diagnostic = getting_diagnostics(similiar_patients, all_patients_diagnostics)
    return diagnostic

def my_test():
    # A small dictionary of patient's symptoms
    all_patients_symptoms = {56374: ({"headache","fever"}, {"coughing", "runny_nose","sneezing"}),
                             45437: ({"coughing", "runny_nose"},{"headache","fever"}),
                             16372: ({"coughing", "sore_throat"},{"fever"}),
                             54324: ({"vomiting", "coughing","stomach_pain"},{"fever"}),
                             73454: ({"coughing", "runny_nose"},{"headache","fever"}),
                             35249: ({"sore_throat", "coughing","fever"},{"stomach_pain", "runny_nose"}),
                             44274: ({"fever", "headache"},{"stomach_pain", "runny_nose","sore_throat",
                                      "coughing",}), 
                             74821: ({"vomiting", "fever"},{"headache"}),
                             94231: ({"stomach_pain", "fever","sore_throat","coughing","headache"},
                                     {"vomiting"})}
    # A small dictionary of patient's diagnostics                  
    all_patients_diagnostics = {45437: "cold",
                                56374: "meningitis",
                                54324: "food_poisoning", 
                                16372: "cold",
                                73454: "cold",
                                35249: "pharyngitis",
                                44274: "meningitis", 
                                74821: "food_poisoning",
                                94231: "unknown"}
    ### Regarding patients: 
    ### - Data: Patient's symptoms and diagnostics were stored in separate dictionaries:
    ###         all_patient_symptoms and all_patient_diagnostics
    ### - Code: similarity_to_patients and getting_diagnostics    
    
    # Three test patients
    yang = ({"coughing", "runny_nose", "sneezing"},{"headache","fever"})
    maria = ({"coughing", "fever", "sore_throat"},{"muscle_pain"})
    jaspal = ({"fever", "sore_throat", "sneezing"},{"sneezing"})
    barry = ({"coughing", "runny_nose","sore_throat"},{"sneezing"})
    #Testing function symptom_similarity
    sim = symptom_similarity(jaspal, barry)
    print("The similarity between Yang and Jaspal is", sim)
    
    #Testing function similarity_to_patients
    sim_set_Yang = similarity_to_patients(jaspal, all_patients_symptoms)
    print("Similarity set for Yang is ", sim_set_Yang)
    sim_set_Jaspal = similarity_to_patients(barry, all_patients_symptoms)
    print("Similarity set for Jaspal is ", sim_set_Jaspal)
    
    #Testing getting_diagnostics
    diag_str = getting_diagnostics(sim_set_Yang, all_patients_diagnostics)
    print("The diagnostic for Yang based on the most frequent diagnostics is ", diag_str)
    diag_str = getting_diagnostics(sim_set_Jaspal, all_patients_diagnostics)
    print("The diagnostic for Jaspal based on the most frequent diagnostics is ", diag_str)           
    
    #Testing protocol
    diag_str = protocol(yang, all_patients_symptoms, all_patients_diagnostics)
    print("The diagnostic for Yang' symptoms is ", diag_str)
    diag_str = protocol(jaspal, all_patients_symptoms, all_patients_diagnostics)
    print("The diagnostic for Jaspal' symptoms is ", diag_str)    

def read_data_from_file(filename):
    """
    args:
        filename: Name of file containing medical data
    Returns:
        Tuple of a dictionary of symptoms and a dictionary of diagnostics
    """
    
    f = open(filename,'r')
    lines = f.read().splitlines()
    
    i =0
    symptoms_by_patient={}
    diagnostic_by_patient={}
    l=len(lines)
    while i<l:
        ID=int(lines[i].split()[0])
        present = set(lines[i+1].split())
        absent = set(lines[i+2].split())
        diag = lines[i+3].split()[0]
        symptoms_by_patient[ID]=(present,absent)
        diagnostic_by_patient[ID]=diag
        i += 4
        
    return symptoms_by_patient, diagnostic_by_patient


my_test()