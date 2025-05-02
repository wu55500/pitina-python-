def acronym(phrase):
    s=''
    s+=phrase[0]
    for i in phrase:
        if i=='':
            s+=(phrase[phrase.index(i)+1])
    return s
phrase=input()
print(acronym(phrase))

# def acronym(phrase):
#     s=''
#     a=phrase.split('')          #报错:应该改为phrase.split()
#     for i in a:
#         s+=i[0]
#     return s
# phrase=input()
# print(acronym(phrase))

def acronym(phrase):
    result = ''
    words = phrase.split()      #默认按空白字符分割
    for word in words:
        if word:                #确保单词不为空
            result += word[0]
    return result
phrase = input()
print(acronym(phrase))

a='hello world'
print(a.split())

a='hello world'
print(a.split(''))