class Employee:
    
    def __init__(self, name, positions):
        self.name = name 
        self.positions = positions
        
    def get_info(self):
         return f"{self.name} = {self.positions}"


    @staticmethod #best for general utility function within a class 
    def is_valid_position(position):
        valid_positions = ["manager", "Cashier", "Cook", "Janitor"]
        return position in valid_positions
    
    
employee1 = Employee("Eugene", "Manager")
employee2 = Employee("SpongeBob", "Cook")
employee3 = Employee("Squidward", "Cashier")
employee4 = Employee("Patrick", "Janitor")



print(employee1.get_info())
print(employee2.get_info())
print(employee3.get_info())
print(employee4.get_info())
