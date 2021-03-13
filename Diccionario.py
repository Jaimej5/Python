#Variables que son ojetos clave valor
product={
    "name": "book",
    "quantity": 3,
    "price": 2.9
}

#diccionario de diccionarios
products = [
    {"name": 'book', "price": 10.99},
    {"name": 'laptop', "price": 1099}
]

print(products)

print(product.keys())  #imprime sus valores
print(product.items()) #imprime todo
#del product