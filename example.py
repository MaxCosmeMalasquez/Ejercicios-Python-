# cuadrados = {1: 1, 2: 4, 3: "error", 4: 16,} 
# cuadrados [8] = 64 
# cuadrados [3] = 9 
# print (cuadrados)
# [
     
# print (",". join (["" spam "," eggs "," ham "])) 
# #prints" spam, eggs, ham " 

# print (" Hello ME ". replace (" ME "," world ")) 
# # imprime "Hola mundo" 

# print ("Esta es una oración". comienza con ("Esto")) 
# # imprime "Verdadero" 

# print ("Esta es una oración". termina con ("oración")) 
# # imprime "Verdadero" " 

# print (" Esta es una oración ". upper ()) 
# # imprime" THIS IS A SENTENCE ". 

# print ("UNA SENTENCIA CON MAYÚSCULAS" . lower ()) 
# # imprime "una oración con mayúsculas"

# def count_char (text, char): 
#   count = 0 
#   para c en text: 
#     if c == char: 
#       count + = 1 
#   return count 

# filename = input ("Ingrese un nombre de archivo:") 
# con open (filename) como f: 
#   text = f .read () 

# para char en "abcdefghijklmnopqrstuvwxyz": 
#   perc = 100 * count_char (text, char) / len (text) 
#   print ("{0} - {1}%". format (char, round (perc, 2)) )



def apply_twice (func, arg): 
   return func (func (arg)) 

def add_five (x): 
   return x + 100 

print (apply_twice (add_five, 10))