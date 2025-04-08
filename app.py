from flask import Flask
import getpass
import time
import subprocess
import pytz
from datetime import datetime

app = Flask(__name__)

@app.route('/htop')
def htop():
    name = "Sushmitha Reddy"  # Replace with your full name
    username = getpass.getuser()
    
    # Get current IST time
    ist = pytz.timezone('Asia/Kolkata')
    current_time = datetime.now(ist).strftime('%Y-%m-%d %H:%M:%S')
    
    # Get top command output
    try:
        top_output = subprocess.check_output(['top', '-b', '-n', '1']).decode('utf-8')
    except Exception as e:
        top_output = str(e)

    html = f"""
    <html>
    <body>
        <h2>Name: {name}</h2>
        <h2>Username: {username}</h2>
        <h2>Server Time (IST): {current_time}</h2>
        <pre>{top_output}</pre>
    </body>
    </html>
    """
    return html

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
