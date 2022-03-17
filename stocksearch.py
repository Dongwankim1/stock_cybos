from bs4 import BeautifulSoup
import urllib.request

def nacvSearch(stock_code_list):
    data = []
    for code in stock_code_list:
         url="http://comp.fnguide.com/SVO2/ASP/SVD_Invest.asp?pGB=1&gicode=" + code[0] + "&cID=&MenuYn=Y&ReportGB=&NewMenuID=105&stkGb=701"
         f = urllib.request.urlopen(url).read()
         soup = BeautifulSoup(f, 'html.parser')
         cells = soup.find('div', {'id': "corp_group2"}).find_all("dd")
         #pbr 구하기
         pbr = cells[7].string
         per = code[3]
         pcr = float(code[4])/float(code[1])
         psr = float(code[5]) / float(code[1])
         if(float(pbr)<=0.2):
             continue
         data.append([code[0],pbr,per,pcr,psr])

    return data