[app]

# (str) Title of your application
title = rgb_hex_converter

# (str) Package name
package.name = converter

# (str) Package domain (needed for android/ios packaging)
package.domain = org.test

# (str) Source code where the main.py lives
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas,gif

# (list) List of inclusions using pattern matching
source.include_patterns = assets/*

# (list) Source files to exclude (let empty to not exclude anything)
source.exclude_dirs = tests, bin, venv

# (str) Application versioning (method 1)
version = 0.1

# (list) Application requirements
requirements = python3,kivy,Cython

# (str) Application icon
icon.filename = assets/logo.png

# (str) Presplash background color (for Android toolchain)
android.presplash_color = #000000

# (str) Presplash image
android.presplash_path = assets/loading.gif

# (list) Supported orientations
orientation = portrait

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 1

# (str) Android entry point, default is ok for Kivy-based app
android.entrypoint = org.kivy.android.PythonActivity

# (int) Target Android API, should be as high as possible
android.api = 31

# (int) Minimum API your APK / AAB will support
android.minapi = 21

# (int) Android NDK version to use
android.ndk = 23b

# (str) Android app theme, default is ok for Kivy-based app
# android.apptheme = "@android:style/Theme.NoTitleBar"

# (list) The Android archs to build for
android.archs = arm64-v8a, armeabi-v7a

# (bool) Enables Android auto backup feature (Android API >=23)
android.allow_backup = True

[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug)
log_level = 2

# (int) Display warning if buildozer is run as root (0 = False, 1 = True)
warn_on_root = 1

# (str) Path to build artifact storage, absolute or relative to spec file
build_dir = ./.buildozer

# (str) Path to build output (i.e. .apk, .aab, .ipa) storage
 bin_dir = ./bin
