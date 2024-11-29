import time
import random
from datetime import datetime, timezone
from azure.iot.device import IoTHubDeviceClient, Message

# Replace with your actual IoT Hub device connection string
CONNECTION_STRING = "HostName=RCSiot.azure-devices.net;DeviceId=deviceO2;SharedAccessKey=1JsRFz7AQTMwGNXr7skQmr6qf7t9OuZiQrZRAPpZkEo="

def get_telemetry():
    return {
        "location": "Fifth Avenue",  # Hardcoded location
        "iceThickness": random.randint(20, 40),  # Ice thickness in cm (no decimals)
        "surfaceTemperature": random.randint(-5, 5),  # Surface temperature in °C (no decimals)
        "snowAccumulation": random.randint(0, 20),  # Snow accumulation in cm (no decimals)
        "externalTemperature": random.randint(-10, 5),  # External temperature in °C (no decimals)
        "timestamp": datetime.now(timezone.utc).isoformat()  # Current UTC timestamp
    }

def main():
    # Create IoT Hub client
    client = IoTHubDeviceClient.create_from_connection_string(CONNECTION_STRING)

    print("Sending telemetry to IoT Hub...")
    try:
        while True:
            # Generate telemetry data
            telemetry = get_telemetry()
            message = Message(str(telemetry))  # Convert to string for transmission
            client.send_message(message)  # Send to IoT Hub
            print(f"Sent message: {message}")
            time.sleep(10)  # Wait for 10 seconds
    except KeyboardInterrupt:
        print("Stopped sending messages.")
    finally:
        client.disconnect()  # Disconnect the client

if __name__ == "__main__":
    main()
