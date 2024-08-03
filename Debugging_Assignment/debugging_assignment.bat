@echo off
SETLOCAL EnableDelayedExpansion
for /F "tokens=1,2 delims=#" %%a in ('"prompt #$H#$E# & echo on & for %%b in (1) do rem"') do (
  set "DEL=%%a"
)
@echo off
:::
:::         ________        ___.                       .__                
:::         \______ \   ____\_ |__  __ __  ____   ____ |__| ____    ____  
:::          |    |  \_/ __ \| __ \|  |  \/ ___\ / ___\|  |/    \  / ___\ 
:::          |    `   \  ___/| \_\ \  |  / /_/  > /_/  >  |   |  \/ /_/  >
:::         /_______  /\___  >___  /____/\___  /\___  /|__|___|  /\___  / 
:::                 \/     \/    \/     /_____//_____/         \//_____/  
:::        _____                .__                                     __   
:::       /  _  \   ______ _____|__| ____   ____   _____   ____   _____/  |_ 
:::      /  /_\  \ /  ___//  ___/  |/ ___\ /    \ /     \_/ __ \ /    \   __\
:::     /    |    \\___ \ \___ \|  / /_/  >   |  \  Y Y  \  ___/|   |  \  |  
:::     \____|__  /____  >____  >__\___  /|___|  /__|_|  /\___  >___|  /__|  
:::             \/     \/     \/  /_____/      \/      \/     \/     \/      
:::                        _________       __                
:::                       /   _____/ _____/  |_ __ ________  
:::                       \_____  \_/ __ \   __\  |  \____ \ 
:::                       /        \  ___/|  | |  |  /  |_> >
:::                      /_______  /\___  >__| |____/|   __/ 
:::                              \/     \/           |__|    
:::
for /f "delims=: tokens=*" %%A in ('findstr /b ::: "%~f0"') do @echo(%%A

@echo off

@REM This is a batch file that will help you setup and run the debugging assignment
@REM It will check if docker is installed, if not it will install it
@REM It will check if the docker image is built, if not it will build it
@REM It will run the docker image
@REM It will save your changes to the docker image


@REM Check if hyper-v is installed
systeminfo | findstr /C:"Hyper-V Requirements" | findstr /C:"A hypervisor has been detected" >nul 2>&1
if %errorlevel% equ 0 (
    @echo off
    echo:
    call :ColorText 0a "Hyper-V is enabled"
    echo:
    @REM echo:
) else (
    @echo off
    call :ColorText 0c "Hyper-V is disabled"
    echo Please enable Hyper-V 
    echo:
    echo "https://docs.microsoft.com/en-us/virtualization/hyper-v-on-windows/quick-start/enable-hyper-v" 
    echo:
    echo:
)
@echo off

@REM Check if WSL is installed

wsl --list --quiet >nul 2>&1
if %errorlevel% neq 0 (
    @echo off
    call :ColorText 0c "WSL is not installed"
    echo:
    echo Please enable WSL 
    echo "https://docs.microsoft.com/en-us/windows/wsl/install-win10" 
    echo:
    echo:
) else (
    @echo off
    call :ColorText 0a "WSL is enabled"
    echo:
    @REM echo:
)

@REM Check if docker is installed

docker --version >nul 2>&1
if %errorlevel% neq 0 (
    
    call :ColorText 0c "Docker is not installed"
    echo:
    echo:
    call :ColorText 0e "Installing Docker"
    echo:
    @echo off
    @REM Install docker
    @REM https://docs.docker.com/docker-for-windows/install/
    @REM download the installer from https://desktop.docker.com/win/main/amd64/Docker%20Desktop%20Installer.exe?utm_source=docker&utm_medium=webreferral&utm_campaign=docs-driven-download-win-amd64
    if not exist "%~dp0Docker Desktop Installer.exe" (
        REM Installer not found in current relative path
        REM Add your code here to handle the case when the installer is not found
        echo Installer not found in current relative path
        echo Please download the installer from 
        @echo off
        echo "https://desktop.docker.com/win/main/amd64/Docker%20Desktop%20Installer.exe?utm_source=docker&utm_medium=webreferral&utm_campaign=docs-driven-download-win-amd64"
        echo and place it in the same directory as this script with the name "Docker Desktop Installer.exe"
        echo:
        echo:
        pause
        exit /b
    )
    start /w "" "%~dp0Docker Desktop Installer.exe" install
    echo:
    echo:
    call :ColorText 0a "Docker is successfully installed"
    @REM Start Docker
    start /w "" "%ProgramFiles%\Docker\Docker\Docker Desktop.exe"
    pause
    exit /b
) else (
    call :ColorText 0a "Docker is already installed"
    @REM Start Docker
    start /w "" "%ProgramFiles%\Docker\Docker\Docker Desktop.exe"
    echo:
    pause
    exit /b
)

:ColorText
echo off
<nul set /p ".=%DEL%" > "%~2"
findstr /v /a:%1 /R "^$" "%~2" nul
del "%~2" > nul 2>&1
goto :eof