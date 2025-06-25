from flask import Flask, jsonify
import boto3
import os
app = Flask(__name__)
dynamodb = boto3.resource('dynamodb')
table_name = os.environ['DYNAMODB_TABLE']
table = dynamodb.Table(table_name)
@app.route('/health')
def health():
   return jsonify({"status": "healthy"})
@app.route('/api/order/<order_id>')
def get_order(order_id):
   response = table.get_item(Key={'OrderId': order_id})
   return jsonify(response.get('Item', {}))
if __name__ == '__main__':
   app.run(host='0.0.0.0', port=8080)
