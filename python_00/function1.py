def grader(g):
  if (g >= 90):
    print("A")
  elif (g >= 80):
    print("B")
  elif (g >= 70):
    print("C")
  elif (g >= 60):
    print("D")
  else:
    print("F")
# Main
gr = int(input("What is your number grade?"))
grader(gr)