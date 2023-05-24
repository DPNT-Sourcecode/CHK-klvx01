

# noinspection PyUnusedLocal
# skus = unicode string


def checkout(skus):
    # Set up checkout dictionary to store all the prices of each item. 

    
    # --------------------------------------------------------------------
    # Creating a dictionary for all the prices and items in relevant offers

    checkout_dict = {'A':{'price':50,'offer1':[5,200],'offer2':[3,130]},'B':{'price':30,'offer1':[2,45],'offer2':None},'C':20,'D':15, 'E': {'price':40,'offer1':None,'offer2':None}, 'F': {'price':10,'offer1':None,'offer2':None},'G':20,'H':{'price':10,'offer1':[10,80],'offer2':[5,45]},'I':35,'J':60,'K':{'price':80,'offer1':[2,150],'offer2':None},'L':90,'M':{'price':15,'offer1':None,'offer2':None},'N':{'price':40,'offer1':None,'offer2':None},'O':10,'P':{'price':50,'offer1':[5,200],'offer2':None},'Q':{'price':30,'offer1':[3,80],'offer2':None},'R':{'price':50,'offer1':None,'offer2':None},'S':30,'T':20,'U':{'price':40,'offer1':None,'offer2':None},'V':{'price':50,'offer1':[3,130],'offer2':[2,90]},'W':20,'X':90,'Y':10,'Z':50}

    # Identifying all items involved in an offer
    items_with_offers = ['A','B','E','F','H','K','M','N','P','Q','R','U','V']

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

    for i in range(len(items_with_offers)):
        values.append(value_letter(items_with_offers[i],checkout_dict[items_with_offers[i]]['offer1'],checkout_dict[items_with_offers[i]]['offer2'],checkout_dict[items_with_offers[i]]['price'],item_count))
        

    # Taking the sum of the array and adding it onto the total
    total += sum(values)
    
    return total



        


