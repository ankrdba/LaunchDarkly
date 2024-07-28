# LaunchDarkly Demo Instructions

This application demonstrates the following features of Launchdarkly platform.

1. Feature Flag and Listener Implementation
2. Individual and Rule-based targeting
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
      ```bash
   git clone https://github.com/ankrdba/LaunchDarkly.git
      ```
      
   b. Setup SDK Key and Client ID in constants.py
      ```bash
   echo "LAUNCHDARKLY_SDK_KEY='YOUR_SDK_KEY'" >>constants.py
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
## Part 1: Release and Remediate 
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
## Part 2: Target
In this part, we will demo individual targeting and rule-based targeting.

### Individual Targeting

Every time you refresh the application, the user counter increments by 1. The show-textbox flag has been configured to work only for the first ten users - User1 to User10

1. Open the application
   http://127.0.0.1:8080

2. Ensure that the show-textbox flag is enabled

   Curl for toogle flag:
   
   ```bash
   curl -X PATCH 'https://app.launchdarkly.com/api/v2/flags/default/show-textbox' \
    -H 'LD-API-Version: 20240415' \
    -H 'Authorization: YOUR_ACCESS_TOKEN' \
    -H 'Content-Type: application/json' \
    -d '[
        {
          "op": "replace",
          "path": "/environments/test/on",
          "value": true
        }
   ]'
   ```

4. Refresh the application 10 times to reach User11. The textbox feature will not be there for User11

### Rule-based Targeting

The application has two features called developer-feature and tester-feature which work as per a user's role - developer or a tester. All even-number users are developers and odd-number users are testers. e.g. User2, User4, User 6 are developers and User1, User3, User5 are testers. The rule-based targeting is demonstrated by displaying a different graphic as per a user's role.

1. Open the application
   http://127.0.0.1:8080

2. Ensure that the tester-feature is enabled

  Curl for toogle flag :
  
   ```bash
   curl -X PATCH 'https://app.launchdarkly.com/api/v2/flags/default/tester-feature' \
    -H 'LD-API-Version: 20240415' \
    -H 'Authorization: YOUR_ACCESS_TOKEN' \
    -H 'Content-Type: application/json' \
    -d '[
        {
          "op": "replace",
          "path": "/environments/test/on",
          "value": true
        }
   ]'
   ```
3. Ensure that the developer-feature is enabled

  Curl for toogle flag :
  
   ```bash
   curl -X PATCH 'https://app.launchdarkly.com/api/v2/flags/default/developer-feature' \
    -H 'LD-API-Version: 20240415' \
    -H 'Authorization: YOUR_ACCESS_TOKEN' \
    -H 'Content-Type: application/json' \
    -d '[
        {
          "op": "replace",
          "path": "/environments/test/on",
          "value": true
        }
   ]'
   ``` 

4. Refresh the application multiple times to see both roles and their respective graphics alternate

