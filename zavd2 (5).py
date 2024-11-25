import pandas as pd
import json

with open('digits.json', 'r') as file:
    data = json.load(file)

series1 = pd.Series(data['dict1'])
series2 = pd.Series(data['dict2'])

unique_elements = pd.Series(list(set(series1).symmetric_difference(set(series2))))

unique_elements.to_json('uniq.json')

print("Унікальні елементи збережено у файл uniq.json")