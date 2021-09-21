#Sept 2021
#MShep TTA
#Motorbike calculator
##A motorbike costs £2000 and loses 10% of its value every year.
## Print the bike’s value every year until it falls below £1000.##

print ("\n\n\tMotorbike calculator")
print ("your motorbike is worth £2000")
print("It will lose 10% every year\n")

year =1
m_price=2000

while m_price>1000:
  m_price=m_price*.9 # times by .9 
  print("price after year ",year," : £",round(m_price,2)) # use round to 2dp
  year +=1 #year = year + 1 - adds 1 to the year
