class Symptoms:
    ''' The class Symptoms stores information about symptoms that are known to be present or absent in a patient'''
    
    def __init__(self, pres: set, ab: set) -> None:
        '''
        This function initialize the Set of Strings present and absent with the symptoms 
        of the object Symptoms on which the method is called 
        '''
        self.present = pres
        self.absent = ab
        
    def symptom_similarity(self, other) -> int:
        """
        Returns the similarity between self (i.e., the Symptoms object on which the method is called)
        and other(i.e., the Symptoms object we want to compare to). 
        """
        present_present = len(self.present.intersection(other.present))
        absent_absent = len(self.absent.intersection(other.absent))
        present_absent = len(self.present.intersection(other.absent))
        absent_present= len(self.absent.intersection(other.present))
        return  present_present + absent_absent - present_absent - absent_present
    
    def __str__(self) -> str:
        '''
        Returns a String describing the symptom object. 
        '''
        return 'Symptoms present= ' + str(self.present) + '\nSymptoms absent= ' + str(self.absent) 

if __name__ == '__main__':
    my_symptoms = Symptoms({'headache', 'fever'}, {'coughing'})
    print(my_symptoms.present)
    print(my_symptoms)
    other_symptoms = Symptoms({'fever'}, {'sneezing'})
    sim = my_symptoms.symptom_similarity(other_symptoms)
    print(sim)