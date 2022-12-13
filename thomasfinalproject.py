class Product:
    def __init__(self, name, productID, brand, price):#class to store all of the product information
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
        totalRuns = int(input("Please enter the amount of products you would like to enter: "))# asking the user how many products they want to add to their text file
        loop = 1
    except:
        print("That wasn't a valid answer")
while totalRuns > 0:#runs the loop until the user has done all of their desired products

    name = input("Enter product name: ")#asking the user for their products information
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
    totalRuns = totalRuns -1#removes one from the total loops left counter
    print(totalRuns)
    printOut=(" Product #"+str(productNumber)+ ": "+productInfo[0] +", Product ID: "+productInfo[1]+", Brand: "+ productInfo[2]+ ", Price: " + productInfo[3])#Setting the printout so the information is neatly printed to the txt file
    print(end="\n")
    productNumber = productNumber +1#upping the product number for each time the loop runs
    file.write(printOut)#printing the printout to the txt file
