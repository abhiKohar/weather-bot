#!/bin/bash
aws lambda update-function-code --function-name arn:aws:lambda:us-east-2:536283227883:function:weather-bot --zip-file fileb://weather-bot.zip  --region us-east-2