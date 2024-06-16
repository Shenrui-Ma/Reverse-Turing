@echo off
chcp 65001

setlocal enabledelayedexpansion

cd /D "%~dp0"

set PATH="%PATH%";%SystemRoot%\system32

echo %PATH%

set TMP=%CD%\turenv
set TEMP=%CD%\turenv

(call conda deactivate && call conda deactivate && call conda deactivate) 2>nul

set INSTALL_DIR=%cd%\turenv
set CONDA_ROOT_PREFIX=%cd%\turenv\conda
set INSTALL_ENV_DIR=%cd%\turenv\env
set PIP_CMD=%cd%\turenv\env\python -m pip
set PYTHON_CMD=%cd%\turenv\env\python
set MINICONDA_DOWNLOAD_URL=https://mirrors.tuna.tsinghua.edu.cn/anaconda/miniconda/Miniconda3-py310_23.3.1-0-Windows-x86_64.exe
set MINICONDA_CHECKSUM=307194e1f12bbeb52b083634e89cc67db4f7980bd542254b43d3309eaf7cb358
set conda_exists=F

call "%CONDA_ROOT_PREFIX%\conda\_conda.exe" --version >nul 2>&1
if "%ERRORLEVEL%" EQU "0" set conda_exists=T

if "%conda_exists%" == "F" (
    echo.
    echo Downloading Miniconda...
    mkdir "%INSTALL_DIR%\conda" 2>nul
    call curl -Lk "%MINICONDA_DOWNLOAD_URL%" > "%INSTALL_DIR%\conda\miniconda_installer.exe"
    if errorlevel 1 (
        echo.
        echo Failed to download Miniconda.
        goto end
    )
    for /f %%a in ('
        certutil -hashfile "%INSTALL_DIR%\conda\miniconda_installer.exe" sha256
        ^| find /i /v " "
        ^| find /i "%MINICONDA_CHECKSUM%"
    ') do (
        set "hash=%%a"
    )
    if not defined hash (
        echo.
        echo Miniconda hash mismatched!
        del "%INSTALL_DIR%\conda\miniconda_installer.exe"
        goto end
    ) else (
        echo.
        echo Miniconda hash matched successfully.
    )
    echo Downloaded "%CONDA_ROOT_PREFIX%\conda"
    start /wait "" "%INSTALL_DIR%\conda\miniconda_installer.exe" /InstallationType=JustMe /NoShortcuts=1 /AddToPath=0 /RegisterPython=0 /NoRegistry=1 /S /D=%CONDA_ROOT_PREFIX%\conda

    call "%CONDA_ROOT_PREFIX%\conda\_conda.exe" --version
    if errorlevel 1 (
        echo.
        echo Cannot install Miniconda.
        goto end
    ) else (
        echo.
        echo Miniconda Install success.
    )

    del "%INSTALL_DIR%\conda\miniconda_installer.exe"
)

if not exist "%INSTALL_ENV_DIR%" (
    echo.
    echo Creating Conda Environment...
    call "%CONDA_ROOT_PREFIX%\conda\_conda.exe" create --no-shortcuts -y -k --prefix "%INSTALL_ENV_DIR%" python=3.8

    if errorlevel 1 (
        echo.
        echo Failed to Create Environment.
        goto end
    )
)

if not exist "%INSTALL_ENV_DIR%\python.exe" (
    echo.
    echo Conda Env does not exist.
    goto end
)

set PYTHONNOUSERSITE=1
set PYTHONPATH=
set PYTHONHOME=

call "%CONDA_ROOT_PREFIX%\conda\condabin\conda.bat" activate "%INSTALL_ENV_DIR%"

if errorlevel 1 (
    echo.
    echo Failed to activate Env.
    goto end
) else (
    echo.
    echo Successfully created and activated env.
)

echo Installing required packages...
%PIP_CMD% install fastapi requests pydantic uvicorn pillow nltk websocket-client python-dotenv numpy python-docx transformers faiss-cpu

if errorlevel 1 (
    echo.
    echo Failed to install packages.
    goto end
) else (
    echo.
    echo Successfully installed all packages.
)

echo Environment setup complete.

endlocal
:end
pause