import json, re

# Read template
with open('index-template.html', 'r', encoding='utf-8') as f:
    template = f.read()

# Read products
with open('products.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

grid_html    = '\n'.join(data.get('grid', []))
toppick_html = '\n'.join(data.get('topPicks', []))

# Inject into template
output = template.replace('{{TOP_PICKS}}', toppick_html)
output = output.replace('{{GRID_PRODUCTS}}', grid_html)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(output)

print(f"Built index.html with {len(data.get('grid',[]))} grid products and {len(data.get('topPicks',[]))} top picks")
