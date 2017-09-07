import requests
import json
import threading
import time

# 定义请求基本地址
base_url = "http://127.0.0.1:8000"
success = 0
fail = 0


# 查询线程
def get_guest_list_thread(start_user, end_user):
    for i in range(start_user, end_user):
        phone = 13511001095 + i  # 13511001100
        r = requests.get(base_url + '/api/get_guest_list/', params={'eid': 1, 'phone': phone})
        # print(r.status_code) # 200
        # print(r.content) # b'{"status": 200, "message": "success", "data": {"realname": "alen", "phone": "13511001100", "email": "alen@mail.com", "sign": false}}'
        # print(r.json()) # {'status': 200, 'message': 'success', 'data': {'realname': 'alen', 'phone': '13511001100', 'email': 'alen@mail.com', 'sign': False}}
        # print(type(r)) # <class 'requests.models.Response'> ,这个类型有json方法，不需要import json
        # print(r) # <Response [200]>
        # print(json.loads(r.content)) #需要import json，{'status': 200, 'message': 'success', 'data': {'realname': 'alen', 'phone': '13511001100', 'email': 'alen@mail.com', 'sign': False}}
        result = r.json()
        global success, fail
        try:
            if phone == '13511001100' or phone == '13511001101':
                assert result['status'] == 20
                success += 1
            else:
                assert result['status'] == 10022
                success += 1
        except AssertionError as e:
            print('get error:' + str(phone))
            fail += 1


# 5个线程，25个数据
# lists = {1:6, 6:11, 11:16, 16:21, 21:26} # 可以这样写数据，也可以通过下面生成
data = 25
n = 5
step = int(data / n)
lists = {}
for i in range(1, n + 1):
    lists[(i - 1) * step + 1] = i * step + 1
print(lists)

# 创建线程列表
threads = []
# 创建线程
for start_user, end_user in lists.items():
    t = threading.Thread(target=get_guest_list_thread, args=(start_user, end_user))  # args是一个元组
    threads.append(t)
if __name__ == '__main__':
    # 开始时间
    start_time = time.time()
    # 启动线程
    for i in range(len(lists)):
        threads[i].start()
    for i in range(len(lists)):
        threads[i].join()
    # 结束时间
    time.sleep(3)  # 为了更明显看出用例执行耗时，加上休眠
    end_time = time.time()
    print("开始时间:" + str(start_time) + '>>>>>' + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(start_time)))
    print("结束时间:" + str(end_time) + '>>>>>' + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(end_time)))
    print('总共耗时:' + str(end_time - start_time))
    print('总共耗时:%.2f' % (end_time - start_time))  # 保留两位小数
    print('测试通过用例数：{}， 测试失败用例数：{}， 测试通过率为：{}'.format(success, fail, str(success * 100 / (success + fail)) + '%'))