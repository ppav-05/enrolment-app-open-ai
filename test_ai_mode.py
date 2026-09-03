#!/usr/bin/env python3
"""
AI-Mode Integration Test Script

Tests Ollama connectivity, model availability, and Flask backend endpoints.
Run with: python test_ai_mode.py
"""

import os
import sys
import time
import requests
from pathlib import Path

# Colors for output
GREEN = "\033[92m"
RED = "\033[91m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
RESET = "\033[0m"


def print_header(text):
    print(f"\n{BLUE}{'='*60}{RESET}")
    print(f"{BLUE}{text}{RESET}")
    print(f"{BLUE}{'='*60}{RESET}\n")


def print_pass(text):
    print(f"{GREEN}✓{RESET} {text}")


def print_fail(text):
    print(f"{RED}✗{RESET} {text}")


def print_info(text):
    print(f"{YELLOW}ℹ{RESET} {text}")


def check_ollama_port():
    """Check if Ollama is accessible on port 11434."""
    print_header("1. Checking Ollama Runtime")
    
    try:
        response = requests.get("http://localhost:11434/api/tags", timeout=5)
        print_pass("Ollama API accessible on port 11434")
        return True
    except requests.exceptions.ConnectionError:
        print_fail("Ollama API not accessible on port 11434")
        print_info("Start Ollama with: ollama serve")
        return False
    except Exception as exc:
        print_fail(f"Error: {exc}")
        return False


def check_models():
    """Check if qwen2.5:0.5b is available."""
    print_header("2. Checking Available Models")
    
    try:
        response = requests.get("http://localhost:11434/api/tags", timeout=5)
        data = response.json()
        
        models = [m.get("name", "") for m in data.get("models", [])]
        
        if not models:
            print_fail("No models found")
            print_info("Pull a model with: ollama pull qwen2.5:0.5b")
            return False
        
        print(f"Available models:")
        for model in models:
            if "qwen2.5" in model:
                print_pass(f"  {model}")
            else:
                print_info(f"  {model}")
        
        if any("qwen2.5" in m for m in models):
            return True
        else:
            print_fail("qwen2.5:0.5b not found")
            print_info("Install with: ollama pull qwen2.5:0.5b")
            return False
            
    except Exception as exc:
        print_fail(f"Error checking models: {exc}")
        return False


def check_flask_backend():
    """Check if Flask backend is running."""
    print_header("3. Checking Flask Backend")
    
    try:
        response = requests.get("http://localhost:5001/", timeout=5)
        print_pass("Flask backend accessible on port 5001")
        return True
    except requests.exceptions.ConnectionError:
        print_fail("Flask backend not accessible on port 5001")
        print_info("Start with: docker compose up -d")
        print_info("Or: cd enrolment-service && python -m flask run")
        return False
    except Exception as exc:
        print_fail(f"Error: {exc}")
        return False


def check_frontend():
    """Check if Frontend is running."""
    print_header("4. Checking Frontend (Optional)")
    
    try:
        response = requests.get("http://localhost:8001/", timeout=5)
        print_pass("Frontend accessible on port 8001")
        return True
    except requests.exceptions.ConnectionError:
        print_info("Frontend not on port 8001 (expected for Release 0)")
        print_info("Lab 04 uses port 8080, Release 0 uses port 8001")
        return False
    except Exception as exc:
        print_info(f"Frontend check skipped: {exc}")
        return False


def test_ask_endpoint():
    """Test the /ask endpoint."""
    print_header("5. Testing /ask Endpoint")
    
    try:
        data = {"question": "What is the Student Enrolment App?"}
        response = requests.post(
            "http://localhost:5001/ask",
            data=data,
            timeout=30,
            headers={"Content-Type": "application/x-www-form-urlencoded"}
        )
        
        if response.status_code == 200:
            print_pass(f"Endpoint responded with status 200")
            print_info(f"Response preview: {response.text[:100]}...")
            return True
        else:
            print_fail(f"Endpoint returned status {response.status_code}")
            print_info(f"Response: {response.text[:200]}")
            return False
            
    except requests.exceptions.Timeout:
        print_fail("Request timed out (30 seconds)")
        print_info("Ollama may be slow or unresponsive")
        return False
    except Exception as exc:
        print_fail(f"Error testing endpoint: {exc}")
        return False


def test_ask_with_context_endpoint():
    """Test the /ask-with-context endpoint."""
    print_header("6. Testing /ask-with-context Endpoint")
    
    try:
        data = {"question": "What are the CRUD operations?"}
        response = requests.post(
            "http://localhost:5001/ask-with-context",
            data=data,
            timeout=30,
            headers={"Content-Type": "application/x-www-form-urlencoded"}
        )
        
        if response.status_code == 200:
            print_pass(f"Endpoint responded with status 200")
            print_info(f"Response preview: {response.text[:100]}...")
            return True
        else:
            print_fail(f"Endpoint returned status {response.status_code}")
            print_info(f"Response: {response.text[:200]}")
            return False
            
    except requests.exceptions.Timeout:
        print_fail("Request timed out (30 seconds)")
        return False
    except Exception as exc:
        print_fail(f"Error testing endpoint: {exc}")
        return False


def test_architecture_review_endpoint():
    """Test the /architecture-review endpoint."""
    print_header("7. Testing /architecture-review Endpoint")
    
    try:
        data = {"architecture_request": "Review the microservices architecture"}
        response = requests.post(
            "http://localhost:5001/architecture-review",
            data=data,
            timeout=30,
            headers={"Content-Type": "application/x-www-form-urlencoded"}
        )
        
        if response.status_code == 200:
            print_pass(f"Endpoint responded with status 200")
            print_info(f"Response preview: {response.text[:100]}...")
            return True
        else:
            print_fail(f"Endpoint returned status {response.status_code}")
            print_info(f"Response: {response.text[:200]}")
            return False
            
    except requests.exceptions.Timeout:
        print_fail("Request timed out (30 seconds)")
        return False
    except Exception as exc:
        print_fail(f"Error testing endpoint: {exc}")
        return False


def main():
    """Run all tests."""
    print_header("AI-MODE INTEGRATION TEST SUITE")
    
    print("This script verifies:")
    print("  • Ollama runtime connectivity")
    print("  • Model availability (qwen2.5:0.5b)")
    print("  • Flask backend responsiveness")
    print("  • AI endpoints (/ask, /ask-with-context, /architecture-review)")
    print()
    
    # Run checks
    checks = [
        ("Ollama", check_ollama_port),
        ("Models", check_models),
        ("Flask", check_flask_backend),
        ("Frontend", check_frontend),
        ("Ask", test_ask_endpoint),
        ("Ask+Context", test_ask_with_context_endpoint),
        ("Architecture", test_architecture_review_endpoint),
    ]
    
    results = {}
    for name, check_func in checks:
        try:
            result = check_func()
            results[name] = result
        except Exception as exc:
            print_fail(f"Unexpected error in {name}: {exc}")
            results[name] = False
    
    # Summary
    print_header("TEST SUMMARY")
    
    passed = sum(1 for v in results.values() if v)
    total = len(results)
    
    for name, result in results.items():
        status = f"{GREEN}PASS{RESET}" if result else f"{RED}FAIL{RESET}"
        print(f"  {name}: {status}")
    
    print()
    print(f"Result: {passed}/{total} checks passed")
    print()
    
    if passed == total:
        print_pass("All checks passed! AI-Mode is ready.")
        return 0
    elif passed >= 3:
        print_info("Core checks passed. Some optional checks failed.")
        return 1
    else:
        print_fail("Critical checks failed. Fix issues above.")
        return 2


if __name__ == "__main__":
    try:
        exit_code = main()
        sys.exit(exit_code)
    except KeyboardInterrupt:
        print("\n\nTest interrupted.")
        sys.exit(1)
    except Exception as exc:
        print_fail(f"Unexpected error: {exc}")
        sys.exit(2)
