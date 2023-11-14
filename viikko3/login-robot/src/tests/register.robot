*** Settings ***
Resource  resource.robot
Test Setup  Input New Command And Create User

*** Test Cases ***
Register With Valid Username And Password
    Input Credentials  maija  maija123
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Input Credentials  kalle  kalle123
    Output Should Contain  This username is already taken

Register With Too Short Username And Valid Password
    Input Credentials  m  maija123
    Output Should Contain  Username has to consist of letters a-z and at least 3 characters

Register With Enough Long But Invalid Username And Valid Password
    Input Credentials  maija9  maija123
    Output Should Contain  Username has to consist of letters a-z and at least 3 characters

Register With Valid Username And Too Short Password
    Input Credentials  maija  m123
    Output Should Contain  The password has to contain numbers and at least 8 characters

Register With Valid Username And Long Enough Password Containing Only Letters
    Input Credentials  maija  maijaykskakskolme
    Output Should Contain  The password has to contain numbers and at least 8 characters

*** Keywords ***
Input New Command And Create User
    Input New Command
    Create User  kalle  kalle123
