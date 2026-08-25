letter =  ''' Dear <Name> 
you are selected 
<Date>'''

letter.replace("<Name>", "Monu").replace("<Date>", "25th August 2026") #strings are immutable
print(letter)

letter = letter.replace("<Name>", "Monu").replace("<Date>", "25th August 2026")
print(letter)