


def scrapper(company_name):
    #company_name = input("Enter the company code")

    # import libraries 

    import requests 
    from bs4 import BeautifulSoup

    url = "https://www.cnbc.com/quotes/"+ company_name

    # have to defind the user agent as below otherwise you will ban from the wabsite because website might recognize you as robort
    headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.66 Safari/537.36"}

    page = requests.get(url, headers = headers)
    soup = BeautifulSoup(page.content , "html.parser")
    soup_1 = BeautifulSoup(soup.prettify(),"html.parser")
    body = soup.find("body")

    find = soup.find_all("div", class_ = "QuoteStrip-lastPriceStripContainer")
    for line in find:
        stake_price = line.find("span").string

    return print(stake_price)


company_name = input("Enter The company Name")
scrapper(company_name)
