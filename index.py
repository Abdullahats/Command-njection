import subprocess
from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def index():
    return '''
        <form method="post" action="/run-command">
            Komut Girin: <input type="text" name="command">
            <input type="submit" value="Çalıştır">
        </form>
    '''

@app.route('/run-command', methods=['POST'])
def run_command():
    user_input = request.form['command']
    output = subprocess.getoutput(user_input)  # Komutun çıktısını al
    return f"<pre>{output}</pre>"  # HTML içinde düzgün göster

if __name__ == '__main__':
    app.run(debug=True)
