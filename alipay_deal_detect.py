# 使用selenium 操纵chrome游览器完美模拟人为操作从而登录支付宝

# 导入相应模板
from bs4 import BeautifulSoup
from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import ActionChains

# ALIPAY_LOGIN_URL = "http://service.spiritsoft.cn/ua.html"
ALIPAY_DEAL_RECORD_URL = "https://lab.alipay.com/consume/record/items.htm" # 可以考虑换查看余额的网址
ALIPAY_LOGIN_URL = "https://lab.alipay.com/consume/record/items.htm"
ALIPAY_USER_NAME = "13879478299" # 可以考虑用多个支付宝账号
ALIPAY_USER_PWD = "Tchyou636."
SEND_KEYS_INTERVAL = 0.04 # 最低0.04


def send_keys_slowly(element, value: iter, interval):
    for c in value:
        element.send_keys(c)
        time.sleep(interval)

def start_detect(deal_qr_id: str):
    # chrome option
    opt = Options()
    # opt.add_argument("--headless")  # 浏览器不提供可视化页面. linux下如果系统不支持可视化不加这条会启动失败
    # opt.add_argument('--user-agent=iphone') # 伪装身份
    opt.add_argument('--disable-gpu')  # 谷歌文档提到需要加上这个属性来规避bug
    opt.add_argument('blink-settings=imagesEnabled=false')  # 不加载图片, 提升速度


    driver = webdriver.Chrome(options=opt)  # 实例化driver对象
    driver.get(ALIPAY_LOGIN_URL)  # 访问login页面
    # time.sleep(1)
    pwd_login = driver.find_element_by_css_selector("li[data-status='show_login']")  # 点击账号密码登录
    # ActionChains(driver).move_to_element(pwd_login)  # 移动鼠标到账号密码登录
    pwd_login.click()
    uname = driver.find_element_by_id("J-input-user")  # 获取username input 对象
    # time.sleep(1)
    send_keys_slowly(uname, ALIPAY_USER_NAME, SEND_KEYS_INTERVAL)  # 间隔时间填入username值
    password = driver.find_element_by_id("password_rsainput")  # 获取password 对象
    # time.sleep(1)
    send_keys_slowly(password, ALIPAY_USER_PWD, SEND_KEYS_INTERVAL)  # 间隔时间填入密码
    # time.sleep(50)
    driver.find_element_by_id("J-login-btn").click()  # 获取登陆按键并登陆

    # driver.get(ALIPAY_DEAL_RECORD_URL) # 访问deal_record_page #
    html = driver.page_source #获取账单页面html
    # time.sleep(50)
    driver.close()  # 关闭游览器回收资源


    # 分析网页数据
    soup = BeautifulSoup(html, "lxml") # 将账单页面html导入到soup中
    soup = soup.select("tr.record-list")
    # now_time = int(time.strftime("%Y%m%d%H%M%S", time.localtime(time.time())))
    if len(soup) == 0:
        return -1,"需扫描二维码查看账单"
    for case in soup[0:10]:
        datetime = time.mktime(time.strptime(case.select("td.time")[0].text.strip(),"%Y-%m-%d %H:%M:%S"))
        info = case.select("li[class='name emoji-li']")[0]
        [s.extract() for s in info("span")]
        # name 和 deal_qr_id 相同 且 时间间隔在三分钟内 则交易成功   同一个QR_Code 只能在3分钟内使用一次  deal_qr_id这个弄复杂一点以免相同
        if info.text.strip() == "支付-"+ deal_qr_id and (time.time() - datetime) < 180:
            return True,0

    return False,0

def detect(deal_qr_id: str):
    """
    返回一个包含两个元素的元组,如果元组第一个元素是-1 则 detect程序发生错误 第二个元素是错误原因
    若第一各元素不是-1 那么就是一个boolean 类型 表示detect的结果
    :param deal_qr_id: 二维码id
    :return: 返回一个包含两个元素的元组
    """
    try:
        return start_detect(deal_qr_id)
    except (TypeError,Exception) as e:
        return -1,str(e)

# 速度加快


# 4. 代码思路改变
#      1) 登录部分模拟游览器 获取账单用普通爬虫
#      2) 使用一个脚本不停的爬取那个账单网站 以此保存cookie 有任务便提示其查询 这个思路是否可以取决于alipaycookie的模式
#      3) 使用纯爬虫代码访问 此步较难但速度最快
#      4) 多线程 排除

# 最优方案一
# 登录游览器每过x秒获取一次账单 如果有新数据则post到网站上
# 如果cookie失效则重新登录然后继续执行

# 最优方案二
# 登录游览器每x秒检查共享数据里是否有任务，如果有则立即检查账单和任务比对 并且通过某种方式传达
# 如果没有则休眠y秒之后再获取账单(仅获取账单无需比对以此来维持登录状态)，一旦cookie失效则重新登录
if __name__ == '__main__':
    stime = time.time()
    rst = detect("id1786406223")
    if rst[0] == -1:
        print("Error occur when detection execute error_reason:",rst[1])
    else:
        print("the detection result:",rst[0])
    print("消耗时间: %.2f"%(time.time()-stime))


