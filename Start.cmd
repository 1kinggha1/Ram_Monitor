@echo off
python -m uvicorn Main:Ram_Api --reload
cd ../../
cmd /k