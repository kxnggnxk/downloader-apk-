[app]
title = Downloader Pro
package.name = downloaderpro
package.domain = org.test
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.1.6
requirements = python3, kivy==2.2.1, yt_dlp, certifi, requests, urllib3
orientation = portrait
osx.python_version = 3
osx.kivy_version = 1.9.1
fullscreen = 0
android.permissions = INTERNET, WRITE_EXTERNAL_STORAGE, READ_EXTERNAL_STORAGE
android.api = 31
android.minapi = 21
android.ndk = 25b
android.skip_update = False
android.accept_sdk_license = True
android.archs = arm64-v8a

[buildozer]
log_level = 2
warn_on_root = 1
