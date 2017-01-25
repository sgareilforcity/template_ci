class ClassToTest(object):

    def run(self, name=str):
        #IDEA factorize the return with the method hello.
        if (name is not None or name != ""):
            return "hello %s" % name
        else:
            return "bye bye !"

    @classmethod
    def hello(self, name=str):
        #FIXME implements a performant algorythme.
        if (name is not None or name != ""):
            return "hello %s" % name
        else:
            return "bye bye !"

    @property
    def why_the_life(self):
        #TODO implements the solution of the world.
        return "42"
