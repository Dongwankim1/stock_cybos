
import win32com.client
import win32com

# ### CpSvrNew7224  투자자(기관,외국인,개인 등등) 들의 일일 매매 동향데이터(매수,매도,순매수)를 요청하고 수신합니다
def subCpSvrNew7224(m_Market, m_NumOrMoney, m_FromDate, m_ToDate):
   ## 대신 api 세팅
    obj = win32com.client.Dispatch("cpsysdib.CpSvrNew7224")
    obj.SetInputValue(0, ord('1'))          # 1:일반, 2: 챠트
    obj.SetInputValue(1, ord(m_Market))     # A:시장전체 선택
    obj.SetInputValue(2, '0')          # 0:투자자전체
    obj.SetInputValue(3,  ord('1'))          # 1:기간
    obj.SetInputValue(4,  ord(m_NumOrMoney)) # 1:계약 2:금액
    obj.SetInputValue(5,  '0')         # 1:기간선택
    obj.SetInputValue(6, m_FromDate)  # 시작일자
    obj.SetInputValue(7, m_ToDate)    # 최종일자
    obj.SetInputValue(8,  ord('1'))        # 1:순매수
    obj.BlockRequest()

    numData=obj.GetHeaderValue(5)
    data=[]
    for ixRow in range(numData):
        tempdata=[]
        for ixCol in range(13):
            tempdata.append(obj.GetDataValue(ixCol, ixRow))
        data.append(tempdata)

    while obj.Continue:
        obj.BlockRequest()
        numData = obj.GetHeaderValue(5)
        for ixRow in range(numData):
            tempdata=[]
            for ixCol in range(13):
                tempdata.append(obj.GetDataValue(ixCol, ixRow))
            data.append(tempdata)


    return data