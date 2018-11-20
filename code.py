for i in range(100):
  if int(i/3) == i/3 and int(i/5) == i/5:
    print("Fizz Buzz")
  else:
    if int(i/3) == i/3:
      print("Fizz")
    elif int(i/5) == i/5:
      print("Buzz")
    else:
      print(i)
