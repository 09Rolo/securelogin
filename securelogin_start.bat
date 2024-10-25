@echo off
title SecureLogin
mode con cols=10 lines=10

cd %cd%

python securelogin.py

start "" securelogin_start.bat
exit