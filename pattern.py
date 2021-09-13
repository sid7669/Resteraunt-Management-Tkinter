# def pt(n):
#     for i in range(0,n):
#         for j in range(1,i+1):
#             print(" ",end="")
#         for j in range(0,n):
#             print("*",end="")    
#         print()    
# pt(5)        

def pt(n):
    for i in range(0,n+1):
        for j in range(1,i+1):
            print(" ",end="")

        for j in range(i+1,n+2):
            print("*",end="")
        print()    
pt(5)  
