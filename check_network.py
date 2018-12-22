import requests
import time
import base64


class NetworkCheck:


    def __init__(self, username, password):
        source = """
            Accept: */*
            Accept-Encoding: gzip, deflate
            Accept-Language: en-US,en;q=0.9
            Connection: keep-alive
            Content-Length: 100
            Content-Type: application/x-www-form-urlencoded
            Cookie: login=bQ0pOyR6IXU7PJaQQqRAcBPxGAvxAcrsyjNPfUWDLH%252FPslDP%252B%252Fgbtx81TRl9G%252BYoZopChqLee6UHBJagAF%252FzQQMH0vOEVd3mg3dV8HCSfpffYG7ndn29Cmy90FOCT%252F8n9nJU4dHNehXxNdPydqSDfNt%252FVgAuxRVPtHoSA2T506JN6CX7VTgrp1k%253D; login=bQ0pOyR6IXU7PJaQQqRAcBPxGAvxAcrsyjNPfUWDLH%252FPslDP%252B%252Fgbtx81TRl9G%252BYoZopChqLee6UHBJagAF%252FzQQMH0vOEVd3mg3dV8HCSfpffYG7ndn29Cmy90FOCT%252F8n9nJU4dHNehXxNdPydqSDfNt%252FVgAuxRVPtHoSA2T506JN6CX7VTgrp1k%253D
            Host: aaa.ncu.edu.cn:802
            Origin: http://aaa.ncu.edu.cn:802
            Referer: http://aaa.ncu.edu.cn:802/srun_portal_pc.php?ac_id=1&
            User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36
            X-Requested-With: XMLHttpRequest
            """
        self.username = username
        self.password = password


    @staticmethod
    def source_to_dict(s):
        s = s.strip().split('\n')
        s = {x.split(':')[0].strip() : x.split(':')[1].strip() for x in s}
        return s

    @staticmethod
    def connect_to_network(username, password):
        while True:
            print("trying to connect network....")
            data = "action=login&username=%s&password={B}%s&ac_id=1&user_ip=&nas_ip=&user_mac=&save_me=1&ajax=1" % (username, base64.b64encode(password))
            login_res = requests.post(url='http://aaa.ncu.edu.cn:802/include/auth_action.php', data=data, headers=source_to_dict(self.source))
            print(login_res.status_code, login_res.text)
            if 'ok' in login_res.text:
                break
            time.sleep(1)
        return True


    def start_check(self):
        while True:
            try:
                res = requests.get("https://www.baidu.com/", timeout=3)
            except:
                print("[warning]network downline!")
                connect_to_network(self.username, self.password)
            print("[OK]Network works nice!")
            time.sleep(3)

    # print(source_to_dict(source))

check = NetworkCheck("your_username", "your_password")
check.start_check()
