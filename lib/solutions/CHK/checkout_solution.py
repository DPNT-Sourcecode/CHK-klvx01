

# noinspection PyUnusedLocal
# skus = unicode string


def checkout(skus):
    checkout_dict = {'A':50,'B':30,'C':20,'D':15}

    if not isinstance(skus,str):
        return -1
    else:
        # Set the total for the amount of shopping.
        total = 0
        # Collecting the  number of As
        num_a = 0
        # Collecting the number of Bs
        num_b = 0

        # No need to collect other letter as they do not have an offer
        for letter in skus:
            if letter.upper() == 'A':
                num_a += 1
            elif letter.upper() == 'B':
                num_b += 1
            elif letter.upper() == 'C':
                total += checkout_dict['C']
            elif letter. upper() == 'D':
                total += checkout_dict['D']
            else:
                return -1 
        
        # Work out the number of times a user buys A in accordance to the offer:
        # We can use the floor division to see the number of time the customer triggers the offer:
        offer_a = num_a // 3
        # Same for the offer on B:
        offer_b = num_b // 2

        # Add everything to to the total:

        total += (130*offer_a) + (checkout_dict['A']*(num_a-(3*offer_a))) + (45*offer_b) + (checkout_dict['B']*(num_b-(2*offer_b)))

        return total

        


