FROM python:3.11-slim

WORKDIR /app

# Install dependencies first for better layer caching
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Expose ports: 8000 for FastAPI backend, 8501 for Streamlit frontend
EXPOSE 8000 8501

# Start both backend and frontend using a shell script
COPY start.sh .
RUN chmod +x start.sh

CMD ["./start.sh"]
