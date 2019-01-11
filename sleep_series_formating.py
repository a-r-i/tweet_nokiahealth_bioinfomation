# データの整形
def sleep_series_formating(sleep_series):
    sorted_sleep_series = sorted(sleep_series, key=lambda x: x["startdate"])

    left_array = []
    height_array = []
    count = 0

    sleep_level_conversion_table = {
                                    0: 4,
                                    1: 2,
                                    2: 1,
                                    3: 3
                                    }

    before_enddate = sorted_sleep_series[0]["startdate"]

    for data in sorted_sleep_series:
        startdate = data["startdate"]
        enddate = data["enddate"]

        # seriesとseriesの間のギャップを求める
        gap = startdate - before_enddate

        if gap >= 0: # seriesとseriesが被っていない時だけ、処理に進む
            if gap > 0:# seriesとseriesの間にギャップがある場合
                gap_minutes = int(gap / 60)

                for i in range(gap_minutes): #空の棒グラフでギャップを埋める
                    left_array.append(count)
                    height_array.append(0)
                    count += 1

            series_length = enddate - startdate
            series_minutes = int(series_length / 60)

            for i in range(series_minutes):
                left_array.append(count)
                height_array.append(sleep_level_conversion_table[data["sleep_level"]])
                count+=1

            before_enddate = enddate

    # もっとも時間が早いstartdateと時間が遅いenddateの差分(ベッドの中にいた時間)を取る
    in_to_bed_date = sorted_sleep_series[0]["startdate"]
    out_of_bed_date = sorted_sleep_series[-1]["enddate"]
    sum_in_bed_time = out_of_bed_date - in_to_bed_date
    sum_in_bed_time_minutes = int(sum_in_bed_time / 60)

    result = {
              "left_array": left_array,
              "height_array": height_array,
                "in_to_bed_date": in_to_bed_date,
                "out_of_bed_date": out_of_bed_date
              }
    return result