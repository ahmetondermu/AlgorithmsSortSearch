# Bubble Sort algoritması diziyi dizi eleman saysının bir
# eksiği kadar döner daha ve her seferde ilk elemandan son
# eleman eksi ilk döngü sayısı eksi 1 kadar elemanı ikili
# ikili alarak küçükse daha küçük indisteki sayı sayıların 
# yerini değiştirmez ama eğer küçük indisli sayı daha büyük
# ise bu iki sayı yer değiştirilir. Bu işlemler tekrarlanarak dizi küçükten büyüğe sıralanır.


#Buraya data gönderilir ve datanın direkt kendisi deiştirilir yani pass by value
#Gİbi gözükse de aslında dizinin referansı alınır ve değişim dizi üzerinde yapılır.
def BubbleSort(array, length):
    for i in range(0, length-1):
        for j in range(0, length-i-1):
            if(array[j] > array[j+1]):
                temp = array[j]
                array[j] = array[j+1]
                array[j+1] = temp
    
    return array

def main():
    array = [2, 9, 11, 3, 1, -4, 9, 5]
    arrLen = len(array)
    print("Before sort processes: ")
    print(array)
    arrSort = BubbleSort(array, arrLen)
    print("After sort processes:")
    print(arrSort)
    
# Call main
main()
    

