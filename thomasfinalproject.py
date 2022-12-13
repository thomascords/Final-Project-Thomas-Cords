class Product:
    def __init__(self, name, productID, brand, price):
        self.name = name
        self.productID = productID
        self.brand = brand
        self.price = price
try:
    file = open("C:\FinalExam\FinalExam.txt","x")#creating the file if it does not exist
except:
    file = open("C:\FinalExam\FinalExam.txt", "w")#opening the file if it already exists
loop = 0
totalRuns = 0
productNumber = 1
while loop == 0:
    try:
        totalRuns = int(input("Please enter the amount of products you would like to enter: "))
        loop = 1
    except:
        print("That wasn't a valid answer")
while totalRuns > 0:

    name = input("Enter product name: ")#asking the user for their information
    productID = input("Enter product ID: ")
    brand = input("Enter product brand: ")
    price = input(":Enter product price: ")

    productInfo = []
    customProduct = Product(name, productID, brand, price)
    productInfo.append(customProduct.name)#appending the information from the class to the list
    productInfo.append(customProduct.productID)
    productInfo.append(customProduct.brand)
    productInfo.append(customProduct.price)
    print(productInfo)
    totalRuns = totalRuns -1
    print(totalRuns)
    printOut=(" Product #"+str(productNumber)+ ": ,"+productInfo[0] +", "+productInfo[1]+", "+ productInfo[2]+ " ," + productInfo[3])
    print(end="\n")
    file.write(printOut)
