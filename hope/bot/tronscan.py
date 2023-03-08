import requests


class TTC:
    def __init__(self) -> None:
        self.base_api = "https://apilist.tronscan.org/api/transaction-info?hash="
        
    def check(self, hash) -> dict:
        try : 
            req = requests.get(self.base_api + hash)
            js = req.json()
            toAddress = js.get('toAddress', None)
            ownerAddress = js.get('ownerAddress', None)
            tokenTransferInfo=js.get('tokenTransferInfo', None)
            contractRet=js.get('contractRet', None)#SUCCESS
            amount = js['contractData'].get('amount', None)
            srConfirmList = len(js['srConfirmList']) #if < 6 == False
            contract_address = None
            if tokenTransferInfo:
                contract_address = tokenTransferInfo.get('contract_address', None)#if tron == None
                amount = js["tokenTransferInfo"].get("amount_str", None)
                
            return {
                "contractRet": contractRet,
                "ownerAddress": ownerAddress,
                "toAddress": toAddress,
                "amount": int(amount) / 1000000,
                "srConfirmList": srConfirmList,
                "contract_address": contract_address
            }
        except:
            return False    

# ttc = TTC()
# print(ttc.check("9911e9895aa22f0909b68f34040e92181325adb175775ceaf1e3b1b03cd33e98"))
# print(ttc.check("1ff57b269d245ebae352a554be00f9e952e517f2ba64e19aaa6f381067dff5aa"))


class ChangeToRial:
    def __init__(self) -> None:
        self.base_api = "https://api.nobitex.ir/v2/orderbook/"
        
    def change(self, symbol) -> dict:
        try : 
            req = requests.get(self.base_api + symbol)
            js = req.json()
            return js['lastTradePrice']
        except:
            return False
    