# Python 開発環境セットアップガイド

## はじめに

このガイドでは、VSCode と devContainer を使用した Python 開発環境のセットアップ方法を説明します。このセットアップは、Python 初心者でも簡単に使い始められるように設計されています。

## 前提条件

以下のソフトウェアがインストールされていることを確認してください：

1. [Visual Studio Code](https://code.visualstudio.com/)
2. [Docker Desktop](https://www.docker.com/products/docker-desktop)
3. VSCode の[Dev Containers 拡張機能](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers)

## セットアップ手順

1. プロジェクトフォルダを作成します
2. `.devcontainer`フォルダを作成します
3. 提供されたファイルを以下のように配置します：

   - `.devcontainer/devcontainer.json`
   - `.devcontainer/Dockerfile`
   - `requirements.txt`（プロジェクトのルートディレクトリに）

4. VSCode でプロジェクトフォルダを開きます
5. 左下の緑色のアイコンをクリックし、「Reopen in Container」を選択します
6. コンテナのビルドが完了するまで待ちます（初回は数分かかることがあります）

## 含まれる主な機能

### Python 開発ツール

- **Python 3.12**: 最新の Python 環境
- **Jupyter Lab**: データ分析や実験に便利なノートブック環境
- **Black & isort**: コードフォーマッターとインポート順整理ツール
- **mypy & flake8**: 型チェックとコード品質チェックツール

### VSCode 拡張機能

- **Python 関連**:
  - Python 拡張機能（IntelliSense など）
  - Pylance（高性能な言語サーバー）
  - 各種コードフォーマッターと検証ツール
- **便利な機能**:
  - Auto Docstring: ドキュメント文字列の自動生成
  - GitHub Copilot: AI によるコード補完（要サブスクリプション）
  - Jupyter 拡張機能: ノートブックのサポート
  - Docker 拡張機能: Docker コンテナの管理

### インストール済みの Python パッケージ

- **データ分析**: numpy, pandas, matplotlib, seaborn
- **機械学習**: scikit-learn
- **Web 開発**: fastapi, uvicorn
- **開発ツール**: pytest, rich, tqdm
- **その他**: requests, python-dotenv

## 使い方のヒント

### 新しい Python ファイルの作成

1. 新しいファイル（例: `main.py`）を作成します
2. 以下のようなサンプルコードを書いて試してみましょう：

```python
def hello_world():
    """シンプルな挨拶関数"""
    print("Hello, Python World!")

if __name__ == "__main__":
    hello_world()
```

3. ファイルを実行するには：
   - ファイル右上の「▶」ボタンを押す
   - または、ターミナルで`python main.py`を実行

### Jupyter ノートブックの使用

1. コマンドパレット（`Ctrl+Shift+P`または`Cmd+Shift+P`）を開き、「Python: Create Jupyter Notebook」を選択
2. 新しいノートブックファイル（`.ipynb`）が作成されます
3. セルにコードを書いて「▶」ボタンを押すと実行できます

### コードフォーマットとエラーチェック

- ファイル保存時に自動的にコードがフォーマットされます（Black）
- インポート文も自動的に整理されます（isort）
- エラーや警告は問題パネルに表示されます（flake8, mypy）

## トラブルシューティング

- **コンテナが起動しない場合**: Docker が実行されていることを確認してください
- **拡張機能が機能しない場合**: コンテナを再起動してみてください
- **パッケージが見つからない場合**: ターミナルで`pip install <パッケージ名>`を実行してください
