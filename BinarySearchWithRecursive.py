# Binary search algoritamsı, bir sıralanmış dizide yani sort yöntemlerini
# kullanılarak sıralanmış veya bize sıralı olarak verilmiş bir dizideki istediğimiz
# bir elemanın tam olarak hangi indiste olduğunu bize döndürür. Bunu yaparken şu
# algoritmik adımları izler: Once dizinin minimum ve max indisleri alınır ve bu indislerin
# durumuna göre bir while döngüsü kurulur. Döngüde eğer dizi elemanı dizide bulunudysa
# o eleman döndürülerek süreçten çıkarılır ama eğer dizi elemanı bulunamamış ve dizideki
# en küçük indis en büyük indisten büyük olacak duruma gelmişse genelde return -1 yapılır.
# Peki nasıl olacak da en küçük eleman en büyük elemandan büyük duruma gelecek? Bu şundan
# dolayıdır. Her seferinde (en küçük indis + en büyük indis)/2 yani ortanca indis bulunur
# ve eğer ortanca indisdeki değer aradığımız değere eşitse bu indis döndürülür. Ancak eğer
# bu sayı aradığımız sayıdan büyükse  o halde dizinin en büyük indisi değiştirilir ve ortanca indis-1
# olarak ayarlanı neden çünkü aradığımız değer max ortanca indis -1 deki indise eşit olabilir çünkü
# dizi sıralanmış haldedir. Eğer son durum yani ortanca indisdeki değer aradığımız değerden küçükse bu
# durumda minimum indise ortanca +1 indisi atanır ve böylece bu durum sayı bulununcaya veya küçük
# indis büyük indisi geçinceye kadar devam eder.

# Bu arama algoritmasını rekursif fonksiyon ile uygulamak istiyorum. Peki nedir rekursif fonksiyon?
# Rekursif fonksiyon ise dizi içinde alt dizilerin bulunması ve bu dizilerden kaç tane daha alt dizi var
# ve bunların boyutları nedir eğer bu tarz bilinmezlikleri varsa diğer bir değişli durumun derinliği
# bilinmiyorsa bu nokta de rekursif ile farklı derinlikteki noktalara fonksiyonu kendi içinde tekrar
# tekrar çağırarak bu yapıyı çözmeye çalışırız.
#Good

def BinarySearch(array, wanned, higher, lower):
    if(lower > higher):
        return -1
    else:
        mean = (higher + lower) // 2
        if(array[mean] == wanned):
            return mean
        elif(array[mean] > wanned):
            return BinarySearch(array, wanned, mean-1, lower)
        else:
            return BinarySearch(array, wanned, higher, mean+1)
            
def main():
    array = [1, 3, 5, 6, 7, 9, 11, 34]
    wanned = 3
    length = len(array)-1
    index = BinarySearch(array, wanned, length, 0)
    print("Index of searching : " + str(index))

# Call main
main()





