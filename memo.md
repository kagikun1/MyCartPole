ssh接続手順

鍵ペア作成
cd ~/.ssh
ssh-keygen -t rsa

鍵アップロード後確認
https://github.com/settings/keys
ssh -T git@github.com
参考：https://qiita.com/shizuma/items/2b2f873a0034839e47ce

git push 手順
git add <filename>
git commit
git push origin <branch>
 
