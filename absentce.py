name = input("employee?")
no_absence = ""
most_absence = 0
no_people = 0
total_absence = 0
people = []
absences = []
while name != "$":
    days = int(input("absences"))
    if days == 0:
        no_absence += f" {name}"
    elif days > most_absence:
        most_absence = days
        most_absence_person = name
    no_people += 1
    total_absence += days
    absences.append(days)
    people.append(name)

    name = input("employee?")
average_absences = total_absence/no_people
over_average = ""
for n in range(0,len(absences)):
    if average_absences < absences[n]:
        over_average += f" {people[n]} {absences[n]}" \
                        f""
print(f"average number of days staff were absent:  {average_absences}")
print(f"")
print(f"person with the most absents is:           {most_absence_person} with {most_absence} days")
print(f"")
print(f"people who weren't absent at all:          {no_absence}")
print(f"")
print(f"people who were absent above average:      {over_average}")
print(f"")
print(f"")
