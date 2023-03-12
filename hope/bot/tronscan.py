import requests


class TronScan:
    def __init__(self) -> None:
        self.base_api = "https://apilist.tronscan.org/api/transaction-info?hash={}"

    def check(self, transaction_id: str) -> dict | bool:
        """Get information about transaction id"""
        try:
            response = requests.get(self.base_api.format(transaction_id))
            data = response.json()
            transfer_info = data.get('tokenTransferInfo')
            amount = data.get('contractData', {}).get('amount')
            contract_address = None
            if transfer_info:
                contract_address = transfer_info.get('contract_address')
                amount = transfer_info.get("amount_str")

            return {
                "contractRet": data.get('contractRet'),
                "ownerAddress": data.get('ownerAddress'),
                "toAddress": data.get('toAddress'),
                "contract_address": contract_address,
                "srConfirmList": len(data.get('srConfirmList')),
                "amount": int(amount) / 1000000
            }
        except:
            return False


class Exchange:
    """
    Get price of currency by symbol
    """

    def __init__(self) -> None:
        self.base_api = "https://api.bitpin.ir/v1/mkt/markets/"

    def get_symbol_price(self, symbol: str) -> dict:
        symbol += "_IRT"
        try:
            req = requests.get(self.base_api)
            js = req.json()
            for code in js['results']:
                if code.get("code") == symbol:
                    if code.get("price"):
                        return int(code.get("price"))
                    else:
                        return None
        except:
            return False
