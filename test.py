
def fast_modular(a, n): #a % n
  a_return=a
  while(a_return>=n):           #for modular
    n_factor=n
    while(n_factor*2<a_return): #for calculate quickly
      n_factor*=2
    a_return-=n_factor
  return (a_return)

def fast_factor_in_modular(num, e, N):
  num_return=num
  e_tmp=0
  return_val=1
  while(e_tmp!=e):           # for exponential function
    e_factor=1
    num_factor=num
    while(e_factor*2+e_tmp<e): #for calculate quickly
      e_factor*=2
      num_factor*=num_factor
    e_tmp+=e_factor
    return_val*=num_factor
    return_val=fast_modular(return_val,N)
  return (return_val)

def is_coprime(num1, num2):
  if(num1 > num2): #for sorting number - num1 > num2
    num=num1
    num1=num2
    num2=num
  while(num1!=0):
    num1_tmp = fast_modular(num2,num1) #num2%num1
    num2=num1
    num1=num1_tmp
  return_val=num2==1 #does it have same factor?
  return(return_val)

def is_prime(N):
  return_val=True
  test_val=2
  while(test_val*test_val<=N):
    if(fast_modular(N,test_val)==0):
      return_val=False
      break
    test_val+=1
  return(return_val)

def next_prime(N):
  return_val=N+1
  while(is_prime(return_val)==False):
    return_val+=1
  return(return_val)

def find_key(e, Euler_PI_N):
  d=0
  e_result=0
  while(e_result!=1):
    d_adder=1
    e_next_factor=e_result+e*d_adder
    while(e_next_factor<=Euler_PI_N):
      d_adder+=1
      e_next_factor+=e
    e_result = fast_modular(e_next_factor,Euler_PI_N)
    #print(e_next_factor,e_result,d_adder)

    d+=d_adder

  return(d)

"""
RSA Algorithm
"""

#generate prime number and N
p = next_prime(0x20)
q = next_prime(0x30)
N = p*q

#generate key pair
e = 0x11
Euler_PI_N=(p-1)*(q-1)
d=find_key(e,Euler_PI_N)

# the example of RSA data transfer
M = 123
C = fast_factor_in_modular(M, e, N)
C_to_M = fast_factor_in_modular(C,d,N)

# for print
print("plain text = "+str(M))
print("crypto text = "+str(C))
print("decrypto text = "+str(C_to_M))

