# 🌸 匂いマッピングプラットフォーム - SmellMap

街中で感じた匂いをクラウドソースで集め、日本地図上にマッピングするWebアプリケーション。  
「花の香り」「焼き魚」「排気ガス」など、匂いの強度やカテゴリを可視化し、  
嗅覚を通じた都市の“空気感”を共有・分析します。

## 🚀 特徴

- 🌍 匂いを位置情報つきで投稿（GeoDjango）
- 📊 時間帯・季節別の匂いアニメーションマップ
- 🛠 管理画面でカテゴリ追加・統計ダッシュボード確認
- 📁 投稿データのCSVエクスポート機能

---

## 📦 使用技術

- Django 4.x
- GeoDjango（PostGIS対応）
- Leaflet.js（地図描画）
- PostgreSQL + PostGIS
- Django REST Framework（API用）
- JavaScript（タイムラインアニメーション）
- Bootstrap または Tailwind（UI）

---

## 🛠 インストール手順

```bash
# 仮想環境を作成
python -m venv venv
source venv/bin/activate

# 依存パッケージのインストール
pip install -r requirements.txt

# PostgreSQL + PostGIS 環境が必要です
# 設定例:
# DATABASE_URL=postgres://user:password@localhost:5432/smellmap

# マイグレーション実行
python manage.py migrate

# 管理ユーザー作成
python manage.py createsuperuser

# サーバー起動
python manage.py runserver
