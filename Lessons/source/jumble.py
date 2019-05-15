def permutations(array):
  if len(array) < 2:
      return array
  if len(array) == 2:     # base case
      return [array, [array[1], array[0]]]
  all_perms = []
  for i in array:
      new_array = array[:]
      new_array.remove(i)
      all_perms_extension = permutations(new_array)
      for group in all_perms_extension:
          group.insert(0,i)
      all_perms.extend(all_perms_extension)
  return all_perms

f = open('/usr/share/dict/words' , 'r')
words = f.readlines()
f.close()
all_words = set(words)

list_of_permutations = permutations(['1','2','3'])

# print(permutations(['T','E','F','O','N']))
# print(all_words)
