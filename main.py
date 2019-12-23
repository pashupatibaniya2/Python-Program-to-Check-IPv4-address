# Python-Program-to-Check-IPv4-address
#This is the program in python language which help you to check the IPv4 address weather the are valid or not
#usr/env/python3
import sys

def cont():
  print("Do you want to continue ")
  print("Press Y/N to continue and exit respectively")
  inputchar=input()
  if(inputchar=="Y" or inputchar=="y"):
       switch()
  elif(inputchar=="N" or inputchar=="n"):
       sys.exit()
       

def switch():
    print("-----------------------------------------------------------")
    print("1) Check Class of IPV4 Address")
    print("2) Exit")
    print("-----------------------------------------------------------")
    option = int(input("your option : "))
    if option == 1:
        data = input("Enter the ip address to check its class:")
        octet=data.split(".")
        first_byte=int(octet[0])
        second_byte=int(octet[1])
        third_byte=int(octet[2])
        fourth_byte=int(octet[3])
        if len(str(first_byte))>3 :
            print("Incorrect lenght of  IP in first octet")
            cont()
        elif  len(str(second_byte))>3 :
            print("Incorrect lenght of  IP in second octet")
            cont()
        elif  len(str(third_byte))>3 :
            print("Incorrect lenght of  IP in third octet")
        elif len(str(fourth_byte))>3 :
            print("Incorrect lenght of  IP in fourth octet")
            cont()
        elif (first_byte==0 or first_byte<=127 )and (second_byte==0 or second_byte<=255) and (third_byte==0 or third_byte<=255 )and (fourth_byte==0 or fourth_byte<=255):
                print("Class A IP")
                cont()
        elif (first_byte==128 or first_byte<=191) and (second_byte==0 or second_byte<=255) and( third_byte==0 or third_byte<=255 )and (fourth_byte==0 or fourth_byte<=255):
                print("Class B IP")
                cont()
        elif (first_byte==192 or first_byte<=223 )and (second_byte==0 or second_byte<=255 )and (third_byte==0 or third_byte<=255 )and (fourth_byte==0 or fourth_byte<=255):
                print("Class C IP")
                cont()
        elif  (first_byte==224 or first_byte<=239 )and (second_byte==0 or second_byte<=255) and (third_byte==0 or third_byte<=255 )and (fourth_byte==0 or fourth_byte<=255):
                print("Class D IP")
                cont()
        elif (first_byte==240 or first_byte<=255 )and (second_byte==0 or second_byte<=255 )and (third_byte==0 or third_byte<=255 )and (fourth_byte==0 or fourth_byte<=255):
                print("Class E IP")
                cont()
        else:
                print("Invalid IP")
                cont()
        
    elif option == 2:
                print("Exit")
   
      

switch()
