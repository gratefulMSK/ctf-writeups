key = "ZGSOCXPQUYHMILERVTBWNAFJDK"
s = """
Qctcnrel Mcptzlo ztebc, fuwq z ptzac zlo bwzwcmd zut, zlo gtenpqw ic wqc gccwmc
xtei z pmzbb szbc ul fqusq uw fzb clsmebco. Uw fzb z gcznwuxnm bsztzgzcnb, zlo, zw
wqzw wuic, nlhlefl we lzwntzmubwb—ex sentbc z ptczw rtukc ul z bsuclwuxus reulw
ex aucf. Wqctc fctc wfe tenlo gmzsh brewb lczt elc cjwtciuwd ex wqc gzsh, zlo z
melp elc lczt wqc ewqct. Wqc bszmcb fctc cjsccoulpmd qzto zlo pmebbd, fuwq zmm wqc
zrrcztzlsc ex gntlubqco pemo. Wqc fcupqw ex wqc ulbcsw fzb actd tcizthzgmc, zlo,
wzhulp zmm wqulpb ulwe selbuoctzwuel, U senmo qztomd gmzic Ynruwct xet qub eruluel
tcbrcswulp uw.
"""

c = "Wqc xmzp ub: ruseSWX{5NG5717N710L_3A0MN710L_357GX9XX}"

table = {}
for i in range(26):
  table[ord(key[i]) - 65] = i

m = ""
for i in s:
  if 65 <= ord(i) and ord(i) <= 90:
    m += chr(table[ord(i) - 65] + 65)
  elif 97 <= ord(i) and ord(i) <= 122:
    m += chr(table[ord(i) - 97] + 97)
  else:
    m += i
print(m)

m = ""
for i in c:
  if 65 <= ord(i) and ord(i) <= 90:
    m += chr(table[ord(i) - 65] + 65)
  elif 97 <= ord(i) and ord(i) <= 122:
    m += chr(table[ord(i) - 97] + 97)
  else:
    m += i

print(m)