from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.utils import get_color_from_hex

class WhatsAppCleanerApp(App):
    def build(self):
        self.title = "مساعد حل مشاكل واتساب"
        layout = BoxLayout(orientation='vertical', padding=20, spacing=20)
        
        lbl = Label(
            text="مساعد حل مشاكل واتساب", 
            font_size='24sp', 
            color=get_color_from_hex('#25D366')
        )
        btn = Button(
            text="بدء عملية التطهير", 
            size_hint=(1, 0.2), 
            background_color=get_color_from_hex('#25D366')
        )
        
        layout.add_widget(lbl)
        layout.add_widget(btn)
        return layout

if __name__ == '__main__':
    WhatsAppCleanerApp().run()
