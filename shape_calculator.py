class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height
       
    def __str__(self):
        return "Rectangle(width=" + str(self.width) + ", height=" + str(self.height) + ")"


    def set_width(self, width):
        self.width = width
        self.side = width

    def set_height(self, height):
        self.height = height        

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return 2 * self.width + 2 * self.height
    
    def get_diagonal(self): 
       return ((self.width ** 2 + self.height ** 2) ** .5)

    def get_picture(self):
        pic = list()
        w, h = 0, 0
        if type(self) == Rectangle:
            while h < self.height:
                while w < self.width:
                    pic.append(("*" * self.width) + "\n")
                    w = w + 1
                    h = h + 1 
                    break

        if type(self) == Square:
            w, h = 0, 0
            while h < self.side:
                while w < self.side:
                    pic.append(("*" * self.side) + "\n")
                    w = w + 1
                    h = h + 1                     
                    break
        picture = "".join(pic)
        if self.width > 50 or self.height > 50:
            picture = "Too big for picture."
        
        return picture
        

    def get_amount_inside(self, shape):
        amount= 0

        s1_area = self.get_area()
        s2_area = shape.get_area()

        # if the self shape is a multiple of the other shape, divide it to get the amount
        if s1_area % s2_area == 0:
            amount = int(s1_area / s2_area)
        # if the self shape width and height is higher than the other shape, divide the widths and heights and add the two
        elif self.width / shape.width > 0 and self.height / shape.height > 0:
            w = int(self.width / shape.width)
            h = int(self.height / shape.height)

            # if the height or the width is 1, then do not count it
            if w >= 1 and h == 1:
                h = 0
            if w == 1 and h >= 1:
                w = 0
            amount = w + h
        else:
            amount = 0
        
        return amount
        


class Square(Rectangle):

        def __init__(self, side):
            self.side = side
            Rectangle.width = side
            Rectangle.height = side

        def __str__(self):
            return "Square(side=" + str(self.side) +")"  


        def set_side(self, side):
            self.side = side
            Rectangle.width = side
            Rectangle.height = side  