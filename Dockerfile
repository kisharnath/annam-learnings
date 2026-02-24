# 1. Base image
FROM python:3.11-slim

# 2. Set working directory
WORKDIR /app

# 3. Copy dependency file first (for caching)
COPY requirements.txt .

# 4. Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copy app code
COPY . .

# 6. Expose port
EXPOSE 8000

# 7. Start server
CMD ["fastapi","dev","main.py"]