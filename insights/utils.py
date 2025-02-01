from transformers import AutoTokenizer

#what's the longuest whitespace sequence mapped to a single token?
def longest_whitespace_token(tokenizer):

    whitespace_sequence = " "
    max_whitespace_length = 0
    
    while True:
        tokens = tokenizer.tokenize(whitespace_sequence)
        
        if len(tokens) == 1:
            max_whitespace_length = len(whitespace_sequence)
        else:
            break
        
        whitespace_sequence += " "
    
    return max_whitespace_length

#what's the longuest tab sequence mapped to a single token?
def tab_tokenization(tokenizer):
  max_tab_length = 0
  tabs = "\t"
  while True:
    tokens = tokenizer.tokenize(tabs)
    if len(tokens) == 1: 
      max_tab_length += 1
      tabs += "\t"
    else:
      break
  return max_tab_length


#what is the ratio of keywords (Python, Java, C++) mapped to a single token?
def keywords_with_single_token(tokenizer, keywords_set):
  kw_with_single_token = 0
  for kw in keywords_set:
    tokens = tokenizer.tokenize(kw)
    if len(tokens) == 1:
      kw_with_single_token += 1
  share = round((kw_with_single_token/len(keywords_set)) * 100, 1)
  return share


#what is the ratio of operators (Python, Java, C++) mapped to a single token?
def operators_with_single_token(tokenizer, operators_set):
  ops_with_single_token = 0
  for op in operators_set:
    tokens = tokenizer.tokenize(op)
    if len(tokens) == 1:
      ops_with_single_token += 1
  share = round((ops_with_single_token/len(operators_set)) * 100, 1)
  return share

#to show tokens (inspired by the function in the Jay Alammar's book)
colors_list = [
    '102;194;165', '252;141;98', '141;160;203',
    '231;138;195', '166;216;84', '255;217;47'
]

def show_tokens(sentence, tokenizer):
    token_ids = tokenizer(sentence).input_ids

    for idx, t in enumerate(token_ids):
        color = colors_list[idx % len(colors_list)]
        print(
            f'\x1b[0;30;48;2;{color}m' +
            tokenizer.decode([t]) +
            '\x1b[0m',
            end=' '
        )
    print()  


