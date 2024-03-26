class Author:
    all =[]

    def __init__(self,name) -> None:
        self.name = name

        Author.all.append(self)
    
    def contracts(self):
        return[contract for contract in Contract.all if contract.author == self]
    
    def books(self):
        #check if the author attribute of each book contract matches the current author (self).
        return[contract.book for contract in Contract.all if contract.author == self]

    def sign_contract(self,book,date,royalties):
        #create and return a new contract object
        contract = Contract(self,book,date,royalties)
        
        return contract   #return the created contract
    
    
    def total_royalties(self):
        total = 0
        # iterate through all contracts related to the author and sum up their royalties
        for contract in self.contracts():
            total += contract.royalties

        return total        

class Book:
    all=[]

    def __init__(self,title) -> None:
        self.title = title
        Book.all.append(self)
    
    def contracts(self):
        return[contract for contract in Contract.all if contract.book == self]
        
    def authors(self):
        return[contract.author for contract in Contract.all if contract.book == self]

class Contract:
    all= []

    def __init__(self,author, book,date,royalties) -> None:
        if not isinstance(author, Author):
            raise TypeError("author must be an instance of class Author")
        if not isinstance(book, Book):
            raise TypeError("book must be an instance of class Book")
        if not isinstance(date, str):
            raise TypeError("date must be a string")
        if not isinstance(royalties, (int, float)):
            raise TypeError("royalties must be a number")

        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        Contract.all.append(self)
    
    @classmethod
    def contracts_by_date(cls, date):
        #filter contracts by date
        return [contract for contract in cls.all if contract.date == date]