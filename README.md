Flask Command Injection Demo
Bu proje, Flask tabanlı bir web uygulamasında Command Injection (Komut Enjeksiyonu) zafiyetini ve nasıl düzeltileceğini göstermektedir.

📌 Zafiyetin Açıklaması

Uygulama, kullanıcının girdiği komutu subprocess.run() ile çalıştırmaktadır. Eğer giriş doğrulanmazsa, saldırgan sistem komutları çalıştırabilir.

🛠 Zafiyetin İstismarı
Web arayüzünde aşağıdaki gibi bir giriş yapılırsa:
whoami; cat /etc/passwd
Saldırgan sistem dosyalarını okuyabilir veya uzaktan erişim sağlayabilir.
🔧 Güvenli Versiyon
Zafiyeti gidermek için:
Kullanıcı girdisi doğrulandı.
Sadece belirli komutlara izin verildi.
subprocess.run() yerine güvenli bir allowlist mekanizması oluşturuldu.
✅ Güvenli Kod
from flask import Flask, request
import subprocess

app = Flask(__name__)

ALLOWED_COMMANDS = {
    "list": ["ls", "-la"],
    "help": ["echo", "Bu bir yardım mesajıdır."],
    "status": ["uptime"]
}

@app.route('/')
def index():
    return 
        <form method="post" action="/run-command">
            Komut Girin: <input type="text" name="command">
            <input type="submit" value="Çalıştır">
        </form>

@app.route('/run-command', methods=['POST'])
def run_command():
    user_input = request.form['command']
    if user_input in ALLOWED_COMMANDS:
        result = subprocess.run(ALLOWED_COMMANDS[user_input], capture_output=True, text=True)
        return f"<pre>{result.stdout}</pre>"
    else:
        return "Geçersiz komut!"

if __name__ == '__main__':
    app.run(debug=True)

📊 OWASP ve CVSS Bilgileri

OWASP Kategorileri:
A01: Injection
A05: Security Misconfiguration
CVSS Skoru: 9.8 (Kritik)
