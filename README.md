# 🔐 Secure AI Agent Sandbox

Run autonomous AI agents safely on a low-cost VPS.

This project provides a secure runtime environment for AI agents using Docker sandboxing, network isolation, and controlled internet access.

---

## 🚀 Features

- 🐳 Docker-based sandbox environment
- 🔒 Read-only container filesystem
- 👤 Non-root execution
- 🌐 Network isolation using internal Docker network
- 🧱 Proxy-controlled internet access (Squid)
- ⚡ API rate limiting (NGINX)
- 🔐 SSH key-based secure deployment

---

## 🏗️ Architecture
Developer → SSH → VPS
↓
Docker Runtime
↓
Internal Network (agent-net)
├── Agent Container
└── Proxy (Squid)
↓
Allowed Internet Access
---

## ⚠️ Problem

Most AI agent frameworks run with unrestricted system access, which can:

- modify system files
- abuse APIs
- expose sensitive data
- break environments

---

## ✅ Solution

This project provides:

- sandboxed execution
- controlled networking
- resource isolation
- beginner-friendly setup

---

## 🛠️ Setup

```bash
git clone https://github.com/rushilpatel2608-crypto/secure-ai-agent-sandbox.git
cd secure-ai-agent-sandbox
chmod +x run-agent.sh
./run-agent.sh
