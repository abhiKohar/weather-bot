#!/bin/bash
cd weather-env/Lib/site-packages/
7z a -tzip  ../../../weather-bot.zip .
cd ../../../
7z u ./weather-bot.zip lambda_function.py .env -r lambda_lib

# add 7z or winrar to windows path variable in order for above commands to work in windows.
