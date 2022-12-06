import shapes

rectangle = shapes.Rectangle(name='Rectangulo Verde', width=35, height=65, color='Verde')

if __name__ == '__main__':
    print(rectangle)
    print('Área: ', rectangle.area())
    print(shapes.Rectangle.mro())