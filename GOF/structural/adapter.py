class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw_point(self):
        print(".", end="")


class Line:
    def __init__(self, start, end):
        self.start = start
        self.end = end


class Rectangle(list):

    def __init__(self, x,y, width, height):
        self.append(Line( Point(x,y), Point(x+width,y)))
        self.append(Line( Point(x,y), Point(x,y+height)))
        self.append(Line( Point(x+width,y), Point(x+width,y+height)))
        self.append(Line( Point(x,y+height), Point(x+width,y+height)))



class LinePointAdapter():

    def __init__(self, line):
        self._line = line
        self.points=[]

        horiz_start = min(line.start.x, line.end.x)
        horiz_end = max(line.start.x, line.end.x)

        vert_start = min(line.start.y, line.end.y)
        vert_end = max(line.start.y, line.end.y)

        if line.start.x == line.end.x:
            for i in range(vert_start, vert_end):
                self.points.append(Point(vert_start, i))

        elif line.start.y == line.end.y:
            for i in range(horiz_start, horiz_end):
                self.points.append(Point(horiz_start, i))

        else:
            raise Exception("Not Rectangle")


def draw_rec(rec):
    for line in rec:
        adapter = LinePointAdapter(line)
        for p in adapter.points:
            p.draw_point()
        print("|", end="")

rec = Rectangle(1,1, 10, 20)

draw_rec(rec)


