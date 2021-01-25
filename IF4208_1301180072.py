'''
Luqman Haries - 1301180072 - IF4208

Flow
1. import semua data Diabetes.csv kedalam variable

2.1 pembagian data ke 1 - 613 sebagai testing set
2.2 pembagian data ke 1 - 461 dan , 642 - 768 sebagai training set dan yang lain sebagai testing set
2.3 pembagian data ke 1 - 307 dan , 462 - 768 sebagai training set dan yang lain sebagai testing set
2.4 pembagian data ke 1 - 154, dan 308 - 768 sebagai training set dan yang lain sebagai testing set
2.5 pembagian data ke 155 - 768 sebagai training set dan yang lain sebagai testing set

3. masukkan data dari 2.x ke perhitungan ukuran jarak
4. masukkan data dari 2.x ke prapemproses data
5. lakukan klasifikasi kNN dari data 2.x 
6. cari nilai K terbaik dari data 2.x dan simpan
7. hitung rata-rata akurasi kNN (5-fold cross validation)

8. outputkan nilai K terbaik dan akurasi kNN
'''
import pandas as pd

#read file
data = pd.read_csv('Diabetes.csv') #path cvs

x1 = data['Pregnancies'].values
x2 = data['Glucose'].values
x3 = data['BloodPressure'].values
x4 = data['SkinThickness'].values
x5 = data['Insulin'].values
x6 = data['BMI'].values
x7 = data['DiabetesPedigreeFunction'].values
x8 = data['Age'].values
outcome = data['Outcome'].values

#createobjek
class x:
    def __init__(self):
        self.x1 = x1[i]
        self.x2 = x2[i]
        self.x3 = x3[i]
        self.x4 = x4[i]
        self.x5 = x5[i]
        self.x6 = x6[i]
        self.x7 = x7[i]
        self.x8 = x8[i]
        self.outcome = outcome[i]

class dataSet:
    def __init__(self):
        self.trainingSet = []
        self.testingSet = []

#Manhattan Distance titik a dan b
def manDistance(a,b):
    return (abs(a.x1 - b.x1) + abs(a.x2 - b.x2) + abs(a.x3 - b.x3) + abs(a.x4 - b.x4) + abs(a.x5 - b.x5) + abs(a.x6 - b.x6) + abs(a.x7 - b.x7) + abs(a.x8 - b.x8))

#klasifikasi K
def klasifikasi(k, distance, x):
    xNearest = []
    posNearest = []
    negNearest = []
    for i in distance[:k]:
        xNearest.append(i[1])
        if listData[i[1]].outcome == 1:
            posNearest.append(i[1]) 
        else: 
            negNearest.append(i[1])

    projection = None
    if len(posNearest) > len(negNearest) : 
        projection = 1  
    else: 
        projection = 0

    if projection == listData[x].outcome: 
        return True
    else:
        return False

#praproses menghitung distance dan menyimpan dalam list
def praProcess(k, train, x):
    distance = list()
    for i in train:
        if i+1 == train[-1]:
            break
        distance.append([manDistance(listData[x],listData[i]),i])
    distance.sort()

    return (klasifikasi(k, distance,x))

#fivefold
def fiveFold(listOfdataset,i,k):
    test = listOfdataset[i].testingSet
    train = listOfdataset[i].trainingSet

    success = []
    fail = []

    for i in test:
        if i+1 == test[-1]:
            break
        if praProcess(k,train,i):
            success.append(i)
        else:
            fail.append(i)
    accuracy = ( len(success) / len(test) )
    result.append(accuracy)
    print('rata-rata akurasi ', sum(result) / len(test))
    return(accuracy)

##################### MAIN ######################
i = 0
listData = []
while i <= (len(data) - 1):
    titik = x()
    listData.append(titik)
    i = i + 1
#print(listData[0].x1,listData[0].outcome)

#list of dataset, panjang 5
listOfdataset = []

#dataset1
dSet = dataSet()

i = 0
while i <= 614:  
    dSet.trainingSet.append(i)
    i = i + 1   

i = 615
while i <= len(data):
    dSet.testingSet.append(i)
    i = i + 1

listOfdataset.append(dSet)
dSet = None

#dataset2
dSet = dataSet()

i = 0
while i <= 461:  
    dSet.trainingSet.append(i)
    i = i + 1   

i = 645
while i <= 768:  
    dSet.trainingSet.append(i)
    i = i + 1

i = 462
while i <= 641:  
    dSet.testingSet.append(i)
    i = i + 1   
listOfdataset.append(dSet)
dSet = None

#dataset3
dSet = dataSet()

i = 0
while i <= 307:  
    dSet.trainingSet.append(i)
    i = i + 1

i = 462
while i <= 768:  
    dSet.trainingSet.append(i)
    i = i + 1

i = 308
while i <= 461:  
    dSet.testingSet.append(i)
    i = i + 1

listOfdataset.append(dSet)
dSet = None

#dataset4
dSet = dataSet()

i = 0
while i <= 154:  
    dSet.trainingSet.append(i)
    i = i + 1

i = 308
while i <= 768:  
    dSet.trainingSet.append(i)
    i = i + 1

i = 155
while i <= 307:  
    dSet.testingSet.append(i)
    i = i + 1

listOfdataset.append(dSet)
dSet = None

#dataset5
dSet = dataSet()

i = 155
while i <= 768:  
    dSet.trainingSet.append(i)
    i = i + 1

i = 0
while i <= 154:  
    dSet.testingSet.append(i)
    i = i + 1

listOfdataset.append(dSet)
dSet = None
result = list()


#print(listOfdataset[0].testingSet[0])
#print(listOfdataset[1].testingSet[0])

#print(manDistance(listData[listOfdataset[0].testingSet[0]],listData[listOfdataset[0].trainingSet[0]]))

k=1
while k <= 5:
    print("############## K = ",k,"##############")

    print('data set ke = 1')
    print('akurasi ',fiveFold(listOfdataset,0,k))
    print()
    print('data set ke = 2')
    print('akurasi ',fiveFold(listOfdataset,1,k))
    print()
    print('data set ke = 3')
    print('akurasi ',fiveFold(listOfdataset,2,k))
    print()
    print('data set ke = 4')
    print('akurasi ',fiveFold(listOfdataset,3,k))
    print()
    print('data set ke = 5')
    print('akurasi ',fiveFold(listOfdataset,4,k))
    print()
    print('result = ', result)
    print()
    k = k + 1
    print()
    
    result.pop()
    result.pop()
    result.pop()
    result.pop()
    result.pop()

