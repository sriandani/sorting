data=[ 19, 6, 20, 5, 9, 12, 24, 2, 8, 18]
print("data sebelum diurutkan:",data)
banyak_data= len(data)
for i in range(banyak_data-1):
    for j in range(banyak_data-1):
        if data[j]>data[j+1]:
            temp=data[j]
            data[j]=data[j+1]
            data[j+1]=temp
print(data,"data setelah diurutan")
