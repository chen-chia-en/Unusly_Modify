wrong_address = [
    '555 Fulton St, Unit 520, San Francisco, California',
    '555 Fulton St, Unit 510, San Francisco, California',
    '555 Culton St, Unit 510, Winters, California']

ans =  '555 Culton St, Unit 510, San Francisco'.replace(', ','')
ans = ans.replace(" ",'')
ans = list(ans)
# print(ans)


trim_address =list()
for address in wrong_address:
    address = address.replace(', ','')
    address = address.replace(" ",'')
    trim_address.append(list(address))
    
# print(trim_address)


for i,value in enumerate(trim_address):
    compare_score = 0
    for x in range(0,len(ans)):
        if trim_address[i][x] == ans[x]:
            compare_score +=1
    print(str(i+1) + ' choice: ' + str(compare_score))
