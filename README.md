# super_powerTestPlan
Test plan and single test in python for code that takes the power of number provided as input


Positive Tests:
| Name | Steps | Results |
| -----| ----- | ------- |
| Happy Path  | 1. Provide randomly generated integer x     2. Manually recieve the power of x (x * x)    3. Compare and verify with function  | Returns power on integer provided |
| Happy Path with Negative integer | 1. Provide randomly generated negative integer x     2. Manually recieve the power of x (x * x)    3. Compare and verify with function  | Returns power on integer provided |
|Stress test|  1. Provide sys.max_size as input     2. Manually recieve the power of x (x * x)    3. Compare and verify with function  | Returns power on integer provided |


Negative Tests:
| Name | Steps | Results |
| -----| ----- | ------- |
|Invalid input| 1. Provide some form on invalid input (string, char, etc.) 2. Pass invalid input to function | Expect Type Error|
| Input using none whole numbers (float)| 1. Provide float 2. Pass float to function | Expected result either works with float, type error, or converts float to int|
