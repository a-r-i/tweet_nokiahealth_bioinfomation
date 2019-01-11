# from config_local import TWITTER_CONSUMER_KEY, TWITTER_CONSUMER_SECRET, TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_TOKEN_SECRET
# from config_starging import TWITTER_CONSUMER_KEY, TWITTER_CONSUMER_SECRET, TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_TOKEN_SECRET
from config_production import TWITTER_CONSUMER_KEY, TWITTER_CONSUMER_SECRET, TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_TOKEN_SECRET
from requests_oauthlib import OAuth1Session
import json

oauth_sess = OAuth1Session(
                TWITTER_CONSUMER_KEY,
                TWITTER_CONSUMER_SECRET,
                TWITTER_ACCESS_TOKEN,
                TWITTER_ACCESS_TOKEN_SECRET
                )

# https://qiita.com/sugurunatsuno/items/8899dacbabfab43f6ee8
def tweet_with_image(tweet_text, path_list_images):
    url_media = "https://upload.twitter.com/1.1/media/upload.json"
    url_text = "https://api.twitter.com/1.1/statuses/update.json"

    media_ids = ""

    # 画像の枚数分ループ
    for path in path_list_images:
        files = {"media" : open(path, 'rb')}
        req_media = oauth_sess.post(url_media, files = files)

        # レスポンスを確認
        if req_media.status_code != 200:
            print ("画像アップデート失敗: {}".format(req_media.text))
            return -1

        media_id = json.loads(req_media.text)['media_id']
        media_id_string = json.loads(req_media.text)['media_id_string']
        print ("Media ID: {} ".format(media_id))
        # メディアIDの文字列をカンマ","で結合
        if media_ids == "":
            media_ids += media_id_string
        else:
            media_ids = media_ids + "," + media_id_string

    print ("media_ids: ", media_ids)
    params = {'status': tweet_text, "media_ids": [media_ids]}
    req_text = oauth_sess.post(url_text, params = params)

    # 再びレスポンスを確認
    if req_text.status_code != 200:
        print ("テキストアップデート失敗: {}".format(req_text.text))
        return -1

    print ("tweet uploaded\n")
    return 1