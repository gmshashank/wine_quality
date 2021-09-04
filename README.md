create env
```bash
conda create -n wineq python=3.9 -y
```

activate env
```bash
conda activate wineq
```

create a requirement file

install requirements
```bash
pip install -r requirements.txt
```

download the data from
https://drive.google.com/drive/folders/18zqQiCJVgF7uzXgfbIJ-04zgz1ItNfF5?usp=sharing


```bash
git init
dvc init
dvc add data_given/winequality.csv
git add .
git commit -m "first commit"
git branch -M main
git remote add origin git@github.com:gmshashank/wine_quality.git
git add . && git commit -m "updated README.md"
git push origin main
```
after stage in dvc.yaml
```bash
dvc repro
dvc metrics show
dvc metrics diff
```