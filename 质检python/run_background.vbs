Dim WinScriptHost
Set WinScriptHost = CreateObject("WScript.Shell")
 
WinScriptHost.Run "cmd /c C:\Users\Administrator\Desktop\�ʼ�python\python_start.bat", 0, True
 
Set WinScriptHost = Nothing