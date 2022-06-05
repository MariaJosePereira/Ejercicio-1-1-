
# Online Python - IDE, Editor, Compiler, Interpreter
"""Ejercicio 1"""

print("Escuela de Ingeniería de Geología, Minas y Geofísica")
print("******************************************************")


measure=""
days=0
max_with_errors=[]
min_with_errors=[]
max=[]
min=[]
errors=0
errors_bigger_than_100=0
errors_smaller_than_negative_100=0
final_data=[]
media_max=0
media_min=0



while measure!="0,0":
    measure = input("Enter the measure in shape x,y: ")
    
    if "," in measure:
        measureaux=measure.split(",")
        max_day=measureaux[0]
        min_day=measureaux[1]
            
        while measureaux[0]<measureaux[1]:
            
            print('The min measure cannot be bigger than the max measure')
            measure = input("Enter the measure in shape x,y: ")
            measureaux=measure.split(",")
        
        
        if int(max_day)>50 or int(min_day)<0:
            errors+=1
            
            max_with_errors.append(max_day)
            min_with_errors.append(min_day)
            
            if int(max_day)>100:
                errors_bigger_than_100+=1
            elif int(min_day)<-100:
                errors_smaller_than_negative_100+=1
            
            days+=1
        else:
            min.append(min_day)
            max.append(max_day)
            
            max_with_errors.append(max_day)
            min_with_errors.append(min_day)
            days+=1 
    else: measure = input("Enter the measure in shape x,y: ")

for i in range(len(max_with_errors)-1):
    final_data.append(f"days{i+1} max_measure: ({max_with_errors[i]}), min_measure: ({min_with_errors[i]})")

for i in max:
    media_max+=int(i)

for i in min:
    media_min+=int(i)

media_max=media_max/len(max)
media_min=media_min/len(min)

print(final_data,errors)
print('')
print(f'Se tuvieron en total {errors} dias con medidas de error, se midieron {errors_bigger_than_100} errores mayores a 100 y {errors_smaller_than_negative_100} errores menores que -100. ')
print(f'Para un total de {errors_smaller_than_negative_100+errors_bigger_than_100} de errores considerables')
print('')
print(f' La media de las medidas maximas son: {media_max} y la minima: {media_min}')



True or False