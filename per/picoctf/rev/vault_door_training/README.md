# 問題

>Description<br>
>Your mission is to enter Dr. Evil's laboratory and retrieve the blueprints for his Doomsday Project. The laboratory is protected by a series of locked vault doors. Each door is controlled by a computer and requires a password to open. Unfortunately, our undercover agents have not been able to obtain the secret passwords for the vault doors, but one of our junior agents obtained the source code for each vault's computer! You will need to read the source code for each level to figure out what the password is for that vault door. As a warmup, we have created a replica vault in our training facility.

説明<br>
あなたの任務は、ドクター・イービルの研究所に潜入し、彼の終末計画の設計図を入手することです。研究所は一連の施錠された金庫扉で守られています。各扉はコンピューターで制御されており、開けるにはパスワードが必要です。残念ながら、潜入捜査官たちは金庫扉の秘密のパスワードを入手できませんでしたが、若手捜査官の一人が各金庫のコンピューターのソースコードを入手しました！各レベルのソースコードを読み解いて、その金庫扉のパスワードを突き止める必要があります。準備として、訓練施設に金庫のレプリカを作成しました。

# 解法要約
java読む、直書き、勝ち

# 解法

配布ファイルは javaファイル<br>
以下抜粋

```Java
    public static void main(String args[]) {
        VaultDoorTraining vaultDoor = new VaultDoorTraining();
        Scanner scanner = new Scanner(System.in); 
        System.out.print("Enter vault password: ");
        String userInput = scanner.next();
	String input = userInput.substring("picoCTF{".length(),userInput.length()-1);
	if (vaultDoor.checkPassword(input)) {
	    System.out.println("Access granted.");
	} else {
	    System.out.println("Access denied!");
	}
   }

    public boolean checkPassword(String password) {
        return password.equals("w4rm1ng_Up_w1tH_jAv4_000AXPNPN0i");
    }
```

つまり picoCTF{......} の中身を input という変数に入れ、それと直書きした　`w4rm1ng_Up_w1tH_jAv4_000AXPNPN0i` が同じかをチェックしている<br>
よってフラグゲット

余談
```
    // The password is below. Is it safe to put the password in the source code?
    // What if somebody stole our source code? Then they would know what our
    // password is. Hmm... I will think of some ways to improve the security
    // on the other doors.
    //
    // -Minion #9567
```
コメントでこれが書いていたが、直書きはこのような危険性があるためやってはいけない<br>
手っ取り早く対策するのであれば hash化して正しいか検知すればよい

`- Minion #9567` についてよくわからなかったのでわかる人がいれば教えてほしい

# 解答
picoCTF{w4rm1ng_Up_w1tH_jAv4_000AXPNPN0i}
