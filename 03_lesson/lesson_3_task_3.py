
from address import Address
from mailing import Mailing


sending = Mailing(Address("123456", "г. Череповец", "ул. Синяя", "д.13", "кв.11"), 
                 Address("654321",  "г. Канск", "ул. Чапаева", "д.7", "кв.4"), 
                 "500 рублей", "1234567890")

print(f"Номер отслеживания {sending.track} отправлено с адреса: {sending.from_address} на адрес: {sending.to_address}. стоимость: {sending.cost}")
      
    
    
    
    
    
    
    


    