@echo off
title SecureLogin
mode con cols=20 lines=2

cd %cd%

python securelogin.py

start "" securelogin_start.bat
exit