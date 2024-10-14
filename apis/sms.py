import vonage 




client = vonage.Client(key="cef9c06c", secret="jQrxQfMy6cJ8Z3kw")
sms = vonage.Sms(client)

def send_sms():
    responseData = sms.send_message(
        {
            "from": "Vonage APIs",
            "to": "919369489827",
            "text": "Alert. The water level is increasing. Glacier Lake Outbreak Forcasted.",

        }
    )

    if responseData["messages"][0]["status"] == "0":
        print("Message sent successfully.")
    else:
        print(f"Message failed with error: {responseData['messages'][0]['error-text']}")


