input("___________________________________________________")
print("       BUSINESS OF RADHEKRISHAN BHAN SAHAB         ")
print(" ADDRESS: MAYBEKNOWS DEEPU JI BANTU JI AND SETH JI \n")
import datetime
x = datetime.datetime.now()
print("DATE AND TIME OF BILL:",x)
input("___________________________________________________")
import uuid
x = 1
Y = id(x)
print("YOUR BILLING ID IS:",Y)
input("___________________________________________________")
n = int(input("HOW MANY ITEMS DO YOU WANT TO ENTER:. . . "))
DIS = {}
for i in range(0,n,1):
    I = input("ENTER ITEM NAME:")
    P = int(input("ENTER ITEM PRICE:"))
    N = int(input("ENTER ITEM QUANTITY:"))
    F = P*N
    T =(P*N)/100*12
    G = T+(P*N)
    input("______________________________________________________")
    print("BILL:",F"\n""GST:",T,"\n""TOTAL BILL:",G,"\n")
    DIS.update({I:G})
    print("YOUR ITEMS:",DIS)
    print("\n","YOUR TOTAL PAYABLE BILL IS:",sum(DIS.values()))
    input("______________________________________________________")
    print("RADHEKRISHAN BHAN SAHAB THANKS YOU FOR YOUR BUSINESS")
    input("______________________________________________________")
    input("R.K.Bhan / SethJi, / Deepuji / Bantuji says please visit again\n")
ST = input("DO YOU WANT TO LOOK INTO YOU STOCK?. . . . . . ")
A = {}
y = 0
n = 1
if ST == 0:
    print("YES I WANT TO LOOK INTO STOCK:")
    if N == N:
        A.update({I:P,I:N-N})
        print(A)
    elif N == 0:
        A.update({I:P,I:N})
        print(A)
elif ST == 1:
    print("YES I WANT TO LOOK INTO STOCK:")and print("EXIT")
