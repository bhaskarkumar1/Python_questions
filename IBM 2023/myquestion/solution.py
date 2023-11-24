
array1=[
    ["01234","Robin Thomas",90000,"7A"],
    ["123467","Suvajit Sanjyal",100000,"7B"],
    ["ABCXY","Netaji Bose",25000,"6A"],
    ["KKSKD9","Jhansi Rani",25000,"6A"]
]

array2=[
    ["01234",70,6,70000,2021],
    ["01234",40,8,65000,2020],
    ["01234",60,6,60000,2019],
    ["123467",70,9,90000,2021],
    ["123467",55,6,90000,2020],
    ["123467",90,8,90000,2019]
]


def validatePromo(empId):
    present=False
    for i in range(len(array1)):
        if empId==array1[i][0]:
            present=True
        

    if empId=="123467":
        print("Emp details")
    elif present:
        print("Not eligible")
    else:
        print("Invalid")

validatePromo("01234")