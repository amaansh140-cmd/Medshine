const fs = require('fs');

const mainHtml = fs.readFileSync('treatment-skin.html', 'utf8');

// Regex to find all hrefs and their corresponding background-image
// <a href="treatment-skin-acne-treatments.html" class="..." style="background-image: url('/src/assets/treatment_acne_indian.jpeg'); ...">
const cardRegex = /<a href="(treatment-skin-[^"]+\.html)"[^>]*style="background-image:\s*url\('([^']+)'\)/g;

let match;
while ((match = cardRegex.exec(mainHtml)) !== null) {
  const fileName = match[1];
  const imageUrl = match[2];
  
  if (fs.existsSync(fileName)) {
    let content = fs.readFileSync(fileName, 'utf8');
    // Replace all <img src="/src/assets/..." 
    const imgReplaceRegex = /<img src="\/src\/assets\/[^"]+"/g;
    content = content.replace(imgReplaceRegex, `<img src="${imageUrl}"`);
    fs.writeFileSync(fileName, content);
    console.log(`Updated ${fileName} with image ${imageUrl}`);
  }
}
