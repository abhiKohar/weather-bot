# Weather Reminder

## Overview

After the impact Hurricane Ida had on the United States' east coast, I thought it may be a good idea to receive daily weather alerts to ensure readiness.

## Technology Stack

* [Python](https://www.python.org/)
* [AWS Lambda](https://aws.amazon.com/lambda/)
* [AWS Eventbridge](https://aws.amazon.com/eventbridge/)
* [AWS SES](https://aws.amazon.com/ses/)
* [OpenWeatherMap API](https://openweathermap.org/api)

## Example

<img src="./media/email_sample.PNG" alt="Weather email example" />

## Setup

**AWS**

* Configure the [aws cli](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-configure.html)
* [Verify email addresses to send/receive email while in sandbox mode](https://docs.aws.amazon.com/ses/latest/DeveloperGuide/verify-email-addresses.html)
* Sign up for the [OpenWeatherMap API](https://openweathermap.org/appid) and use the provided API key to set an `OPEN_WEATHER_MAP_API` environment variable
* Create a lambda function called `weather-reminder`. Note: if your lambda is called something different, rename instances of `weather-reminder` to your lambda function name. This especially applies to build and deploy shell scripts in the `scripts` directory.
* Provide values for all environment variables mentioned in `.env.template` to the lambda function
* [Configure AWS Eventbridge to trigger the lambda function](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-run-lambda-schedule.html)

**Local**

* Setup a virtual environment, `python3 -m venv .venv`
* Run `pip install -r requirements.txt` to install dependencies
* Run `python lambda_function.py` to test locally
    * Note: Either populate a `.env` file and [load its contents for local development](https://github.com/theskumar/python-dotenv) or manually replace environment variables used in the code with values while testing locally.
    ** pip install python-dotenv
    ** from dotenv import load_dotenv
    ** load_dotenv()

## Deployment

* Run `./scripts/build-deploy.sh` to build and deploy the lambda to AWS
* Run `./aws/ses/scripts/ses-create-weather-reminder-template.sh` to create the `WeatherReminderTemplate` email template in SES
* Run `./aws/ses/scripts/ses-update-template-weather-reminder.sh` to update the `WeatherReminderTemplate` email templae in SES

* Update the email sending persmissions for lamda user
https://docs.aws.amazon.com/ses/latest/dg/control-user-access.html#iam-and-ses-examples-email-sending-actions
* Set the run schedule 
https://docs.aws.amazon.com/lambda/latest/dg/services-cloudwatchevents-expressions.html

* AWS eventbridge
<img src="./media/event_bridge.PNG" alt="Weather email example" />

* AWS lamda function
<img src="./media/lamda-function.PNG" alt="Weather email example" />
IAM 
<img src="./media/IAM.PNG" alt="Weather email example" />
