c:
cd \projects\positive-pay
del /f /q .\output\*.exe
.\venv\Scripts\auto-py-to-exe -c c:\projects\positive-pay\auto-py-to-exe.json
move .\output\positive_pay_converter.exe .\output\ppc.exe


