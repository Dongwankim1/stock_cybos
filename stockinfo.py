import win32com.client




def stockList():
    objCpCybos = win32com.client.Dispatch("CpUtil.CpCybos")
    bConnect = objCpCybos.IsConnect
    if(bConnect==0):
        raise Exception("PLUS가 정상적으로 연결되지 않음.")

    objCpCodeMgr = win32com.client.Dispatch("CpUtil.CpCodeMgr")
    kospiList = objCpCodeMgr.GetStockListByMarket(1) #코스피
    kodaq = objCpCodeMgr.GetStockListByMarket(2) #코스닥

    print("거래소 종목코드", len(kospiList))
    for i, code in enumerate(kospiList):
        secondCode = objCpCodeMgr.GetStockSectionKind(code)
        name = objCpCodeMgr.CodeToName(code)
        stdPrice = objCpCodeMgr.GetStockStdPrice(code)
        print(i, code, secondCode, stdPrice, name)

    print("코스닥 종목코드", len(kodaq))
    for i, code in enumerate(kodaq):
        secondCode = objCpCodeMgr.GetStockSectionKind(code)
        name = objCpCodeMgr.CodeToName(code)
        stdPrice = objCpCodeMgr.GetStockStdPrice(code)
        print(i, code, secondCode, stdPrice, name)