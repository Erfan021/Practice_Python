# Testing Classes Script

class printerError(RuntimeError):
    pass


class printer:
    def __init__(self, pages_per_sec:float, capacity:int):
        self.pages_per_sec = pages_per_sec
        self.capacity = capacity
        
    
    def print_(self, pages):
        if pages > self.capacity:
            raise printerError('Printer doesn\'t have capacity for all the pages')
            
        self.capacity -= pages
        
        return f"Printed {pages} pages in {pages/self.pages_per_sec:0.2f} seconds"