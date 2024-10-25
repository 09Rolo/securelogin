@echo off
title SecureLogin
mode con cols=15 lines=10

cd %cd%

python securelogin.py

start "" securelogin_start.bat
exit