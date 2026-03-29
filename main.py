from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.utils import get_color_from_hex
import os
import shutil

# قائمة حزم النسخ المعدلة المستهدفة بالتنظيف
MODDED_PACKAGES = [
    "com.gbwhatsapp", "com.obwhatsapp", "com.yowhatsapp", 
    "com.goldwhatsapp", "com.whatsapp.plus"
]

class WhatsAppCleanerApp(App):
    def build(self):
        self.title = "مساعد حل مشاكل واتساب"
        main_layout = BoxLayout(orientation='vertical', padding=20, spacing=15)
        
        # العنوان العلوي
        header = Label(
            text="درع الحماية الذكي",
            font_size='28sp',
            color=get_color_from_hex('#25D366'),
            size_hint_y=None, height=60
        )
        main_layout.add_widget(header)

        # منطقة عرض الحالة للمستخدم
        self.status_label = Label(
            text="جاهز لبدء العمل الخيري",
            halign='center',
            text_size=(400, None)
        )
        main_layout.add_widget(self.status_label)

        # زر تطهير الجهاز من النسخ
        btn_clean = Button(
            text="تطهير الجهاز",
            background_color=get_color_from_hex('#2ecc71'),
            font_size='20sp', size_hint_y=None, height=80
        )
        btn_clean.bind(on_press=self.run_cleaner)
        main_layout.add_widget(btn_clean)

        # زر نسخ رسالة فك الحظر
        btn_appeal = Button(
            text="نسخ رسالة فك الحظر",
            background_color=get_color_from_hex('#3498db'),
            font_size='20sp', size_hint_y=None, height=80
        )
        btn_appeal.bind(on_press=self.copy_appeal)
        main_layout.add_widget(btn_appeal)

        return main_layout

    def run_cleaner(self, instance):
        base_path = "/storage/emulated/0/Android/media/"
        found = False
        for pkg in MODDED_PACKAGES:
            full_path = os.path.join(base_path, pkg)
            if os.path.exists(full_path):
                try:
                    shutil.rmtree(full_path)
                    found = True
                except:
                    pass
        
        if found:
            self.status_label.text = "تم تنظيف مخلفات النسخ بنجاح"
        else:
            self.status_label.text = "الجهاز نظيف تماماً من النسخ المعدلة"

    def copy_appeal(self, instance):
        appeal_text = "Dear WhatsApp Support, my account was banned by mistake. Please review my activity. I use the official app now. Thanks."
        self.status_label.text = f"تم تجهيز الرسالة:\n\n{appeal_text}"

if __name__ == '__main__':
    WhatsAppCleanerApp().run()
