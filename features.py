def linear_search(transaction,target):
  for transaction in transactions :
    if transaction['date']==target:
      return transaction
  return "transaction not found"

def bubble_amount(transactions):
  n=len(transactions)
  for i in range(n):
    for j in range(0,n-1):
      if transactions[j]['amount']>transactions[j+1]['amount']:
        transactions[j],transactions[j+1]=transactions[j+1], transactions[j]
  return transactions

def add_data(transactions):
  date=input('Enter the date:' )
  amount=int(input('Enter the amount:'))
  description=input('Enter the description:')
  a ={'date':date,'amount':amount,'description':description}
  transactions.append(a)
  return transactions

def delete_data(transactions):
  date = input('Enter the date:' )
  b=linear_search(transactions,date)
  transactions.remove(b)
  return transactions

def sum_amount(transactions):
  year=input('enter the year:')
  s=0
  for i in transactions:
    if i['date'][5::]==year:
      s+=i['amount']
  return s
