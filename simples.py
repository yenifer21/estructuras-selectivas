#condiciones simples
from turtledemo.chaos import jumpto

a = 33
b = 200
if b > a:
    print(b,"es mayor que",a)

#doble
e = 200
f = 333
if e > f:
   print(f,"es mayor que",e)
else:
    print(f,"no es mayor que",e)

#condicion multiple
j = 200
k = 207
if j>k:
    print(j,"es mayor que",k)
elif j<k:
    print(j,"es menor que",k)
else:
    print(j,"es igual que",k)

   #condiciones enlazadas
x =28

if x > 10:
    print("por encima de diez,")
    if x < 20:
        print("y tambien por encima de 20!")
    else:
        print("pero no por encima de 20.")

        #parametros s end y sep
        print("estudiar los sabados", end=" ")
        print("es genial")

       # print("estudiar los sabados", end=" ")
       # print("es genial")
#sep

print("daniela","luis","carlos","camila") #agregar un espacio por defecto
print("daniela","luis","carlos","camila",sep="")#quitar el espacio
print("daniela","luis","carlos","camila",sep=",")#agrega una coma

print("daniela","luis","carlos","camila",sep="_",end="-curso_python")#implementacion end y sep
