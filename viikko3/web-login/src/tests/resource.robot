*** Settings ***
Library  SeleniumLibrary
Library  ../AppLibrary.py

*** Variables ***
${SERVER}  localhost:5001
${DELAY}  0.2 seconds
${HOME_URL}  http://${SERVER}
${OHTU_URL}  http://${SERVER}/ohtu
${LOGIN_URL}  http://${SERVER}/login
${REGISTER_URL}  http://${SERVER}/register
${RESET_URL}  http://${SERVER}/tests/reset

*** Keywords ***
Open And Configure Browser
    # jos käytät Firefoxia ja Geckodriveriä käytä seuraavaa riviä sitä alemman sijaan
    # ${options}  Evaluate  sys.modules['selenium.webdriver'].FirefoxOptions()  sys
    ${options}  Evaluate  sys.modules['selenium.webdriver'].ChromeOptions()  sys
    Call Method    ${options}    add_argument    --no-sandbox
    # seuraava rivi on kommentoitu toistaiseksi pois
    # Call Method  ${options}  add_argument  --headless
    Open Browser  browser=chrome  options=${options}
    Set Selenium Speed  ${DELAY}

Login Page Should Be Open
    Title Should Be  Login

Main Page Should Be Open
    Title Should Be  Ohtu Application main page

Welcome Page Should Be Open
    Title Should Be  Welcome to Ohtu Application!

Go To Login Page
    Go To  ${LOGIN_URL}

Go To Ohtu Page
    Go To  ${OHTU_URL}

Go To Main Page
    Go To  ${HOME_URL}

Go To Register Page
    Go To  ${RESET_URL}
    Go To  ${REGISTER_URL}

Register Page Should Be Open
    Title Should Be  Register
