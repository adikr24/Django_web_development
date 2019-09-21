import numpy as np
import pandas as pd
import re

### preformatting



class text_clean():
    def __init__(self,sentence):
        self.my_sentence = sentence
    
    def clean_words(self):
        my_sentence = self.my_sentence
        my_sentence=my_sentence.lower()
        rep = {
            "fell down": "loss_of_balance",
            "cant concentrate" : "loss_of_concentration",
            "i feel dizzy": "dizziness",
            "dizzy all the time":"dizziness",
            "mood swings": "mood_swings",
            "tired all the time" : "fatigue",
            "throwing": "vomittig",
            "throwing like a": "vomitting",
            "anxious" : "anxiety",
            "I feel discomfort": "anxiety",    
           "out of breath": "fast_heart_rate",
           "kidneys hurting": "kidney_pain",
           "chest is paining" : "chest_pain",
           "chest pains": "chest_pain",
           "chest hurts": "chest_pain",
           "my heart is throbbing" : "fast_heart_rate",
           "lungs hurt" : "lung_pain",
           "stomach hurt": "stomach_pain",
           "stomach hurts":"stomach_pain",
           "stomach is hurting":"stomach_pain",
           "knees hurt": "joint_pain",
           "knees are paining": "joint_pain",
           "knee hurts": "joint_pain",
           "my heart is throbbing": "fast_heart_rate",
           "constantly sneezing": "continuous_sneezing",
           "feel fatigued": "fatigue",
           "legs are paining": "joint_pain",
           "legs hurt" :"muscle_weakness",
           "arms hurt" :"muscle_weakness",
           "elbow pains" : "joint_pain",
           "severe headaches" :"headache",
           "headaches":"headache",
           } # define desired replacements here
        rep = dict((re.escape(k), v) for k, v in rep.items()) 
        #Python 3 renamed dict.iteritems to dict.items so use rep.items() for latest versions
        pattern = re.compile("|".join(rep.keys()))
        text = pattern.sub(lambda m: rep[re.escape(m.group(0))], my_sentence)
        fp = text
        wordList = re.sub("[^\w]", " ",  fp).split()
        stopwords= ['hey','m','experiencing','my','are','am','think','and','is', 'because','i','of','smoking','running','hurt', 'having']
        
        sp=[]
        for word in wordList:
            if word in stopwords:
                pass
            else:
                sp.append(word)
        
        symptom_list=['itching', 'skin_rash','nodal_skin_eruptions',  'continuous_sneezing',  'shivering',  'chills', 'joint_pain', 'stomach_pain', 'acidity',  'ulcers_on_tongue', 'muscle_wasting', 'vomiting', 'burning_micturition',  'spotting_ urination',  'fatigue',  'weight_gain',  'anxiety',  'cold_hands_and_feets', 'mood_swings',  'weight_loss',  'restlessness', 'lethargy', 'patches_in_throat',  'irregular_sugar_level',  'cough',  'high_fever', 'sunken_eyes',  'breathlessness', 'sweating', 'dehydration',  'indigestion',  'headache', 'yellowish_skin', 'dark_urine', 'nausea', 'loss_of_appetite', 'pain_behind_the_eyes', 'back_pain',  'constipation', 'abdominal_pain', 'diarrhoea',  'mild_fever', 'yellow_urine', 'yellowing_of_eyes',  'acute_liver_failure',  'fluid_overload', 'swelling_of_stomach',  'swelled_lymph_nodes',  'malaise',  'blurred_and_distorted_vision', 'phlegm', 'throat_irritation',  'redness_of_eyes',  'sinus_pressure', 'runny_nose', 'congestion', 'chest_pain', 'weakness_in_limbs',  'fast_heart_rate',  'pain_during_bowel_movements',  'pain_in_anal_region',  'bloody_stool', 'irritation_in_anus', 'neck_pain',  'dizziness',  'cramps', 'bruising', 'obesity',  'swollen_legs', 'swollen_blood_vessels',  'puffy_face_and_eyes',  'enlarged_thyroid', 'brittle_nails',  'swollen_extremeties',  'excessive_hunger', 'extra_marital_contacts', 'drying_and_tingling_lips', 'slurred_speech', 'knee_pain',  'hip_joint_pain', 'muscle_weakness',  'stiff_neck', 'swelling_joints',  'movement_stiffness', 'spinning_movements', 'loss_of_balance',  'unsteadiness', 'weakness_of_one_body_side',  'loss_of_smell',  'bladder_discomfort', 'foul_smell_of urine',  'continuous_feel_of_urine', 'passage_of_gases', 'internal_itching', 'toxic_look_(typhos)',  'depression', 'irritability', 'muscle_pain',  'altered_sensorium',  'red_spots_over_body',  'belly_pain', 'abnormal_menstruation',  'dischromic _patches',  'watering_from_eyes', 'increased_appetite', 'polyuria', 'family_history', 'mucoid_sputum',  'rusty_sputum', 'lack_of_concentration',  'visual_disturbances',  'receiving_blood_transfusion',  'receiving_unsterile_injections', 'coma', 'stomach_bleeding', 'distention_of_abdomen',  'history_of_alcohol_consumption', 'fluid_overload', 'blood_in_sputum',  'prominent_veins_on_calf',  'palpitations', 'painful_walking',  'pus_filled_pimples', 'blackheads', 'scurring', 'skin_peeling', 'silver_like_dusting',  'small_dents_in_nails', 'inflammatory_nails', 'blister',  'red_sore_around_nose', 'yellow_crust_ooze']

        sp_II=[]
        for i in range(len(sp)):
            if sp[i] in symptom_list:
                sp_II.append(sp[i])
            else:
                pass
        
        list_app = len(sp_II)
        sym_append = ['itching','skin_rash','nodal_skin_eruptions','continuous_sneezing']
        
        if list_app < 5:
            sp_II.extend(sym_append)     
        
        s1,s2,s3,s4,s5= sp_II[0],sp_II[1],sp_II[2],sp_II[3],sp_II[4]
        return s1,s2,s3,s4,s5





