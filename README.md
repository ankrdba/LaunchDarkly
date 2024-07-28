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
## Demo Part 1: Release and Remediate 
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
## Demo Part 2: Target
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

4. Refresh the application 10 times to reach User11. The textbox will disappear for all users after User10.

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

## Demo Part 3: Experimentation

### Experiment Objective
The goal of the experiment is to measure the impact of different feature variations on user behaviour. Specifically, you might be testing whether showing certain features (like a textbox, developer-specific content, or tester-specific content) affects user engagement or other key metrics.

### Experiment Design
Variations: Different versions of the feature flag (e.g., showing or hiding a textbox)
Metrics: The outcome you want to measure, such as user engagement, conversion rates, etc
Targeting: Criteria for including users in the experiment (e.g., all users, specific segments)

### Example Scenario

Feature Flag Variations:
Variation A: Show textbox
Variation B: Show developer-specific content
Variation C: Show tester-specific content

Metrics:
Engagement (e.g. clicking the "Engage" button)
Time spent on the page
Interaction with specific features

Audience:
To compare the behaviour of the users exposed to the feature against those who are not, we will target only 90% of the users in this experiment. The remaining 10% (control group) will not receive the feature. 

Random Assignment: Launchdarkly handles the random assignment based on the user key.

1. Create a metric called first-metric with the following settings
   
   <img width="237" alt="Screenshot 2024-07-28 at 11 53 19" src="https://github.com/user-attachments/assets/81f4b072-ef91-44ed-a446-f665955a5347">

2. Create an Experiment with the following settings

   <img width="1165" alt="Screenshot 2024-07-28 at 14 48 52" src="https://github.com/user-attachments/assets/78895389-32d0-4727-a098-de5fdc65fab6">
   <img width="1144" alt="Screenshot 2024-07-28 at 14 49 30" src="https://github.com/user-attachments/assets/3dbfc131-06be-404c-8aa8-56ed53acce49">

3. 

   
   

## Demo Part 4: Github Integration
I am demonstrating the Github integration with Launchdarkly through a yaml workflow that evaluates the status of a Launchdarkly feature flag every time a change is pushed into this repository. This part requires a repository secret called LAUNCHDARKLY_SDK_KEY to be configured in the Github settings. 

1. Configure a repository secret called LAUNCHDARKLY_SDK_KEY in the Github settings
2. Make a change - add a new text file or change an existing one
3. Go to Actions --> Click on the latest workflow run --> Click on eval-flags
4. The workflow will mark True or False based on the status of show-textbox flag
   


