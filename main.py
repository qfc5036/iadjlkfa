# Author Qiaoxu Cui qfc5036@psu.edu
# Collaborator Zhili Bu zjh5625@psu.edu
# Collaborator: Shufang Huang sbh5655@psu.edu
# Collaborator: Isabel Vera ikv5018@psu.edu
# Section: 8
# Breakout: 11
def digit_sum(n):
  if n<10:
    return n
  else:
    r = n//10
    m = n%10
    return m+digit_sum(r)

def run():
  n = input ("Enter an int: ")
  n = int(n)
  n1 = digit_sum(n)
  print(f"sum of digits of {n} is {n1}.")

if __name__=="__main__":
  run()