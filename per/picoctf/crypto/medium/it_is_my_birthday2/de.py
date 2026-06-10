# shattered.ioから拾ってきた2つのPDFのプレフィックスを読み込む
with open("shattered-1.pdf", "rb") as f1, open("shattered-2.pdf", "rb") as f2:
    prefix1 = f1.read(320)
    prefix2 = f2.read(320)

# 配布された問題PDF（招待状）を読み込む
with open("invite.pdf", "rb") as f_invite:
    invite_data = f_invite.read()

# 先頭が prefix1 なら prefix2 に差し替え（逆なら prefix1 に差し替え）
new_invite_data2 = prefix2 + invite_data[320:]
new_invite_data1 = prefix1 + invite_data[320:]

# 偽造した招待状を出力
with open("fake_invite1.pdf", "wb") as f_out:
    f_out.write(new_invite_data1)
with open("fake_invite2.pdf", "wb") as f_out:
    f_out.write(new_invite_data2)

print("偽造PDFの生成が完了しました！")