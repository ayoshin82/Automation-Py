from address import Address
from mailing import Mailing


to_address = Address
from_address = Address
to_address = 6600000, "г. Красноярск", "ул. Телевизорная", 5, 15
from_address = 354000, "г. Сочи", "ул. Любая", 4, 1

sending = Mailing
sending(to_address, from_address, 1000, 1234567890)

print("Отправление", sending.track, "из", from_address, "в", 
      to_address, "Стоимость:", sending.cost, "рублей.")
      
    
    
    
    
    
    
    


    