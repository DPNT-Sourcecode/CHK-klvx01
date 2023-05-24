

# noinspection PyUnusedLocal
# skus = unicode string


def checkout(skus):
    # Set up checkout dictionary to store all the prices of each item. 
    # This allows us to chnage prices of items later if needed
    checkout_dict = {'A':50,'B':30,'C':20,'D':15, 'E': 40, 'F': 10,'G':20,'H':10,'I':35,'J':60,'K':80,'L':90,'M':15,'N':40,'O':10,'P':50,'Q':30,'R':50,'S':30,'T':20,'U':40,'V':50,'W':20,'X':90,'Y':10,'Z':50}
    items_with_offers = ['A','B','E','F','H','K','N','P','Q','R','U','V']
    item_count = {}
    if not isinstance(skus,str):
        # If the input is not a string we immediately return -1
        return -1
    else:
        total = 0

        for letter in skus:
            if letter in items_with_offers:
                try:
                    item_count[f"num_{letter}"] += 1
                except:
                    item_count[f"num_{letter}"] = 1

            else:
                total += checkout_dict[letter]

        
        def value_letter(letter,offer1,offer2,original_price):
            # offer 1 = [3,130]
            # offer 2 = [5,200]
            global item_count
            num_letter = item_count[f"num_{letter}"] 
            value = 0

            offer_1_trig = 0
            offer_2_trig = 0

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
                    
                value += (num_letter * original_price)

                return value
                  
            else:
                return 0

        
        # Offer for E
        try:
            offer_E_trigger = item_count['num_E'] // 3
            item_count['num_B'] -= offer_E_trigger
        except:
            pass

        # Offer for F
        try:
            offer_F_trigger = item_count['num_F'] // 3
            item_count['num_F'] -= offer_F_trigger
        except:
            pass

        try:
            offer_N_trigger = item_count['num_N'] // 3
            item_count['num_M'] -= offer_N_trigger
        except:
            pass

        try:
            offer_R_trigger = item_count['num_R'] // 3
            item_count['num_Q'] -= offer_R_trigger
        except:
            pass

        try:
            offer_U_trigger = item_count['num_U'] // 4
            item_count['num_U'] -= offer_U_trigger
        except:
            pass




        value_A = value_letter('A',[5,200],[3,130],50)
        value_B = value_letter('B',[2,45],None,30)
        value_H = value_letter('H',[10,80],[5,45],10)
        value_K = value_letter('K',[2,150],None,80)
        value_P = value_letter('P',[5,200],None,50)
        value_Q = value_letter('Q',[3,80],None,30)
        value_V = value_letter('V',[3,130],[2,90],50)

        

            



        # # Set the total for the amount of shopping.
        # total = 0
        # # Collecting the number of As
        # num_a = 0
        # # Collecting the number of Bs
        # num_b = 0

        # # Collect num of E
        # num_e = 0

        # # Collect num of f
        # num_f = 0

        # # No need to collect other letter as they do not have an offer

        # # Cycle through each sku in the inputted string
        # for letter in skus:
        #     if letter == 'A':
        #         # Collect the number of As
        #         num_a += 1
        #     elif letter == 'B':
        #         # Collect the number of Bs
        #         num_b += 1
        #     elif letter == 'C':
        #         # Since C does not have an offer we can directly add its price to the total
        #         total += checkout_dict['C']
        #     elif letter == 'D':
        #         # Since D does not have an offer we can directly add its price to the total
        #         total += checkout_dict['D']
        #     elif letter == 'E':
        #         num_e += 1
        #         total += checkout_dict['E']
        #     elif letter == 'F':
        #         num_f += 1
        #         total += checkout_dict['F']
        #     else:
        #         # If an incorrect letter is passed we return -1
        #         return -1 
        
        # # Work out the number of times a user buys A in accordance to the offer:
        # # We can use the floor division to see the number of time the customer triggers the offer:

        # def value_from_a(num_a):
        #     if num_a > 0:
        #         # Set value of sum of items A
        #         value_a = 0

        #         # Check to see the number of times the first offer is triggered
        #         offer_1_a = num_a // 5

        #         # Reduce the number of items used to trigger this offer from the original number of As
        #         num_a -= (offer_1_a*5)

        #         # Check to see the number of times the second offer is triggered
        #         offer_2_a = num_a // 3
        #         # Reduce the number of items used to trigger this offer from the original number of As
        #         num_a -= (offer_2_a * 3)
                
        #         # Add all the respective values of A
        #         value_a += (offer_1_a*200) + (offer_2_a*130) + (num_a * 50) 

        #         return value_a
        #     else:
        #         return 0

        # def value_from_b(num_b):
        #     if num_b > 0:
        #         # Set value of sum of items B
        #         value_b = 0

        #         # Check to see the number of times the offer is triggered
        #         offer_b = num_b // 2

        #         # Reduce the number of items used to trigger this offer from the original number of Bs
        #         num_b -= (offer_b*2)

        #         # Add all the respective values of B
        #         value_b += (offer_b*45) + (num_b*30)
                
        #         return value_b
        #     else:
        #         return 0
            
        

        # # Check the number of E bought:
        # offer_E = num_e // 2

        # # Reduce that number from the number of B bought:
        # num_b -= offer_E

        # # Use function to calculate the value from the A items
        # value_a = value_from_a(num_a)
        
        # # Use function to calculate the value from the B items
        # value_b = value_from_b(num_b)
        
       
        # # Add these values to the total
        # total += value_a + value_b

        #  # Removing added cost of F 
        # offer_F = num_f // 3 # this is the number of free F a customer can get

        # # Remove the value of these F from total 
        # total -= (offer_F * checkout_dict['F'])
        # # Return total
        # return total

        


