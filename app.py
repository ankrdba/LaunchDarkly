from flask import Flask, render_template, jsonify, request
import ldclient
from ldclient.config import Config

app = Flask(__name__)

# LaunchDarkly SDK setup
sdk_key = 'sdk-8df86352-6fb3-4b20-843c-4908d4ea8223'  # Replace with your actual SDK key
ldclient.set_config(Config(sdk_key))

# Create a LaunchDarkly client instance
ld_client = ldclient.get()

# Define a user for LaunchDarkly (this can be dynamic based on actual users)
users = [
    {"key": f"user{i}", "name": f"User{i}", "email": f"user{i}@example.com", "custom": {"role": "tester" if i % 2 == 1 else "developer"}}
    for i in range(1, 101)
]

userIdx = 0

@app.route('/')
def index():
    global userIdx
    user = users[userIdx % len(users)]
    userIdx += 1
    return render_template('index.html', user=user, userIdx=userIdx)

@app.route('/api/track-event', methods=['POST'])
def track_event():
    event_data = request.json
    print(event_data['user'])
    print(event_data['value'])
    ld_client.track("first-metric", event_data['user'], event_data['value'])
    return jsonify({"status": "event tracked"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
