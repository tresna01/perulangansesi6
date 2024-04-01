length = 5
for i in range (5):
    for j in range (length):
         if i % 2 == 0 :
             if j %2 == 0:
                 print ("S", end = " ")
             else :
                 print ("O", end =" ")
         else:
            if j %2 == 1:
                 print ("S", end =" ")
            else :
                 print ("O", end =" ")
                 
    length -= 1
    print () 