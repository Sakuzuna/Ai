import requests
import colorama 
from colorama import Fore

Blue = Fore.BLUE 
White = Fore.WHITE  
Reset = Fore.RESET

                                                                    
print("""                  ████    ████        ████    ██████                
                  ████    ████        ████    ██████                
                      ████████████████████████                      
                      ████████████████████████                      
          ██▓▓    ██▓▓████░░░░░░░░░░░░░░░░████▓▓████    ████        
          ██▓▓    ████████░░░░░░░░░░░░░░  ██████████    ████        
          ░░░░▓▓▓▓░░░░░░░░░░░░▓▓▓▓▓▓▓▓░░░░░░░░░░░░▒▒▓▓▓▓░░          
        ░░░░░░████░░░░░░░░░░░░▓▓▓▓▓▓██░░░░░░░░░░░░░░████░░░░░░      
  ████  ░░██▓▓░░░░░░░░    ████░░  ████████    ░░  ░░░░░░████░░  ████
  ████    ██▓▓░░░░░░░░    ██▓▓░░  ████▓▓██    ░░  ░░░░░░████░░  ████
      ████░░░░    ░░  ░░░░██▓▓████████▓▓▓▓░░░░░░  ░░░░  ░░░░████    
      ████░░              ██▓▓████████▓▓██              ░░░░████    
        ░░▓▓▒▒              ░░▓▓▓▓▓▓██                  ████        
          ██▓▓                ▓▓▓▓▓▓██                  ████        
            ░░████                                  ████            
              ████                                  ████            
                  ████████  ░░░░░░░░░░░░░░██████████                
                  ████████░░░░░░░░░░░░░░  ██████████                
                          ████████████████                          
                          ████████████████""")                          
                      
                                                                                
url = 'https://www.google.com/search'
print("     ")
params = input('                      [𓁿] Input the request')

response = requests.get(url, params=params)

if response.status_code == 200:
    print('[𓁿] Internet connection: ✓ active ✓')

    print(response.text)
else:
    print('[𓁿] Internet connection: ✓ disabled ✓', response.status_code)