# DynamoDB
resource "aws_dynamodb_table" "orders_table" {
  name           = "Orders"
  billing_mode   = "PAY_PER_REQUEST"
  hash_key       = "OrderId"
  attribute {
    name = "OrderId"
    type = "S"
  }
  tags = {
    Name = "OrdersTable"
  }
}

