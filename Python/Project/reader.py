import pandas 

fractions = pandas.read_csv('deputies.csv')
fractionset = set(fractions.fractions.to_list())
print(fractionset)