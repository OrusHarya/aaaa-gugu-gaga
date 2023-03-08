from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen, NoTransition
from kivy.uix.label import Label
from kivy.uix.image import Image


class app(App):
    def build(self):
        self.icon = r'D:\pycharm/ahuetchozaproject/fotki/Ваня не прощает ошибок.jpg'
        self.sm = ScreenManager(transition=NoTransition())
        screen1 = Screen(name='Главная страница')
        screen2 = Screen(name='Расписание')
        screen3 = Screen(name='Расписание звонков')
        bl_main = BoxLayout(orientation='vertical')
        bl_rasp = BoxLayout(orientation='vertical')
        bl_zvon = BoxLayout(orientation='vertical')

        # Главная страница
        main_lb = Label(text=screen1.name)
        main_but = Button(text='Расписание')
        main_but.bind(on_release=self.torasp)
        rasp_but2 = Button(text='Расписание звонков')
        rasp_but2.bind(on_release=self.tozvonki)
        bl_main.add_widget(main_lb)
        bl_main.add_widget(main_but)
        bl_main.add_widget(rasp_but2)
        screen1.add_widget(bl_main)

        # Расписание

        rasp_lb = Label(text=screen2.name,
                        size_hint=(1, .2))
        rasp_img = Image(source='D:\dbljcs\пн, вт, ср.jpg',
                         size_hint=(1, .9),
                         pos_hint={'center_x': 0.5, 'center_y': 0.1})

        rasp_img2 = Image(source='D:\dbljcs\чт и пт.jpg',
                         size_hint=(1, .9),
                         pos_hint={'center_x': 0.5, 'center_y': 0.1})

        rasp_but = Button(text='Главная страница',
                          size_hint=(1, 0.4))
        rasp_but.bind(on_release=self.tomain)
        rasp_but2 = Button(text='Расписание звонков',
                          size_hint=(1, 0.4))

        rasp_but2.bind(on_release=self.tozvonki)
        bl_rasp.add_widget(rasp_lb)
        bl_rasp.add_widget(rasp_img)
        bl_rasp.add_widget(rasp_img2)
        bl_rasp.add_widget(rasp_but)
        bl_rasp.add_widget(rasp_but2)
        screen2.add_widget(bl_rasp)

        # Расписание звонков

        zvon_lb = Label(text=screen3.name,
                        size_hint=(1, 0.2))

        zvon_1 = Label(text='8:00-8:35',
                       size_hint=(1, 0.2),
                       pos_hint={'center_x': 0.5})  # 1

        zvon_2 = Label(text='8:40-9:15',
                       size_hint=(1, 0.2),
                       pos_hint={'center_x': 0.5})  # 2

        zvon_3 = Label(text='9:25-10:00',
                       size_hint=(1, 0.2),
                       pos_hint={'center_x': 0.5})  # 3

        zvon_4 = Label(text='10:15-10:50',
                       size_hint=(1, 0.2),
                       pos_hint={'center_x': 0.5})  # 4

        zvon_5 = Label(text='11:00-11:35',
                       size_hint=(1, 0.2),
                       pos_hint={'center_x': 0.5})  # 5

        zvon_6 = Label(text='11:45-12:20',
                       size_hint=(1, 0.2),
                       pos_hint={'center_x': 0.5})  # 6

        zvon_7 = Label(text='12:25-13:00',
                       size_hint=(1, 0.2),
                       pos_hint={'center_x': 0.5})  # 7

        zvon_but = Button(text='Расписание',
                          size_hint=(1, 0.7))
        zvon_but.bind(on_release=self.torasp)
        zvon_but2 = Button(text='Главная страница',
                           size_hint=(1, 0.7))
        zvon_but2.bind(on_release=self.tomain)

        bl_zvon.add_widget(zvon_lb)
        bl_zvon.add_widget(zvon_1)
        bl_zvon.add_widget(zvon_2)
        bl_zvon.add_widget(zvon_3)
        bl_zvon.add_widget(zvon_4)
        bl_zvon.add_widget(zvon_5)
        bl_zvon.add_widget(zvon_6)
        bl_zvon.add_widget(zvon_7)

        bl_zvon.add_widget(zvon_but)
        bl_zvon.add_widget(zvon_but2)
        screen3.add_widget(bl_zvon)

        self.sm.add_widget(screen1)
        self.sm.add_widget(screen2)
        self.sm.add_widget(screen3)
        self.sm.current = 'Главная страница'
        return self.sm

    def torasp(self, instance):
        self.sm.current = 'Расписание'

    def tomain(self, instance):
        self.sm.current = 'Главная страница'

    def tozvonki(self, instance):
        self.sm.current = 'Расписание звонков'



app().run()