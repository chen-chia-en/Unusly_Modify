def Convert(string):
    list1=[]
    list1[:0]=string
    return list1

wrong_address = [
    '555 Fulton St, Unit 520, San Francisco, California',
    '555 Fulton St, Unit 510, San Francisco, California',
    '555 Culton St, Unit 510, Winters, California']

ans =  '555 Culton St, Unit 510, San Francisco'.replace(', ','')
ans = ans.replace(" ",'')
ans = Convert(ans)


trim_address =list()
for address in wrong_address:
    address = address.replace(', ','')
    address = address.replace(" ",'')
    trim_address.append(address)

compare_list = list()

for i in trim_address:
    compare_list.append(Convert(i))
print(compare_list)


for i in range(3):
    compare_score = 0
    for x in range(0,len(ans)):
        if compare_list[i][x] == ans[x]:
            compare_score +=1
    print(str(i+1) + 'choice: ' + str(compare_score))
