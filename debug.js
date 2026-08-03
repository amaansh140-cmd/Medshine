const fs = require('fs');
console.log('Reading file...');
let c = fs.readFileSync('treatment-skin-acne-treatments.html', 'utf-8');
console.log('Read ' + c.length + ' bytes');
fs.writeFileSync('treatment-skin-acne-treatments.html', c, 'utf-8');
console.log('Done');
