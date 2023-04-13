class Account:
    def __init__(self, accntNo: int, accntName: str, accntBalance: int):
        self.accntNo = accntNo
        self.accntName = accntName
        self.accntBalance = accntBalance


class AccountDemo:
    def __init__(self):
        pass

    def depositAmnt(self, accObj: Account, amount: int):
        accObj.accntBalance += amount
        return accObj.accntBalance

    def withdrawAmnt(self, accObj: Account, amount: int):
        if accObj.accntBalance - amount >= 1000:
            accObj.accntBalance -= amount
            return accObj.accntBalance

        return "No Adequate balance"


# Sample main section. #Do not remove the below portion of code.
if __name__ == '__main__':
    acno = int(input())
    acname = input()
    acntbal = int(input())
    depamnt = int(input())
    withamnt = int(input())
    acnt = Account(acno, acname, acntbal)
    acntdemoobj = AccountDemo()
    print(acntdemoobj.depositAmnt(acnt, depamnt))
    print(acntdemoobj.withdrawAmnt(acnt, withamnt))
