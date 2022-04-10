#!/bin/bash
#aws ses send-templated-email --cli-input-json file://aws/ses/emails/weather-email/weather-reminder-email-template.json
aws ses send-templated-email --cli-input-json file://$1