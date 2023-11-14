*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Register Page

*** Test Cases ***
Register With Valid Username And Password
    Set Username  maija
    Set Password  maija123
    Set Password Confirmation  maija123
    Submit New Credentials
    Register Should Succeed

Register With Too Short Username And Valid Password
    Set Username  m
    Set Password  maija123
    Set Password Confirmation  maija123
    Submit New Credentials
    Register Should Fail With Message  Username has to consist of letters a-z and at least 3 characters

Register With Valid Username And Invalid Password
    Set Username  maija
    Set Password  maijahii
    Set Password Confirmation  maijahii
    Submit New Credentials
    Register Should Fail With Message  The password has to contain numbers and at least 8 characters

Register With Nonmatching Password And Password Confirmation
    Set Username  maija
    Set Password  maija123
    Set Password Confirmation  maija456
    Submit New Credentials
    Register Should Fail With Message  The passwords don't match

Login After Successful Registration
    Set Username  maija
    Set Password  maija123
    Set Password Confirmation  maija123
    Submit New Credentials
    Continue To Login
    Login
    Login Should Succeed

Login After Failed Registration
    Set Username  m
    Set Password  maijahii
    Set Password Confirmation  maijahii
    Submit New Credentials
    Go To Login Page
    Login
    Login Should Fail With Message  Invalid username or password



*** Keywords ***
Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set Password Confirmation
    [Arguments]  ${password_confirmation}
    Input Text  password_confirmation  ${password_confirmation}

Submit New Credentials
    Click Button  Register

Submit Credentials
    Click Button  Login

Register Should Succeed
    Welcome Page Should Be Open

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}

Continue To Login
    Go To Ohtu Page
    Click Button  Logout

Login
    Set Username  maija
    Set Password  maija123
    Submit Credentials

Login Should Succeed
    Main Page Should Be Open

Login Should Fail With Message
    [Arguments]  ${message}
    Login Page Should Be Open
    Page Should Contain  ${message}


