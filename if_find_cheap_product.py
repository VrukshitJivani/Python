product_price1=float(input("Enter first product price :"))
product_weight1=float(input("Enter first product weight :"))

product_price2=float(input("Enter second product price :"))
product_weight2=float(input("Enter second product weight :"))


first_product_per_gram=product_price1/product_weight1
print("First product price per gram is ",first_product_per_gram)

second_product_per_gram=product_price2/product_weight2
print("second product price per gram is ",second_product_per_gram)

if first_product_per_gram<second_product_per_gram:
    print("The first product is cheaper than second product ")
else:
    print("The second product is cheaper than first product")