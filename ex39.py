states = {
    "Oregon": "OR",
    "Florida": "FL",
    "California": "CA",
    "New York": "NY",
    "Michigan": "MI"
}
# this is the same as line 10:
# cities = {"CA": "San Francisco", "MI": "Detroit", "FL": "Jacksonville", "NY": "New York"}
cities = {
    "CA": "San Francisco",
    "MI": "Detroit",
    "FL": "Jacksonville"
}

cities["NY"] = "New York"
cities["OR"] = "Portland"

print("-" * 10)
print("NY State has", cities["NY"])
print("OR state has", cities["OR"])

print('-' * 10)
print('michigans abbreviation is: ', states["Michigan"])

print('-' * 10)
print("Florida has:", cities[states["Florida"]])

print('-' * 10)
for state, abbrev in list(states.items()):
    print(f" {state} has the city {abbrev}")

print('-' * 10)
for abbrev, city in list(states.items()):
    print(f" {abbrev} has the city {city}")

print('-' * 10)
for state, abbrev in list(states.items()):
    print(f"{state} state is abbreviated {abbrev}")
    print(f"and has the city {cities[abbrev]}")

print('-' * 10)
state = states.get('Texas')

if not state:
    print("Sorry, no Texas")

city = cities.get("TX", "Does Not Exist")
print(f"The city for thew state 'TX' is {city}")
