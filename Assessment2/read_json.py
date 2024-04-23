import json

with open ('ex5.json','r') as file:

    ex5 = json.load(file) #load a file

print("The orginal Data :")
print(json.dumps(ex5,indent=4)) # check the orginal data

#step 3
for donut in ex5:
    if donut['name'] == 'Old Fashioned': 
        donut['batters']['batter'].append({'id': '1003', 'type': 'Tea'})

# Display the updated dictionary
print("\nUpdated dictionary:")
print(json.dumps(ex5, indent=4))