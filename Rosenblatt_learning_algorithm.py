class Neuron:
    def __init__(self,name,ind,weight_mass,e):#Массив весов включает w11,w21,...,T
        self.name = name
        self.ind = ind
        self.weight_mass = weight_mass
        self.e = e
    def modification_w(self, obraz,a):
        for i in range(len(self.weight_mass)):
            temp = self.weight_mass[i]
            self.weight_mass[i] = temp+a*(self.e)*obraz[0][i]
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
        for i in range(len(self.weight_mass)):
            net += ws[i]*obraz[0][i]
        return self.threshold_function(net)


NEURON_COUNT = 8
list_name_neurons = ['П','Б','Г','Е','О','Р','С','Т']
N = 15
alpha = 1
error = 0
list_neurons=[]
for i in range(0,NEURON_COUNT):
    list_neurons.append(Neuron(list_name_neurons[i],i,[0]*(N+1),0))
#List of image
list_obr =[]
obrazP = [[1,1,1,1,-1,1,1,-1,1,1,-1,1,1,-1,1,-1],[1,-1,-1,-1,-1,-1,-1,-1]]; list_obr.append(obrazP)# x1,x2,...,x16,  X0 = -1
obrazB = [[1,1,1,1,-1,-1,1,1,1,1,-1,1,1,1,1,-1],[-1,1,-1,-1,-1,-1,-1,-1]]; list_obr.append(obrazB)# x1,x2,...,x16,  X0 = -1

obrazG = [[1,1,1,1,-1,-1,-1,-1,1,1,-1,-1,-1,-1,1,-1],[-1,-1,1,-1,-1,-1,-1,-1]]; list_obr.append(obrazG)# x1,x2,...,x16,  X0 = -1
obrazE = [[1,1,1,1,-1,-1,1,1,1,1,-1,-1,1,1,1,-1],[-1,-1,-1,1,-1,-1,-1,-1]]; list_obr.append(obrazE)# x1,x2,...,x16,  X0 = -1

obrazO = [[1,1,1,1,-1,1,1,-1,1,1,-1,1,1,1,1,-1],[-1,-1,-1,-1,1,-1,-1,-1]]; list_obr.append(obrazO)# x1,x2,...,x16,  X0 = -1
obrazR = [[1,1,1,1,-1,1,1,1,1,1,-1,-1,-1,-1,1,-1],[-1,-1,-1,-1,-1,1,-1,-1]]; list_obr.append(obrazR)# x1,x2,...,x16,  X0 = -1

obrazC = [[1,1,1,1,-1,-1,-1,-1,1,1,-1,-1,1,1,1,-1],[-1,-1,-1,-1,-1,-1,1,-1]]; list_obr.append(obrazC)# x1,x2,...,x16,  X0 = -1
obrazT = [[1,1,1,-1,1,-1,-1,1,-1,-1,1,-1,-1,1,-1,-1],[-1,-1,-1,-1,-1,-1,-1,1]]; list_obr.append(obrazT)# x1,x2,...,x16,  X0 = -1


#for u in range(4):
#    for ob in list_obr:
#        f = True
#        while f:
#            f=False
#            for indNer in range(len(list_neurons)):
#                out = list_neurons[indNer].NET_OUT(ob)
#                e[indNer] = ob[1][indNer] - out;
#                list_neurons[indNer].e = e[indNer]
#                list_neurons[indNer].modification_w(ob,alpha)
#                if e[indNer]>error:
#                    f = True
e=[0]*NEURON_COUNT           
for indNer in range(len(list_neurons)):
        f = True
        while f:
            f=False
            for  ob in list_obr:
                out = list_neurons[indNer].NET_OUT(ob)
                e[indNer] = ob[1][indNer] - out;
                list_neurons[indNer].e = e[indNer]
                list_neurons[indNer].modification_w(ob,alpha)
                if e[indNer]>error:
                    f = True

print("Номер нейрона и веса:")
for i in list_neurons:
    i.printer()

print("\nРаспознание образов:")
print(end = '\t')
for j in range(len(list_neurons)):
    print("Н: {0}".format(j),end = '\t')
print()
for j in list_neurons:# строка это образ
    print("ОБРАЗ: ",end = '\t')
    for c in list_obr:
        print(j.NET_OUT(c),end = '\t')
    print('\n')

test_obraz =  [[1,1,1,-1,1,-1,-1,1,-1,-1,1,-1,-1,1,-1,-1],[-1,-1,-1,-1,-1,-1,-1,1]]; #Похоже больше на T (как I)
for ner in range(len(list_neurons)):
    result = list_neurons[ner].NET_OUT(test_obraz)
    print("Результат ", list_neurons[ner].name, ':\t',str(True) if result == 1 else str(False))