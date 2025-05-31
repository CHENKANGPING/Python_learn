# f = open("hello2.txt", mode="w", encoding="utf-8")
#
# # f.write("hello, ckp")
#
# f.writelines(["hello\n", "xkp\n"])
#
# lines = open("relax.txt",encoding="utf-8").readlines()
# f.writelines(lines)

# mode = "a" 追加
f = open("hello2.txt", mode="a", encoding="utf-8")
f.write("hello,banana~\n")

