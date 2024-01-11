def print_fibonacci(length):
   my_data=[]
   for i in range(length):
      if i == 0:
         my_data.append(0)
      elif i == 1:
         my_data.append(1)
      else:
         next_number = my_data[-1] + my_data[-2]
         my_data.append(next_number)
         
   print(my_data)
   
print_fibonacci(20)