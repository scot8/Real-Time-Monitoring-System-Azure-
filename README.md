# Group_Assignment 20
Seyfullah Burul,
Rohan James Scott,
Erturk Savas.

# Real-Time Monitoring System for Rideau Canal Skateway

## **Scenario Description**
The Rideau Canal Skateway in Ottawa, a UNESCO World Heritage Site and popular winter attraction, requires constant monitoring to ensure skater safety. Ice conditions and weather factors must be assessed in real time to identify potential hazards. This system addresses the need by simulating IoT sensors, processing incoming data in real time, and storing results for further analysis. This enables the National Capital Commission (NCC) to maintain safety and make informed decisions efficiently.

---

## **System Architecture**
The solution captures real-time data from simulated IoT devices and processes it using Azure cloud services. Below is the data flow:

### **Architecture Diagram**

IoT Sensors (Simulated Devices):
- Generate real-time data every 10 seconds from three locations: Dow's Lake, Fifth Avenue, and NAC.
- Each location has multiple devices sending data.

Azure IoT Hub:
- Serves as the ingestion point for sensor data.

Azure Stream Analytics:
- Processes incoming data in real time.
- Aggregates key metrics for every 5-minute window, including average ice thickness and maximum snow accumulation.

Azure Blob Storage:
- Stores processed data in JSON format for further analysis.
- Data is organized by year, month, day, hour, and location.

![Architecture Diagram](https://github.com/user-attachments/assets/7bac241b-1ed8-492a-a075-09281d8f9a67)

---

## **Implementation Details**

### **IoT Sensor Simulation**

**Description:**
A Python script simulates IoT sensors at three locations, with each location having multiple devices. Sensors generate data for ice thickness, surface temperature, snow accumulation, external temperature, and timestamp in UTC.

**JSON Payload Example:**
```json
{
  "location": "Dow's Lake",
  "deviceId": "Device-1",
  "iceThickness": 27,
  "surfaceTemperature": -1,
  "snowAccumulation": 8,
  "externalTemperature": -4,
  "timestamp": "2024-11-23T12:00:00Z"
}
```

**Script Details:**
The `deviceO{x}.py` script generates sensor data every 10 seconds and pushes it to Azure IoT Hub using the Azure IoT Device SDK.

**How to Run:**
```bash
pip install azure-iot-device
```
Set your IoT Hub connection string in the script and run it:
```bash
python deviceO1.py
python deviceO2.py
python deviceO3.py
```

---

### **Azure IoT Hub Configuration**

Create an IoT Hub in the Azure portal and register devices. Configure routing to send incoming data to Azure Stream Analytics.

---

### **Azure Stream Analytics Job**

**Input:**
Connect the IoT Hub as the input source.

**Query Logic:**
```sql
SELECT
    IoTHub.ConnectionDeviceId AS DeviceId,
    AVG(iceThickness) AS AvgIceThickness,
    MAX(snowAccumulation) AS MaxSnowAccumulation,
    System.Timestamp AS EventTime
INTO
    [rcsoutput]
FROM
    [RCSiot]
GROUP BY
    IoTHub.ConnectionDeviceId, TumblingWindow(minute, 5)
```

**Output:**
Define Azure Blob Storage as the output destination and store processed data in JSON format.

---

### **Azure Blob Storage**

**File Format:**
All data is stored in JSON format.
Example file content:
```json
{
  "WindowEnd": "2024-11-23T12:05:00Z",
  "location": "Dow's Lake",
  "AvgIceThickness": 26.5,
  "MaxSnowAccumulation": 10
}
```

---

## **Usage Instructions**

**Running the IoT Sensor Simulation:**
Clone the repository:
```bash
git clone <repository-url>
cd RCS/
```
Run the simulation script:
```bash
python deviceO1.py
python deviceO2.py
python deviceO3.py
```

**Configuring Azure Services:**
Follow the steps above to create and configure an IoT Hub, Stream Analytics job, and Blob Storage container.

**Accessing Stored Data:**
Navigate to the Blob Storage container in the Azure portal. Locate processed data based on the folder structure and download JSON files for analysis.

---

## **Results**

**Key Outputs:**
Aggregated metrics for each location every 5 minutes, including average ice thickness and maximum snow accumulation.

---

## **Reflection**

**Challenges Faced:**
- Simulating realistic data: Resolved by fine-tuning random value generation.
- Azure IoT Hub configuration: Addressed using Azure documentation.
- Stream Analytics query debugging: Iterative testing resolved SQL syntax issues.

**Lessons Learned:**
- Enhanced understanding of real-time data processing pipelines.
- Improved ability to design scalable IoT systems.

---

## **Screenshots**

1. **Storage Creation:**
![Storage Creation](https://github.com/user-attachments/assets/bf84ca9f-138a-48d2-8635-8b193c8402f2)

2. **Functional and Accurate Simulated Sensors:**
![Running All Sensors](https://github.com/user-attachments/assets/3b99e520-d0a2-49a9-a3c9-5fa14d95a911)

3. **IoT Hub Configuration:**
![IoT Hub Configuration](https://github.com/user-attachments/assets/12444133-24db-4198-a8fa-4f258b41c4a3)

4. **Stream Analytics Job Settings:**
![Stream Analytics Query](https://github.com/user-attachments/assets/2e96054d-70e4-4b79-8e71-487e495bf6da)

5. **Blob Storage Output Structure:**
![Blob Storage Output](https://github.com/user-attachments/assets/ff9b7324-737b-4c14-9030-57a32357de40)
![Capture4](https://github.com/user-attachments/assets/846a778d-11e0-45f3-8386-8086c7aa1c06)
![Capture3 - Copy](https://github.com/user-attachments/assets/0b612e9f-97e2-41ab-99d8-5f92a41c67be)


