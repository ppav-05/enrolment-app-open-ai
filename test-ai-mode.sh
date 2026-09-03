#!/bin/bash
# AI-Mode Integration Test Script

echo "============================================"
echo "AI-Mode Integration Verification"
echo "============================================"
echo ""

# Check 1: Ollama Process
echo "[1] Checking Ollama Process..."
if lsof -i :11434 >/dev/null 2>&1; then
    echo "✓ Ollama is running on port 11434"
else
    echo "✗ Ollama is NOT running on port 11434"
    echo "  Start with: ollama serve"
    exit 1
fi

# Check 2: Ollama API
echo "[2] Testing Ollama API..."
OLLAMA_RESPONSE=$(curl -s http://localhost:11434/api/tags)
if echo "$OLLAMA_RESPONSE" | grep -q "models"; then
    echo "✓ Ollama API responding"
    echo "  Response: $OLLAMA_RESPONSE"
else
    echo "✗ Ollama API not responding"
    exit 1
fi

# Check 3: Model Availability
echo "[3] Checking for qwen2.5:0.5b model..."
if echo "$OLLAMA_RESPONSE" | grep -q "qwen2.5"; then
    echo "✓ qwen2.5:0.5b model available"
else
    echo "✗ qwen2.5:0.5b model NOT found"
    echo "  Install with: ollama pull qwen2.5:0.5b"
    exit 1
fi

# Check 4: Flask Backend
echo "[4] Checking Flask backend..."
if curl -s http://localhost:5001/ > /dev/null; then
    echo "✓ Flask backend running on port 5001"
else
    echo "✗ Flask backend not responding"
    exit 1
fi

# Check 5: Frontend
echo "[5] Checking Frontend..."
if curl -s http://localhost:8001/ > /dev/null; then
    echo "✓ Frontend running on port 8001"
else
    echo "✗ Frontend not responding (using Lab 04 port 8080)"
fi

# Check 6: Test /ask endpoint
echo "[6] Testing /ask endpoint..."
TEST_RESPONSE=$(curl -s -X POST http://localhost:5001/ask \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "question=What is 2+2?")

if echo "$TEST_RESPONSE" | grep -q "<p>"; then
    echo "✓ /ask endpoint responding"
    echo "  Response sample: $(echo $TEST_RESPONSE | cut -c1-80)..."
else
    echo "✗ /ask endpoint failed"
    echo "  Response: $TEST_RESPONSE"
    exit 1
fi

echo ""
echo "============================================"
echo "✓ All AI-Mode checks passed!"
echo "============================================"
