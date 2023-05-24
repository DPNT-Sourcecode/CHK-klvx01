

# noinspection PyUnusedLocal
# skus = unicode string


def checkout(skus):
    # Set up checkout dictionary to store all the prices of each item. 
    # This allows us to chnage prices of items later if needed
    checkout_dict = {'A':50,'B':30,'C':20,'D':15}

    if not isinstance(skus,str):
        return -1
    else:
        # Set the total for the amount of shopping.
        total = 0
        # Collecting the number of As
        num_a = 0
        # Collecting the number of Bs
        num_b = 0

        # No need to collect other letter as they do not have an offer

        # Cycle through each sku in the inputted string
        # Use .upper() to incase a use accidentally types the lowercase version of the letter
        for letter in skus:
            if letter.upper() == 'A':
                # Collect the number of As
                num_a += 1
            elif letter.upper() == 'B':
                # Collect the number of Bs
                num_b += 1
            elif letter.upper() == 'C':
                # Since C does not have an offer we can directly add its price to the total
                total += checkout_dict['C']
            elif letter. upper() == 'D':
                # Since D does not have an offer we can directly add its price to the total
                total += checkout_dict['D']
            else:
                # If an incorrect letter is passed we return -1
                return -1 
        
        # Work out the number of times a user buys A in accordance to the offer:
        # We can use the floor division to see the number of time the customer triggers the offer:
        offer_a = num_a // 3 # number of times the offer for A is triggered
        offer_a_amount = 130 # the offer amount for A
        # Same for the offer on B:
        offer_b = num_b // 2 # number of times the offer for B is triggered
        offer_b_amount = 45 # the offer amount for B

        # Add everything to to the total:
        
        # The value accumulated by offer A
        total_value_of_offer_a = offer_a_amount*offer_a
        # Left over value of A items
        leftover_value_a = checkout_dict['A']*(num_a-(3*offer_a))

        # The value accumulated by offer B:
        total_value_of_offer_b = offer_b_amount*offer_b
        # Left over value of B items
        leftover_value_b = checkout_dict['B']*(num_b-(2*offer_b))

        # Add all these values to the total
        total += total_value_of_offer_a + leftover_value_a + total_value_of_offer_b + leftover_value_b

        # Return the total
        return total

        

