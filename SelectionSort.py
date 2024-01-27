# Selection sort algoritmasında ise dizi şu şekil de sıralanır.
# Once dizi içinde ilk indisli yani 0 indisli eleman dizi içinde 
# minimum olarak kabul edilir daha sonra diğer elemanlar ile bu
# eleman kıyaslanır ve geçici olarak bir değişken oluşturulur
# Eğer bu en küçük olarak varsaydığımız elemandan daha küçük eleman olursa
# Bu geçici olarak tanımladığımız değişkene atanır ve tüm bu dizi bu şekilde taranır
# Sonuç olarak en son en küçük eleman başta en küçük olarak varsaydığımız eleman 
# ile yer değiştirir. Ve bir sonraki adımda artık ilk yani en küçük eleman sıralanmıştır
# Bu sebeple her bir sonraki döngüde en baştan birer eleman atlanır(sıralandığı için) ve daha
# sonra en sondan bir önceki indise kadar geldiğimizde dizimiz sıralnmış olacaktır.

def SelectionSort(array, length):
    for i in range(0, length-1):
        temp_index = -1
        for j in range(i+1, length):
            if (array[i] > array[j]):
                temp_index = j
                array[i], array[temp_index] = array[temp_index], array[i]
        
    
    return array

def main():
    array = [2, 5, -11, 45, 3, 2, 0]
    arrLen = len(array)
    print("Before sort processes: ")
    print(array)
    arrSort = SelectionSort(array=array, length=arrLen)
    print("After sort processes: ")
    print(arrSort)
                
main()
            
        