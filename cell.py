from graphics import Line, Point


class Cell:
    def __init__(self, window = None):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.__x1 = -1
        self.__x2 = -1
        self.__y1 = -1
        self.__y2 = -1
        self.__win = window

    def draw(self, x1, y1, x2, y2):
        if self.__win is None:
            return
        self.__x1 = x1
        self.__y1 = y1
        self.__x2 = x2
        self.__y2 = y2

        if self.has_left_wall:
            line = Line(Point(x1, y1), Point(x1, y2))
            self.__win.draw_line(line)
        else:
            line = Line(Point(x1, y1), Point(x1, y2))
            self.__win.draw_line(line, "white")

        if self.has_top_wall:
            line = Line(Point(x1, y1), Point(x2, y1))
            self.__win.draw_line(line)
        else:
            line = Line(Point(x1, y1), Point(x2, y1))
            self.__win.draw_line(line, "white")

        if self.has_right_wall:
            line = Line(Point(x2, y1), Point(x2, y2))
            self.__win.draw_line(line)
        else:
            line = Line(Point(x2, y1), Point(x2, y2))
            self.__win.draw_line(line, "white")

        if self.has_bottom_wall:
            line = Line(Point(x1, y2), Point(x2, y2))
            self.__win.draw_line(line)
        else:
            line = Line(Point(x1, y2), Point(x2, y2))
            self.__win.draw_line(line, "white")

    
    def draw_move(self, to_cell, undo = False):
        if self.__win is None:
            return
        half_length = abs(self.__x2- self.__x1) //2
        x1_center = self.__x1 + half_length
        y1_center = self.__y1 + half_length

        half_length2 = abs(to_cell.__x2 - to_cell.__x1) //2
        x2_center = to_cell.__x1 + half_length2
        y2_center = to_cell.__y1 + half_length2
        
        path_start_point = Point( x1_center, y1_center)
        end_point = Point(x2_center, y2_center)
        
        fill_color = "red"
        if undo:
            fill_color = "gray"
        path = Line(path_start_point, end_point)

        self.__win.draw_line(path, fill_color)