chenn = "A badio dany"
l = []
l.append(chenn)
endeks = 0
print("\n")

for i in range(len(chenn)):
    if l[0][i] == 'a' or l[0][i] == 'A':
        print("let twouve: ",l[0][i] ,"endeks: ",i)
        endeks += i
    
print(f"\nTotal endeks lan bay: {endeks}\n")