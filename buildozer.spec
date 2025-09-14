[app]
title = Radiology AI Assistant
package.name = radiology_assistant
package.domain = org.hackathon
source.dir = .
source.main_py = main.py
version = 0.1

All the libraries used in your code must be listed here
requirements = python3,kivy,pyrebase4,requests,certifi

Android specific permissions
android.permissions = INTERNET

---> THE CRITICAL FIX IS HERE <---
This line tells buildozer to use the latest version of the build tools,
which is compatible with modern macOS and Homebrew.
p4a.branch = master

[buildozer]
log_level = 2
warn_on_root = 1