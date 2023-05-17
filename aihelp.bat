@echo off
cd /d "E:\Dev\OpenAICodeHelp\"
if "%1" == "" (
    python main.py
) else (
    if "%2" == "" (
        python main.py --f -q %1
    ) else (
        python main.py -q %1 -out %2
    )