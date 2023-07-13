## ⚙️ Enviroment setting

```bash
cd unsplash_crawler
conda init
(base) .~/.bashrc
(base) conda create -n up_crawl python=3.10 -y
(base) conda activate up_crawl
(up_crawl) pip install -r requirements.txt
```

## 🔧 How to set pre-commit config

```bash
pip install pre-commit
# Used in case of locale related errors
# apt install locales locales-all
pre-commit install
```

## 🏃 How to run

```bash
python img_main.py
```
