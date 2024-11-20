# FastAPI Factory

## 安裝指南

1. 複製專案
```bash
git clone [your-repository-url]
cd [project-name]
```

2. 安裝依賴
```bash
make build
```


## 啟動方式

### 方法一：直接使用 Python 執行（開發環境）
```bash
python -m app
```
服務將在 http://localhost:5556 啟動

### 方法二：使用 Docker（推薦用於生產環境）

1. 使用 Docker Compose 建構映像檔：
```bash
docker compose -f docker/docker-compose.yml build
```
2. 啟動容器：
```bash
docker compose -f docker/docker-compose.yml up -d
```

3. 查看日誌：
```bash
docker compose -f docker/docker-compose.yml logs -f
```

4. 停止容器：
```bash
docker compose -f docker/docker-compose.yml down
```


## API 端點

服務啟動後，可以訪問以下端點：

- API 文檔：http://localhost:5556/docs
- 健康檢查：
  - Liveness：http://localhost:5556/heartbeat/liveness
  - Readiness：http://localhost:5556/heartbeat/readiness
- Posts API：http://localhost:5556/posts