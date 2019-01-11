import six
import pandas as pd
import numpy as np
import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

# https://stackoverflow.com/questions/19726663/how-to-save-the-pandas-dataframe-series-data-as-a-figure
def render_mpl_table(data, col_width=3.0, row_height=0.625, font_size=12,
                     header_color='midnightblue', row_colors=['#f1f1f2', 'w'], edge_color='w',
                     bbox=[0, 0, 1, 1], header_columns=0,
                     ax=None, **kwargs):
    if ax is None:
        size = (np.array(data.shape[::-1]) + np.array([0, 1])) * np.array([col_width, row_height])
        fig, ax = plt.subplots(figsize=size, dpi=200)
        ax.axis('off')

    font_path = './asset/ipag.ttf'
    font_prop = FontProperties(fname=font_path)

    mpl_table = ax.table(cellText=data.values, bbox=bbox, colLabels=data.columns, **kwargs)

    mpl_table.auto_set_font_size(False)
    mpl_table.set_fontsize(font_size)

    for k, cell in six.iteritems(mpl_table._cells):
        cell.set_edgecolor(edge_color)
        cell.set_text_props(fontproperties=font_prop)
        if k[0] == 0 or k[1] < header_columns:
            cell.set_text_props(weight='bold', color='w')
            cell.set_facecolor(header_color)
        else:
            cell.set_facecolor(row_colors[k[0]%len(row_colors) ])
    return ax

def generate_body_measures_image(body_measures, today_ymd_date):
    member_rows = []
    muscleMass_rows = []
    hydration_rows = []
    boneMass_rows = []

    for body_measure in body_measures:
        member_rows.append("●")

        if body_measure["muscleMass"] is not None:
            muscleMass_rows.append(body_measure["muscleMass"] / 100)
        else:
            muscleMass_rows.append("None")

        if body_measure["hydration"] is not None:
            hydration_rows.append(body_measure["hydration"] / 100)
        else:
            hydration_rows.append("None")

        if body_measure["boneMass"] is not None:
            boneMass_rows.append(body_measure["boneMass"] / 100)
        else:
            boneMass_rows.append("None")

    df = pd.DataFrame()
    df['メンバー'] = member_rows
    df["筋肉率(%)"] = muscleMass_rows
    df["水分量(kg)"] = hydration_rows
    df["骨量(kg)"] = boneMass_rows

    ax = render_mpl_table(df, header_columns=0, col_width=2.0)
    fig = ax.get_figure()
    path_body_measures_image = "/tmp/body_measures_%s.png" % (today_ymd_date)
    fig.savefig(path_body_measures_image)
    plt.close('all')

    return path_body_measures_image

if __name__ == "__main__":
    body_measures = []

    today_ymd_date = "1998-09-04"

    generate_body_measures_image(body_measures, today_ymd_date)