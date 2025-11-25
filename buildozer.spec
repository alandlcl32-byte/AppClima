[app]
title = WeatherApp
package.name = weatherapp
package.domain = org.wheather
source.dir = .
source.include_exts = py, kv, png, jpg
version = 0.1
requirements = python3,kivy,requests
orientation = portrait
android.permissions = INTERNET, ACCESS_FINE_LOCATION, ACCESS_COARSE_LOCATION, WRITE_EXTERNAL_STORAGE, READ_EXTERNAL_STORAGE
android.accept_sdk_license = True
android.skip_update = False
p4a.source_dir = .
p4a.local_recipes = ./p4a-recipes
android.gradle_dependencies = 
android.add_src = False
# icon.filename = icon.png

[buildozer]
log_level = 2
android.api = 33
android.minapi = 21
android.archs = arm64-v8a
android.skip_update = False
android.accept_sdk_license = True
