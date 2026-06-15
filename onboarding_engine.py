name = input('Enter your name: ')
age = int(input('Enter your age: '))


while True:
  
  developer = input('Are you developer(y/N): ').lower().strip()
  if developer in ('y', 'n'):
    break
  print("Invalid choice. Please type 'y' or 'n'.")

if developer=='n':
  developer=False 
else:
  developer=True

if age<18:
  print(f'Tier3: Guest');
elif age>=18 and not developer:
  print(f'Tier 2: Standard Executive Access');
else:
  print(f'Tier 1: Admin Infrastructure Access');




