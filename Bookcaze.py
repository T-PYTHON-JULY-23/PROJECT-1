import style 
from tabulate import tabulate
bookcaze = [
                   {"Id":101,"Ganre":"Fantasy","Title":"A Hero Born by Jin Yong","Price SR":15},
                   {"Id":102,"Ganre":"Fantasy","Title":"What Should Be Wild by Julia Fine","Price SR":18},
                   {"Id":103,"Ganre":"Fantasy","Title":"Game of Thrones","Price SR":20},
                    {"Id":201 ,"Ganre":"Programming","Title":"Clean Code by Robert C. Martin","Price SR":40},
                    {"Id":202 ,"Ganre":"Programming","Title":"Design Patterns by Erich Gamma","Price SR":25},
                    {"Id":203 ,"Ganre":"Programming","Title":"The Pragmatic Programmer by Andrew Hunt","Price SR":29},
                    {"Id":301 ,"Ganre":"Crime","Title":"Crime and Punishment by Fyodor Dostoevsky","Price SR":30},
                    {"Id":302 ,"Ganre":"Crime","Title":"And Then There Were none by Agatha Christie","Price SR":24},
                    {"Id":303 ,"Ganre":"Crime","Title":"The Thursday Murder Club by Richard Osman","Price SR":19},
                    {"Id":401 ,"Ganre":"Thriller","Title":"The Shining","Price SR":22},
                    {"Id":402 ,"Ganre":"Thriller","Title":"If We Were Villains","Price SR":30},
                    {"Id":403 ,"Ganre":"Thriller","Title":"No Longer Human by Andrew Hunt","Price SR":33},
                    {"Id":501 ,"Ganre":"Mystery","Title":"The Big Sleep by Andrew Hunt","Price SR":29},
                    {"Id":502 ,"Ganre":"Mystery","Title":"Anatomy of a Murder","Price SR":40},
                    {"Id":503 ,"Ganre":"Mystery","Title":"In Cold Blood","Price SR":29},
                    {"Id":601 ,"Ganre":"Humour","Title":"A Man Called Ove","Price SR":35},
                    {"Id":602 ,"Ganre":"Humour","Title":"Lucky Jim","Price SR":19},
                    {"Id":603 ,"Ganre":"Humour","Title":"Cat's Cradle","Price SR":29},
        ]
import os
cart =[]
def OurEbooks():
        IdBook = 0
        while IdBook != 9:  
                print(style.blue(style.bold('Choose from the above table the book Id you want to read: ')))
                IdBook = int(input())
                if IdBook == 101:
                        path = 'deff8b49-680b-43b8-ada3-d878e255c66c.pdf'
                        os.system(path)
                        open(path)
                if IdBook == 102:
                        path = 'WhatShouldBeWild.pdf'
                        os.system(path)
                        open(path)
                if IdBook ==103 :
                        path = 'GameOfThrones.pdf'
                        os.system(path)
                        open(path)
                if IdBook ==201 :
                        path = 'cleancode.pdf'
                        os.system(path)
                        open(path)
                if IdBook ==202:
                        path = 'DesignPatterns.pdf'
                        os.system(path)
                        open(path)
                if IdBook ==203 :
                        path = 'ThePragmaticProgrammer1.pdf'
                        os.system(path)
                        open(path)
                if IdBook ==301 :
                        path = 'If_We_Were_Villains.pdf'
                        os.system(path)
                        open(path)
                if IdBook ==302 :
                        path = 'If_We_Were_Villains.pdf'
                        os.system(path)
                        open(path)
                if IdBook ==303 :
                        path = 'InColdBlood.pdf'
                        os.system(path)
                        open(path)
                if IdBook ==401 :
                        path = 'TheShining.pdf'
                        os.system(path)
                        open(path)
                if IdBook ==402 :
                        path = 'If_We_Were_Villains.pdf'
                        os.system(path)
                        open(path)
                if IdBook ==403 :
                        path = 'NoLongerHuman.pdf'
                        os.system(path)
                        open(path)
                if IdBook ==501 :
                        path = 'Thebigsleep.pdf'
                        os.system(path)
                        open(path)
                if IdBook ==502 :
                        path = 'AnatomyOfMurder.pdf'
                        os.system(path)
                        open(path)
                if IdBook ==503 :
                        path = 'InColdBlood.pdf'
                        os.system(path)
                        open(path)
                if IdBook ==601 :
                        path = 'ManCalledOve.pdf'
                        os.system(path)
                        open(path)
                if IdBook ==602 :
                        path = 'LuckyJim.pdf'
                        os.system(path)
                        open(path)
                if IdBook ==603 :
                        path = 'CatsCradle.pdf'
                        os.system(path)
                        open(path)
