[app]

title = English Learning
package.name = englishlearning
package.domain = org.englishlearning

source.dir = .
source.include_exts = py,png,jpg,jpeg,kv,atlas
version = 1.0

requirements = python3==3.13.7,kivy

orientation = portrait
fullscreen = 0

android.api = 33
android.minapi = 24
android.archs = arm64-v8a
android.accept_sdk_license = True

[buildozer]

log_level = 2
warn_on_root = 0
