## 参考サイト
[【2020年】Instagramアカウントのフォロワー情報を自動で取得する方法（python）](https://tachitechi.com/%E3%80%902020%E5%B9%B4%E3%80%91instagram%E3%82%A2%E3%82%AB%E3%82%A6%E3%83%B3%E3%83%88%E3%81%AE%E3%83%95%E3%82%A9%E3%83%AD%E3%83%AF%E3%83%BC%E6%83%85%E5%A0%B1%E3%82%92%E8%87%AA%E5%8B%95%E3%81%A7/)\
[WSL2＋Ubuntu 20.04でGUIアプリを動かす](https://astherier.com/blog/2020/08/run-gui-apps-on-wsl2/)\
[WSL2+Ubuntu 20.04にChromeをインストール](https://astherier.com/blog/2020/08/install-google-chrome-on-wsl2/)

## 環境
Windows10 WSL2 Ubuntu20.04\
Python 3\
Google Chrome 95.0.4638.69\
[Chromedriver 95.0.4638.54](https://chromedriver.storage.googleapis.com/index.html) 

## 環境構築
### 前提
python3がインストール済み\
WSL2環境でGUIでChromeが起動できている

### コマンド
以下をターミナルで実行\
`pip install python-dotenv`\
`pip install beautifulsoup4`\
`pip install lxml`\
`pip install selenium`\
`pip install pandas`

### chromedriverのインストール
バージョンはローカル環境に合わせる\

ex)上記のバージョンでLinux版をDLする場合\
`wget https://chromedriver.storage.googleapis.com/95.0.4638.54/chromedriver_linux64.zip`

`sudo apt install unzip -y` #unzipのインストール\
`sudo mv chromedriver /usr/bin/chromedriver` #ファイルの移動

### envファイルの作成
instagram-scraperフォルダ直下に`.env`ファイルを作成する
```html:.env
   USERNAME="XXXXX"
   PASSWORD="xxxx"
```

### 実行
`python getInstagramFollowers.py`
