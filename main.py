
prophets_list = []
prophets_symptoms = []
symptom_map = {}
d_desc_map = {}
d_treatment_map = {}

#loads the knowledge from .txt files into variables to allow the code to use it
def preprocess():
    #global prophets_list, prophets_symptoms, symptom_map, d_desc_map, d_treatment_map
    prophets = open("prophets.txt")
    prophets_t = prophets.read()
    prophets_list = prophets_t.split("\n")
    prophets.close()

    for prophet in prophets_list:
        prophet_s_file = open("Prophet symptoms/" + prophet + ".txt")
        prophet_s_data = prophet_s_file.read()
        s_list = prophet_s_data.split("\n")
        prophets_symptoms.append(s_list)
        symptom_map[str(s_list)] = prophet
        prophet_s_file.close()

        prophet_s_file = open("Prophet descriptions/" + prophet + ".txt")
        prophet_s_data = prophet_s_file.read()
        d_desc_map[prophet] = prophet_s_data
        prophet_s_file.close()

        prophet_s_file = open("Prophet treatments/" + prophet + ".txt")
        prophet_s_data = prophet_s_file.read()
        d_treatment_map[prophet] = prophet_s_data
        prophet_s_file.close()


def identify_prophet(*arguments):
    symptom_list = []
    for symptom in arguments:
        symptom_list.append(symptom)

    return symptom_map[str(symptom_list)]


def get_details(prophet):
    return d_desc_map[prophet]


def get_treatments(prophet):
    return d_treatment_map[prophet]


def if_not_matched(prophet):
    print("")
    id_prophet = prophet
    prophet_details = get_details(id_prophet)
    treatments = get_treatments(id_prophet)
    print("")
    print("The most probable prophet that you have is %s\n" % (id_prophet))
    print("A short description of the prophet is given below :\n")
    print(prophet_details + "\n")
    print(
        "The common medications and procedures suggested by other real doctors are: \n"
    )
    print(treatments + "\n")
from greetings import Greetings
#driver function
if __name__ == "__main__":
    preprocess()
    #creating class object
    engine = Greetings(symptom_map, if_not_matched, get_treatments, get_details)
    #loop to keep running the code until user says no when asked for another diagnosis
    while 1:
        engine.reset()
        engine.run()
        print("Would you like to diagnose some other symptoms?\n Reply yes or no")
        if input() == "no":
            exit()
