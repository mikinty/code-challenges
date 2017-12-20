# Challenge 4 - Binary String Sum

Given two binary strings, find their equivalent sum, returned as a string. For example, given 

```
a = "11101"
b = "00111"

bsum(a, b) = "100100"
```

Make sure to cut off leading zeros if there are any, e.g. 

````
bsum("001", "001") = "10"
```

Some more test cases:

```
bsum("0", "0") = "0"
bsum("1", "0") = "1"
bsum("11", "11") = "110"
bsum("111111", "111111") = "1111110"
```