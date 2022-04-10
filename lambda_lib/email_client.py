import os
import boto3


class EmailClient:
    ACCESS_ID = os.getenv("AWSAccessKeyId")
    ACCESS_KEY = os.getenv("AWSSecretKey")
    ses = boto3.client('ses', region_name='us-east-2',
                       aws_access_key_id=ACCESS_ID,
                       aws_secret_access_key=ACCESS_KEY)
    EMAIL_SOURCE = os.getenv('EMAIL_SOURCE')
    DEFAULT_RECIPIENT = EMAIL_SOURCE
    AWS_SES_EMAIL_TEMPLATE = 'WeatherReminderTemplate'

    @classmethod
    def verify_email_id(cls):
        response = cls.ses.verify_email_identity(
            EmailAddress="abhinavkohar007@gmail.com"
        )
        print(response)

    @classmethod
    def send_forecast(cls, template_data, recipient=DEFAULT_RECIPIENT):
        # print("-------------------------------------\n",template_data)
        response = cls.ses.send_templated_email(
            Source=cls.EMAIL_SOURCE,
            Destination={
                'ToAddresses': [
                    recipient,
                ],
            },
            Template=cls.AWS_SES_EMAIL_TEMPLATE,
            TemplateData=template_data
        ) 

        print(response)
