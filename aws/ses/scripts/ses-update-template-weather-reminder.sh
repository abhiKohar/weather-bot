#!/bin/bash
echo 'Updating weather-reminder-email-template'
aws/ses/scripts/ses-update-template.sh aws/ses/emails/weather-email/weather-reminder-email-template.json
echo 'Update succcessful'
