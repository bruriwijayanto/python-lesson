"""
Data Dictionary
Key & Value Pair
"""

javanese_eng_dict = {'putro': 'son', 'semah': 'wive', 'romo': 'father', 'ibu': 'mother'}

print(javanese_eng_dict)
print(javanese_eng_dict['semah'])
print(javanese_eng_dict['putro'])


print('\n Nested Object Dictionary ')
myobj = {
    'date': '2020-06-10',
    'driver_list': [
        {'name': 'Eko', 'distance': 10},
        {'name': 'Dwi', 'distance': 30},
        {'name': 'Tri', 'distance': 100},
        {'name': 'Catur', 'distance': 1000}
    ]
}

print(f"\nShow list {myobj['driver_list']}")
print(f"Driver #1 {myobj['driver_list'][0]}")
print(f"Driver #4 {myobj['driver_list'][3]}")
print(f"First driver distance {myobj['driver_list'][0]['distance']} meter")