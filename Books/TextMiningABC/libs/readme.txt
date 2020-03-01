1. msys2-x86_64-20190524.exe をインストール
2. mysys コマンドプロンプトで下記を実行
  pacman -Syu
  pacman -S mingw64/mingw-w64-x86_64-cairo
3. 仮想環境で下記を実行
   ※python3.7以外の場合には下記より探す
     https://www.lfd.uci.edu/~gohlke/pythonlibs/
  py -m pip install pycairo-1.19.1-cp37-cp37m-win_amd64.whl
  py -m pip install python_igraph-0.7.1.post6-cp37-cp37m-win_amd64.whl
4. igraph のフォントを変更する
  venv\Lib\site-packages\igraph\drawing\graph.py
  context.select_font_face の第一引数を変更