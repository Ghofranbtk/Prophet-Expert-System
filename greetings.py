from experta import *
import tkinter as tk
from PIL import Image, ImageTk

class Greetings(KnowledgeEngine ):

    def __init__(self, symptom_map, if_not_matched, get_treatments, get_details):
        self.symptom_map = symptom_map
        self.if_not_matched = if_not_matched
        self.get_details = get_details
        self.get_treatments = get_treatments
        KnowledgeEngine.__init__(self)
        self.root = tk.Tk()
        self.text = tk.Text(self.root)
        self.text.pack()

    # code giving instructions on how to use the Expert System
    @DefFacts()
    def _initial_action(self):
        self.print_message("Dans ce programme on va deviner le prophète")
        self.print_message("Répondez par oui ou non")
        yield Fact(action="trouver_prophete")

    # def get_input(self, question, image_path):
    def get_input(self, question):
        new_window = tk.Toplevel(self.root)
        new_window.geometry("600x600+100+100")  # Vous pouvez ajuster la taille de la fenêtre ici
        new_window.configure(background='black')


    # Ajouter une image
        # Path_image = tk.PhotoImage(file="./images/Qs3.gif")
        # image_label = tk.Label(new_window, image=Path_image)
        # image_label.image = Path_image  # Gardez une référence à l'image
        # image_label.pack()
        
    # Ouvrir l'image avec Pillow
        image = Image.open("./images/Qs3.gif")

# Redimensionner l'image à la taille souhaitée
        image = image.resize((300, 200))

# Convertir l'image Pillow en PhotoImage Tkinter
        Path_image = ImageTk.PhotoImage(image)

# Utiliser l'image dans le label
        image_label = tk.Label(new_window, image=Path_image)
        image_label.image = Path_image  # Gardez une référence à l'image
        image_label.pack()


    # Ajouter une question
        label = tk.Label(new_window, text=question, font=("Helvetica", 16), foreground='red', background='lightblue')
        label.pack(expand=True, anchor='center')
        # label.pack()

    # Ajouter des boutons radio pour les réponses
        self.user_input = tk.StringVar(value="non")
        yes_button = tk.Radiobutton(new_window, text="نعم", variable=self.user_input, value="oui", font=("Helvetica", 14))
        no_button = tk.Radiobutton(new_window, text="لا", variable=self.user_input, value="non", font=("Helvetica", 14))
        yes_button.pack()
        no_button.pack()

    # Ajouter un bouton de soumission
        button = tk.Button(new_window, text="Submit", command=new_window.quit, font=("Helvetica", 14))
        button.pack()

        new_window.mainloop()
        answer = self.user_input.get()
        new_window.destroy()

        return answer

    def print_message(self, message):
        self.text.insert(tk.END, message + "\n")

    #taking various input from user
    
    @Rule(Fact(action="trouver_prophete"), NOT(Fact(Qs1=W())), salience=4)
    def symptom_0(self):
        self.declare(Fact(Qs1=self.get_input("هل هذا الشخص مذكور في سورة البقرة؟")))

    @Rule(Fact(action="trouver_prophete"), NOT(Fact(Qs2=W())), salience=1)
    def symptom_1(self):
        self.declare(Fact(Qs2=self.get_input("هل يعتبرأول رجل في القرآن؟")))

    @Rule(Fact(action="trouver_prophete"), NOT(Fact(Qs3=W())), salience=1)
    def symptom_2(self):
        self.declare(Fact(Qs3=self.get_input("هل له علاقات بالبحر أو الماء؟")))

    @Rule(Fact(action="trouver_prophete"), NOT(Fact(Qs4=W())), salience=3)
    def symptom_3(self):
        self.declare(Fact(Qs4=self.get_input("فهل يعتبر من الأنبياء الخمسة الكبار في الإسلام؟")))

    @Rule(Fact(action="trouver_prophete"), NOT(Fact(Qs5=W())), salience=1)
    def symptom_4(self):
        self.declare(Fact(Qs5=self.get_input("هل بنى فلكاً لينقذ عائلته وحيواناته من الطوفان؟")))

    @Rule(Fact(action="trouver_prophete"), NOT(Fact(Qs6=W())), salience=1)
    def symptom_5(self):
        self.declare(Fact(Qs6=self.get_input("هل هذا الشخص له علاقة بمكة؟ ")))

    @Rule(Fact(action="trouver_prophete"), NOT(Fact(Qs7=W())), salience=1)
    def symptom_6(self):
        self.declare(Fact(Qs7=self.get_input("هل له روابط بفلسطين حسب النصوص الدينية؟")))

    @Rule(Fact(action="trouver_prophete"), NOT(Fact(Qs8=W())), salience=1)
    def symptom_7(self):
        self.declare(Fact(Qs8=self.get_input("هل لهذا الشخص علاقة ببناء الكعبة في مكة؟")))

    @Rule(Fact(action="trouver_prophete"), NOT(Fact(Qs9=W())), salience=1)
    def symptom_8(self):
        self.declare(Fact(Qs9=self.get_input("هل له روابط بمصر حسب النصوص الدينية؟")))

    @Rule(Fact(action="trouver_prophete"), NOT(Fact(Qs10=W())), salience=1)
    def symptom_9(self):
        self.declare(Fact(Qs10=self.get_input("هل يرتبط هذا الشخص بقصة حلم البقرات السبع السمان والسبع البقرات العجاف في القرآن؟")))

    @Rule(Fact(action="trouver_prophete"), NOT(Fact(Qs11=W())), salience=1)
    def symptom_10(self):
        self.declare(Fact(Qs11=self.get_input("هل أصبح هذا الشخص مستشارًا مهمًا لملك مصر؟")))

    @Rule(Fact(action="trouver_prophete"), NOT(Fact(Qs12=W())), salience=1)
    def symptom_11(self):
        self.declare(Fact(Qs12=self.get_input("هل له علاقة بقصة العصا التي تحولت إلى ثعبان ؟")))

    @Rule(Fact(action="trouver_prophete"), NOT(Fact(Qs13=W())), salience=1)
    def symptom_12(self):
        self.declare(Fact(Qs13=self.get_input("هل تم العثور عليه في سلة طافية على النيل عندما كان طفلا؟")))

    @Rule(Fact(action="trouver_prophete"), NOT(Fact(Qs14=W())), salience=1)
    def symptom_13(self):
        self.declare(Fact(Qs14=self.get_input("هل قضى  ثلاثة أيام وثلاث ليال في بطن الحوت الكبير حسب القرآن؟")))
    
    @Rule(Fact(action="trouver_prophete"), NOT(Fact(Qs15=W())), salience=1)
    def symptom_14(self):
        self.declare(Fact(Qs15=self.get_input("هل هذا الشخص قادر على تحديد هوية يونان ؟")))
    @Rule(Fact(action="trouver_prophete"), NOT(Fact(Qs16=W())), salience=1)
    def symptom_15(self):
        self.declare(Fact(Qs16=self.get_input("هل هو آخر رسول بحسب القرآن؟")))

    @Rule(Fact(action="trouver_prophete"), NOT(Fact(Qs17=W())), salience=1)
    def symptom_16(self):
        self.declare(Fact(Qs17=self.get_input("فهل هو مؤسس الإسلام؟")))

    #different rules checking for each prophet match
    
     
    
    
    
    @Rule(
        Fact(action="trouver_prophete"),
        Fact(Qs1="oui"),
        Fact(Qs2="oui"),
        Fact(Qs3="non"),
        Fact(Qs4="non"),
        Fact(Qs5="non"),
        Fact(Qs6="non"),
        Fact(Qs7="non"),
        Fact(Qs8="non"),
        Fact(Qs9="non"),
        Fact(Qs10="non"),
        Fact(Qs11="non"),
        Fact(Qs12="non"),
        Fact(Qs13="non"),
        Fact(Qs14="non"),
        Fact(Qs15="non"),
        Fact(Qs16="non"),
        Fact(Qs17="non"),
    )
    def prophet_0(self):
        self.declare(Fact(prophet="Adam"))

    @Rule(
        Fact(action="trouver_prophete"),
        Fact(Qs1="non"),
        Fact(Qs2="non"),
        Fact(Qs3="oui"),
        Fact(Qs4="oui"),
        Fact(Qs5="oui"),
        Fact(Qs6="non"),
        Fact(Qs7="non"),
        Fact(Qs8="non"),
        Fact(Qs9="non"),
        Fact(Qs10="non"),
        Fact(Qs11="non"),
        Fact(Qs12="non"),
        Fact(Qs13="non"),
        Fact(Qs14="non"),
        Fact(Qs15="non"),
        Fact(Qs16="non"),
        Fact(Qs17="non"),
    )
    def prophet_1(self):
        self.declare(Fact(prophet="Nouh"))

    @Rule(
        Fact(action="trouver_prophete"),
        Fact(Qs1="oui"),
        Fact(Qs2="non"),
        Fact(Qs3="non"),
        Fact(Qs4="oui"),
        Fact(Qs5="non"),
        Fact(Qs6="oui"),
        Fact(Qs7="oui"),
        Fact(Qs8="oui"),
        Fact(Qs9="non"),
        Fact(Qs10="non"),
        Fact(Qs11="non"),
        Fact(Qs12="non"),
        Fact(Qs13="non"),
        Fact(Qs14="non"),
        Fact(Qs15="non"),
        Fact(Qs16="non"),
        Fact(Qs17="non"),
    )
    def prophet_2(self):
        self.declare(Fact(prophet="Ibrahim"))

    @Rule(
   Fact(action="trouver_prophete"),
        Fact(Qs1="non"),
        Fact(Qs2="non"),
        Fact(Qs3="non"),
        Fact(Qs4="non"),
        Fact(Qs5="non"),
        Fact(Qs6="non"),
        Fact(Qs7="non"),
        Fact(Qs8="non"),
        Fact(Qs9="oui"),
        Fact(Qs10="oui"),
        Fact(Qs11="oui"),
        Fact(Qs12="non"),
        Fact(Qs13="non"),
        Fact(Qs14="non"),
        Fact(Qs15="non"),
        Fact(Qs16="non"),
        Fact(Qs17="non"),
    )
    def prophet_3(self):
        self.declare(Fact(prophet="Youssef"))

    @Rule(
        Fact(action="trouver_prophete"),
        Fact(Qs1="oui"),
        Fact(Qs2="non"),
        Fact(Qs3="oui"),
        Fact(Qs4="oui"),
        Fact(Qs5="non"),
        Fact(Qs6="non"),
        Fact(Qs7="non"),
        Fact(Qs8="non"),
        Fact(Qs9="oui"),
        Fact(Qs10="non"),
        Fact(Qs11="non"),
        Fact(Qs12="oui"),
        Fact(Qs13="oui"),
        Fact(Qs14="non"),
        Fact(Qs15="non"),
        Fact(Qs16="non"),
        Fact(Qs17="non"),
    )
    def prophet_4(self):
        self.declare(Fact(prophet="Moussa"))

    @Rule(
        Fact(action="trouver_prophete"),
        Fact(Qs1="non"),
        Fact(Qs2="non"),
        Fact(Qs3="oui"),
        Fact(Qs4="non"),
        Fact(Qs5="non"),
        Fact(Qs6="non"),
        Fact(Qs7="non"),
        Fact(Qs8="non"),
        Fact(Qs9="non"),
        Fact(Qs10="non"),
        Fact(Qs11="non"),
        Fact(Qs12="non"),
        Fact(Qs13="non"),
        Fact(Qs14="oui"),
        Fact(Qs15="oui"),
        Fact(Qs16="non"),
        Fact(Qs17="non"),
    )
    def prophet_5(self):
        self.declare(Fact(prophet="Younus"))

    @Rule(
        Fact(action="trouver_prophete"),
        Fact(Qs1="non"),
        Fact(Qs2="non"),
        Fact(Qs3="non"),
        Fact(Qs4="oui"),
        Fact(Qs5="non"),
        Fact(Qs6="oui"),
        Fact(Qs7="oui"),
        Fact(Qs8="non"),
        Fact(Qs9="non"),
        Fact(Qs10="non"),
        Fact(Qs11="non"),
        Fact(Qs12="non"),
        Fact(Qs13="non"),
        Fact(Qs14="non"),
        Fact(Qs15="non"),
        Fact(Qs16="oui"),
        Fact(Qs17="oui"),
    )
    def prophet_6(self):
        self.declare(Fact(prophet="Mohamed"))

    #when the user's input doesn't match any prophet in the knowledge base
    @Rule(Fact(action="trouver_prophete"), Fact(prophet=MATCH.prophet), salience=-998)
    def prophet(self, prophet):
       
        id_prophet = prophet
        prophet_details = self.get_details(id_prophet)
        treatments = self.get_treatments(id_prophet)
        self.print_message("")
        self.print_message("Your symptoms match %s\n" % (id_prophet))
        self.print_message("A short description of the prophet is given below :\n")
        self.print_message(prophet_details + "\n")
        self.print_message(
            "The common medications and procedures suggested by other real doctors are: \n"
        )
        self.print_message(treatments + "\n")

    @Rule(
        Fact(action="trouver_prophete"),
        Fact(Qs1=MATCH.Qs1),
        Fact(Qs2=MATCH.Qs2),
        Fact(Qs3=MATCH.Qs3),
        Fact(Qs4=MATCH.Qs4),
        Fact(Qs5=MATCH.Qs5),
        Fact(Qs6=MATCH.Qs6),
        Fact(Qs7=MATCH.Qs7),
        Fact(Qs8=MATCH.Qs8),
        Fact(Qs9=MATCH.Qs9),
        Fact(Qs10=MATCH.Qs10),
        Fact(Qs11=MATCH.Qs11),
        Fact(Qs12=MATCH.Qs12),
        Fact(Qs13=MATCH.Qs13),
        Fact(Qs14=MATCH.Qs14),
        Fact(Qs15=MATCH.Qs15),
        Fact(Qs16=MATCH.Qs16),
        Fact(Qs17=MATCH.Qs17),
        NOT(Fact(prophet=MATCH.prophet)),
        salience=-999
    )
    def not_matched(
        self,
        Qs1,
        Qs2,
        Qs3,
        Qs4,
        Qs5,
        Qs6,
        Qs8,
        Qs9,
        Qs10,
        Qs11,
        Qs12,
        Qs13,
        Qs14,
        Qs15,
        Qs16,
        Qs17,
    ):
        self.print_message("\nThe bot did not find any prophets that match your exact symptoms.")
        lis = [
        Qs1,
        Qs2,
        Qs3,
        Qs4,
        Qs5,
        Qs6,
        Qs8,
        Qs9,
        Qs10,
        Qs11,
        Qs12,
        Qs13,
        Qs14,
        Qs15,
        Qs16,
        Qs17,
        ]
        max_count = 0
        max_prophet = ""
        for key, val in self.symptom_map.items():
            count = 0
            temp_list = eval(key)
            for j in range(0, len(lis)):
                if temp_list[j] == lis[j] and lis[j] == "oui":
                    count = count + 1
            if count > max_count:
                max_count = count
                max_prophet = val
        if max_prophet != "":
            self.if_not_matched(max_prophet)