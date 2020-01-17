# friends = ["Roly", "Saino","Ketty","Nicolle", "Ursula","Kevin"]
# for index in range(len(friends)) : 
#     print(friends[index])

# for index in range(5):
#     if index == 0 : 
#         print("first iteration")
#     else:
#         print("Not first")

def raise_to_power(base_num, pow_num):
    result = 1 
    for index in range(pow_num):
        result= result * base_num
    return result

print(raise_to_power(4500,4500))