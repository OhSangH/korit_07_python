from prettytable import PrettyTable
from poketmon_data import pokemon_data

table = PrettyTable()
table.field_names = ["번호", "이름", "타입"]
table.add_rows(pokemon_data)
print(table)
