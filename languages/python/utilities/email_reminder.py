from datetime import datetime

import boto3


def send_plain_email(gre_delta, toefl_delta, application_delta):
    ses_client = boto3.client(
        'ses',
        aws_access_key_id="",
        aws_secret_access_key="",
        region_name="us-east-1"
    )
    CHARSET = "UTF-8"

    response = ses_client.send_email(
        Destination={
            "ToAddresses": [
                "mobasshir.bhuiya@graaho.com",
            ],
        },
        Message={
            "Body": {
                "Text": {
                    "Charset": CHARSET,
                    "Data": f"You have left {gre_delta} for GRE, {toefl_delta} for TOEFL, {application_delta} for Application Processing. Allah Vorosha!! :3",
                }
            },
            "Subject": {
                "Charset": CHARSET,
                "Data": "Reminder!!!",
            },
        },
        Source="mobasshir.bhuiya@graaho.com",
    )


gre_date = datetime.strptime('Aug 15 2022', '%b %d %Y')
toefl_date = datetime.strptime('Aug 25 2022', '%b %d %Y')
application_date = datetime.strptime('Sep 01 2022', '%b %d %Y')

email_sent_dict = {}


while True:
    today = datetime.today()
    today_str = today.strftime('%m/%d/%Y')

    if email_sent_dict.get(today_str, None) is None:
        email_sent_dict[today_str] = False

    if email_sent_dict[today_str] is False:
        gre_delta = gre_date - today
        toefl_delta = toefl_date - today
        application_delta = application_date - today
        send_plain_email(gre_delta, toefl_delta, application_delta)
        print("Email sent :)")
        email_sent_dict[today_str] = True
