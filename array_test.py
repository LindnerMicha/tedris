import keyboard

field = [0,0,0,0,0,0,0 , 0,0,0,0,0,0,0,0,
         0,0,0,0,0,0,0 , 0,0,0,0,0,0,0,0,
         0,0,0,0,0,0,0 , 0,0,0,0,0,0,0,0,
         0,0,0,0,0,0,0 , 0,0,0,0,0,0,0,0,
         0,0,0,0,0,0,0 , 0,0,0,0,0,0,0,0,
         0,0,0,0,0,0,0 , 0,0,0,0,0,0,0,0,
         0,0,0,0,0,0,0 , 0,0,0,0,0,0,0,0,
         0,0,0,0,0,0,0 , 0,0,0,0,0,0,0,0,
         0,0,0,0,0,0,0 , 0,0,0,0,0,0,0,0,
         0,0,0,0,0,0,0 , 0,0,0,0,0,0,0,0,
         0,0,0,0,0,0,0 , 0,0,0,0,0,0,0,0,
         0,0,0,0,0,0,0 , 0,0,0,0,0,0,0,0,
         0,0,0,0,0,0,0 , 0,0,0,0,0,0,0,0,
         0,0,0,0,0,0,0 , 0,0,0,0,0,0,0,0]  # 15
         #13

z_shape =   [0,0,0,0,0,0,1 , 1 ,0,0,0,0,0,0,0,
             0,0,0,0,0,0,0 , 1 ,0,0,0,0,0,0,0,
             0,0,0,0,0,0,0 , 1 ,1,0,0,0,0,0,0,
             0,0,0,0,0,0,0 , 0 ,0,0,0,0,0,0,0,
             0,0,0,0,0,0,0 , 0 ,0,0,0,0,0,0,0,
             0,0,0,0,0,0,0 , 0 ,0,0,0,0,0,0,0,
             0,0,0,0,0,0,0 , 0 ,0,0,0,0,0,0,0,
             0,0,0,0,0,0,0 , 0 ,0,0,0,0,0,0,0,
             0,0,0,0,0,0,0 , 0 ,0,0,0,0,0,0,0,
             0,0,0,0,0,0,0 , 0 ,0,0,0,0,0,0,0,
             0,0,0,0,0,0,0 , 0 ,0,0,0,0,0,0,0,
             0,0,0,0,0,0,0 , 0 ,0,0,0,0,0,0,0,
             0,0,0,0,0,0,0 , 0 ,0,0,0,0,0,0,0,
             0,0,0,0,0,0,0 , 0 ,0,0,0,0,0,0,0]

spawn = 8
temp = 7

for k in range(len(field)):
    for x in range(len(z_shape)):
        if z_shape[x] == 1:
            field[x] = 1


#field.reverse()

i = 0
print(field)
for i in range(len(field)):
    if field[i] == 1 and field[i-15] == 0:
        field[i+15] = 1
        print(i)

while True:
    if keyboard.is_pressed("q"):
        for i in range(len(field)):
            if field[i] == 1 and field[i-15] == 0:
                field[i+15] = 1
                print(i)
                #print(z_shape[0])
                #print(field)

                #region
                p_temp = 0
                print(f"{field[p_temp]}{field[p_temp+1]}{field[p_temp+2]}{field[p_temp+3]}{field[p_temp+4]}{field[p_temp+5]}{field[p_temp+6]}{field[p_temp+7]}{field[p_temp+8]}{field[p_temp+9]}{field[p_temp+10]}{field[p_temp+11]}{field[p_temp+12]}{field[p_temp+13]}{field[p_temp+14]}")
                p_temp +=15
                print(f"{field[p_temp]}{field[p_temp+1]}{field[p_temp+2]}{field[p_temp+3]}{field[p_temp+4]}{field[p_temp+5]}{field[p_temp+6]}{field[p_temp+7]}{field[p_temp+8]}{field[p_temp+9]}{field[p_temp+10]}{field[p_temp+11]}{field[p_temp+12]}{field[p_temp+13]}{field[p_temp+14]}")
                p_temp +=15
                print(f"{field[p_temp]}{field[p_temp+1]}{field[p_temp+2]}{field[p_temp+3]}{field[p_temp+4]}{field[p_temp+5]}{field[p_temp+6]}{field[p_temp+7]}{field[p_temp+8]}{field[p_temp+9]}{field[p_temp+10]}{field[p_temp+11]}{field[p_temp+12]}{field[p_temp+13]}{field[p_temp+14]}")
                p_temp +=15
                print(f"{field[p_temp]}{field[p_temp+1]}{field[p_temp+2]}{field[p_temp+3]}{field[p_temp+4]}{field[p_temp+5]}{field[p_temp+6]}{field[p_temp+7]}{field[p_temp+8]}{field[p_temp+9]}{field[p_temp+10]}{field[p_temp+11]}{field[p_temp+12]}{field[p_temp+13]}{field[p_temp+14]}")
                p_temp +=15
                print(f"{field[p_temp]}{field[p_temp+1]}{field[p_temp+2]}{field[p_temp+3]}{field[p_temp+4]}{field[p_temp+5]}{field[p_temp+6]}{field[p_temp+7]}{field[p_temp+8]}{field[p_temp+9]}{field[p_temp+10]}{field[p_temp+11]}{field[p_temp+12]}{field[p_temp+13]}{field[p_temp+14]}")
                p_temp +=15
                print(f"{field[p_temp]}{field[p_temp+1]}{field[p_temp+2]}{field[p_temp+3]}{field[p_temp+4]}{field[p_temp+5]}{field[p_temp+6]}{field[p_temp+7]}{field[p_temp+8]}{field[p_temp+9]}{field[p_temp+10]}{field[p_temp+11]}{field[p_temp+12]}{field[p_temp+13]}{field[p_temp+14]}")
                p_temp +=15
                print(f"{field[p_temp]}{field[p_temp+1]}{field[p_temp+2]}{field[p_temp+3]}{field[p_temp+4]}{field[p_temp+5]}{field[p_temp+6]}{field[p_temp+7]}{field[p_temp+8]}{field[p_temp+9]}{field[p_temp+10]}{field[p_temp+11]}{field[p_temp+12]}{field[p_temp+13]}{field[p_temp+14]}")
                p_temp +=15
                print(f"{field[p_temp]}{field[p_temp+1]}{field[p_temp+2]}{field[p_temp+3]}{field[p_temp+4]}{field[p_temp+5]}{field[p_temp+6]}{field[p_temp+7]}{field[p_temp+8]}{field[p_temp+9]}{field[p_temp+10]}{field[p_temp+11]}{field[p_temp+12]}{field[p_temp+13]}{field[p_temp+14]}")
                p_temp +=15
                print(f"{field[p_temp]}{field[p_temp+1]}{field[p_temp+2]}{field[p_temp+3]}{field[p_temp+4]}{field[p_temp+5]}{field[p_temp+6]}{field[p_temp+7]}{field[p_temp+8]}{field[p_temp+9]}{field[p_temp+10]}{field[p_temp+11]}{field[p_temp+12]}{field[p_temp+13]}{field[p_temp+14]}")
                p_temp +=15
                print(f"{field[p_temp]}{field[p_temp+1]}{field[p_temp+2]}{field[p_temp+3]}{field[p_temp+4]}{field[p_temp+5]}{field[p_temp+6]}{field[p_temp+7]}{field[p_temp+8]}{field[p_temp+9]}{field[p_temp+10]}{field[p_temp+11]}{field[p_temp+12]}{field[p_temp+13]}{field[p_temp+14]}")
                p_temp +=15
                print(f"{field[p_temp]}{field[p_temp+1]}{field[p_temp+2]}{field[p_temp+3]}{field[p_temp+4]}{field[p_temp+5]}{field[p_temp+6]}{field[p_temp+7]}{field[p_temp+8]}{field[p_temp+9]}{field[p_temp+10]}{field[p_temp+11]}{field[p_temp+12]}{field[p_temp+13]}{field[p_temp+14]}")
                p_temp +=15
                print(f"{field[p_temp]}{field[p_temp+1]}{field[p_temp+2]}{field[p_temp+3]}{field[p_temp+4]}{field[p_temp+5]}{field[p_temp+6]}{field[p_temp+7]}{field[p_temp+8]}{field[p_temp+9]}{field[p_temp+10]}{field[p_temp+11]}{field[p_temp+12]}{field[p_temp+13]}{field[p_temp+14]}")
                p_temp +=15
                print(f"{field[p_temp]}{field[p_temp+1]}{field[p_temp+2]}{field[p_temp+3]}{field[p_temp+4]}{field[p_temp+5]}{field[p_temp+6]}{field[p_temp+7]}{field[p_temp+8]}{field[p_temp+9]}{field[p_temp+10]}{field[p_temp+11]}{field[p_temp+12]}{field[p_temp+13]}{field[p_temp+14]}")
                p_temp +=15
                print(f"{field[p_temp]}{field[p_temp+1]}{field[p_temp+2]}{field[p_temp+3]}{field[p_temp+4]}{field[p_temp+5]}{field[p_temp+6]}{field[p_temp+7]}{field[p_temp+8]}{field[p_temp+9]}{field[p_temp+10]}{field[p_temp+11]}{field[p_temp+12]}{field[p_temp+13]}{field[p_temp+14]}")
                p_temp +=15
                #endregion -> Ausgabe
