def insert_user_in_db(name,age):
  print(f'user inserted in db name {name} age {age}')
print (insert_user_in_db("Shakib",30))

# tax calculation
def calculateTax(amount,state):
  tax_rate = 0.5
  if(state=='TX'):
    tax_rate=1.00
  elif state=='CA':
    tax_rate=1.50
  return amount*tax_rate

print(f'customer of chicago tax: ${calculateTax(1000,'CH'):.2f}')

# there is lambda/anonimus function
double_num_lambda = lambda num:num*2

print(double_num_lambda(3))