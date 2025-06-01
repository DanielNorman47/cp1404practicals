
presale_cost = 0
number_of_items = 1
while number_of_items > 0:
    number_of_items = int(input("Number of items: "))
    price_of_item = int(input("Price of item: $"))
    presale_cost += price_of_item * number_of_items

    if presale_cost > 100:
        postsale_cost = 0.9 * presale_cost
    else:
        postsale_cost = presale_cost
    print(f"Total cost is: ${postsale_cost}")
