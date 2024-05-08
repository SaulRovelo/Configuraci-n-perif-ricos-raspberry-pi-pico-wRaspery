class digital_clock:
    #contructor inicializamos horas minitos y segundos
    def __init__(self,h: int=0,m: int=0,s: int=0) -> None:
        """ contructor inicializamos horas minitos y segundos """ 
        assert h < 24 and >= 0 
        self.__h = h 
        assert m < 60 and >=0
        self.__m= m 
        assert s < 60 and s >=0
    
    def get_time(self)-> tuple[int,int,int]: 
        """  returns the current time the digital clock holds """
        return self.__h, self.__m, self.__s 
    
    def clear_time(self)-> None: 
        """clears the current time """
        self.__h, self.__m, self.__s = 0, 0, 0