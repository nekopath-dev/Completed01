# 名前

e-license使用自動車学校　予約空き自動通知システム

## 簡単な説明

自動車学校で、e-licenseを使用して技能予約などを行っているところは多いのではないでしょうか。

私は、早く卒業したかったので、１分ごとに予約ページを見ていましたが、私は人間。一々確認するのも面倒だったのです。

というわけで、予約の空きがあったら自動で通知してくれるPythonコードを書きました。

５分毎に確認してくれる半永久型のコードなので、一度実行すれば後は放置すれば良きです。

ただし、極稀にエラーが出て止まることがあるので、ご了承ください。

また、現在私は卒業済みで現在これがうまく動くのか保証ができません。全て自己責任で行ってください。

***デモ***

すみません！デモは用意できませんでした。

実際に動かして確認してみてください。

## 機能

ログインページに５分毎にアクセスして、ログインフォームに教習生番号とパスワードを自動入力してログインし、空きを確認します。

空きがあるかどうかは、予約ページのHTMLに<td class="status1">があるかどうかで確認しており、あった場合は、LINE Notifyを使用して通知します。

## 必要要件

VS Codeが十分動かせるPC

その他は、コードのコメントに乗せています。

少し漏れがあるかも知れません。その際は自力で調べてください...すみません。

## 使い方

コードをVS Codeに貼り付け、Pythonファイルで保存します。

後は実行して放置するだけです。

※Pythonが動かせるようにセットアップされていることが前提となります。

ずっと放置する形で使うのですが、PC1台ずっと電源をつけて放置みたいな形になると思うので

いらないPCがない人は、Microsoft Azureなどのクラウドサービスで仮想PCを作って、そこで実行すると良いと思います。

お金がかかると思いますが、私は学生クレジットを使用して、Azureで24時間動かしっぱなしにしてました。

## インストール

私があまり詳しくないので、説明できないです...

pyファイルでダウンロードして、VS Codeで実行するのが良いと思います。

## その他

このコードは、e-license非公式で、個人が作成しています。

特に問題はないと思いますが、このコードを実行する際は、全て自己責任でお願いします。私は責任を取りません。

また、自由にカスタマイズして使用してください。e-licenseのアップデート等により、使用できなくなる可能性は大いにあります。

## 作者

[@nekopath_dev](https://x.com/nekopath_dev)

---

# Name

e-license Auto School Reservation Vacancy Notification System

## Brief Description

Many driving schools use e-license for skill reservations and other tasks. 

I was eager to graduate quickly, so I found myself checking the reservation page every minute. 

But as a human, constantly checking was a hassle. So, I wrote a Python script that automatically notifies you when a reservation slot becomes available.

This is a semi-permanent code that checks every five minutes, so once you run it, you can leave it to do its job. 

However, please note that it may occasionally stop due to an error. 

Also, since I have already graduated, I cannot guarantee that this script still works properly. Please use it at your own risk.

***Demo***

Apologies! I couldn't prepare a demo. Please try running it to see how it works.

## Features

The script accesses the login page every five minutes, automatically inputs your student number and password into the login form, and logs in to check for availability. 

The presence of an available slot is determined by the existence of `<td class="status1">` in the reservation page's HTML. If a slot is found, a notification is sent via LINE Notify.

## Requirements

A PC capable of running VS Code efficiently. 

Other requirements are mentioned in the code comments. There might be some omissions, so please research on your own if necessary... Sorry about that.

## Usage

Paste the code into VS Code, save it as a Python file, and run it. After that, just leave it running. 

Note that this assumes Python is set up and ready to run. 

Since you'll be leaving it running for extended periods, you may want to use a spare PC that can remain powered on. 

If you don't have a spare PC, you can create a virtual PC using cloud services like Microsoft Azure and run it there. 

It may cost money, but I used a student credit to keep it running on Azure 24/7.

## Installation

I'm not very familiar with the installation process, so I can't explain it in detail... It's probably best to download the .py file and run it in VS Code.

## Other

This script is unofficial and was created by an individual. 

While I don't foresee any issues, please use it at your own risk. I take no responsibility for any consequences. 

Feel free to customize and use it as you like. Keep in mind that future updates to e-license may render this script unusable.

## Author

[@nekopath_dev](https://x.com/nekopath_dev)

※ This translation was done using a generative AI. Please understand that there might be errors.
