class mydefaultdict (dict): #
    def __init__(self, func, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.func = func

    def __missing__(self, key):
        self[key] = self.func()
        return self[key]


