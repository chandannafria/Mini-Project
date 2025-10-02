class DoubleBookingError (Exception):
    """Raised When an employee is assigned to more then shift"""
    pass

class ShiftCapacityError (Exception):
    """" Raised when a shift has reached its maximum capacity"""
    pass

class EmployeeNotFound (Exception):
    """" Raised when an employee is not found in records"""
    pass

class TypeError(Exception):
    pass