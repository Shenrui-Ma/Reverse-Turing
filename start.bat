@echo off
echo Activating frontend services...
echo Activating backend services...

:: Frontend activating...
start cmd.exe /k "cd webui && pnpm run dev"

:: Backend activating with environment...
start cmd.exe /k "cd reverse_turing && ..\turenv\env\python.exe -m uvicorn main:app --reload"

:: Open frontend in default browser
start http://localhost:3000

echo Activated successfully.
pause