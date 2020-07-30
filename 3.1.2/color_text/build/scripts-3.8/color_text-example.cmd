@echo off
set now_path = %~f0
set PATH  = %PATH%;%now_path%
echo from color_text import output_example > color_text-example.py
echo output_example(time_to_sleep = 0) >> color_text-example.py
python color_text-example.py
del /F /S /Q %now_path%\color_text-example.py
