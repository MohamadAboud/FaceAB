
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
            print(*args, sep=' ', end='\n', file=None)