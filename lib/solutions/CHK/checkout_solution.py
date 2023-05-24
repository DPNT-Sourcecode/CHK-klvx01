

# noinspection PyUnusedLocal
# skus = unicode string


def checkout(skus):
    # Set up checkout dictionary to store all the prices of each item. 
    # This allows us to chnage prices of items later if needed
    checkout_dict = {'A':50,'B':30,'C':20,'D':15, 'E': 40}

    if not isinstance(skus,str):
        # If the input is not a string we immediately return -1
        return -1
    else:
        # Set the total for the amount of shopping.
        total = 0
        # Collecting the number of As
        num_a = 0
        # Collecting the number of Bs
        num_b = 0

        # Collect num of E
        num_e = 0

        # No need to collect other letter as they do not have an offer

        # Cycle through each sku in the inputted string
        for letter in skus:
            if letter == 'A':
                # Collect the number of As
                num_a += 1
            elif letter == 'B':
                # Collect the number of Bs
                num_b += 1
            elif letter == 'C':
                # Since C does not have an offer we can directly add its price to the total
                total += checkout_dict['C']
            elif letter == 'D':
                # Since D does not have an offer we can directly add its price to the total
                total += checkout_dict['D']
            elif letter == 'E':
                num_e += 1
                total += checkout_dict['E']
            else:
                # If an incorrect letter is passed we return -1
                return -1 
        
        # Work out the number of times a user buys A in accordance to the offer:
        # We can use the floor division to see the number of time the customer triggers the offer:

        def value_from_a(num_a):
            # Set value of sum of items A
            value_a = 0

            # Check to see the number of times the first offer is triggered
            offer_1_a = num_a // 5

            # Reduce the number of items used to trigger this offer from the original number of As
            num_a -= (offer_1_a*5)

            # Check to see the number of times the second offer is triggered
            offer_2_a = num_a // 3
            # Reduce the number of items used to trigger this offer from the original number of As
            num_a -= (offer_2_a * 3)
            
            # Add all the respective values of A
            value_a += (offer_1_a*200) + (offer_2_a*130) + (num_a * 50) 

            return value_a

        def value_from_b(num_b):
            # Set value of sum of items B
            value_b = 0

            # Check to see the number of times the offer is triggered
            offer_b = num_b // 2

            # Reduce the number of items used to trigger this offer from the original number of Bs
            num_b -= (offer_b*2)

            # Add all the respective values of B
            value_b += (offer_b*45) + (num_b*30)
            
            return value_b

        # Check the number of E bought:
        offer_E = num_e // 2

        # Reduce that number from the number of B bought:
        num_b -= offer_E

        
        if num_a > 0:
            # Use function to calculate the value from the A items
            value_a = value_from_a(num_a)
        
        if num_b > 0:
            # Use function to calculate the value from the B items
            value_b = value_from_b(num_b)

        # Add these values to the total
        total += value_a + value_b

        # Return total
        return total

        


