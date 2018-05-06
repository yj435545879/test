import math
class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def distance(self,p2):
        return math.sqrt((self.x-p2.x)**2+(self.y-p2.y)**2)

class Polygon:
    def __init__(self,points=[]):
        self.vertices = []
        for point in points:
            if isinstance(point,tuple):
                point = Point(*point)
                self.vertices.append(point)

    def add_point(self,point):
        self.vertices.append((point))

    def perimeter(self):
        perimeter = 0
        points = self.vertices+[self.vertices[0]]
        for i in range(len(self.vertices)):
            perimeter += points[i].distance(points[i+1])
        return perimeter


class Color:
    def __init__(self,rgb_value,name):
        self.rgb_value = rgb_value
        self.__name = name

    def __set_name(self,name):
        if not name:
            raise Exception("Invalid Name.")
        self.__name = name

    def __get_name(self):
        return self.__name
    name = property(__get_name,__set_name)

###案例学习
class Document:
    def __init__(self):
        self.characters = []
        self.cursor = Cursor(self)
        self.filename = ''

    def insert(self,character):
        self.characters.insert(self.cursor.position,character)
        self.cursor.forward()

    def delete(self):
        del self.characters[self.cursor.position]

    def save(self):
        f = open(self.name,'w')
        f.write(''.join(self.characters))
        f.close()

    def forward(self):
        self.cursor += 1

    def back(self):
        self.cursor -= 1

    @property
    def string(self):
        return "".join(self.characters)

class Cursor:
    def __init__(self,document):
        self.document=document
        self.position = 0

    def forward(self):
        self.position += 1

    def back(self):
        self.position -= 1

    def home(self):
        while self.document.characters[self.position - 1] != '\n':
            self.position -= 1
            if self.position == 0:
                break

    def end(self):
        while self.position < len(self.document.characters) \
            and self.document.characters[self.position] != '\n':
            self.position += 1

class Character:
    def __init__(self,character,bold=False,italic=False,underline=False):
        assert len(character) == 1
        self.character = character
        self.bold = bold
        self.italic = italic
        self.underline = underline

    def __str__(self):
        bold = "*" if self.bold else ''
        italic = '/' if self.italic else ''
        underline = '_' if self.underline else ''
        return bold+italic+underline+self.character
