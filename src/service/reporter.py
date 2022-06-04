from datetime import datetime
from src.service.util import diff_percentage, paint_diff


def render_console(report):
    for item in report:
        asset, last_item, x_df, y_df = item

        date = datetime.fromtimestamp(last_item["time_open"])

        # Measure
        last_real = x_df['open'].tail(1).values[0]

        # 3 intervals
        # predict what to be:
        # 15min (5 x 3)
        # 45min (15 x 3)
        tail = y_df['open'].tail(4).values
        last = tail[0]
        prediction = tail[3]

        diff = diff_percentage(v2=prediction, v1=last)

        if diff > 0.6:
            print(f''
                  f'{asset} \t |'
                  f'{paint_diff(diff)} \t |'
                  f'{last_item["trades"]} \t |'
                  f'{last_real:.4f} - {last:.4f} {tail[1]:.4f} {tail[2]:.4f} {tail[3]:.4f} \t | '
                  f'{date.strftime("%Y %m %d %H:%M:%S")} - '
                  f'https://www.binance.com/en/trade/{asset}_USDT')

    print(datetime.now().strftime('%Y %m %d %H:%M:%S'))
