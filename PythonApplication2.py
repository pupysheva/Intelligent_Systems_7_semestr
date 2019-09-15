class Neuron:
    def __init__(self,ind,weight_mass):#Массив весов включает w11,w21,...,T
        self.ind = ind
        self.weight_mass = weight_mass
    def modification_w(self, obraz):
        for i in range(len(self.weight_mass)):
            if i==len(self.weight_mass)-1:
                temp = self.weight_mass[i]
                self.weight_mass[i] = temp-obraz[1][self.ind]
            else:
                temp = self.weight_mass[i]
                self.weight_mass[i] = temp+obraz[0][i]*obraz[1][self.ind]###
    def printer(self):
        print(self.ind, self.weight_mass)
    def threshold_function(self,net):
        if net>0:
            return 1
        else:
            return -1
    def NET_OUT(self,obraz):
        #summing block (NET output)
        ws = self.weight_mass
        net = 0
        for i in range(len(obraz[0])):
            net += ws[i]*obraz[0][i]
        return self.threshold_function(net)
 
#Initialization of weights by random values ​​close to 0
#10 neurons
N = 15 
list_neurons=[]
for i in range(0,10):
    list_neurons.append(Neuron(i,[0]*(N+1)))
#List of image
list_obr =[]
obraz0 = [[1,1,1,1,-1,1,1,-1,1,1,-1,1,1,1,1,-1],[1,-1,-1,-1,-1,-1,-1,-1,-1,-1]]; list_obr.append(obraz0)
obraz1 = [[1,-1,-1,-1,1,1,1,-1,1,-1,-1,1,1,-1,-1,-1],[-1,1,-1,-1,-1,-1,-1,-1,-1,-1]]; list_obr.append(obraz1)#цифра 1, последний элемент - дополнительный параметр 
obraz2 = [[1,1,1,-1,-1,1,-1,1,-1,1,-1,-1,1,1,1,-1],[-1,-1,1,-1,-1,-1,-1,-1,-1,-1]];list_obr.append(obraz2)
obraz3 = [[1,1,1,-1,-1,1,1,1,1,-1,-1,1,1,1,1,-1],[-1,-1,-1,1,-1,-1,-1,-1,-1,-1]];list_obr.append(obraz3)
obraz4 = [[1,-1,1,1,-1,1,1,1,1,-1,-1,1,1,-1,-1,-1],[-1,-1,-1,-1,1,-1,-1,-1,-1,-1]];list_obr.append(obraz4)
obraz5 = [[1,1,1,1,-1,-1,1,1,1,-1,-1,1,1,1,1,-1],[-1,-1,-1,-1,-1,1,-1,-1,-1,-1]];list_obr.append(obraz5)
obraz6 = [[1,1,1,1,-1,-1,1,1,1,1,-1,1,1,1,1,-1],[-1,-1,-1,-1,-1,-1,1,-1,-1,-1]];list_obr.append(obraz6)
obraz7 = [[1,1,1,-1,-1,1,1,-1,-1,-1,1,-1,-1,-1,1,-1],[-1,-1,-1,-1,-1,-1,-1,1,-1,-1]];list_obr.append(obraz7)
obraz8 = [[1,1,1,1,-1,1,1,1,1,1,-1,1,1,1,1,-1],[-1,-1,-1,-1,-1,-1,-1,-1,1,-1]];list_obr.append(obraz8)
obraz9 = [[1,1,1,1,-1,1,1,1,1,-1,-1,1,1,1,1,-1],[-1,-1,-1,-1,-1,-1,-1,-1,-1,1]];list_obr.append(obraz9)
flag = True

#for indNer in range(len(list_nerons)):
for temp in range(20):
    for indNer in range(len(list_neurons)):
        for ob in list_obr:
            if(list_neurons[indNer].NET_OUT(ob)!=ob[1][indNer]):
                list_neurons[indNer].modification_w(ob)
                list_neurons[indNer].printer()
for j in list_neurons:
    print("NERON")
    j.printer()
    print("\n")

print(end = '\t')
for j in range(len(list_neurons)):
    print("Н: {0}".format(j),end = '\t')
print()
for j in list_neurons:# строка это образ
    print("ОБРАЗ: ",end = '\t')
    for c in list_obr:
        print(j.NET_OUT(c),end = '\t')
    print('\n')

test_obraz = test_obraz =  [[1,-1,1,-1,1,1,1,-1,1,-1,-1,1,1,-1,1,-1],[-1,1,-1,-1,-1,-1,-1,-1,-1,-1]]#больше похоже на 1
for ner in range(len(list_neurons)):
    result = list_neurons[ner].NET_OUT(test_obraz)
    print("Результат: ", str(ner) if result == 1 else str(False))