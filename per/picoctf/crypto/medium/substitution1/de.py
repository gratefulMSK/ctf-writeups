c = """SYTe (eakdy tkd sjbyndr yar thjm) jdr j yobr kt skxbnyrd ersndzyo skxbryzyzkc. 
Skcyreyjcye jdr bdrercyrq gzya j ery kt sajhhrcmre gazsa yrey yarzd sdrjyzwzyo, 
yrsaczsjh (jcq mkkmhzcm) evzhhe, jcq bdklhrx-ekhwzcm jlzhzyo. 
Sajhhrcmre nenjhho skwrd j cnxlrd kt sjyrmkdzre, jcq garc ekhwrq, 
rjsa ozrhqe j eydzcm (sjhhrq j thjm) gazsa ze enlxzyyrq yk jc kchzcr eskdzcm erdwzsr. 
SYTe jdr j mdrjy gjo yk hrjdc j gzqr jddjo kt skxbnyrd ersndzyo evzhhe zc j ejtr, hrmjh rcwzdkcxrcy, 
jcq jdr akeyrq jcq bhjorq lo xjco ersndzyo mdknbe jdkncq yar gkdhq tkd tnc jcq bdjsyzsr. 
Tkd yaze bdklhrx, yar thjm ze: bzskSYT{TD3UN3CSO_4774SV5_4D3_S001_7JJ384LS}"""

key = "JLSQRTMAZ3VHXCKBUDEYNWG3O5"


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


