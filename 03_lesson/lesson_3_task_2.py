
from smartphone import Smartphone

catalog = []

catalog.append(Smartphone("Xiaomy", "11PRO", "+791038556832"))
catalog.append(Smartphone("Samsung", "Galaxy S20FE", "+79111111111"))
catalog.append(Smartphone("Nokia", "3110", "+79000000000"))
catalog.append(Smartphone("OPPO", "A60", "+79222222222"))
catalog.append(Smartphone("Xiaomy", "Redmi", "+79333333333"))

for phone in catalog:
    print(f"{phone.phone_maker} - {phone.model}. {phone.phone_number}")

