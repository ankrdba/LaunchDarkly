# LaunchDarkly App Instructions

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

2. Run application
   ```bash
   python3 app.py
   ```
3. Curl for toogle flag:
   ```bash
   curl -X PATCH 'https://app.launchdarkly.com/api/v2/flags/default/developer-feature' \
    -H 'LD-API-Version: 20240415' \
    -H 'Authorization: api-219fe34d-0f60-481d-ae24-87b3446dd9ff' \
    -H 'Content-Type: application/json' \
    -d '[
        {
          "op": "replace",
          "path": "/environments/test/on",
          "value": false
        }
   ]'
  ```
