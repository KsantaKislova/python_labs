num_list = [10, 2, 30, 100, 10, 50, 11, 30, 15, 7]
word_list = ['python', 'ruby', 'perl', 'ruby', 'perl', 'python', 'ruby', 'perl']
print(num_list)
num_list.reverse()
a = input('Enter value')
a = int(a)
index = num_list.index(a)
print('last index {}'.format(len(num_list)-index))
print('_'*50)
print(word_list)
word_list.reverse()
b = input('Enter word')
index = word_list.index(b)
print('last index{}'.format(len(word_list)-index))