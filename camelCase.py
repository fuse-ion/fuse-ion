def to_camel(ident):
  switch = 0
  counter = -1
  w_l = list(ident)
  for i in w_l:
    counter += 1
    if i == "_":
      w_l.pop(counter)
      w_l[counter] = w_l[counter].upper()
  return "".join(w_l)
      
if __name__ == '__main__':
  print(to_camel('foo'))
  print(to_camel('raw_input'))
  print(to_camel('num2words'))
  print(to_camel('num_to_SMS'))
