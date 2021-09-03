create env
'''bash
conda create -n wineq python=3.9 -y
'''

activate env
'''bash
conda activate wineq
'''

create a requirement file

install requirements
'''bash
pip install -r requirements.txt
'''

download the data from
https://drive.google.com/drive/folders/18zqQiCJVgF7uzXgfbIJ-04zgz1ItNfF5?usp=sharing


git init
dvc init

dvc add data_given/winequality.csv

git add .
git commit -m "first commit"