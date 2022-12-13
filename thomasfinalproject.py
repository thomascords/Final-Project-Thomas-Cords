class Product:
    def __init__(self, name, productID, brand, price):
        self.name = name
        self.productID = productID
        self.brand = brand
        self.price = price

name = input("Enter product name: ")#asking the user for their information
productID = input("Enter product ID: ")
brand = input("Enter product brand: ")
price = input(":Enter product price: ")

productInfo = []#setting up the list for the product information
customProduct = Product(name, productID, brand, price)
productInfo.append(customProduct.name)#appending the information from the class to the list
productInfo.append(customProduct.productID)
productInfo.append(customProduct.brand)
productInfo.append(customProduct.price)
print(productInfo)#testing if it works

try:
    file = open("FinalExam.txt","x")#creating the file if it does not exist
except:
    file = open("FinalExam.txt", "w")#opening the file if it already exists
