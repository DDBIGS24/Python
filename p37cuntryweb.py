
import webbrowser

c=input("Enter the Country Name =>").lower()
if c=="india":
    webbrowser.open('http://www.india.gov.in')
elif c=="united states":
    webbrowser.open('http://www.usa.gov')
elif c=="japan":
    webbrowser.open('http://www.japan.go.jp')
else:
    print("Wrong Name!!!")  