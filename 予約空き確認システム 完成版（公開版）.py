# 予約空き確認システム 完成版（e-license使用自動車学校対象） - Python
# 開発者：nekopath
# 作成日：2024年3月5日
# 使い始める前に、必ず準備をすること。
# 1. このプログラムを実行するために、以下のライブラリをインストールしてください。
# pip install selenium
# pip install chromedriver-binary
# pip install requests
# 2. このプログラムを実行するために、以下のファイルをダウンロードしてください。
# https://chromedriver.chromium.org/downloads
# 3. ダウンロードしたファイルを解凍し、chromedriver.exeを以下のパスに置くと動くと思います。違ったらごめんなさい！
# C:\Users\ユーザー名\AppData\Local\Programs\Python\Python312\Lib\site-packages\chromedriver_binary\chromedriver.exe
# 4. このプログラムを実行するために、以下の手順を実行してください。
# 4-1. このプログラムを実行するために、以下のファイルをダウンロードしてください。
# https://notify-bot.line.me/ja/
# 4-2. ダウンロードしたファイルを解凍し、line_notify_token.txtを作成してください。
# その後に、トークンを以下のコードの指定した場所に書き換えてください。

import time
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

def send_line_notify(notification_message):
    line_notify_token = 'LINE Notifyのトークンを入れてね'
    line_notify_api = 'https://notify-api.line.me/api/notify'
    headers = {'Authorization': f'Bearer {line_notify_token}'}
    data = {'message': notification_message}
    response = requests.post(line_notify_api, headers=headers, data=data)
    print(response.text)

while True:
    chrome_options = Options()
    # ヘッドレスモードを有効にする場合（ブラウザのUIを表示しないモード）
    # chrome_options.add_argument('--headless')

    # WebDriverのインスタンスを自動管理されるChromeDriverで作成
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

    # ログインするページにアクセス
    driver.get('ログイン画面のURLをここに入れてね')

    # 10秒待機
    time.sleep(10)

    # ログイン情報を入力してログイン
    driver.find_element(By.ID, 'studentId').send_keys('教習生番号を入れてね')
    driver.find_element(By.ID, 'password').send_keys('パスワードを入れてね')
    driver.find_element(By.ID, 'login').click()

    # 6秒待機
    time.sleep(6)

    # ページのソースコードを取得して条件チェック
    page_source = driver.page_source
    if '<td class="status1">' in page_source:
        send_line_notify("\n予約の空きを検知しました。予約ページを確認してください。\nログインページのURLをここに置き換えるとすぐアクセスできるよ")

    # ブラウザを閉じる
    driver.quit()

    # 5分待機
    time.sleep(300)
