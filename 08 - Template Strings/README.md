# Challenge 8 - Template Strings

This is a very Javascript-y question, so I encourage you to try out your solution in JS.

So the problem is, given a template string, in the format
```javascript
const str = 'Hello, I am <%name%>, and I like eating <%food%>!'
```
create a class that takes this string as an argument, and has a function `fill()` that will, given a JSON object with the appropriate fields, output the template strings with its fields replaced by the fields given by the JSON object. For example, consider the following snippet of code:
```javascript
const obj = new Class(str);

const a = {
  name: 'Mike',
  food: 'bananas',
};

const b = {
  name: 'Mike',
  vehicle: 'cars',
};

const c = {};

obj.fill(a); // Hello, I am Michael, and I like eating bananas!
obj.fill(b); // Hello, I am Michael, and I like eating !
obj.fill(c); // Hello, I am , and I like eating !
```
noticed that unmatched fields are left blank.
