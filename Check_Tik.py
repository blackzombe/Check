from flask import Flask
from requests import get , post

app = Flask(__name__)



@app.route("/")
def start ():
    return {"Hello":"welcome in my API","by":"Glitch5" , "CH_TELE" : "@G5python3"}




@app.route('/email=<email>')
def all (email):
    email2 = str(email).split("@")[0]
    check = str(email).split("@")[1]
    yes = {"DEV":{"user_tele" : "@Glich5" , "CH" : "@G5python3"},"result":{"email": str(email) , "check": "available"}}
    no = {"DEV":{"user_tele" : "@Glich5" , "CH" : "@G5python3"},"result":{"email": str(email) , "check": "unavailable"}}
    
    
    def tiktok(email):
        try:
            url = "https://api2-t2.musical.ly/aweme/v1/passport/find-password-via-email/?version_code=7.6.0&language=ar&app_name=musical_ly&vid=4JUdGzvrMFDWrUUwY3toJATSeNwjn54LkCnKBPRzDuhzi5vSepHfUckJNxRL2gjkNrSqtCoRUrEDAgRwsQvVCjZbRyFTLRNyDmT1a1boZV6999590732555060741&tz_offset=10800&account_region=&sys_region=SA&aid=1233&screen_width=1242&openudid=a0594f8115e0a1a51e1a31490aeef9afc2409ff4&os_api=18&ac=WIFI&os_version=12.5.4&app_language=ar&tz_name=Asia/Riyadh&device_platform=iphone&build_number=76001&iid=7021194671750481669&device_type=iPhone7,1&idfa=20DB6089-D1C6-4JUdGzvrMFDWrUUwY3toJATSeNwjn54LkCnKBPRzDuhzi5vSepHfUckJNxRL2gjkNrSqtCoRUrEDAgRwsQvVCjZbRyFTLRNyDmT1a1boZV16347494182"
            header = {
                'Host': 'api2-t2.musical.ly',
                'Cookie': 'store-country-code=sa; store-idc=alisg; install_id=7021194671750481669; odin_tt=7b67a77e780e497b1c89d483072f567580c860fe622a9ad519c8af998a287f424ed5f97297928981fa70ca6e8cb2648ebc46af23c9c9588a540567c77f877d307588080b16d8b92d3c3f875da9cd2291; ttreq=1$ee9fd401f276e956ba82d3ffd7392ffa6829472d',
                'Accept': '*/*',
                'Content-Type': 'application/x-www-form-urlencoded',
                'User-Agent': 'Musically/7.6.0 (iPhone; iOS 12.5.4; Scale/3.00)',
                'Accept-Language': 'ar-SA;q=1',
                'Content-Length': '25',
                'Connection': 'close'
            }

            req = post(url, headers=header, data={"email": str(email)}).text
            if 'Bind device by email failed' in req: return False
            else:return True
        except:return False



    
    if check == "yahoo.com":
        
        try:
            headers = {
                'Cookie': 'DSS=ts=1634040223&cnt=0&sdts=1634153022&sdtp=mcafee; F=d=0szPO.09vA_spNXCYZvk.mEelkwHPEibfA--; PH=l=en-JO; Y=v=1&n=0scmfk29v1jsr&l=ap3bt2as5sphig52evohvlsnbcjbb77d66pbfbt1/o&p=n33vvjo00000000&r=19k&intl=xa; OTH=v=1&d=eyJraWQiOiIwMTY0MGY5MDNhMjRlMWMxZjA5N2ViZGEyZDA5YjE5NmM5ZGUzZWQ5IiwiYWxnIjoiUlMyNTYifQ.eyJjdSI6eyJndWlkIjoiUUFWTEhCVE9YQUVLSEk2UUlWWExFTUJZRkUiLCJwZXJzaXN0ZW50Ijp0cnVlLCJzaWQiOiJyR0hrdlZIS0dvdXMifX0.f7NQFuieV40E_fGidanHZLEC1wSSNQZA618MNHugMXzf50Gu16ZZX6hIhYncmeqoiqtlwe3DcTm-4faFFxfdrJkEsTHN4m5NU2lAn4WevGKr7y_8-sQrJw967XTYJAfgWcPCzMfhxttKsLYxJgsf6sYGysQe93VDUeCh38NWJDo; T=af=JnRzPTE2NDMyODAyMjcmcHM9MmlqRGVxaDNGeGhSU0w2Q1cuQzRWUS0t&d=bnMBeWFob28BZwFRQVZMSEJUT1hBRUtISTZRSVZYTEVNQllGRQFhYwFBUG9iRExSVAFhbAFvZm9qeAFzYwFkZXNrdG9wX3dlYgFmcwFFT1JFWlh4aDNhUmwBenoBamRuOGhCQTdFAWEBUUFFAWxhdAFsUmEzaEIBbnUBMA--&kt=EAA.5EP4iN64ehB.oVekYNIHA--~I&ku=FAAHRNTVxc79zKh8KTQTaeMfGabALUsOAHb7aulACNuSDIJgX6yvEZVtN7hmiI5Xy7pDBWkxx05keO4zoOBB3.3YFXM5GbtMgwocXJbt7YtGNO2QaRdVoe4EMSmGDys8MXcaan4heKDNYIet0AKBToTDeTxPk1T2bP7Kz14iIysG.4-~E; FS=v=1&d=aqnF5ym1CTFTliJbTvmL7YAREbjRqgIGmErz.7Q6b9js5efh.pMYXDxZCMiDXQ--~A; A1=d=AQABBFGSK2ECEC8K6aFQ2aj0GMNwYVbXjpAFEgEABgLy3mHIYmJcb2UB_eMBAAcIUZIrYVbXjpAID3Ao0cdNUmQZcHtsXP54MQkBBwoBeQ&S=AQAAAu-3fX5jVAUYZNpBjfElXKw; A3=d=AQABBFGSK2ECEC8K6aFQ2aj0GMNwYVbXjpAFEgEABgLy3mHIYmJcb2UB_eMBAAcIUZIrYVbXjpAID3Ao0cdNUmQZcHtsXP54MQkBBwoBeQ&S=AQAAAu-3fX5jVAUYZNpBjfElXKw; B=913mnapgin4ih&b=4&d=yTv0rVttYFnZ.hMBxEdp&s=jj&i=cCjRx01SZBlwe2xc_ngx; GUC=AQEABgJh3vJiyEIdrASN; A1S=d=AQABBFGSK2ECEC8K6aFQ2aj0GMNwYVbXjpAFEgEABgLy3mHIYmJcb2UB_eMBAAcIUZIrYVbXjpAID3Ao0cdNUmQZcHtsXP54MQkBBwoBeQ&S=AQAAAu-3fX5jVAUYZNpBjfElXKw&j=WORLD; ucs=tr=1645725812000; cmp=t=1645639416&j=0; AS=v=1&s=TUe1JSxq&d=D6217cbb8|sp2IP77.2SpnQpy.doOIBEFvco1eubghVaHHL.mPq64IQShwoDDMCA6dexTwzdZQo.CTcF38k5adWq346l_Pnr3YEOz8d.d5ovqcEqug.zxtxToiYY1oIoNvZyejZwSs3I_Ay6Pl_HWxGbgFHfjy2RllAu0zSuYD1ZXNrta5a1_Kg0mIZPrODloe_IfXDQdWQRKl8tV9ymA7q3OUfyRBU2qP.v4_6pxD14zBxAn2fzPd1.9A_1XKpC1CWpnyjoiDT8stmcE5EuJBQ4NbPM_XAW3gjxWUhNshSt3W7sczgeM3CrABKyXEJB1TQLh33HZfIJyRHlgpmpvSJ3FIIXRl8bzX5p6e1NYqCFVLuOc7wyK8Fz.6oDfITDjG4fesLGRP6Hiz7b17A68.L.tJ4nc.cM3S0T1gmqDjY_zP7I6fEu4ylTjQnk.BjNTjCXpHca2YxbiaoA4Peft2FJohuCCdcmSXqVMM9.KnKN3m.IFxa0iOnCpbE8VkX3.WZaLfAOHH.M9AvLUWzXEFdjhz39_wsOay8BQPtL60e6XT4uqihSVt5yYY1C2SrrdgWvvtojPa1s_cnQY0Ns5pjKp.brjPR_MuRlYlo90jVZaZkzKwq9q.GBbk_qiI7df6Bbt7sYerjKB4wbxkKVkFzaDqLa.EgOT89Vt_qdH1EufxuOpJAyx0Dl9nv6fKgIjI2Ga9TjkZA0t_d42FYpksB5C2Di0Osq_2Kgs8l_voEy7izAT_d950PM.hAjZxcuUxhuvJXJfnF1boXP_fjTfQt9i.v91LIYKdcS3V7zhLwoLbvkvBK.S2Y0Re58Q4TQ--~A',
                'Referer': 'https://login.yahoo.com/account/create?.lang=ar-JO&src=homepage&activity=ybar-signin&pspid=2142947267&add=1&done=https%3A%2F%2Fmaktoob.yahoo.com%2F&specId=yidReg',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36',
                'X-Requested-With': 'XMLHttpRequest',
            }
            data = {
                'specId': 'yidreg',
                'acrumb': 'TUe1JSxq',
                'yid': str(email2),
            }
            req1 = post('https://login.yahoo.com/account/module/create?validateField=yid', headers=headers,data=data).text
            if '"IDENTIFIER_EXISTS"' in req1:
                return no
            elif '"IDENTIFIER_EXISTS"' not in req1:
                tik = tiktok(email)
                if tik == True :return yes
                else:return no
            else:return no
        except:return no
        

    elif check == "outlook.com" or check == "hotmail.com" or check == "outlook.sa":
        try:
            url = f'https://odc.officeapps.live.com/odc/emailhrd/getidp?hm=0&emailAddress={email}&_=1604288577990'
            header = {
                'content-type': 'application/x-www-form-urlencoded',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36',
            }

            req2 = post(url, headers=header).text
            if req2 == 'Neither':
                tik = tiktok(email)
                if tik == True :return yes
                else:return no
            elif req2 == 'MSAccount':return no
            else:return no
        except: return no

    elif check == "@mail.ru":
        try:
            req3 = post('https://account.mail.ru/api/v1/user/exists', data={'email': str(email)}, headers={
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36'}).text
            if 'exists":false' in req3:
                tik = tiktok(email)
                if tik == True :return yes
                else:return no
            elif 'exists":true' in str(req3): return no
            else: return no
        except: return no

    else :
        error = {"DEV":{"user_tele" : "@Glich5" , "CH" : "@G5python3"},"result":{"check": "error","email": str(email)}}
        return error

if __name__ == "__main__":
    app.run()
