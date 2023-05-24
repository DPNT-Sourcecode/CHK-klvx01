

# noinspection PyUnusedLocal
# skus = unicode string

# -----------------------------------------------------------------------------------------------------------

def checkout(skus):
    # --------------------------------------------------------------------

    # Creating a dictionary for all the prices and items in relevant offers

    checkout_dict = {'A':{'price':50,'offer1':[5,200],'offer2':[3,130]},'B':{'price':30,'offer1':[2,45],'offer2':None},'C':20,'D':15, 'E': {'price':40,'offer1':None,'offer2':None}, 'F': {'price':10,'offer1':None,'offer2':None},'G':20,'H':{'price':10,'offer1':[10,80],'offer2':[5,45]},'I':35,'J':60,'K':{'price':70,'offer1':[2,120],'offer2':None},'L':90,'M':{'price':15,'offer1':None,'offer2':None},'N':{'price':40,'offer1':None,'offer2':None},'O':10,'P':{'price':50,'offer1':[5,200],'offer2':None},'Q':{'price':30,'offer1':[3,80],'offer2':None},'R':{'price':50,'offer1':None,'offer2':None},'S':{'price':20,'offer1':None,'offer2':None},'T':{'price':20,'offer1':None,'offer2':None},'U':{'price':40,'offer1':None,'offer2':None},'V':{'price':50,'offer1':[3,130],'offer2':[2,90]},'W':20,'X':{'price':17,'offer1':None,'offer2':None},'Y':{'price':20,'offer1':None,'offer2':None},'Z':{'price':21,'offer1':None,'offer2':None}}

    # Identifying all items involved in an offer
    items_with_offers = ['A','B','E','F','H','K','M','N','P','Q','R','U','V','S','T','X','Y','Z']

    # A way to track the number of items involved in offers
    item_count = {}
    # --------------------------------------------------------------------

    if not isinstance(skus,str):
        # If the input is not a string we immediately return -1
        return -1
    else:
        total = 0

        # Iterating through each item in the string
        for letter in skus:
            if letter in items_with_offers:
                try:
                    item_count[f"num_{letter}"] += 1
                except:
                    item_count[f"num_{letter}"] = 1

            else:
                try:
                    total += checkout_dict[letter]
                except:
                    return -1
    # --------------------------------------------------------------------

    # This function calculates the value that a set of the same item will cost
    def value_letter(letter,offer1,offer2,original_price,item_count):
        
        try:
            num_letter = item_count[f"num_{letter}"] 
            value = 0

            offer_1_trig = 0
            offer_2_trig = 0

            # Applying the offers of the items
            if num_letter > 0:
                if offer1 != None:
                    offer_1_trig = num_letter // offer1[0]
                    num_letter -= (offer_1_trig * offer1[0])
                    value += (offer_1_trig * offer1[1])

                    if offer2 != None:
                        offer_2_trig = num_letter // offer2[0]
                        num_letter -= (offer_2_trig * offer2[0])
                        value += (offer_2_trig * offer2[1])

                    else:
                        pass
                
                # Adding any extra items not invoved in the bundle deal
                value += (num_letter * original_price)

                return value
                
            else:
                return 0
        except:
            return 0
    # --------------------------------------------------------------------

    # This function updates the item count of the items involed in offers to account for any free items
    def update_item_count(letter1,letter2,discount_amount,item_count):
        
        if letter1 != None and letter2 != None:
            try:
                free_item_count = item_count[f'num_{letter1}'] // discount_amount
                try:
                    item_count[f'num_{letter2}'] -= free_item_count
                    if item_count[f'num_{letter2}'] < 0 :
                        item_count[f'num_{letter2}'] = 0
                    else:
                        pass
                except:
                    pass  
            except:
                pass
        else:
            try:
                free_item_count = item_count[f'num_{letter1}'] // discount_amount
                item_count[f'num_{letter1}'] -= free_item_count
                if item_count[f'num_{letter1}'] < 0:
                    item_count[f'num_{letter1}'] = 0
                else:
                    pass
            except:
                pass

    
    # Update all item counts involved in free item offers

    update_item_count('E','B',2,item_count)
    update_item_count('F',None,3,item_count)
    update_item_count('N','M',3,item_count)
    update_item_count('R','Q',3,item_count)
    update_item_count('U',None,4,item_count)

    # --------------------------------------------------------------------

    # Appending the values of items that are involved in offers into an array
    values = []

    for i in range(13):
        values.append(value_letter(items_with_offers[i],checkout_dict[items_with_offers[i]]['offer1'],checkout_dict[items_with_offers[i]]['offer2'],checkout_dict[items_with_offers[i]]['price'],item_count))
        

    # Taking the sum of the array and adding it onto the total
    total += sum(values)
    # --------------------------------------------------------------------
    
    # This function calculates the price of the bundled items
    def group_bundle_discount(checkout_dict,item_count):
        # These are the items in the bundle discount in ascending order based by price
        bundle_items_asc = ['X','S','T','Y','Z']

        # Track the total cost of the bundle discount section
        total = 0

        # Track the number of items in the bundle offer
        sum_items_bundle = 0
        for letter in bundle_items_asc:
            try:
                sum_items_bundle += item_count[f'num_{letter}']
            except:
                pass

        # Work out the number of times the offer is triggered
        offer_trigger = sum_items_bundle // 3
        # Price of the bundle
        offer_value = 45
        # And the value of offers to the total
        total += (offer_trigger * offer_value)

        # Work out the number of items leftover
        leftover_val = sum_items_bundle - (offer_trigger * 3)

        # Now we want to add the price of the cheapest remaining items
        # Track the sub total of this section

        sub_total = 0

        for letter in bundle_items_asc:
            try:
                letter_count = item_count[f'num_{letter}']
                for i in range(letter_count):
                    # Reduce lefotver value by 1
                    leftover_val -= 1
                    # Add the price of the item to the sub total
                    sub_total += checkout_dict[letter]['price']

                    # Check to see if we have fulfilled all the remaining items:
                    if leftover_val == 0:
                        total += sub_total
                        return total
            except:
                pass
        
        return total
    
    # Gather the price of the bundle items
    group_bundle_val = group_bundle_discount(checkout_dict,item_count)

    # Add this price to the overall total
    total += group_bundle_val

    return total





        


