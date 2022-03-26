# ###################################################################################################
# ### file Name: practice_1_2_3_02.py 코스피, 코스닥, 선물, 옵션 일별 투자 주체별 매매 정보
# ###################################################################################################

from subDS import subCpSvrNew7224
from stockinfo import stockList,financialInfo
from stocksearch import nacvSearch
from pandas import DataFrame
from yahoofin import getSp500
import numpy as np
if __name__ == "__main__":
    '''
    m_InfoList = [0,4,20, 67,124,123, 70, 71, 74, 75, 76, 77, 78, 79, 80, 82, 86, 87, 88, 89, 90, 91, 92, 93, 95, 96, 98, 99, 100,
                  101, 102, 103, 104, 105, 106, 107, 109, 110, 111]
    customlist = stockList()

    data = financialInfo(customlist,m_InfoList)

    df = DataFrame(data, columns=['종목코드','현재가','총상장주식수', 'PER','CFPS','SPS', 'EPS', '자본금', '배당수익률', '부채비율', '유보율', '자기자본이익률', '매출액증가율', '경상이익증가율',
                                  '순이익증가율', 'VR', '매출액', '경상이익', '당기순이익', 'BPS', '영업이익증가율', '영업이익', '매출액영업이익률',
                                  '매출액경상이익률', '결산년월', '분기BPS', '분기영업이익증가율', '분기경상이익증가율', '분기순이익증가율', '분기매출액', '분기영업이익',
                                  '분기경상이익', '분기당기순이익', '분기매출액영업이익률', '분기매출액경상이익률', '분기ROE', '분기유보율', '분기부채비율',
                                  '최근분기년월','시가총액'])

    order = df.sort_values(by='시가총액',ascending=True)

    data=nacvSearch(order.values.tolist()[:200])

    df = DataFrame(data, columns=['종목코드', 'PBR','PER','PCR','PSR'])
    df['PBR_RANK'] = df['PBR'].rank(ascending=True)
    df['PER_RANK'] = df['PER'].rank(ascending=True)
    df['PCR_RANK'] = df['PCR'].rank(ascending=True)
    df['PSR_RANK'] = df['PSR'].rank(ascending=True)

    df.to_csv('subCpSvr7224.csv')
    '''

    getSp500()
