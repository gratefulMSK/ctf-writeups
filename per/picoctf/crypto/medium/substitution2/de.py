plane_c = """
nafyffoxenefufytpqnafymfppfentkpxeafbaxraezaqqpzqgswnfyefzwyxnh zqgsfnxnxql  exlzpwbxlrzhkfystnyxqntlbwezhkfyzatppflrfnafef zqgsfnxnxql  evqzwesyxgtyxphqlehenfgetbgxlxenytnxqlvwlbtgflntpemaxzatyfufyhwefvwptlbgtycfntkpfecxppeaqmfufymfkfpxfufnafsyqsfyswysqefqvtaxraezaqqpzqgswnfyefzwyxnh zqgsfnxnxql  xelqnqlphnqnftzautpwtkpfecxppekwntpeqnqrfnenwbflnexlnfyfenfbxltlbfozxnfbtkqwnzqgswnfyezxflzfbfvflexuf zqgsfnxnxql  etyfqvnflptkqyxqwetvvtxyetlbzqgfbqmlnqywllxlrzafzcpxenetlbfofzwnxlrzqlvxrezyxsneqvvflefqlnafqnafyatlbxeaftuxphvqzwefbqlfospqytnxqltlbxgsyquxetnxqltlbqvnflatefpfgflneqvspthmfkfpxfuft zqgsfnxnxql  nqwzaxlrqlnafqvvflexuffpfgflneqvzqgswnfyefzwyxnhxenafyfvqyftkfnnfyufaxzpfvqynfzafutlrfpxegnqenwbflnexltgfyxztlaxraezaqqpevwynafymfkfpxfufnatntlwlbfyentlbxlrqvqvvflexufnfzalxiwfexefeeflnxtpvqygqwlnxlrtlfvvfznxufbfvfleftlbnatnnafnqqpetlbzqlvxrwytnxqlvqzweflzqwlnfyfbxlbfvflexuf zqgsfnxnxql  ebqfelqnpftbenwbflnenqclqmnafxyflfghtefvvfznxufphtenftzaxlrnafgnqtznxufphnaxlcpxcftltnntzcfysxzqznvxetlqvvflexufphqyxflnfbaxraezaqqpzqgswnfyefzwyxnh zqgsfnxnxql  natneffcenqrflfytnfxlnfyfenxlzqgswnfyezxflzftgqlraxraezaqqpfyenftzaxlrnafgflqwratkqwnzqgswnfyefzwyxnhnqsxiwfnafxyzwyxqexnhgqnxutnxlrnafgnqfospqyfqlnafxyqmltlbfltkpxlrnafgnqkfnnfybfvflbnafxygtzaxlfenafvptrxesxzqZNV{L6Y4G_4L41H515_15_73B10W5_8F1KV808}
"""

c = """
naf yffo xe nefufytpqnafymfpp fentkpxeafb axra ezaqqp zqgswnfy efzwyxnh zqgsfnxnxqle xlzpwbxlr zhkfy 
stnyxqn tlbwe zhkfy zatppflrf nafef zqgsfnxnxqle vqzwe syxgtyxph ql ehenfge tbgxlxenytnxql 
vwlbtgflntp emaxzat yfufyh wefvwp tlb gtycfntkpf ecxppe
aqmfufymfkfpxfufnaf syqsfy swysqef qv t axraezaqqp zqgswnfy efzwyxnh zqgsfnxnxql xe lqn qlph nq nftza utpwtkpf 
ecxppe kwn tpeq
nq rfn enwbflne xlnfyfenfb xl tlbfozxnfbtkqwn zqgswnfy ezxflzf bfvflexuf zqgsfnxnxqle tyf qvnfl ptkqyxqwetvvtxyetlbzqgfbq
mlnqywllxlrzafzcpxen etlbfofzwnxlrzqlvxrezyxsne qvvfle fq lna fqnaf yatlbxeaftuxphv qzwefbqlfospqytnxqltlbxgsyquxetn
xqltlbqvnflatefpfgfl  neqvspthmfkfpxfuftzqgsfnx nxqlnqwzaxlrqlnafqvvflexuffpfgfl neqvzqgswnfyefzwyxnhxenafyfvqyft
kfnnfyufaxzpfvqynfzaf utlrfpxegnqenwbflnexltgfy xztlaxraezaqqpevwynafymfkfpxfufn atntlwlbfyentlbxlrqvqvvflexufnf
zalxiwfexefeeflnxtpvq ygqwlnxlrtlfvvfznxufbfvfl eftlbnatnnafnqqpetlbzqlvxrwytnxq lvqzweflzqwlnfyfbxlbfvflexufzqg
sfnxnxqlebqfelqnpftbe nwbflnenqclqmnafxyflfghte fvvfznxufphtenftzaxlrnafgnqtznxu fphnaxlcpxcftltnntzcfysxzqznvxe
tlqvvflexufphqyxflnfb axraezaqqp zqgswnfy efzwyxnh zqgsfnxnxql natn effce nq rflfytnf xlnfyfenxl zqgswnfy ezxflzf tgqlr 
axraezaqqpfy enftzaxlr nafg flqwra tkqwn zqgswnfy efzwyxnh nqs xiwf nafxy zwyxqexnh gqnxutnxlr nafg nq fospqyfqlnafxyqmltlbfl
tkpxlr nafg nq kfnnfy bfvflb nafxy gtzaxlfe naf vptr xe : sxzqZNV{L6Y4G_4L41H515_15_73B10W5_8F1KV808}
"""


key = "TKZBFVRAX3CPGLQS3YENWU23H5"


table = {}
for i in range(26):
  table[ord(key[i]) - 65] = i

m = ""
for i in c:
  if 65 <= ord(i) and ord(i) <= 90:
    if not ord(i) - 65 in table:
      m += i
      continue
    m += chr(table[ord(i) - 65] + 65)
  elif 97 <= ord(i) and ord(i) <= 122:
    if not ord(i) - 97 in table:
      m += i
      continue
    m += chr(table[ord(i) - 97] + 97)
  else:
    m += i
print(m)

