class DigitalClock:
    def __init__(self, h:int = 0, m:int = 0, s:int = 0) -> None:
        """ Constructor a DigitalClock object with three parameters: hours, minutes, and seconds (h,m,s).

        Args:
            h (int): Hours. Defaults to 0.
            m (int): Minutes. Defaults to 0.
            s (int): Seconds. Defaults to 0.
        """
        assert h < 24 and h >= 0
        self.__h = h
        assert m < 60 and m >= 0
        self.__m = m
        assert s < 60 and s >= 0
        self.__s = s
        

    def get_time(self) -> tuple[int, int, int]:
        """Return the time in a tuple format (h,m,s).
        Returns:
            tuple[int, int, int]: A tuple with the time (h,m,s).
            24hrs format.
        """
        return self.__h, self.__m, self.__s
        
    def clear_time(self) -> None:
        """Clear the time of the clock. 
            Set the time to 0:0:0.     
        """
        self.__h = 0
        self.__m = 0
        self.__s = 0
    def increment(self)  -> None:
        """Increment the time by one second.\n
            If the seconds reach 59, increment the minutes by one. \n
            If the minutes reach 59, increment the hours by one. \n
            If the hours reach 23, set the time to 0:0:0.
        """
        self.__h = self.__h + 1 if self.__s == 59 and self.__m == 59 else self.__h
        self.__h = 0 if self.__h == 24 else self.__h
        self.__m = self.__m + 1 if self.__s == 59 else self.__m
        self.__m = 0 if self.__m == 60 else self.__m
        self.__s = self.__s + 1 if self.__s < 59 else 0
            
        

            
    
        
    
    