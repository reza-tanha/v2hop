from perfectmoney import PerfectMoney

proxies = {"http":"socks5h://127.0.0.1:1359","https":"socks5h://127.0.0.1:1359"}
p = PerfectMoney("15226661", "reza2020", proxies=proxies)



print(p.voucher_activation("U42122089", 2341153204, 4817106345785966))
print(p.voucher_activation("U42122089", 1234567890, 1234567890123456))
print(p.balance())



# HEAD = {
#     "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36",
#     # "request": "eyJtZXRob2QiOiAiR0VUIiwgInVyaSI6ICJodHRwczovL3d3dy5hcGFyYXQuY29tL2FwaS9mYS92MS92aWRlby92aWRlby9zaG93L3ZpZGVvaGFzaC9kZGRkZCIsICJoZWFkZXJzIjoge30sICJhdXRoIjogeyJfdCI6ICJOb25lIn19",
# }

# DATA = {
# "method":"G",
# "url":"https://www.aparat.com/api/fa/v1/video/video/show/videohash/Sg1CJ",
# "bodytype":"T",
# "locationid":"10"
# }

# proxy = {"socks5":"127.0.0.1:20170"}
# url = "https://www.site24x7.com/tools/restapi-tester"
# # r = requests.post(
# #     url,
# #     headers=HEAD,
# #     data=DATA,
# #     proxies=proxy
# # )

# # print(r.text)
# # # exit()

# # b = json.dumps({"method":"GET","uri":f"https://www.aparat.com/api/fa/v1/video/video/show/videohash/ddddd","headers":{},"auth":{"_t":"None"}})
# # base = base64.b64encode(b.encode("ascii"))

# # # base = base64.b64encode(b)
# # print(base)

# def site24x7(url_):
#     url = "https://extendsclass.com/rest-client-request"
#     DATA = {"method":"GET","url":url_,"headers":[],"body":""} 
#     proxy = {"socks5":"127.0.0.1:9090"}
#     # r = requests.post(url, headers=HEAD,data=DATA, proxies=proxy)
        
#     r = requests.post(url,headers=HEAD,data=json.dumps(DATA))
#     text = r.json()["responseText"]
    
#     print(text)
    
#     # return json.loads(text["htmlresponse"])
    
# # print(site24x7("https://www.aparat.com/api/fa/v1/video/video/show/videohash/Sg1CJ"))
    
    
# def restninja_io(uri):
#     try:
#         url = "https://restninja.io/in/proxy"
#         b = {"method":"GET","uri":uri,"headers":{},"auth":{"_t":"None"}}
#         base = base64.b64encode(json.dumps(b).encode("ascii"))
#         HEAD = {"user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36","request": base,}
#         r = requests.post(url,headers=HEAD,data=DATA)
#         return r.text
#     except:
#         return False
    
# # print(restninja_io("https://www.aparat.com/api/fa/v1/video/video/show/videohash/Sg1CJ"))
    
    
    
# def extendsclass(url_):
#     try:
#         url = "https://extendsclass.com/rest-client-request"
#         DATA = {"method":"GET","url":url_,"headers":[],"body":""}         
#         r = requests.post(url,headers=HEAD,data=json.dumps(DATA))
#         text = r.json()["responseText"]
#         return text
#     except:
#         return False
# # print(extendsclass("https://www.aparat.com/api/fa/v1/video/video/show/videohash/Sg1CJ"))

    

# # "form_is_submited": "base64-tools-http-request-online",
# # "form_action_url": "/tools/http-request-online",
# # "url": "https://www.aparat.com/api/fa/v1/video/video/show/videohash/Sg1CJ",
# # "http_method": "GET",
# # "http_version": 1_0,
# # "execute_http_request": 1


# from perfectmoney import PerfectMoney
# proxies = {"http":"socks5h://127.0.0.1:2021","https":"socks5h://127.0.0.1:2021"}
# # proxies = {"http":"socks5://127.0.0.1:20170","https":"socks5://127.0.0.1:20170"}
# # p = PerfectMoney("15226661", "3x9183qESqUzQSaAXQtMdtTAN", proxies=proxies) 
# # p = perfectmoney.PerfectMoney.("15226661", "3x9183qESqUzQSaAXQtMdtTAN", proxies=proxies) 
# # print(p.balance())
# # print(p("U42122089", 19.95))


# {"VOUCHER_NUM": "2341153204", "VOUCHER_AMOUNT": "1.00", "VOUCHER_AMOUNT_CURRENCY": "1", "Payee_Account": "U42122089", "PAYMENT_BATCH_NUM": "506554665"}