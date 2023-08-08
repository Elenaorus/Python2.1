names = ['Alex', 'Vlad', 'Elena']
salaries = [15000, 20000, 25000]
awards = ['10.25%', '7.25%', '5.56%']

print({name: salary * float(award[:-1]) / 100 for name, salary, award in zip(names, salaries, awards)})