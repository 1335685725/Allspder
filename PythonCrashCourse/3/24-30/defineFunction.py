# 8.1
def greet_user():
    '''显示简单的问题'''
    print("hello")
greet_user()
# 8.1.1
def greet_user(mes):
    print(mes)
greet_user("aaa")
# Ex8-1
def display_message():
    print("function")
display_message()
# Ex8-2
def favorite_book(title):
    print("one of my favorite books is ", title)
favorite_book("a_book")

#Ex8-3 8-4
def make_shirt(word= "love Python", size= 5):
    print("The word is ", word, "the size is ", size)
make_shirt("aaa", 5)
make_shirt(size=2)
make_shirt(word="bbb")



