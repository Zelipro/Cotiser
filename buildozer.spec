[app]
title = Cotiser
package.name = Zelipro
package.domain = org.example
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,webp
source.include_patterns = assets/*,images/*,Base_de_donne/*
version = 1.0
requirements = python3,kivy,kivymd,pillow
icon.filename = %(source.dir)s/Logo.png

# Permissions Android
android.permissions = WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE

[buildozer]
log_level = 2

[android]
api = 34
minapi = 21
ndk = 25b
sdk = 34
android.archs = arm64-v8a, armeabi-v7a
# Configuration pour permettre toutes les orientations
orientation = all
android.orientation = all
android.orientations = landscape,portrait,portrait-reverse,landscape-reve

android.add_src = .
android.gradle_dependencies = 
android.add_compile_options = sourceCompatibility JavaVersion.VERSION_1_8, targetCompatibility JavaVersion.VERSION_1_8
