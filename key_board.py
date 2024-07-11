from kivy.lang import Builder
from kivymd.uix.label import MDLabel
from kivymd.uix.screen import Screen
from kivymd.uix.button import MDFlatButton, MDFillRoundFlatButton
from kivymd.uix.dialog import MDDialog


Builder.load_file("key_board.kv")

class KeyBoard_Tick(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.score = 0
        self.question_index = 0
        self.questions = [
            {"question": "____ is used to type anything on a computer", "answer": "a.keyboard"},
            {"question": "There are ______ alphabet keys on a keyboard", "answer": "c.26"},
            {"question": "The number keys are used to type____", "answer": "b.number"},
            {"question": "The ____ key is used to type capital letters.", "answer": "c.Caps Lock"},
            {"question": "_____ key removes letters, numbers, and symbols from the left side of the cursor", "answer": "b.Backspace"}
        ]
        self.options = [
            ["a.keyboard", "b.mouse", "c.cpu", "d.monitor"],
            ["a.108", "b.20", "c.26", "d.36"],
            ["a.alphabet", "b.number", "c.symbol", "d.all"],
            ["a.Enter", "b.Backspace", "c.Caps Lock", "d.Number"],
            ["a.Caps Lock", "b.Backspace", "c.Enter", "d.Delete"]
        ]
        

    def check_answer(self):
        selected_option = None
        if self.ids.option1.active:
            selected_option = self.ids.option11.text
        elif self.ids.option2.active:
            selected_option = self.ids.option22.text
        elif self.ids.option3.active:
            selected_option = self.ids.option33.text
        elif self.ids.option4.active:
            selected_option = self.ids.option44.text

        correct_answer = self.questions[self.question_index]["answer"]
        if selected_option == correct_answer:
            self.score += 1
            dialog_text = f"Correct answer! Your score: {self.score}"
        else:
            dialog_text = f"Wrong answer! Your score: {self.score}"

        self.show_dialog(dialog_text)

        self.question_index += 1
        if self.question_index < len(self.questions):
            self.update_question()
        else:
            self.end_quiz()

    def show_dialog(self, dialog_text):
        close_button = MDFlatButton(text="Close", on_release=self.close_dialog)
        self.dialog = MDDialog(title="Result",
                               text=dialog_text,
                               size_hint=(0.8, 0.28),
                               radius=[15, 4, 15, 4],
                               buttons=[close_button])
        self.dialog.open()

    def close_dialog(self, *args):
        self.dialog.dismiss()

    def update_question(self):
        question = self.questions[self.question_index]["question"]
        self.ids.question_label.text = question
        options = self.options[self.question_index]
        self.ids.option11.text = options[0]
        self.ids.option22.text = options[1]
        self.ids.option33.text = options[2]
        self.ids.option44.text = options[3]

        self.ids.option1.active = False
        self.ids.option2.active = False
        self.ids.option3.active = False
        self.ids.option4.active = False

    def end_quiz(self):
        final_score = f"Your final score is: {self.score}"
        self.clear_widgets()
        self.add_widget(MDLabel(text=final_score, font_style="H4", halign="center", theme_text_color="Custom", text_color="teal"))

        self.restart_button = MDFillRoundFlatButton(
            text="Restart",
            size_hint=(None, None),
            size=(100, 50),
            pos_hint={'center_x': 0.5, 'center_y': 0.4},
            text_color=(177 / 255, 61 / 255, 225 / 255, 1),
            md_bg_color=(163 / 255, 203 / 255, 237 / 255, 1),
            on_release=self.restart_quiz
        )
        self.add_widget(self.restart_button)

    def restart_quiz(self, *args):
        self.clear_widgets()
        self.score = 0
        self.question_index = 0
        self.add_widget(self.ids.head)
        self.add_widget(self.ids.question_label)
        self.add_widget(self.ids.option11)
        self.add_widget(self.ids.option1)
        self.add_widget(self.ids.option22)
        self.add_widget(self.ids.option2)
        self.add_widget(self.ids.option33)
        self.add_widget(self.ids.option3)
        self.add_widget(self.ids.option44)
        self.add_widget(self.ids.option4)
        self.add_widget(self.ids.Submit)
        self.update_question()


class KeyBoard_Rearrange(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.score = 0
        self.question_index = 0
        self.questions = [
            {"question": "ETNER ", "answer": "ENTER"},
            {"question": "UNMBRE", "answer": "NUMBER"},
            {"question": "PSAEC", "answer": "SPACE"},
            {"question": "ACPS LOCK", "answer": "CAPS LOCK"},
            {"question": "UNMBREYKE", "answer": "NUMBER KEY"}
        ]
        

    def check_answer(self, user_answer):
        correct_answer = self.questions[self.question_index]['answer']
        if user_answer == correct_answer:
            self.score += 1
            dialog_text = f"Correct answer. Your score: {self.score}"
        else:
            dialog_text = f"Wrong answer. Your score: {self.score}"

        self.show_dialog(dialog_text)
        self.question_index += 1
        if self.question_index < len(self.questions):
            self.update_question()
        else:
            self.end_quiz()

    def show_dialog(self, dialog_text):
        close_button = MDFlatButton(text="Close", on_release=self.close_dialog)
        self.dialog = MDDialog(title="Result",
                               text=dialog_text,
                               size_hint=(0.8, 0.8),
                               radius=[15, 4, 15, 4],
                               buttons=[close_button])
        self.dialog.open()

    def close_dialog(self, *args):
        self.dialog.dismiss()

    def update_question(self):
        question = self.questions[self.question_index]["question"]
        self.ids.question_label.text = question
        self.ids.answer_input.text = ""

    def end_quiz(self):
        final_score = f"Quiz Over! Your final score is {self.score}."
        self.clear_widgets()
        self.add_widget(MDLabel(text=final_score, font_style="H4", halign="center", theme_text_color="Custom", text_color=(0.0, 0.5, 0.5, 1)))

        restart_button = MDFillRoundFlatButton(
            text="Restart",
            size_hint=(None, None),
            size=(100, 50),
            pos_hint={'center_x': 0.5, 'center_y': 0.4},
            text_color=(177/255, 61/255, 225/255, 1),
            md_bg_color=(163/255, 203/255, 237/255, 1),
            on_release=self.restart_quiz
        )
        self.add_widget(restart_button)

    def restart_quiz(self, *args):
        self.clear_widgets()
        self.score = 0
        self.question_index = 0
        self.add_widget(self.ids.head)
        self.add_widget(self.ids.question_label)
        self.add_widget(self.ids.answer_input)
        self.add_widget(self.ids.Submit)
        self.update_question()




class KeyBoard_QNA(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.score = 0
        self.question_index = 0
        self.questions = [
            {"question": "Which is the longest key on the keyboard ?", "answer": ["space bar","space"]},
            {"question": "Name the key you use to type your age", "answer": "number key"},
            {"question": "Which key is used to bring the cursor on the next line ?", "answer": "enter key"},
            {"question": "What is the use of backspace key ?", "answer": "remove letters, numbers and symbols from the left side of the cursor"},
            
        ]
        

    def check_answer(self, user_answer):
        if user_answer.strip() == "":
            dialog_text = "Please input your answer"
        else:
            correct_answers = self.questions[self.question_index]['answer']
        
            if user_answer.lower() in correct_answers:
                self.score += 1
                dialog_text = f"Correct answer. Your score: {self.score}"
            else:
                dialog_text = f"Wrong answer. Your score: {self.score}"
        

        
            self.question_index += 1
            if self.question_index < len(self.questions):
                self.update_question()
            else:
                self.end_quiz()
        self.show_dialog(dialog_text)
    def show_dialog(self, dialog_text):
        close_button = MDFlatButton(text="Close", on_release=self.close_dialog)
        self.dialog = MDDialog(title="Result",
                               text=dialog_text,
                               size_hint=(0.8, 0.8),
                               radius=[15, 4, 15, 4],
                               buttons=[close_button])
        self.dialog.open()

    def close_dialog(self, *args):
        self.dialog.dismiss()

    def update_question(self):
        question = self.questions[self.question_index]["question"]
        self.ids.question_label.text = question
        self.ids.answer_input.text = ""

    def end_quiz(self):
        final_score = f"Quiz Over! Your final score is {self.score}."
        self.clear_widgets()
        self.add_widget(MDLabel(text=final_score, font_style="H4", halign="center", theme_text_color="Custom", text_color=(0.0, 0.5, 0.5, 1)))

        restart_button = MDFillRoundFlatButton(
            text="Restart",
            size_hint=(None, None),
            size=(100, 50),
            pos_hint={'center_x': 0.5, 'center_y': 0.4},
            text_color=(177/255, 61/255, 225/255, 1),
            md_bg_color=(163/255, 203/255, 237/255, 1),
            on_release=self.restart_quiz
        )
        self.add_widget(restart_button)

    def restart_quiz(self, *args):
        self.clear_widgets()
        self.score = 0
        self.question_index = 0
        self.add_widget(self.ids.head)
        self.add_widget(self.ids.question_label)
        self.add_widget(self.ids.answer_input)
        self.add_widget(self.ids.Submit)
        self.update_question()