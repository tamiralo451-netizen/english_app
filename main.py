from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button


class EnglishApp(App):

    def build(self):
        self.home_screen()
        return self.main_layout

    def home_screen(self):
        self.main_layout = BoxLayout(
            orientation="vertical",
            padding=25,
            spacing=15
        )

        title = Label(
            text="ENGLISH LEARNING",
            font_size=30
        )

        subtitle = Label(
            text="Learn English Every Day",
            font_size=20
        )

        vocabulary = Button(
            text="VOCABULARY",
            font_size=22
        )

        lessons = Button(
            text="LESSONS",
            font_size=22
        )

        quiz = Button(
            text="QUIZ",
            font_size=22
        )

        practice = Button(
            text="PRACTICE",
            font_size=22
        )

        vocabulary.bind(on_press=self.vocabulary_screen)

        self.main_layout.add_widget(title)
        self.main_layout.add_widget(subtitle)
        self.main_layout.add_widget(vocabulary)
        self.main_layout.add_widget(lessons)
        self.main_layout.add_widget(quiz)
        self.main_layout.add_widget(practice)

    def vocabulary_screen(self, instance):

        self.main_layout.clear_widgets()

        title = Label(
            text="VOCABULARY",
            font_size=30,
            size_hint_y=None,
            height=70
        )

        self.main_layout.add_widget(title)

        words = [
            "Apple - A fruit",
            "Book - Something you read",
            "Friend - A person you like",
            "Happy - Feeling good",
            "Learn - To gain knowledge",
            "Beautiful - Very nice to see",
            "Strong - Having power",
            "Quick - Fast",
            "Help - To assist someone",
            "Dream - Something you want to achieve"
        ]

        for word in words:
            label = Label(
                text=word,
                font_size=20
            )
            self.main_layout.add_widget(label)

        back = Button(
            text="BACK",
            font_size=20,
            size_hint_y=None,
            height=60
        )

        back.bind(on_press=self.go_home)

        self.main_layout.add_widget(back)

    def go_home(self, instance):
        self.home_screen()


EnglishApp().run()