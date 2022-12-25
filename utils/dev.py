

class Style:
    GREEN = '\033[92m'
    WARNING = '\033[93m'
    ERROR = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

class Developer:
    isTesting = True

    @classmethod
    def log(cls,*args, sep=' ', end='\n', file=None,mode=None):
        """
        :param args:
        :param sep:
        :param end:
        :param file:
        :param mode: [ 'info' , 'error' , 'warning' , 'test ]
        :return: If it is in developer mode it will print
        """
        if Developer.isTesting:
            if mode == "info":
                print(f"{Style.UNDERLINE}{Style.BOLD}",*args,f"{Style.ENDC}", sep=' ', end='\n', file=None)
            elif mode == "error":
                print(f"{Style.ERROR}",*args,f"{Style.ENDC}", sep=' ', end='\n', file=None)
            elif mode == "warning":
                print(f"{Style.WARNING}",*args,f"{Style.ENDC}", sep=' ', end='\n', file=None)
            elif mode == "test":
                print(f"{Style.UNDERLINE}",*args,f"{Style.ENDC}", sep=' ', end='\n', file=None)
            else:
                print(*args, sep=' ', end='\n', file=None)