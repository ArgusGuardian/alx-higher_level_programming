#!/usr/bin/python3
"""code for Module base"""
import json
import csv
import turtle


class Base:
    """Block define the Base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """initialize the Base class"""
        if id:
            self.id = id
        else:
            Base.__nb_objects = Base.__nb_objects + 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """static method to to convert dict to str"""
        if not list_dictionaries or list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """class method save str to file"""
        f = cls.__name__+".json"
        with open(f, "w") as json_f:
            if not list_objs:
                json_f.write("[]")
            else:
                dicts = [num.to_dictionary() for num in list_objs]
                json_f.write(Base.to_json_string(dicts))

    @staticmethod
    def from_json_string(json_string):
        """static method to load dicts from json file"""
        if not json_string or json_string is None:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """create class with **dictionary asa aguments"""
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                new = cls(1, 1)
            else:
                new = cls(1)
            new.update(**dictionary)
        return new

    @classmethod
    def load_from_file(cls):
        """load dicts from file"""
        f = str(cls.__name__) + ".json"
        try:
            with open(f, "r") as json_f:
                dicts = Base.from_json_string(json_f.read())
                return [cls.create(**d) for d in dicts]
        except IOError:
            return []

    @classmethod
    def load_from_file_csv(cls):
        """load from csv file"""
        f = cls.__name__ + ".csv"
        try:
            with open(f, "r", newline="") as csv_f:
                if cls.__name__ == "Rectangle":
                    fields = ["id", "width", "height", "x", "y"]
                else:
                    fields = ["id", "size", "x", "y"]
                dicts = csv.DictReader(csv_f, fieldnames=fields)
                dicts = [dict([k, int(v)] for k, v in d.items())
                         for d in dicts]
                return [cls.create(**d) for d in dicts]
        except IOError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """save dict in csv file"""
        f = cls.__name__ + ".csv"
        with open(f, "w", newline="") as csv_f:
            if list_objs is None or list_objs == []:
                csv_f.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    fields = ["id", "width", "height", "x", "y"]
                else:
                    fields = ["id", "size", "x", "y"]
                writer = csv.DictWriter(csv_f, fieldnames=fields)
                for obj in list_objs:
                    writer.writerow(obj.to_dictionary())

    @staticmethod
    def draw(list_rectangles, list_squares):
        """draw rectangle using the turtle module"""
        turt = turtle.Turtle()
        turt.screen.bgcolor("#b7312c")
        turt.pensize(3)
        turt.shape("turtle")

        turt.color("#ffffff")
        for rect in list_rectangles:
            turt.showturtle()
            turt.up()
            turt.goto(rect.x, rect.y)
            turt.down()
            for i in range(2):
                turt.forward(rect.width)
                turt.left(90)
                turt.forward(rect.height)
                turt.left(90)
            turt.hideturtle()

        turt.color("#b5e3d8")
        for sq in list_squares:
            turt.showturtle()
            turt.up()
            turt.goto(sq.x, sq.y)
            turt.down()
            for i in range(2):
                turt.forward(sq.width)
                turt.left(90)
                turt.forward(sq.height)
                turt.left(90)
            turt.hideturtle()

        turtle.exitonclick()
