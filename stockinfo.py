import win32com.client
import win32com


def stockList():
    objCpCybos = win32com.client.Dispatch("CpUtil.CpCybos")
    bConnect = objCpCybos.IsConnect
    if(bConnect==0):
        raise Exception("PLUS가 정상적으로 연결되지 않음.")

    objCpCodeMgr = win32com.client.Dispatch("CpUtil.CpCodeMgr")
    kospiList = objCpCodeMgr.GetStockListByMarket(1) #코스피
    kodaq = objCpCodeMgr.GetStockListByMarket(2) #코스닥
    stocklist = []
    print("거래소 종목코드", len(kospiList))
    #for i, code in enumerate(kospiList):
    #    secondCode = objCpCodeMgr.GetStockSectionKind(code)
    #    name = objCpCodeMgr.CodeToName(code)
    #    stdPrice = objCpCodeMgr.GetStockStdPrice(code)
    #    print(i, code, secondCode, stdPrice, name)

    """
    value = object.GetStockCapital ( code )
    code 에해당하는자본금규모구분반환한다.

    code : 주식코드
    반환값 : 자본금규모구분
    [helpstring("대")]   CPC_CAPITAL_LARGE  = 1,
    [helpstring("중")]   CPC_CAPITAL_MIDDLE  = 2,
    [helpstring("소")]   CPC_CAPITAL_SMALL  = 3
    """

    print("코스닥 종목코드", len(kodaq))
    for i, code in enumerate(kodaq):
        if(objCpCodeMgr.GetStockSupervisionKind(code)!=0):
            continue
        if(objCpCodeMgr.GetStockStatusKind(code)!=0):
            continue
        if(objCpCodeMgr.GetOverHeating(code)!=0):
            continue
        if(objCpCodeMgr.GetStockCapital(code)!=3):
            continue
        if(objCpCodeMgr.IsStockIoi(code)):
            continue
        if(objCpCodeMgr.IsSPAC(code)):
            continue
        stocklist.append(code)
        #stocklist.append(objCpCodeMgr.GetStockSectionKind(code))
        name = objCpCodeMgr.CodeToName(code)
        stdPrice = objCpCodeMgr.GetStockStdPrice(code)
    print(len(stocklist))
    return stocklist

"""
stock_code_list : 주식 코드 리스트
stock_info_list : 가져올 재무정보 list

"""
def financialInfo(stock_code_list,stock_info_list):
    obj = win32com.client.Dispatch("cpsysdib.MarketEye")

    data = []

    for i in range(round(len(stock_code_list)/200)):
        indexNum = (200*i)+200
        if(indexNum>len(stock_code_list)):
            indexNum = len(stock_code_list)

        obj.SetInputValue(0,stock_info_list)
        obj.SetInputValue(1,stock_code_list[i*200:indexNum])
        obj.BlockRequest()
        numField = obj.GetHeaderValue(0)
        numData = obj.getHeaderValue(2)


        for ixRow in range(numData):
            tempdata=[]
            for ixCol in range(numField):
                tempdata.append(obj.GetDataValue(ixCol,ixRow))

            if(float(tempdata[3])<=0.01 or float(tempdata[3])>8):
                continue

            sichong = tempdata[1]*tempdata[2]

            tempdata.append(sichong)
            data.append(tempdata)

    return data