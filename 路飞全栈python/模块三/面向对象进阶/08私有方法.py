# class AirConditioner:
#     def __init__(self):
#         pass
#
#     def cool(self,temperature):
#         self.__turn_on_compressor()
#         self.__set_temperature(temperature)
#         self.__blow_cold_air()
#         self.__turn_off_compressor()
#
#
#     def __turn_on_compressor(self):
#
#         print("打开压缩机")
#
#     def __set_temperature(self,temperature):
#
#         print("设置温度")
#
#     def __blow_cold_air(self):
#
#         print("吹冷气")
#
#     def __turn_off_compressor(self):
#
#         print("关闭压缩机")
#
#
# ac = AirConditioner()
# ac.cool(100)



class Base:

    def __foo(self):
        print("foo from Base")


    def test(self):
        self.__foo()


class Son(Base):
    def __foo(self):
        print("foo from son ")


s = Son()
s.test()













