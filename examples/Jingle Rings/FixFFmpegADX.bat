@echo off
set prev_cd=%cd%
cd "%~dp0"../../dependencies/FixFFmpegADX/
call FixFFmpegADX.exe %1 %2 %3 %4 %5 %6 %7 %8 %9
cd %prev_cd%