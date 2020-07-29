from  _collections import OrderedDict
command = input()
data = {}
while command != "End":
    command = command.split(' -> ')
    company = command[0]
    employee = command[1]
    if company not in data:
        data[company] = [employee]
    else:
        if employee not in data[company]:
            data[company].append(employee)
    command = input()
ordered = OrderedDict(sorted(data.items(), key=lambda x: x[0]))
for k, v in ordered.items():
    print(k)
    for value in v:
        print(f'-- {value}')