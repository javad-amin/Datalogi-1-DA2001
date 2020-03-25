

"""
Modul med olika köer.
"""

class fifoQueue:
    """
    implementation av en kö (FIFO-kö).
    """
    __Q = None
    
    def __init__(self):
        """Konstruktor för kö.
        Skapar en ny tom kö."""
        self.__Q = []

    def __len__(self):
        """Antal element i kön."""
        return len(self.__Q)

    def empty(self):
        """Predikat för att avgöra om kön är tom.
        Svarar True om kön är tom, False annars."""
        return len(self.__Q) == 0

    def enqueue(self, e):
        """Lägg in `e` sist i kön."""
        if self.empty(): self.__Q = [e]
        else: self.__Q.append(e)

    def dequeue(self):
        """Ta bort första elementet från kön och återsänd det."""
        if self.empty(): return None
        return self.__Q.pop(0)


    def __str__(self):
        """Återsänd en strängrepresentation av kön."""
        return str(self.__Q)



class stack:
    """
    implementation av en stack (LIFO-kö).
    """
    __S = None
    
    def __init__(self):
        """Konstruktor för stack.
        Skapar en ny tom stack."""
        self.__S = []

    def __len__(self):
        """Antal element i stacken."""
        return len(self.__S)

    def empty(self):
        """Predikat för att avgöra om stacken är tom.
        Svarar True om stacken är tom, False annars."""
        return len(self.__S) == 0

    def push(self, e):
        """Lägg in `e` överst i stacken."""
        if self.empty(): self.__S = [e]
        else: self.__S.insert(0, e)

    def pop(self):
        """Ta bort första elementet från stacken och återsänd det."""
        if self.empty(): return None
        return self.__S.pop(0)

    def __str__(self):
        """Återsänd en strängrepresentation av stacken."""
        return str(self.__S)

class prioQueue:
    """
    implementation av en kö (FIFO-kö).
    """
    __P = None
    
    def __init__(self):
        """Konstruktor för prioritetskö.
        Skapar en ny tom prioritetskö."""
        self.__P = []

    def __len__(self):
        """Antal element i prioritetskön."""
        return len(self.__P)

    def empty(self):
        """Predikat för att avgöra om prioritetskön är tom.
        Svarar True om prioritetskön är tom, False annars."""
        return len(self.__P) == 0

    def enqueue(self, e, p):
        """Lägg in `e` sist i kön och sedan sorterar listan beroende på 
        prioriteten."""
        if self.empty(): self.__P = [(e, p)]
        else: 
            self.__P.append((e, p))
            for index in range(1,len(self.__P)):
                _currentValue = self.__P[index]
                _currentPriority = self.__P[index][1]
                _position = index
                while _position > 0 and self.__P[_position - 1][1] < _currentPriority:
                    self.__P[_position] = self.__P[_position - 1]
                    _position = _position - 1
                    
                    self.__P[_position] = _currentValue

    def dequeue(self):
        """Ta bort första elementet från kön och återsänd det."""
        if self.empty(): return None
        return self.__P.pop(0)[0]

    def __str__(self):
        """Återsänd en strängrepresentation av prioritetskön."""
        return str(self.__P)
    
