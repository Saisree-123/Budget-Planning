# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.12.0
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# +
class Service:
    def __init__(self):
        self.__choice=-1
    def list(self):
        print('1.Simple savings tracker 2.Basic budget Planning 3.Detailed analysis and customized suggestion')
        
    def show(self,service_number):
        if service_number == 1:
            print('This service can store your userid and password.')
        elif service_number == 2:
            print('This service can help you manage your money and making a monthly budget plan.')
        elif service_number == 3:
            print('This service can give you some suggestions on how to save your money.')
        else:
            print('The service you chose is not available.Please provide a vaild service number.')

    def choice(self,c_num):
        if c_num == 1:
            print('This service is included in free membership')
            self.__choice=c_num
        elif c_num == 2:
            print('This service is included in basic membership. The monthly sibscription fee is $15.')
            self.__choice=c_num
        elif c_num == 3:
            print('This service is included in premium membership. The monthly sibscription fee is $25.')
            self.__choice=c_num
        else:
            print('The service you chose is not available.Please provide a vaild service number.')

    def getChoice(self):
        return self.__choice


