import pickle
def write():
    patient=()
    patientfile=open("PATIENT.DAT","ab")
    ans='y'
    while ans=='y':
        PID=int(input("Enter Patient ID:"))
        NAME=input("Enter patient Name:")
        DISEASE=input("Enter disease name:")
        patient=(PID,NAME,DISEASE)
        pickle.dump(patient,patientfile )
        ans=input("Want to enter more records?(y/n)...")
    patientfile.close()

def read():
    count=0
    patientfile=open("PATIENT.DAT","rb")
    print("COVID-19 patient details")
    print(" "*20,"-----------------output------------------")
    print("")
    try:
        while True:
            patient=pickle.load(patientfile)
            if patient[2] in ["COVID-19","covid-19"]:
                print(" "*20,patient)
                count=count+1
           
    except EOFError:
        patientfile.close()
    print("")
    print(" "*20,"---------------END--------------")
    print("")
    print(" "*20,"Total number of COVID-19 patients=",count)
print("1. write")
print("2. read")
ask=input("enter your choice  :  ")
if ask=='1':
    write()
    ans=input("do you want to read data (y\n)  :")
    if ans=='y':
        read()
elif ask=='2':
    read()
    ans=input("do you want to write (y\n)   :")
    if ans=='y':
        write()
else:
    print(" invalid choice")


