def count_words(filename):
    # filename = 'E:\\make the change\\python\\2019年1月13日\\alice.txt'
    try:
        with open(filename) as f:
            contents = f.read()
    # except FileNotFoundError:
    #     msg = "Sorry,the file "+filename+" dose exist."
    #     print(msg)     
    except:
        pass
    else:
        words = contents.split() #split 以空格为分割符将字符串拆分成多部分
        num_words = len(words)  #len 查看长度
        print("The file "+filename+" has about "+str(num_words)+"words.")

filenames = [
    'E:\\make the change\\python\\2019年1月13日\\alice.txt',
    'E:\\make the change\\python\\2019年1月13日\\siddhartha.txt',
    'E:\\make the change\\python\\2019年1月13日\\moby_dick.txt',
    'E:\\make the change\\python\\2019年1月13日\\little_women.txt',
]
for filename in filenames:
    count_words(filename)