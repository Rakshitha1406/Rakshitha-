# Combining the feature into application
from features import add_data,linear_search,bubble_amount,delete_data,sum_amount

#List of dict in variable
transactions =[ {"date":'29-8-2024',"amount":200,"description":'Ice cream'},
               {"date":'6-4-2008',"amount":500,"description":'cake'},
               {"date":'20-6-1986',"amount":600,"description":'chocolates' },
               {"date":'4-5-2024',"amount":300,"description":"dress"},
               ]

flag=True
while flag:
  R=int(input('Enter the number which function should run:'))
  if R==1: 
    print(add_data(transactions)) 
  elif R==2:
    target=input('Enter the date:')
    print(linear_search(transactions,target))
  elif R==3:
    print(bubble_amount(transactions))
  elif R==4:
    print(delete_data(transactions))
  elif R==5:
    print('Display:',transactions)
  elif R==6:
    flag=False
    print('the program is stopped')
  elif R==7:
    print(sum_amount(transactions))
  else:
    print('Enter the right choice')
  
    
       
    
