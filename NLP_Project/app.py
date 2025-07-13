from tkinter import*
from mydb import Database
from tkinter import messagebox

class NLPApp:
    def __init__(self):
        #login ka gui load karna
        self.sentiment_result = None
        self.sentiment_input = None
        self.dbo = Database()
        self.name_input = None
        self.password_input = None
        self.email_input = None
        self.root = Tk()
        self.root.title("NLP_App")
        self.root.iconbitmap('resources/favicon.ico')
        self.root.geometry('400x600')
        self.root.configure(bg='#2C3E50')

        self.login_gui()
        self.root.mainloop() # GUI hold karega

    def login_gui(self):
        self.clear()
        heading = Label(self.root, text = "NLP_App", bg='#2C3E50',fg='White')
        heading.pack(pady = (30,30))
        heading.configure(font=('verdana',24,'bold'))

        label1 = Label(self.root,text='Enter Email')
        label1.pack(pady = (10,10))

        self.email_input = Entry(self.root,width = 50)
        self.email_input.pack(pady = (5,10),ipady=3)

        label2 = Label(self.root, text='Enter Password')
        label2.pack(pady=(10, 10))

        self.password_input = Entry(self.root, width=50, show = '*')
        self.password_input.pack(pady=(5, 10), ipady=3)

        login_btn = Button(self.root,text = "Login", width = 20 , height = 1, command = self.perform_login)
        login_btn.pack(pady=(10,10))

        label3 = Label(self.root, text='Not a member?')
        label3.pack(pady=(20, 10))

        redirect_btn = Button(self.root, text = "Register Now", width = 10, height = 1, command = self.register_gui)
        redirect_btn.pack(pady = (10,10))


    def clear(self):
        for i in self.root.pack_slaves():
            i.destroy()

    def register_gui(self):
        # CLear the existing Gui
        self.clear()
        heading = Label(self.root, text="NLP_App", bg='#2C3E50', fg='White')
        heading.pack(pady=(30, 30))
        heading.configure(font=('verdana', 24, 'bold'))

        label0 = Label(self.root, text='Enter Name : ')
        label0.pack(pady=(10, 10))

        self.name_input = Entry(self.root, width=50)
        self.name_input.pack(pady=(5, 10), ipady=3)

        label1 = Label(self.root, text='Enter Email')
        label1.pack(pady=(10, 10))

        self.email_input = Entry(self.root, width=50)
        self.email_input.pack(pady=(5, 10), ipady=3)

        label2 = Label(self.root, text='Enter Password')
        label2.pack(pady=(10, 10))

        self.password_input = Entry(self.root, width=50, show='*')
        self.password_input.pack(pady=(5, 10), ipady=3)

        register_btn = Button(self.root, text="Register", width=20, height=1, command = self.perform_registration)
        register_btn.pack(pady=(10, 10))

        label3 = Label(self.root, text='Already a member?')
        label3.pack(pady=(20, 10))

        redirect_btn = Button(self.root, text="Login Now", width=10, height=1, command=self.login_gui)
        redirect_btn.pack(pady=(10, 10))

    def perform_registration(self):
        name = self.name_input.get()
        email = self.email_input.get()
        password = self.password_input.get()
        response = self.dbo.add_data(name,email,password)
        if response:
            messagebox.showinfo("Success","Registration Successfull.")
        else:
            messagebox.showinfo("Error","Email already Registered.")

    def perform_login(self):
        email = self.email_input.get()
        password = self.password_input.get()
        response = self.dbo.search(email,password)

        if response:
            messagebox.showinfo("Success","Login Successfull")
            self.home_gui()
        else:
            messagebox.showinfo("Error","Incorrect email/password.")


    def home_gui(self):
        self.clear()

        heading = Label(self.root, text="NLP_App", bg='#2C3E50', fg='White')
        heading.pack(pady=(30, 30))
        heading.configure(font=('verdana', 24, 'bold'))

        sentiment_btn = Button(self.root, text="Sentiment Analysis", width=30, height=2, command = self.sentiment_gui)
        sentiment_btn.pack(pady=(10, 10))

        NER_btn = Button(self.root, text="Named Entity Recognition", width=30, height=2, command=self.ner_gui)
        NER_btn.pack(pady=(10, 10))

        Emotion_btn = Button(self.root, text="Emotion Prediction", width=30, height=2, command=self.emotion_gui)
        Emotion_btn.pack(pady=(10, 10))

        Logout_button = Button(self.root, text="Logout", width=10, height=1, command=self.login_gui)
        Logout_button.pack(pady=(10, 10))



    def sentiment_gui(self):
        self.clear()

        heading = Label(self.root, text="NLP_App", bg='#2C3E50', fg='White')
        heading.pack(pady=(30, 30))
        heading.configure(font=('verdana', 24, 'bold'))

        heading = Label(self.root, text="Sentiment Analysis", bg='#2C3E50', fg='White')
        heading.pack(pady=(10, 20))
        heading.configure(font=('verdana', 20))

        label1 = Label(self.root, text = "Enter the text")
        label1.pack(pady = (10,10))
        
        self.sentiment_input = Entry(self.root, width = 50)
        self.sentiment_input.pack(pady = (10,10), ipady = 4)

        sentiment_btn = Button(self.root, text="Analyze Sentiment", width=30, height=1, command=self.analyze_sentiment)
        sentiment_btn.pack(pady = (10,10))

        self.sentiment_result = Label(self.root, text="",bg="#34495E", fg = "White")
        self.sentiment_result.pack(pady=(10, 10))
        self.sentiment_result.configure(font=('verdana',16))

        goback_btn = Button(self.root, text="Back", width=8, height=1, command=self.home_gui)
        goback_btn.pack(pady=(10, 10))

    def analyze_sentiment(self):
        text = self.sentiment_input.get()
        if not text.strip():
            self.sentiment_result.config(text="Please enter some text.")
            return

        # Dummy sentiment logic
        if "good" in text.lower():
            sentiment = "Positive"
        elif "bad" in text.lower():
            sentiment = "Negative"
        else:
            sentiment = "Neutral"

        self.sentiment_result.config(text=f"Sentiment: {sentiment}")

    def ner_gui(self):
        self.clear()

        heading = Label(self.root, text="Named Entity Recognition", bg='#2C3E50', fg='White')
        heading.pack(pady=(30, 20))
        heading.configure(font=('verdana', 20))

        label = Label(self.root, text="Enter text for NER:")
        label.pack(pady=(10, 5))

        self.ner_input = Entry(self.root, width=50)
        self.ner_input.pack(pady=(5, 10), ipady=4)

        self.ner_result = Label(self.root, text="", bg="#34495E", fg="White")
        self.ner_result.pack(pady=(10, 10))
        self.ner_result.configure(font=('verdana', 14))

        analyze_btn = Button(self.root, text="Analyze NER", width=30, height=1, command=self.analyze_ner)
        analyze_btn.pack(pady=(10, 10))

        back_btn = Button(self.root, text="Back", width=10, command=self.home_gui)
        back_btn.pack(pady=(10, 10))

    def analyze_ner(self):
        text = self.ner_input.get()
        # Dummy logic
        self.ner_result.config(text="Named Entities: [John, India, Monday]")

    def emotion_gui(self):
        self.clear()

        heading = Label(self.root, text="Emotion Prediction", bg='#2C3E50', fg='White')
        heading.pack(pady=(30, 20))
        heading.configure(font=('verdana', 20))

        label = Label(self.root, text="Enter text for emotion prediction:")
        label.pack(pady=(10, 5))

        self.emotion_input = Entry(self.root, width=50)
        self.emotion_input.pack(pady=(5, 10), ipady=4)

        self.emotion_result = Label(self.root, text="", bg="#34495E", fg="White")
        self.emotion_result.pack(pady=(10, 10))
        self.emotion_result.configure(font=('verdana', 14))

        analyze_btn = Button(self.root, text="Predict Emotion", width=30, height=1, command=self.predict_emotion)
        analyze_btn.pack(pady=(10, 10))

        back_btn = Button(self.root, text="Back", width=10, command=self.home_gui)
        back_btn.pack(pady=(10, 10))

    def predict_emotion(self):
        text = self.emotion_input.get()
        # Dummy logic
        self.emotion_result.config(text="Predicted Emotion: Happy")


nlp =NLPApp()
