from  alipay_deal_detect import*
from threading import Thread

def test_detect(times):
    bad_count = 0
    for i in range(times):
        rst = detect("id1786406222")
        if rst[0]== -1:
            bad_count += 1
        print("detect_status: {}\tresult:{}\n".format(rst[0],rst[1]))
        time.sleep(60)

if __name__ == '__main__':
    for j in range(1):
        trd = Thread(target=test_detect,args=[100])
        trd.start()