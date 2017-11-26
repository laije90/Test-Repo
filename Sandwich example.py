sandwich_orders = ['Ham','pastrami','cheese','onions','PAstrami','pasTrami','taco','bbq']
finished_sandwiches = []

print("Tough Luck for the pastrami lovers")

#while 'pastrami' in sandwich_orders:
#    sandwich_orders.remove('pastrami')

lost_ingredient = 'Pastrami'

# use List > Filter > lambda to circumvent cases sensitivity
sandwich_orders = list(filter(lambda lost_ingredient: lost_ingredient.lower()!= 'pastrami',sandwich_orders))

# this is a comment for testing

while sandwich_orders:
    current_order = sandwich_orders.pop()
    finished_sandwiches.append(current_order)

print("\nThe folowing Sandwiches have been made:")
for finished_sandwiches in finished_sandwiches:
    print(finished_sandwiches.title())
    
