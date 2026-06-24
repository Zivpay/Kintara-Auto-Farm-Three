@echo off
:loop
py bot.py
timeout /t 2
goto loop