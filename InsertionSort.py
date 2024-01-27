# Insertion Sort algoritması literatürde sokmalı sıralama
# olarak geçiyor. Burada ilk indisten başlayarak sürekli bir
# sonraki indise kadar elemanları kendi içinde seçip aralara
# büyüklük küçüklük durumlarına göre sıralam işlemi yapar.
# Genellikle while döngüsü kullanılır ve dizi sıralana kadar 
# koşullu bir şekilde döngü devam eder.

def insertionSort(arr):
    """
    Insertion Sort algoritması ile bir diziyi sıralayan fonksiyon.
    
    Argümanlar:
    arr -- sıralanacak dizi
    
    Dönüş:
    None (fonksiyon, dizi üzerinde değişiklik yaparak sıralanmış hale getirir)
    """
    # Dizinin uzunluğunu al
    n = len(arr)

    # Diziyi dolaş
    for i in range(1, n):
        key = arr[i]  # Karşılaştırılacak elemanı key olarak sakla
        j = i - 1

        # Diziyi sondan başa doğru dolaşarak key'den küçük olan elemanları sağa kaydır
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1

        # Eksilen yerde key'i ekle
        arr[j + 1] = key

def main():
    # Diziyi oluştur
    arr = [12, 11, 13, 5, 6]
    
    # Oluşturulan diziyi ekrana yazdır
    print("Orijinal dizi:", arr)

    # Insertion Sort algoritmasını kullanarak diziyi sırala
    insertionSort(arr)

    # Sıralanmış diziyi ekrana yazdır
    print("Sıralanmış dizi:", arr)

# main fonksiyonunu çağırarak programı çalıştır
if __name__ == "__main__":
    main()
