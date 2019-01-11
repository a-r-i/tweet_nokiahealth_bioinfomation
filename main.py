from datetime import date
from request_bio_infomation import request_bio_infomation
from sleep_series_formating import sleep_series_formating
from generate_sleep_series_image import generate_sleep_series_image, get_concat_v
from generate_body_measures_image import generate_body_measures_image
from tweet import tweet_with_image

members = []
today_ymd_date = str(date.today().isoformat())

path_sleep_series_images = []
body_measures = []

for member in members:
    bio_infomation = request_bio_infomation(member)

    try:
        formatted_sleep_series = sleep_series_formating(bio_infomation["sleep"])
        path_sleep_series_image = generate_sleep_series_image(formatted_sleep_series, member, today_ymd_date)
        path_sleep_series_images.append(path_sleep_series_image)
    except IndexError as e:
        print("type:{0}".format(type(e)))
        print("args:{0}".format(e.args))

    try:
        last_body_measure = sorted(bio_infomation["body"], key=lambda x: x["timestamp"], reverse=True)[0]
        body_measures.append(last_body_measure)
    except IndexError as e:
        print("type:{0}".format(type(e)))
        print("args:{0}".format(e.args))

path_tweet_images = []

try:
    path_concat_sleep_series_image = "/tmp/sleep_series_%s.jpg" % today_ymd_date
    get_concat_v(path_sleep_series_images).save(path_concat_sleep_series_image)
    path_tweet_images.append(path_concat_sleep_series_image)
except IndexError as e:
    print("type:{0}".format(type(e)))
    print("args:{0}".format(e.args))

try:
    path_body_measures_image = generate_body_measures_image(body_measures, today_ymd_date)
    path_tweet_images.append(path_body_measures_image)
except IndexError as e:
    print("type:{0}".format(type(e)))
    print("args:{0}".format(e.args))

tweet_text = "第13回定期公演「Tokyo in Bio」\n\n今日の生体情報です！\n\nTokyo in Bioの概要と楽しみ方のヒント👇\nhttps://twitter.com/tokyo_tsukurou/status/1022091094467567616" \
             "\n\n#Tokyo_in_Bio\n#今日の生体情報\n#NokiaSleep"

if path_tweet_images != []:
    path_tweet_images.append("./asset/Tokyo_in_Bio.001.jpeg")
    path_tweet_images.append("./asset/Tokyo_in_Bio.002.jpeg")
    tweet_with_image(tweet_text, path_tweet_images)
else:
    print("path_tweet_images is empty")