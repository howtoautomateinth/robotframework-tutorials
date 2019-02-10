*** Setting ***
Library           library/example_lib.py

*** Test Case ***
Test execute custom js in robot
    ${result}=     Execute Custom Js
    Log To Console  ${result}
