import yahoo_fin.stock_info as si


def getSp500():
    sp500_tickers = si.tickers_sp500()
    for key in sp500_tickers:
        #stock_info = si.get_income_statement("AAPL")
        stats = si.get_stats("AAPL")
        #발행주식수 가져오기
        strSharesOut = stats.loc[stats['Attribute'] == 'Shares Outstanding 5'].values[0][1]
        #마지막 문자열 가져오기(B,M 체크)
        check = strSharesOut[-1]
        print(check)
        arithmetic = 0
        if(check=='B'):
            # 발행주식수에서 B 문자열 제거
            strSharesOut = strSharesOut.replace('B', '')
            arithmetic = 1000000000
        else:
            # 발행주식수에서 B 문자열 제거
            strSharesOut = strSharesOut.replace('M', '')
            arithmetic = 1000000

        #문자열 발행주식수를 float 변환뒤 *100000000 하기
        sharesOut = float(strSharesOut)*arithmetic
        print(sharesOut)
        # for change '.' -> '-'  , 1. divide key list,val list


        break
