# for-fun
遊びでつくりました

仕様上 Discord.py v2.0が必要 (required python 3.8 or above)

` pip install git+https://github.com/Rapptz/discord.py `

Amazon Linux(EC2)上で動かした際の覚書

1. Pythonのバージョンを上げる、もしくは3.8以上をインストール
>red hat系列なのでyum install python38とかで行けたはずだけど、エラーが出た覚えが....

2. Windows版にモジュールを入れる場合と違って以下のコードで2.0aをインストール可能

    git clone https://github.com/Rapptz/discord.py
    cd discord.py
    python3 -m pip install -U .[voice]

以上！
