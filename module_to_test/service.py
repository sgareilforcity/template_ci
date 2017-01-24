class ClassToTest(object):

    def hello(self, name=str):
        if (name is not None or name != ""):
            return "hello %s" % name
        else:
            return "bye bye !"