
def get_drink_by_profession(param):
    pessoas = {"Jabroni": "Patron Tequila", "School Counselor": "Anything with Alcohol", "Programmer": "Hipster Craft Beer",
    "Bike Gang Member": "Moonshine", "Politician": "Your tax dollars", "Rapper": "Cristal"}

    return pessoas.get (param.title(), "Beer") #O .get vai fazer com que o valor da chave param seja descoberto. Porem, caso ele nao seja encontrado, o valor pre definido é 'Beer'

print (get_drink_by_profession('School Counselor'))