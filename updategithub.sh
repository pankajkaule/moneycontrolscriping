#!/bin/sh
python main.py

git add .

git commit -m "updated data"

git push -u origin main
