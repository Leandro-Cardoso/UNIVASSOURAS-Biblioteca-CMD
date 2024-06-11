setlocal EnableDelayedExpansion
set X=100
set Y=30
set PYTHON=python
set FILE=main.py

rem Console size:
mode con cols=%X% lines=%Y%

rem Run Python script:
%PYTHON% %FILE%
