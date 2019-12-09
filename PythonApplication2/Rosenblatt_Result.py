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


NEURON_COUNT = 26
list_name_neurons = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
N = 25 #Пикселей
alpha = 1
error = 0
list_neurons=[]
for i in range(0,NEURON_COUNT):
    list_neurons.append(Neuron(list_name_neurons[i],i,[0]*(N+1),0))
#List of image
list_obr =[]
obrazA = [[-1,-1,1,-1,-1,-1,1,-1,1,-1,-1,1,-1,1,-1,-1,1,1,1,-1,-1,1,-1,1,-1,-1],[]]; list_obr.append(obrazA)# x1,x2,...,x25,  X0 = -1
obrazB = [[-1,1,1,1,-1,-1,1,-1,1,-1,-1,1,1,1,-1,-1,1,-1,1,-1,-1,1,1,1,-1,-1],[]]; list_obr.append(obrazB)# x1,x2,...,x25,  X0 = -1
obrazC = [[-1,1,1,1,-1,-1,1,-1,-1,-1,-1,-1,-1,1,-1,-1,1,-1,-1,-1,-1,1,1,1,-1,-1],[]]; list_obr.append(obrazC)# x1,x2,...,x25,  X0 = -1
obrazD = [[-1,-1,1,1,-1,-1,1,-1,1,-1,-1,1,-1,1,-1,-1,1,-1,1,-1,-1,-1,1,1,-1,-1],[]]; list_obr.append(obrazD)# x1,x2,...,x25,  X0 = -1
obrazE = [[-1,1,1,1,-1,-1,1,-1,-1,-1,-1,1,1,1,-1,-1,1,-1,-1,-1,-1,1,1,1,-1,-1],[]]; list_obr.append(obrazE)# x1,x2,...,x25,  X0 = -1
obrazF = [[-1,1,1,1,-1,-1,1,-1,-1,-1,-1,1,1,1,-1,-1,1,-1,-1,-1,-1,-1,-1,1,-1,-1],[]]; list_obr.append(obrazF)# x1,x2,...,x25,  X0 = -1
obrazG = [[-1,1,1,1,1,1,-1,-1,-1,-1,-1,1,1,-1,1,1,-1,-1,1,-1,-1,1,1,1,1,-1],[]]; list_obr.append(obrazG)# x1,x2,...,x25,  X0 = -1
obrazH = [[-1,1,-1,1,-1,-1,1,-1,1,-1,-1,1,1,1,-1,-1,1,-1,1,-1,-1,1,-1,1,-1,-1],[]]; list_obr.append(obrazH)# x1,x2,...,x25,  X0 = -1
obrazI = [[1,1,1,1,1,-1,-1,1,-1,-1,-1,-1,1,-1,-1,-1,-1,1,-1,-1,1,1,1,1,1,-1],[]]; list_obr.append(obrazI)# x1,x2,...,x25,  X0 = -1
obrazJ = [[-1,1,-1,-1,-1,-1,-1,-1,1,-1,-1,1,-1,-1,-1,-1,1,-1,1,-1,-1,1,1,1,-1,-1],[]]; list_obr.append(obrazJ)# x1,x2,...,x25,  X0 = -1
obrazK = [[1,-1,-1,1,-1,-1,1,-1,1,-1,-1,-1,1,1,-1,-1,1,-1,1,-1,1,-1,-1,1,-1,-1],[]]; list_obr.append(obrazK)# x1,x2,...,x25,  X0 = -1
obrazL = [[-1,-1,-1,1,-1,-1,1,-1,-1,-1,-1,-1,-1,1,-1,-1,1,-1,-1,-1,1,1,1,1,-1,-1],[]]; list_obr.append(obrazL)# x1,x2,...,x25,  X0 = -1
obrazM = [[1,-1,-1,-1,1,1,1,-1,1,1,1,-1,1,-1,1,1,-1,-1,-1,1,1,-1,-1,-1,1,-1],[]]; list_obr.append(obrazM)# x1,x2,...,x25,  X0 = -1
obrazN = [[1,-1,-1,-1,1,1,1,-1,-1,1,1,-1,1,-1,1,1,-1,-1,1,1,1,-1,-1,-1,1,-1],[]]; list_obr.append(obrazN)# x1,x2,...,x25,  X0 = -1
obrazO = [[-1,1,1,1,-1,-1,1,-1,1,-1,-1,1,-1,1,-1,-1,1,-1,1,-1,-1,1,1,1,-1,-1],[]]; list_obr.append(obrazO)# x1,x2,...,x25,  X0 = -1
obrazP = [[-1,1,1,1,-1,-1,1,-1,1,-1,-1,1,1,1,-1,-1,1,-1,-1,-1,-1,-1,-1,1,-1,-1],[]]; list_obr.append(obrazP)# x1,x2,...,x25,  X0 = -1
obrazQ = [[-1,1,1,1,1,1,-1,-1,1,-1,-1,1,-1,-1,1,1,-1,1,1,-1,1,1,1,1,1,-1],[]]; list_obr.append(obrazQ)# x1,x2,...,x25,  X0 = -1
obrazR = [[-1,1,1,1,-1,-1,1,-1,1,-1,-1,1,1,1,-1,-1,1,1,-1,-1,-1,1,-1,1,-1,-1],[]]; list_obr.append(obrazR)# x1,x2,...,x25,  X0 = -1
obrazS = [[-1,1,1,1,-1,-1,1,-1,-1,-1,-1,1,1,1,-1,-1,-1,-1,1,-1,-1,1,1,1,-1,-1],[]]; list_obr.append(obrazS)# x1,x2,...,x25,  X0 = -1
obrazT = [[1,1,1,1,1,-1,-1,1,-1,-1,-1,-1,1,-1,-1,-1,-1,1,-1,-1,-1,-1,1,-1,-1,-1],[]]; list_obr.append(obrazT)# x1,x2,...,x25,  X0 = -1
obrazU = [[-1,1,-1,1,-1,-1,1,-1,1,-1,-1,1,-1,1,-1,-1,1,-1,1,-1,-1,1,1,1,-1,-1],[]]; list_obr.append(obrazU)# x1,x2,...,x25,  X0 = -1
obrazV = [[-1,-1,-1,-1,-1,1,-1,-1,-1,1,-1,1,-1,1,-1,-1,1,-1,1,-1,-1,-1,1,-1,-1,-1],[]]; list_obr.append(obrazV)# x1,x2,...,x25,  X0 = -1
obrazW = [[1,-1,-1,-1,1,1,-1,1,-1,1,1,-1,1,-1,1,1,-1,1,-1,1,-1,1,-1,1,-1,-1],[]]; list_obr.append(obrazW)# x1,x2,...,x25,  X0 = -1
obrazX = [[1,-1,-1,-1,1,-1,1,-1,1,-1,-1,-1,1,-1,-1,-1,1,-1,1,-1,1,-1,-1,-1,1,-1],[]]; list_obr.append(obrazX)# x1,x2,...,x25,  X0 = -1
obrazY = [[1,-1,-1,-1,1,-1,1,-1,1,-1,-1,-1,1,-1,-1,-1,-1,1,-1,-1,-1,-1,1,-1,-1,-1],[]]; list_obr.append(obrazY)# x1,x2,...,x25,  X0 = -1
obrazZ = [[1,1,1,1,1,-1,-1,-1,1,-1,-1,-1,1,-1,-1,-1,1,-1,-1,-1,1,1,1,1,1,-1],[]]; list_obr.append(obrazZ)# x1,x2,...,x25,  X0 = -1

for i in range(len(list_obr)):
    for j in range(NEURON_COUNT):
        if i==j:
            list_obr[i][1].append(1)
        else:  list_obr[i][1].append(-1)


e=[0]*NEURON_COUNT    
for i in range(3):
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
print('\t',end = "\t")
for j in range(len(list_neurons)):
    print("{0}".format(j),end = '  ')
print()
for ind_c,c in enumerate(list_obr):# строка это образ
    print("ОБРАЗ ",list_name_neurons[ind_c],":", end = '\t')
    for ind_j,j in enumerate(list_neurons):
        str_ = " "

        if(len(str(ind_j))>1):
            str_ = '   '
        else: str_ = '  '

        if j.NET_OUT(c) == 1:
            print(j.NET_OUT(c),end = str_)
        else:
            print('-',end = str_)
    print('\n')

test_obraz = [[1,1,1,1,1,-1,-1,1,-1,-1,-1,-1,1,-1,-1,-1,-1,1,-1,-1,1,-1,1,-1,-1,-1],[]]; #Like T
for ner in range(len(list_neurons)):
    result = list_neurons[ner].NET_OUT(test_obraz)
    print("Результат ", list_neurons[ner].name, ':\t',str(True) if result == 1 else str(False))
