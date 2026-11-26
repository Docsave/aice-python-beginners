african_countries = "Nigeria,Ghana,Kenya,Ethopia,Egypt"
date = "26/11/2026"

print(african_countries.split())
print(date.split())

countries_list = african_countries.split(",")
print(countries_list[0])
print(countries_list[1])
print(countries_list[2])
print(countries_list[3])
print(countries_list[4])

date_component = date.split("/")
print("Day:", date_component[0])
print("Month:", date_component[1])
print("Year:", date_component[2])

