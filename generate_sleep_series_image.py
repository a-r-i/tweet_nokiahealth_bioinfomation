import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime, timezone, timedelta
from PIL import Image
from matplotlib.font_manager import FontProperties

JST = timezone(timedelta(hours=+9), 'JST')

height_to_color_conversion_table = {
    0: "white",  # no data
    1: "midnightblue",  # deep sleep
    2: "royalblue",  # light sleep
    3: "skyblue",  # REM sleep
    4: "gainsboro"  # awake
}

def generate_sleep_series_image(formatted_sleep_series, member, today_ymd_date):
    plt.figure(figsize=(8, 2), dpi=200)

    for i in formatted_sleep_series["left_array"]:
        height = formatted_sleep_series["height_array"][i]

        x = [i]
        y = [height]

        plt.bar(x,
                y,
                color=height_to_color_conversion_table[height],
                width=1,
                label='Data',
                align="center")

    font_path = './asset/ipag.ttf'
    font_prop = FontProperties(fname=font_path, size=8)
    plt.title("睡眠情報 ●", fontproperties=font_prop)
    plt.xlabel("時間", fontproperties=font_prop)
    plt.ylabel("眠りの深さ", fontproperties=font_prop, rotation=0)

    in_to_bed_mdhms_date_JST = str(datetime.fromtimestamp(formatted_sleep_series["in_to_bed_date"], JST))[5:19]
    out_of_bed_mdhms_date_JST = str(datetime.fromtimestamp(formatted_sleep_series["out_of_bed_date"], JST))[5:19]

    plt.xticks([0, len(formatted_sleep_series["height_array"])], [in_to_bed_mdhms_date_JST, out_of_bed_mdhms_date_JST], fontproperties=font_prop)
    plt.yticks(np.arange(5), ('', '深い', '浅い', "とても浅い", '覚醒'), fontproperties=font_prop)

    path_sleep_series_image = "/tmp/sleep_series_%s_dot%i.png" % (today_ymd_date, member)
    plt.savefig(path_sleep_series_image)
    plt.close('all')

    return path_sleep_series_image

#https://note.nkmk.me/python-pillow-concat-images/
def get_concat_v(path_sleep_series_images):
    im0 = Image.open(path_sleep_series_images[0])
    dst = Image.new('RGB', (im0.width, im0.height * len(path_sleep_series_images)))
    count = 0
    for path_sleep_series_image in path_sleep_series_images:
        im = Image.open(path_sleep_series_image)
        dst.paste(im, (0, im.height * count))
        count+=1
    return dst

if __name__ == "__main__":
    sleep_series = {}
    today_ymd_date = "2018-07-02"
    member = 0
    generate_sleep_series_image(sleep_series, member, today_ymd_date)