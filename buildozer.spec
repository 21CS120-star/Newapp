[app]
title = RGB/Hex Converter
package.name = rgb_hex_converter
package.domain = org.example
source.main = main.py
requirements = kivy==1.9.1
icon.filename = icon.png
presplash.filename = background.png
orientation = portrait
android.permissions = INTERNET
android.api = 33
android.minapi = 21
android.ndk = 23b
p4a.branch = master

[buildozer]
log_level = 2
warn_on_root = 1
android.accept_sdk_license = True
