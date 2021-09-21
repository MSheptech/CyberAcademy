#Sept 2021
#MShep TTA
#Motorbike calculator
##A motorbike costs £2000 and loses 10% of its value every year.
## Print the bike’s value every year until it falls below £1000.##

print ("\n\n\tMotorbike calculator")
print ("your motorbike is worth £2000")
print("It will lose 10% every year")
m_price=2000

new_price = m_price*.9
print(new_price) 

if new_price<=1000:
    print (new_price)
else:
    m_price=new_price
    new_price = m_price*.9
    print(new_price)
    if new_price<=1000:
        print (new_price)
        
    else:
        m_price=new_price
        new_price = m_price*.9
        print(new_price)
        if new_price<=1000:
            quit()
        else:
            m_price=new_price
            new_price = m_price*.9
            print(new_price)
            if new_price<=1000:
                print (new_price)
            else:
                m_price=new_price
                new_price = m_price*.9
                print(new_price)
                if new_price<=1000:
                    print (new_price)
                else:
                    m_price=new_price
                    new_price = m_price*.9
                    print(new_price)
                    if new_price<=1000:
                        print (new_price)
                    else:
                        m_price=new_price
                        new_price = m_price*.9
                        print(new_price)
                        if new_price<=1000:
                            exit()
                            #print (new_price)
                        else:
                            m_price=new_price
                            new_price = m_price*.9
                            print(new_price)



##while m_price>1000:
##  m_price=m_price*.9# times by .9 
##  print("price : £",round(m_price,2)) # use round to 2dp
