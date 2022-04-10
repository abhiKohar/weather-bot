#!/bin/bash
#aws ses create-template --cli-input-json file://aws/ses/emails/weather-email/weather-reminder-email-template.json
aws ses create-template --cli-input-json file://$1