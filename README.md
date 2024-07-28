# LaunchDarkly Demo Instructions

This application demonstrates the following features of Launchdarkly platform.

1. Feature Flag and Listener Implementation
2. Individual and Rule based targeting
3. Feature experimentation using metrics
4. Integration of Launchdarkly with Github

## Setup Instructions

1. Install Required Dependencies**

   a. Install pip** (if not already installed):
   ```bash
   curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
   python3 get-pip.py
   ```
   b. Install ldclient :
   ```bash
   pip install ldclient-py
   ```
   c. Install Flask :
   ```bash
   pip install Flask
   ```
2. Set up repository on the local machine

   a. Clone git repository
      ```git clone https://github.com/ankrdba/LaunchDarkly.git
      ```
      
   b. Setup SDK Key and Client ID in constants.py
      ```echo "LAUNCHDARKLY_SDK_KEY='YOUR_SDK_KEY'" >>constants.py
         echo "CLIENT_ID = 'YOUR_CLIENT_ID'" >>constants.py
      ```
3. Create Feature Flags

   a. Create a feature flag called show-textbox with the following settings

      <img width="1168" alt="Screenshot 2024-07-28 at 11 00 21" src="https://github.com/user-attachments/assets/99f04265-307c-4475-b0e2-7448ce659413">

   b. Create a feature flag called tester-feature with the following settings

      <img width="1158" alt="Screenshot 2024-07-28 at 11 02 39" src="https://github.com/user-attachments/assets/1107a5cc-e3e1-41a7-a250-139d590fc1c7">

   c. Create a feature flag called developer-feature with the following settings

      <img width="1161" alt="Screenshot 2024-07-28 at 11 03 44" src="https://github.com/user-attachments/assets/7f979842-a4e9-437d-898d-01e53b1160fd">   

2. Run application
   ```bash
   python3 app.py
   ```
## Part 1 Release and Remediate 
The application has a textbox feature that is managed with show-textbox flag. The textbox is displayed only if the feature is enabled.

1. Open the application
   http://127.0.0.1:8080
   
2. Curl for toogle flag :
   ```bash
   curl -X PATCH 'https://app.launchdarkly.com/api/v2/flags/default/show-textbox' \
    -H 'LD-API-Version: 20240415' \
    -H 'Authorization: YOUR_ACCESS_TOKEN' \
    -H 'Content-Type: application/json' \
    -d '[
        {
          "op": "replace",
          "path": "/environments/test/on",
          "value": false
        }
   ]'
  ```

