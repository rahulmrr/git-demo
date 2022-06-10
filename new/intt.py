import re
print(re.findall("\d","abc123"))
print(re.findall("\w","abc123"))
print(re.findall("\W","@#$%asd987"))
print(re.findall("\d","@#$%asd987"))
print(re.findall("\d","@#$%asd987"))
final_word_found = ["help","abc123","PromoRevoooooooooooo","123",".jp7g","abs","321",".247","@#$%asd987","$fdf","oju*"]
a = [word for word in final_word_found if len(re.findall("\d",word))==0 if len(re.findall("\W",word))==0]
print(a)
#print(re.findall("{\}","@#$%asd987"))
#final_word_found = ["help","abc123","123",".jpg","abs","321",".247","@#$%asd987"]
#[word for word in b if re.findall()]
##if len(re.findall("\W",word)


c=8
b=5
print(c+b)

fjyvfffyujv
ljkvh gfd

e=0
t=6
print(e*t)
