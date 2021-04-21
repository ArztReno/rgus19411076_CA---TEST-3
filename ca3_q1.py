'''
nci programme: BSHDS 
program: library system
author: Renato Gusani
studentID: x19411076
date: 09/04/2020

'''
import sys
class Library:
      def __init__(self,listofbooks):
            self.availablebooks=listofbooks

      def displayAvailablebooks(self):
                   print("These are all 10 books in stock:")
                   print(" \ \ \ ")
                   for book in self.availablebooks:
                         print(book)
      def getBook(self,requestedBook):
            if requestedBook in self.availablebooks:
                  print("The book you requested has now been taken")
                  self.availablebooks.remove(requestedBook)
            else:
                  print("Sorry the book you have requested has already been taken or is not in stock")
                  

class Students:
      def requestBook(self):
            print("Enter the name of the book you want to get")
            self.book=input()
            return self.book

def main():            
      library=Library(["Book 1", "Book 2", "Book 3", "Book 4", "Book 5", "Book 6", "Book 7", "Book 8", "Book 9", "Book 10"])
      students=Students()
      done=False
      while done==False:
            print(""" \ \ \ LIBRARY MENU / / /
                  1. Display books in stock
                  2. Get a book
                  3. Stop Program
                  """)
            choice=int(input("Enter an option:"))
            if choice==1:
                        library.displayAvailablebooks()
            elif choice==2:
                        library.getBook(students.requestBook())
            elif choice==3:
                  sys.exit()
                  
main()
