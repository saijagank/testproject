from datetime import date, datetime
from jugaad_data.nse import stock_df
import pandas as pd


def main_daily1(fromdate, todate, path, symbollist):
    filename2 = path + 'EQUITY_' + str(date.today()) + ".csv"
    df_final = []

    for i in range(0, len(symbollist)):
        #df = stock_df(symbol=symbollist[i], from_date=date(2024, 8, 29),
        #              to_date=date(2024, 8, 30), series="EQ")

        df = stock_df(symbol=symbollist[i], from_date=datetime.strptime(fromdate, '%Y%m%d').date(),
                      to_date=datetime.strptime(todate, '%Y%m%d').date(), series="EQ")

        df_final.append(df)

    final_df = pd.concat(df_final)
    final_df.to_csv(filename2, encoding='utf-8', header='true', index=False)
