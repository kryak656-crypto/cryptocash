from flask import Flask, render_template_string

app = Flask(__name__)

# Дизайн у стилі Binance з назвою CryptoCash Machine
css = '''
body {
    background-color: #0b0e11;
    color: #eaecef;
    font-family: 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
    margin: 0; padding: 0;
}
header {
    background-color: #181a20;
    padding: 15px 8%;
    display: flex; justify-content: space-between; align-items: center;
    border-bottom: 1px solid #2b2f36;
}
.logo { color: #fcd535; font-size: 24px; font-weight: 800; letter-spacing: 1px; }
.hero { text-align: center; padding: 80px 20px; }
.hero h1 { font-size: 52px; color: #ffffff; margin-bottom: 10px; font-weight: 700; }
.price-tag { color: #fcd535; font-size: 32px; font-weight: bold; margin: 20px 0; }
.btn-main {
    background-color: #fcd535; color: #181a20;
    padding: 14px 45px; border-radius: 4px;
    text-decoration: none; font-weight: bold; font-size: 18px;
    display: inline-block; transition: 0.3s;
}
.btn-main:hover { background-color: #e2c02d; transform: scale(1.05); }

.hot-btn-box { margin-top: 40px; background: #1e2329; padding: 25px; border-radius: 12px; display: inline-block; border: 1px solid #474d57; }
.hot-btn {
    background-color: #fcd535; color: #181a20;
    border: none; padding: 12px 25px;
    cursor: pointer; border-radius: 4px; font-weight: bold; font-size: 16px;
}
.wallet-label { display: block; color: #848e9c; margin-bottom: 10px; font-size: 14px; }

.features { 
    background-color: #0b0e11; padding: 60px 10%; 
    display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 25px; 
}
.feature-card { 
    background: #181a20; padding: 30px; border-radius: 12px; 
    border: 1px solid #2b2f36; transition: 0.3s;
}
.feature-card:hover { border-color: #fcd535; background: #1e2329; }
.feature-card h3 { color: #fcd535; margin-top: 0; font-size: 22px; }
.feature-card p { color: #848e9c; line-height: 1.6; }

footer { text-align: center; padding: 40px; color: #474d57; border-top: 1px solid #2b2f36; font-size: 13px; }
'''

html = '''
<!DOCTYPE html>
<html lang="uk">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>CryptoCash Machine | Trading Bot</title>
    <style>{{ css|safe }}</style>
</head>
<body>
    <header>
        <div class="logo">CryptoCash <span style="color:white;">Machine</span></div>
        <div style="color: #848e9c; font-size: 14px; font-weight: 500;">Markets | Trade | Futures</div>
    </header>

    <div class="hero">
        <h1>Торгуй розумніше з CryptoCash</h1>
        <p style="color: #848e9c; font-size: 18px;">Твій персональний бот для автоматизації прибутку</p>
        <div class="price-tag">$30 <span style="font-size: 18px; color: #848e9c;">/ Life-time access</span></div>
        <a href="#" class="btn-main">Запустити Машину</a>

        <br>
        <div class="hot-btn-box">
            <span class="wallet-label">Оплата на TON (натисніть для копіювання):</span>
            <button class="hot-btn" onclick="copyWallet()">🔥 КОПІЮВАТИ ГАМАНЕЦЬ</button>
            <p id="status" style="color: #02c076; margin-top: 10px; font-weight: bold; height: 20px;"></p>
        </div>
    </div>

    <div class="features">
        <div class="feature-card">
            <h3>Повний офлайн</h3>
            <p>CryptoCash Machine працює в хмарі. Ваша присутність не потрібна — бот заробляє гроші навіть під час вашого сну.</p>
        </div>
        <div class="feature-card">
            <h3>Доступ назавжди</h3>
            <p>Жодних щомісячних чеків. Один платіж $30 відкриває повний функціонал без обмежень у часі.</p>
        </div>
        <div class="feature-card">
            <h3>Алгоритми Binance</h3>
            <p>Ми використовуємо передові стратегії аналізу ринку, щоб мінімізувати ризики та максимізувати ROI.</p>
        </div>
    </div>

    <footer>
        © 2024 CryptoCash Machine Pro. Не є фінансовою порадою.
    </footer>

    <script>
    function copyWallet() {
        const wallet = "UQDp96IiqWlf7voqDzxjTppcTmJheRQKb7nZCNv2LNDhfn5R";
        navigator.clipboard.writeText(wallet).then(() => {
            const status = document.getElementById('status');
            status.innerText = "Адресу скопійовано! Очікуємо оплату.";
            setTimeout(() => { status.innerText = ""; }, 3000);
        });
    }
    </script>
</body>
</html>
'''

@app.route('/')
def index():
    return render_template_string(html, css=css)

if __name__ == '__main__':
    # Запускаємо на порту 5555
    app.run(host='0.0.0.0', port=5555, debug=False)
