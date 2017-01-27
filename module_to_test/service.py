class ClassToTest(object):


    bye_bye =  "bye bye !"

    def run(self, name=str):
        helloWorld = "hello %s"
        #IDEA factorize the return with the method hello.
        if (name is not None or name != ""):
            return helloWorld % name
        else:
            return ClassToTest.bye_bye

    @classmethod
    def hello(self, name=str):
        #TODO implements a performant algorythme.
        if (name is not None or name != ""):
            return "hello %s" % name
        else:
            return self.bye_bye

    @property
    def why_the_life(self):
        #TODO implements the world's solution.
        return "42"
