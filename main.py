
#ファイルの読み込み
f = open('neko1.txt')
data = f.read()
#print(data)

#形態素解析
tg = MeCab.Tagger("-Ochasen")
output=tg.parse(data)
#print(output)

#1行単位に分割
list_a=output.split("\n")

#あとで使うリストを定義
list0=[]
list1=[]
list2=[]
list3=[]
list_count=[]
cate=[]

#全行をループ
for i in range(len(list_a)):

  #タブで分割
  list_buf=list_a[i].split("\t")

  #形態素解析が正確にできているかどうかを要素数で判定
  if len(list_buf) > 3:

    #各要素をリストに追加
    list0.append(list_buf[0])
    list1.append(list_buf[1])
    list2.append(list_buf[2])
    list3.append(list_buf[3])


#品詞一覧作成
for i in range(len(list3)):
  if cate.count(list3[i])==0:
    cate.append(list3[i])

#ソート
#print(cate)
cate.sort()
#print(cate)

#品詞のカウント
for i in range(len(cate)):
  count=0
  for j in range(len(list3)):
    if cate[i] == list3[j]:
      count=count+1
  list_count.append(count)

print(list_count)

#上位50個を表示
for i in range(10):
  #print(list2[i],list_count[i])
  index=list_count.index(sorted(set(list_count))[-1*(i+1)])
  print(cate[i],":",list_count[index])
