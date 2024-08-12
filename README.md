# Beginning Python: From Novice to Professional

## この本に求めること
実践開発プロジェクトをなぞることで、
開発のベストプラクティスを理解して、
その手法を独自のアプリケーション開発に展開する。

また、そのプロジェクト開発でテストツールの使用方法についても学ぶ。


## dockerの実行について

各sectionにDockerfileとdocker.shを用意しています。

```
$ sh docker.sh
```


```bash
#!/bin/bash
docker build -t section9 .
docker run section9
```

