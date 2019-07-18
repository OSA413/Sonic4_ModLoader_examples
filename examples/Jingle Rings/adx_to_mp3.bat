@echo off
call ffmpeg.bat -version && (
echo.

where /Q /R SOUND *.adx && robocopy SOUND SOUND_raw *.adx /S > NUL

for /F "delims==" %%f in ('where /F /R SOUND_raw *.adx') DO (
    echo %%f
    call ffmpeg.bat -y -loglevel quiet -hide_banner -nostats -i %%f "%%~dpnf.mp3" && (
    del %%f )
))
pause