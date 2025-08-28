from flask import Flask, render_template, request, jsonify
import re
import urllib.parse

app = Flask(__name__)

def extract_shopee_ids(url):
    """
    แยก Shop ID และ Product ID จากลิงค์ Shopee
    """
    try:
        # รูปแบบที่ 1: .i.SHOP_ID.PRODUCT_ID
        pattern1 = r'\.i\.(\d+)\.(\d+)'
        match1 = re.search(pattern1, url)
        if match1:
            return match1.group(1), match1.group(2)
        
        # รูปแบบที่ 2: -i.SHOP_ID.PRODUCT_ID
        pattern2 = r'-i\.(\d+)\.(\d+)'
        match2 = re.search(pattern2, url)
        if match2:
            return match2.group(1), match2.group(2)
        
        # รูปแบบที่ 3: /product/SHOP_ID/PRODUCT_ID
        pattern3 = r'/product/(\d+)/(\d+)'
        match3 = re.search(pattern3, url)
        if match3:
            return match3.group(1), match3.group(2)
        
        return None, None
    except:
        return None, None

def convert_to_short_url(shop_id, product_id):
    """
    แปลงเป็นลิงค์สั้น
    """
    if shop_id and product_id:
        return f"https://shopee.co.th/product/{shop_id}/{product_id}"
    return None

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/convert', methods=['POST'])
def convert_links():
    try:
        data = request.get_json()
        input_links = data.get('links', [])
        
        results = []
        converted_count = 0
        
        for link in input_links:
            link = link.strip()
            if not link:
                continue
                
            shop_id, product_id = extract_shopee_ids(link)
            short_url = convert_to_short_url(shop_id, product_id)
            
            result = {
                'input': link,
                'output': short_url,
                'shop_id': shop_id,
                'product_id': product_id,
                'success': short_url is not None
            }
            
            results.append(result)
            if short_url:
                converted_count += 1
        
        return jsonify({
            'success': True,
            'results': results,
            'total_input': len(input_links),
            'total_converted': converted_count,
            'conversion_rate': f"{(converted_count/len(input_links)*100):.1f}%" if input_links else "0%"
        })
        
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 400

@app.route('/api/convert', methods=['POST'])
def api_convert():
    """
    API endpoint สำหรับแปลงลิงค์
    """
    try:
        data = request.get_json()
        url = data.get('url', '').strip()
        
        if not url:
            return jsonify({'error': 'URL is required'}), 400
        
        shop_id, product_id = extract_shopee_ids(url)
        short_url = convert_to_short_url(shop_id, product_id)
        
        if short_url:
            return jsonify({
                'success': True,
                'original_url': url,
                'short_url': short_url,
                'shop_id': shop_id,
                'product_id': product_id
            })
        else:
            return jsonify({
                'success': False,
                'error': 'Invalid Shopee URL format'
            }), 400
            
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)
