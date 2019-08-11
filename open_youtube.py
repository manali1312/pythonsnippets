import webbrowser
youTubeUrl = "https://www.youtube.com/"

chrome_path = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"

webbrowser.get(chrome_path).open(youTubeUrl)