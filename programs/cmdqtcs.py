for _ in range(int(input())):
    inventory = [['shoe', 0, 0.0], ['shirt',0, 0.0]]
    cart = [['shoe', 0], ['shirt',0]]
    while(True):
        query = list(map(str, input().split()))
        #print(inventory)
        if query[0] != 'END':
            if query[1] == 'SM':
                if query[2] == 'ADD':
                    #print(query)
                    if (query[3] == 'SHIRT' and (float(query[4])-int(float(query[4])))==0 ):
                        inventory[1][1] += int(query[4])
                        print(query[4])
                    elif (query[3] == 'SHOE' and (float(query[4])-int(float(query[4])))==0) :
                        inventory[0][1] += int(query[4])
                        print(query[4])
                    else:
                        print(-1)

                elif query[2] == 'REMOVE':
                    if query[3] == 'SHOE':
                        inventory[0][1] = -1
                        print(1)
                    elif query[3] == 'SHIRT':
                        inventory[1][1] = -1
                        print(1)    
                    else:
                        print(-1)

                elif query[2] == 'GET_QTY':
                    if query[3] == 'SHOE':
                        if inventory[0][1] != -1:
                            print(inventory[0][1])
                        elif inventory[0][1] == -1:
                            print(0)
                    elif query[3] == 'SHIRT':
                        if inventory[1][1] != -1:
                            print(inventory[1][1])
                        elif inventory[1][1] == -1:
                            print(0)
                    else:
                        print(0)

                elif query[2] == 'INCR':
                    if query[3] == 'SHOE':
                        if ((inventory[0][1] > -1) and ((float(query[4])-int(float(query[4])))==0)):
                            inventory[0][1] += int(query[4])
                            print(query[4])
                        #elif (inventory[0][1] == -1):
                            # inventory[0][1] += int(query[4]) + 1
                        #    print(-1)
                        else:
                            print(-1)

                    elif query[3] == 'SHIRT':
                        if ((inventory[0][1] > -1) and ((float(query[4])-int(float(query[4])))==0)):
                            inventory[1][1] += int(query[4])
                            print(query[4])
                        #elif inventory[1][1] == -1:
                            # inventory[1][1] += int(query[4]) + 1
                        #    print(-1)
                        else:
                            print(-1)

                elif query[2] == 'DCR':
                    if query[3] == 'SHOE':
                        #print((float(query[4])-int(float(query[4])))==0,(int(inventory[0][1]) >=int(query[4])),int(inventory[0][1]),int(query[4]))
                        if (((float(query[4])-int(float(query[4])))==0) and (int(inventory[0][1]) >=int(query[4]))) :
                            inventory[0][1] -= int(query[4])
                            #if inventory[0][1] > -1:
                            print(query[4])
                        #elif inventory[0][1] == -1:
                            # inventory[0][1] += int(query[4]) + 1
                        #    print(-1)
                        else:
                            print(-1)

                    elif query[3] == 'SHIRT':
                        #print((float(query[4])-int(float(query[4])))==0,(int(inventory[1][1]) >=int(query[4])),int(inventory[1][1]),int(query[4]))
                        if (((float(query[4])-int(float(query[4])))==0) and (int(inventory[0][1]) >=int(query[4]))) :
                            inventory[1][1] -= int(query[4])
                            #if inventory[1][1] > -1:
                            print(query[4])
                        #elif inventory[1][1] == -1:
                            # inventory[1][1] += int(query[4]) + 1
                        #    print(-1)
                        else:
                            print(-1)
                elif query[2] == 'SET_COST':
                    if query[3] == 'SHOE':
                        inventory[0][2] = int(query[4])
                        print(float(query[4]))
                    elif query[3] == 'SHIRT':
                        inventory[1][2] = int(query[4])
                        print(float(query[4]))                    
                    else:
                        print(-1)
        
            elif query[1] == 'S':
                qty = 0
                if query[2] == 'ADD':
                    if query[3] == 'SHIRT':
                        cart[1][1] += int(query[4])
                        inventory[1][1] -= int(query[4])
                        qty = int(query[4])
                        print(query[4])
                    elif query[3] == 'SHOE':
                        cart[0][1] += int(query[4])
                        inventory[0][1] -= int(query[4])
                        print(query[4])
                    else:
                        print(-1)

                elif query[2] == 'REMOVE':
                    if query[3] == 'SHOE':
                        cart[0][1] = -1
                        inventory[0][1] += qty
                        print(1)
                    elif query[3] == 'SHIRT':
                        cart[1][1] = -1
                        inventory[1][1] += qty
                        print(1)    
                    else:
                        print(-1)

                elif query[2] == 'INCR':
                    if query[3] == 'SHOE':
                        if cart[0][1] > -1:
                            inventory[0][1] -= int(query[4])
                            cart[0][1] += int(query[4])
                            print(query[4])
                        elif cart[0][1] == -1:
                            # inventory[0][1] += int(query[4]) + 1
                            print(-1)
                        else:
                            print(-1)

                    elif query[3] == 'SHIRT':
                        if cart[1][1] > -1:
                            inventory[1][1] -= int(query[4])
                            cart[1][1] += int(query[4])
                            print(query[4])
                        elif cart[1][1] == -1:
                            # inventory[1][1] += int(query[4]) + 1
                            print(-1)
                        else:
                            print(-1)

                elif query[2] == 'DCR':
                    if query[3] == 'SHOE':
                        if cart[0][1] > -1:
                            inventory[0][1] += int(query[4])
                            cart[0][1] -= int(query[4])
                            if cart[0][1] > -1:
                                print(query[4])
                        elif cart[0][1] == -1:
                            # inventory[0][1] += int(query[4]) + 1
                            print(-1)
                        else:
                            print(-1)

                    elif query[3] == 'SHIRT':
                        if cart[1][1] > -1:
                            inventory[1][1] += int(query[4])
                            cart[1][1] -= int(query[4])
                            if cart[1][1] > -1:
                                print(query[4])
                        elif cart[1][1] == -1:
                            # inventory[1][1] += int(query[4]) + 1
                            print(-1)
                        else:
                            print(-1)
                elif query[2] == 'GET_ORDER_AMOUNT':
                    amt = 0
                    if cart[0][1] or cart[1][1]:
                        if cart[0][1]:
                            amt += cart[0][1]*inventory[0][2]
                        if cart[1][1]:
                            amt += cart[1][1]*inventory[1][2]
                        print(amt)
                    else:
                        print(-1)
            else:
                print(-1)
        else:
            break