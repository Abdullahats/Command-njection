from flask import Flask, request
import subprocess

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
    allowed_commands = ['list', 'help', 'status']  # Yalnızca bu komutlara izin veriliyor
    if user_input in allowed_commands:
        subprocess.run([user_input])  # Güvenli komut çalıştırma
        return f"Komut çalıştırıldı: {user_input}"
    else:
        return "Geçersiz komut!"

if __name__ == '__main__':
    app.run(debug=True)
