Here is a detailed **README.md** file for your project:

---

# Real-Time Monitoring System for Rideau Canal Skateway

## **Scenario Description**
The Rideau Canal Skateway in Ottawa, a UNESCO World Heritage Site and popular winter attraction, requires constant monitoring to ensure skater safety. Ice conditions and weather factors must be assessed in real time to identify potential hazards. Our system addresses this need by simulating IoT sensors, processing incoming data in real time, and storing results for further analysis. This enables the National Capital Commission (NCC) to maintain safety and make informed decisions efficiently.

---

## **System Architecture**
The solution is designed to capture real-time data from simulated IoT devices and process it using Azure cloud services. Below is the data flow:

### **Architecture Diagram**
1. **IoT Sensors (Simulated Devices)**:
   - Generate real-time data every 10 seconds from three locations:
     - Dow's Lake
     - Fifth Avenue
     - NAC
   - Each location has 3 devices sending the data.

2. **Azure IoT Hub**:
   - Serves as the ingestion point for sensor data.

3. **Azure Stream Analytics**:
   - Processes the incoming data in real time.
   - Aggregates key metrics for every 5-minute window:
     - Average ice thickness.
     - Maximum snow accumulation.

4. **Azure Blob Storage**:
   - Stores processed data in JSON format for further analysis.
   - Data is organized by year, month, day, hour, and location.

![alt text](<Untitled Diagram.drawio.png>)

---

## **Implementation Details**

### **IoT Sensor Simulation**
#### **Description**
- A Python script simulates IoT sensors at three locations, with each location having three devices.
- Sensors generate data for:
  - Ice Thickness (in cm)
  - Surface Temperature (in °C)
  - Snow Accumulation (in cm)
  - External Temperature (in °C)
  - Timestamp (in UTC)
  
#### **JSON Payload Example**
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

#### **Script Details**
The `deviceO{x}.py` script:
- Generates sensor data every 10 seconds.
- Pushes the data to Azure IoT Hub using the Azure IoT Device SDK.

#### **How to Run**
1. Install dependencies:
   ```bash
   pip install azure-iot-device
   ```
2. Set your IoT Hub connection string in the script.
3. Run the script:
   ```bash
   python deviceO1.py
   python deviceO2.py
   python deviceO3.py
   ```

---

### **Azure IoT Hub Configuration**
1. **Create an IoT Hub**:
   - Navigate to the Azure portal and create an IoT Hub.
2. **Register Devices**:
   - Add three devices for each location (9 devices total).
3. **Set Up Routing**:
   - Configure routing to send incoming data to Azure Stream Analytics.

---

### **Azure Stream Analytics Job**
#### **Input**
- Connect the IoT Hub as the input source.
- Use the default message routing endpoint for ingestion.

#### **Query Logic**
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

#### **Output**
- Define Azure Blob Storage as the output destination.
- Store processed data in JSON format.

---

### **Azure Blob Storage**


#### **File Format**
- All data is stored in JSON format.
- Example `0_a35d604d5a7f4acb8d6c8df287e3aff0_1.json.json` content:
  ```json
  {?
    "WindowEnd": "2024-11-23T12:05:00Z",
    "location": "Dow's Lake",
    "AvgIceThickness": 26.5,
    "MaxSnowAccumulation": 10
  }
  ```

---?

## **Usage Instructions**

### **Running the IoT Sensor Simulation**
1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd RCS/
   ```
2. Run the simulation script:
   ```bash
   python deviceO1.py
   python deviceO2.py
   python deviceO3.py
   ```

### **Configuring Azure Services**
1. **IoT Hub**:
   - Follow steps above to create and configure an IoT Hub.
2. **Stream Analytics**:
   - Set up input (IoT Hub), output (Blob Storage), and query logic as described.
3. **Blob Storage**:
   - Configure the storage container and ensure output data is written successfully.

### **Accessing Stored Data**
1. Navigate to the Blob Storage container in the Azure portal.
2. Locate processed data based on folder structure.
3. Download or view the `0_a35d604d5a7f4acb8d6c8df287e3aff0_1.json` file for analysis.

---

## **Results**

### **Key Outputs**
1. **Aggregated Data:**
   - Average Ice Thickness and Maximum Snow Accumulation calculated for each location every 5 minutes.
2. **Sample Output:**
   - JSON files in Blob Storage with aggregated metrics.

---

## **Reflection**
### **Challenges Faced**
- **Simulating Realistic Data:**
  - Solved by fine-tuning random value generation to match real-world conditions.
- **Azure IoT Hub Configuration:**
  - Addressed by using Azure documentation and tutorials for setup.
- **Stream Analytics Query Debugging:**
  - Overcame SQL syntax issues through iterative testing.

### **Lessons Learned**
- Hands-on experience with Azure services enhanced understanding of real-time data processing pipelines.
- Designing scalable IoT systems requires careful planning and configuration.

---

## **Screenshots**
Screenshots:
1. Storage creation
![alt text](Capture4.PNG)
2. Functional and accurate simulated sensors generating proper JSON payloads.
![alt text](<running all sensors.PNG>)
3. IoT Hub configuration.
![alt text](Capture.PNG)
4. Stream Analytics job settings and queries.
![alt text](Capture3.PNG)
![alt text](Capture2.PNG)
5. Blob Storage output structure.
![alt text](Capture3.PNG)
![alt text](Capture4.PNG)
![alt text](<Capture3 - Copy.PNG>)

---