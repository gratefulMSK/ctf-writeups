#--------"ABCDEFGHIJKLMNOPQRSTUVWXYZ"------------
deckey = "LRFWIMHVTQP_E_BUDGYSCOKN_A"
s = """
-------------------------------------------------------------------------------
uvxrbzit gmbm et svpb cazr - cbmjpmxus_et_u_vhmb_azfoqz_m4903514
-------------------------------------------------------------------------------
dm dmbm xvi fpug fvbm igzx z jpzbimb vc zx gvpb vpi vc vpb tgek ieaa dm tzd gmb texw, zxq igmx e pxqmbtivvq cvb igm cebti iefm dgzi dzt fmzxi os z tgek cvpxqmbexr ex igm tmz.  e fpti zuwxvdamqrm e gzq gzbqas msmt iv avvw pk dgmx igm tmzfmx ivaq fm tgm dzt texwexr; cvb cbvf igm fvfmxi igzi igms bzigmb kpi fm exiv igm ovzi igzx igzi e fergi om tzeq iv rv ex, fs gmzbi dzt, zt ei dmbm, qmzq deigex fm, kzbias deig cbergi, kzbias deig gvbbvb vc fexq, zxq igm igvprgit vc dgzi dzt smi omcvbm fm.
"""

table = {}
for i in range(26):
  if deckey[i] != "_":
    table[i] = ord(deckey[i]) - 65

m = ""
for i in s:
  if 65 <= ord(i) and ord(i) <= 90:
    if ord(i) - 65 in table:
      m += chr(table[ord(i) - 65] + 65)
    else:
      m += "*"
  elif 97 <= ord(i) and ord(i) <= 122:
    if ord(i) - 97 in table:
      m += chr(table[ord(i) - 97] + 97)
    else:
      m += "*"
  else:
    m += i
print(m)
