# def speak():
#     print("Inside the function!")
#     return "Message from return"

# output = speak()
# print("Output is:", output)

def test_numbers(lista):
    new_list = []
    if type(lista)!=list:
        return "No Valid Numbers"
    else:
        for x in lista:
            if x!=int or x!=float:
                return "No Valid Numbers"
            else:
                new_list.append(x*2)
        print(new_list)
        return new_list
        

teste = test_numbers([1,2,"a"])

print(teste)




  
    