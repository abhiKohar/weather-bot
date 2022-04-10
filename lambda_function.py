import json
from lambda_lib.weather_client import WeatherClient
from lambda_lib.email_client import EmailClient

def lambda_handler(event, context):
    try:
        forecasts = WeatherClient.get_seven_forecast_formatted() # can pass the lat_long here
        # EmailClient.verify_email_id()
        EmailClient.send_forecast(forecasts)

        return {
            'statusCode': 200,
            'body': json.dumps({'message': 'Email sent'})
        }
    except Exception as e:
        print(str(e))
        return {
            'statusCode': 500,
            'body': json.dump({'message': 'Internal server error'})
        }

if __name__ == '__main__':
    lambda_handler(None, None)