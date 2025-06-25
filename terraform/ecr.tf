# ECR Repositories
resource "aws_ecr_repository" "frontend_repo" {
  name = "microservices-frontend"
}

resource "aws_ecr_repository" "backend_repo" {
  name = "microservices-backend"
}

