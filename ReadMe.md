# このソフトウェアについて

認証クラス配列を生成するクラスを作った。

* GitHubAPIの認証用requestsライブラリ引数生成を抽象化した
    * 認証なし, Basic, TwoFactor, OAuth
    * DBからTokenを取得する
    * APIでTokenを生成してDBに登録する（未実装）
* APIごとに認証方法を使い分ける
    * `RequestParameter.py`
* 認証クラス配列を生成する
    * `AuthenticationsCreator.py`
        * DBとユーザ名から以下の認証クラス配列を生成する
        * OAuth, TwoFactor/Basicの優先順に作成できるものがあれば作る

# 開発環境

* Linux Mint 17.3 MATE 32bit
* [Python 3.4.3](https://www.python.org/downloads/release/python-343/)
* [SQLite](https://www.sqlite.org/) 3.8.2

## WebService

* [GitHub](https://github.com/)
    * [アカウント](https://github.com/join?source=header-home)
    * [AccessToken](https://github.com/settings/tokens)
    * [Two-Factor認証](https://github.com/settings/two_factor_authentication/intro)
    * [API v3](https://developer.github.com/v3/)

# ライセンス

このソフトウェアはCC0ライセンスである。

[![CC0](http://i.creativecommons.org/p/zero/1.0/88x31.png "CC0")](http://creativecommons.org/publicdomain/zero/1.0/deed.ja)

Library|License|Copyright
-------|-------|---------
[requests](http://requests-docs-ja.readthedocs.io/en/latest/)|[Apache-2.0](https://opensource.org/licenses/Apache-2.0)|[Copyright 2012 Kenneth Reitz](http://requests-docs-ja.readthedocs.io/en/latest/user/intro/#requests)
[dataset](https://dataset.readthedocs.io/en/latest/)|[MIT](https://opensource.org/licenses/MIT)|[Copyright (c) 2013, Open Knowledge Foundation, Friedrich Lindenberg, Gregor Aisch](https://github.com/pudo/dataset/blob/master/LICENSE.txt)
[pytz](https://github.com/newvem/pytz)|[MIT](https://opensource.org/licenses/MIT)|[Copyright (c) 2003-2005 Stuart Bishop <stuart@stuartbishop.net>](https://github.com/newvem/pytz/blob/master/LICENSE.txt)
[pyotp](https://github.com/pyotp/pyotp)|[MIT](https://opensource.org/licenses/MIT)|[Copyright (C) 2011-2016 Mark Percival <m@mdp.im>,
Nathan Reynolds <email@nreynolds.co.uk>, and PyOTP contributors](https://github.com/pyotp/pyotp/blob/master/LICENSE)

