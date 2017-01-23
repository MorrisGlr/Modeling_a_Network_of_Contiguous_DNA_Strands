file = open('rosalind_grph.txt','r')
rawdata = file.readlines()
data = []
K = 3       #the length of the suffix and prefix string/ sequence string
for i in rawdata:
    appendtodata = i.strip('\n')
    data.append(appendtodata)


fastanames = []
fastanamesindexes = []
dataindexes = []
for i in data:
    dataindexes.append(data.index(i))
    if '>' in i:
        fastanames.append(i)
for i in fastanames:
    index = data.index(i)
    fastanamesindexes.append(index)


dict ={}
for i in fastanamesindexes:
    y = data[i]
    dict[y]={'seq':'', 'connections':[]}
    dataindexes.pop(0)
    countforpop = 0
    for i in dataindexes:
        if i not in fastanamesindexes:
            dict[y]['seq'] = (dict[y]['seq']) + data[i]
            countforpop +=1
            continue
        if i in fastanamesindexes:
            for i in range(0,countforpop):
                dataindexes.pop(0)
            break


#check if a prefix of a sequence (s) length k matches a suffix of length k in sequence(t)
#given that I am looking at prefix and suffix, I can compare the full string, then remove
#one character at a time from one end of each string/sequence
#suffix = tail(remove nucleotides from the beginning)     prefix = head(removve nucleotide from end)
###e.g  AAATAAA ->X no match-> AATAAA ->X skip some steps->TAAA-> X ->AAA -> !
###     AAATCCC ->X no match-> AAATCC ->X                ->AAAT-> X ->AAA -> !
for i in dict:                  #for loop 1
    tail_name = i
    tail_seq = dict[i]['seq']
    for s in dict:
        if s != tail_name:
            tail_seq2 = tail_seq
            head_name = s
            head_seq = dict[s]['seq']
            while len(head_seq) >3:
                head_seq = head_seq[:-1]    #deletes last character in string/sequence
            while len(tail_seq2) >3:
                tail_seq2 = tail_seq2[1:]     #deletes first character in string/sequence
            if tail_seq2 == head_seq and len(tail_seq2)==3 and len(head_seq)==3: #graph of k=3!!!
                if head_name not in dict[tail_name]['connections']: #stops duplicate additions
                    dict[tail_name]['connections'].append(head_name)


f = open('rosalind_Graph_Theory_Output.txt','w')
for i in dict:
    if len(dict[i]['connections']) > 0:
        for j in dict[i]['connections']:
            f.write(i.strip('>')+ ' ' + str(j.strip('>'))+ '\n')
