from app import Resident

resident = Resident(name='Jordan', age='23', id=23)

resident.print_name()
resident.print_age()
resident.print_id()

resident.title()
print(Resident.mro())
print(Resident.__mro__)


  