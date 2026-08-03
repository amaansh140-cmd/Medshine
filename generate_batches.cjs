const fs = require('fs');

const baseDir = '/Users/amaanshaikh/Library/Mobile Documents/com~apple~CloudDocs/Infodesk Solutions/Clients/Dr Priya/Website';
const files = fs.readdirSync(baseDir).filter(f => f.startsWith('treatment-') && f.endsWith('.html'));

const mainCategories = [
  'treatment-bridal.html', 'treatment-hair.html', 'treatment-injectables.html',
  'treatment-laser.html', 'treatment-medical.html', 'treatment-non-surgical.html',
  'treatment-skin.html', 'treatment-acne.html'
];
const treatmentFiles = files.filter(f => !mainCategories.includes(f));

// Let's divide the 56 files into 6 batches
const batches = [[], [], [], [], [], []];
treatmentFiles.forEach((file, index) => {
  batches[index % 6].push(file);
});

let output = '';
batches.forEach((batch, i) => {
  output += `\n=== BATCH ${i + 1} ===\n`;
  batch.forEach(file => {
    let content = fs.readFileSync(`${baseDir}/${file}`, 'utf-8');
    let h1Start = content.indexOf('<h1');
    let h1End = content.indexOf('</h1>', h1Start);
    let h1Tag = content.substring(h1Start, h1End);
    let nameStart = h1Tag.indexOf('>') + 1;
    let treatmentName = h1Tag.substring(nameStart).trim();
    
    // We will name the target image exactly as the file but with .jpg
    let imgName = file.replace('.html', '.jpg');
    
    output += `- ${treatmentName} -> ${imgName}\n`;
  });
});

fs.writeFileSync(`${baseDir}/batches.txt`, output, 'utf-8');
console.log('Batches generated at batches.txt');
