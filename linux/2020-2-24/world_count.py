def count_words(filename):
    """计算一个文件大致包含多少个单词"""
    try:
        with open(filename) as f_obj:
            contents = f_obj.read()
    except FileNotFoundError:
        #msg = "Sorry, the file "+filename+" does not exist."
        #print(msg)
        pass
    else:
        words = contents.split()
        num_words = len(words)
        print("The file "+ filename +" has about " +str(num_words)+" words")
filenames = ['alice_advantures.txt','alice.txt','error.txt']
for filename in filenames:
    count_words(filename)
