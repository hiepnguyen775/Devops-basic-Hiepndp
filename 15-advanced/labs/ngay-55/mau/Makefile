# Bộ lệnh CHUẨN cho mọi dịch vụ — người mới chỉ cần nhớ `make help`
.PHONY: help cai dev test lint build chay quet sach

TEN_DICH_VU ?= $(shell basename $(CURDIR))
TAG ?= $(shell git rev-parse --short HEAD 2>/dev/null || echo "local")
IMAGE = $(TEN_DICH_VU):$(TAG)

help:            ## Hiện danh sách lệnh
	@grep -E '^[a-z-]+:.*?##' $(MAKEFILE_LIST) | \
	  awk 'BEGIN {FS = ":.*?## "}; {printf "  \033[36m%-10s\033[0m %s\n", $$1, $$2}'

cai:             ## Cài thư viện
	npm install

dev:             ## Chạy ở chế độ phát triển
	npm start

test:            ## Chạy test
	npm test

lint:            ## Kiểm tra chất lượng code
	npm run lint --if-present

build:           ## Build Docker image
	docker build -t $(IMAGE) .
	@echo "✅ Đã build: $(IMAGE)"

chay: build      ## Build rồi chạy container
	docker run --rm -p 3000:3000 --name $(TEN_DICH_VU) $(IMAGE)

quet: build      ## Quét bảo mật image (Ngày 49)
	docker run --rm -v /var/run/docker.sock:/var/run/docker.sock \
	  aquasec/trivy:latest image --severity HIGH,CRITICAL --ignore-unfixed $(IMAGE)

sach:            ## Dọn dẹp
	docker rmi $(IMAGE) 2>/dev/null || true
	rm -rf node_modules
