@echo off
call ffmpeg.bat -version && (
echo.

where /Q /R SOUND_raw *.wav *.mp3 *.flac && robocopy SOUND_raw SOUND *.wav *.mp3 *.flac /S > NUL

for /F "delims==" %%f in ('where /F /R SOUND *.wav *.mp3 *.flac') DO (
    echo %%f
    call ffmpeg.bat -y -loglevel quiet -hide_banner -nostats -i %%f "%%~dpnf.adx" && (
    call FixFFmpegADX.bat "%%~dpnf.adx" > NUL && (
    del %%f))
))
pause