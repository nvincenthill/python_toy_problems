function replace(ref) {
  ref = {}; // this code does _not_ affect the object passed
}

function update(ref) {
  ref.key = 'newvalue'; // this code _does_ affect the _contents_ of the object
}

var example = { key: 'value' };

replace(example); // a still has its original value - it's un-modified
console.log(example);

update(example); // the _contents_ of 'a' are changed
console.log(example);
