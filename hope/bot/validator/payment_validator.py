from dataclasses import dataclass


@dataclass
class PaymentValidator:
    user: object
    contract: object
    payment: object
    wallet: object
    tron_scan: object
    transactionid: str
    MESSAGES: dict

    def check_transactionid_len(self) -> bool:
        """Check the length of the user transaction ID
        """
        if len(self.transactionid) != 64:
            return False, self.MESSAGES['message_transactionid_len_error']
        return True, None

    def check_payment_exists_before(self) -> bool | str | object:
        """Check to see user transactionID exists before or not
        """
        try:
            user_payment = self.payment.objects.create(
                user=self.user,
                transaction_id=self.transactionid,
            )
            user_payment.save()
            return True, user_payment
        except:
            return False, self.MESSAGES['message_transaction_id_invalid_error']

    def validate_owner_address(self) -> bool | str:
        """Check the OwnerAddress of the transaction
           is the same as the user wallet address or not
        """
        self.info = self.tron_scan().check(transaction_id=self.transactionid)
        if not self.info or self.info['ownerAddress'] != self.user.user_balance.wallet:
            return False, self.MESSAGES["message_user_transaction_not_related_error"]
        return True, None

    def validate_wallet(self) -> bool | str:
        """Check whether the user dest transaction address
            is the same as the admin address"""
        wallet = self.wallet.objects.filter(wallet=self.info['toAddress'])
        if not wallet:
            return False, self.MESSAGES["message_user_transaction_dst_invalid_error"]
        return True, None

    def validate_contract_ret(self) -> bool | str:
        """Check contractRet value and confirm list"""
        if self.info['contractRet'].lower() != "success" and self.info['srConfirmList'] < 6:
            return False, self.MESSAGES['message_transaction_not_verified_error']
        return True, None

    def validate_contract_address(self) -> bool | str | object:
        """Check User transaction ContractAdress 
            exists in the valid list or not
        """
        contract = self.contract.objects.filter(
            contract_addres=self.info["contract_address"])
        if not contract:
            return False, self.MESSAGES["message_user_transaction_invalid_error"]

        return True, contract

    def update_user_payment(self, user_payment: object) -> None:
        user_payment.status = True
        user_payment.ownerAddress = self.info['ownerAddress']
        user_payment.amount = self.info['amount']
        user_payment.contract_address = self.info['contract_address']
        user_payment.contractRet = self.info['contractRet']
        user_payment.srConfirmList = self.info['srConfirmList']
        user_payment.save()

    def main(self):
        status, data = self.check_transactionid_len()
        if not status:
            return None, data

        status, user_payment = self.check_payment_exists_before()
        if not status:
            return None, user_payment

        status, data = self.validate_owner_address()
        if not status:
            return None, data

        status, data = self.validate_wallet()
        if not status:
            return None, data

        status, data = self.validate_contract_ret()
        if not status:
            return None, data

        status, contract = self.validate_contract_address()
        if not status:
            return None, contract

        user_payment = self.update_user_payment(user_payment)
        return contract, self.info
