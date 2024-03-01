from selenium import webdriver
import sys
import time
from selenium.webdriver.common.by import By

#selenium版本：4.1.0
#chrome版本：122.0.6261.95

#货币代号对照表
currency_dict ={"HK":"港币","GBP":"英镑","USD":"美元","CHF":"瑞士法郎","DEM":"德国马克","FRF":"法国法郎","SGD":"新加坡元",
                "SEK":"瑞典克朗","DKK":"丹麦克朗","NOK":"挪威克朗","JPY":"日元","CAD":"加拿大元","AUD":"澳大利亚元","EUR":"欧元","MOP":"澳门元",
                "PHP":"菲律宾比索","THP":"泰国铢","NZD":"新西兰元","SUR":"卢布","ESP":"西班牙比塞塔",
                "ITL":"意大利里拉","NLG":"荷兰盾","BEF":"比利时法郎","FIM":"芬兰马克","INR":"印度卢比","IDR":"印尼卢比","BRC":"巴西里亚尔",
                "ZAR":"南非兰特","SAR":"沙特里亚尔","TRL":"土耳其里拉"}
def get_exchange_rate(date, currency_code):
    # 设置WebDriver路径，确保替换为你本地的路径
    webdriver_path = './chromedriver.exe'
    driver = webdriver.Chrome(webdriver_path)

    # 打开中国银行外汇牌价网站
    driver.get("https://www.boc.cn/sourcedb/whpj/")

    # 等待页面加载
    time.sleep(2)

    #输入起始时间
    start_input = driver.find_element(By.NAME,"erectDate");
    start_input.send_keys(date)

    #输入结束时间
    end_input = driver.find_element(By.NAME, "nothing");
    end_input.send_keys(date)

    #选择货币
    coin_select = driver.find_element(By.ID, "pjname");
    coin_select.send_keys(currency_code)

    #点击查询按钮
    query_btn = driver.find_element(By.CSS_SELECTOR, '[onclick="executeSearch()"]')
    query_btn.click()
    time.sleep(2)

    #获取价格
    try:
        tr = driver.find_element(By.XPATH,"/html/body/div/div[4]/table/tbody/tr[2]")
        td_list = tr.find_elements(By.TAG_NAME, 'td')
        exchange_rate = td_list[3].text
        print(exchange_rate)
        fo = open("result.txt", "a")
        fo.write(f"日期: {date}, 货币代号: {currency_code}, 现汇卖出价: {exchange_rate}\n")
    except:
        print("对不起，搜索出错，请重试！请注意您的检索词拼写!")


    # 关闭浏览器
    driver.quit()

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python3 yourcode.py <日期> <货币代号>")
    else:
        date = sys.argv[1]
        try:
            currency_code = currency_dict[sys.argv[2]]
            get_exchange_rate(date, currency_code)
        except KeyError:
            print("输入的货币符号有误")

