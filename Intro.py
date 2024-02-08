''' 
function : A function is a reusable block of code that performs a specific task or set of tasks.
* In function there's mainly two things that is parameter and arguments.
              print vs return.
              
#normal parameters
#default parameters
#default argument
#keyword arguments
'''


def greet():
     print(f'hello,yeonsa')
     greet()

'''
*parameter:
whenever we define a function then we use the parameter and 
*argument:
whenever we call the function then we use arguments.

'''

def dear(name):
     print(f'Hello! How are you doing? Ah, I just missed you, {name}. 😔')
     dear('yeonsa')

def hello(a,b,c,d = 40): # normal and default parameter
     print(a+b+c+d)
hello(10,20,30,60) 

def hi(e,f,g,h =30):
    print(f)  
hi(f = 10,g = 45, e =56 )    
def evenodd(a):
  if a%2 == 0:
      print('even') 
  else:
       print('odd')
evenodd(12)   

''' print v return  '''    

def food(pizza, samosa, biryani):
    if pizza == True:
        return 'best food'
    else:
        return 'worst food'

result = food(True, False, False)  # Passing values for all three parameters
print(result)  
 
