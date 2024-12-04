print('hello')
print("hello")
print("I don't know")
print('I don\'t know')
print('say "I don\'t know" ')
print("say \"I don't know\"")

print(r'C:\name\name')

print("############")
print("""\
line1
line2
line3
line4\
""")
print("############")

print("Hi." * 3 + "Mike")

word = 'python'

for v in word:
    print("今の文字は{}です".format(v))

s = 'My name is Yuta. Hi Yuta'
print(s)
# 文字列オブジェクトの最初に引数の文字が含まれるか
is_start = s.startswith('My')
print(is_start)
is_start = s.startswith('x')
print(is_start)

print(s.find('Mike'))
print(s.find('Yuta'))
print(s.count('Yuta'))
print(s.capitalize())
print(s.upper())
print(s.lower())
print(s.replace('Yuta','Nancy'))

# formatを使った書き方
print('My name is {name} {family}'.format(name ='hoge',family='fuga'))

# f-stringsを使った書き方
name = 'hoge'
family = 'fuga'
print(f'My name is {name} {family}')