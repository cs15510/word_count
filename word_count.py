#讀取
lines = []
with open("reviews.txt", "r", encoding = "utf-8") as f:
	for line in f:
		lines.append(line.strip())

#計算留言數
print("共有", len(lines), "筆留言")

#平均的留言字數
count = 0
for line in lines:
	count += len(line)
print("留言的平均字數為", count/len(lines), "字")


#以空格分割每個留言
new_lines = []
for line in lines:
	new_lines.append(line.split())
#計算每個字出現的次數
wc = {}
word_sep = []
for line in new_lines:
	for word in line:
		word_sep.append(word)
for word in  word_sep:
	word = word.replace(".","")
	word = word.replace(",","")
	word = word.replace(":","")
	word = word.replace("(","")
	word = word.replace(")","")
	word = word.replace("-","")
	word = word.replace("!","")
	word = word.replace("?","")
	word = word.replace("/","")
	word = word.replace("'","")
	word = word.replace('"','')
	word = word.replace("_","")
	if word in wc:
		wc[word] += 1
	else:
		wc[word] = 1
for i in wc:
	print(i, ":", wc[i])

#輸入想要找的字
while True:
	find_word = input("請輸入想要找的字:")
	if find_word == "q":
		break
	if find_word in wc:
		print(find_word, "出現", wc[find_word], "次")
	else:
		print("你要找的字不在留言內")

	

