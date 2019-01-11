# description

アイドルの生体情報をNokia Sleep&Body+で計測し毎日ツイートする  
https://qiita.com/a-r-i/items/288496f47f279445a35b

上記企画で使用したプログラム

1. Nokia Sleep&Body+で計測した生体情報を、自前のAPIから取得(reqest_bio_infomation.py)
1. 生体情報をもとに図を生成(generate_body_measures_image.py, generate_sleep_series_image.py)
1. 2で生成した図を添付してTwitterにツイート(tweet.py)

本プログラムで使用する生体情報をNokia Health APIから取得するプログラムはこちら  
https://github.com/a-r-i/record_nokiahealth_bioinfomation

## 引用したソースコード
このプログラムは以下のソースコードを引用しています。

https://stackoverflow.com/questions/19726663/how-to-save-the-pandas-dataframe-series-data-as-a-figure
https://note.nkmk.me/python-pillow-concat-images/
https://github.com/nkmk/python-snippets/blob/4e232ef06628025ef6d3c4ed7775f5f4e25ebe19/notebook/pillow_concat.py
https://qiita.com/sugurunatsuno/items/8899dacbabfab43f6ee8