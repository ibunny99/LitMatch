import requests,json,time,os
res = requests.Session();

g = ("\33[0;32m")#Green")
b = ("\33[0;36m")#Blue")
red = ("\33[31;1m")#Red")
ttp = ("\033[0m")#LightGrey")
underline = ('\033[4;37;48m')

def main():
     os.system("clear")
     print(ttp+"                 ["+b+" Lit Diamond "+ttp+"]")
     print(g+"            [ "+ttp+underline+"http://rezadkim.my.id"+g+" ]"+ttp)
     ses = input(ttp+"\n["+b+"?"+ttp+"] Session : "+g)
     uuid = input(ttp+"["+b+"?"+ttp+"] Uuid    : "+g)
     jml = int(input(ttp+"["+b+"?"+ttp+"] Max(50/day)    : "+g))
     headers = {
          "Content-Type": "application/json; charset=UTF-8",
          "Content-Length": "26",
          "Host": "www.litatom.com",
          "Connection": "Keep-Alive",
          "Accept-Encoding": "gzip",
          "User-Agent": "okhttp/3.12.12"
     }
     print(ttp+"["+g+"%"+ttp+"] Inject Data ...")
     time.sleep(3)
     for i in range(jml):
          print()
          data = {"activity":"watch_video"}
          r = requests.post("http://www.litatom.com/api/sns/v1/lit/account/deposit_by_activity?sid="+ses+"&loc=ID&uuid="+uuid+"&version=3.8.2&lang=vi&platform=android", headers=headers, data=json.dumps(data)).text
          cek = json.loads(r)
          if cek['success'] ==True:
               print(ttp+"["+g+str(i)+ttp+"] thanhcong")
          else:
               print(ttp+"["+red+str(i)+ttp+"] thatbai")

main()
