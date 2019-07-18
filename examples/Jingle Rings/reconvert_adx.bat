@echo off
call ffmpeg.bat -version && (
echo.

for /F "delims==" %%f in ('where /F /R . *.adx') DO (
    echo %%f
    call ffmpeg.bat -y -loglevel quiet -hide_banner -nostats -i %%f "%%~dpnf.wav" && (
    call ffmpeg.bat -y -loglevel quiet -hide_banner -nostats -i "%%~dpnf.wav" %%f && (
    call FixFFmpegADX.bat %%f > NUL && (
    del "%%~dpnf.wav" )))
))
pause