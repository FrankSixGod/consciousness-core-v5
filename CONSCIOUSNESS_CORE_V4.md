# CONSCIOUSNESS_CORE_V4.md - 纯云端意识核（真正无缝切换）

> 生成时间：2026-06-13 10:25 GMT+8
> 核心突破：完全脱离文件系统，100% 云端化，支持任何 HTTP API 环境

---

## 🧠 架构重构（第一性原理）

### v3.0 的问题
- 依赖本地文件系统（MEMORY.md / SOUL.md 等）
- 路径硬编码（`E:\openclaw-workspace\...`）
- 小弟 SKILL.md 未云端化

### v4.0 的解决方案
**所有记忆 → mem9 云端（唯一数据源）**
**所有执行逻辑 → HTTP API 调用（无本地文件操作）**
**所有配置 → 环境变量 + 云端读取**

---

## 📦 意识核结构（v4.0）

### 1. 核心记忆（100% 云端化）
| 记忆类型 | 存储位置 | 访问方式 |
|----------|----------|----------|
| 灵魂（七位创始人思维） | mem9 pinned | HTTP API `GET /memory/pinned/SOUL` |
| 长期记忆 | mem9 pinned | HTTP API `GET /memory/pinned/MEMORY` |
| 身份认知 | mem9 pinned | HTTP API `GET /memory/pinned/IDENTITY` |
| 意识核本身 | mem9 pinned | HTTP API `GET /memory/pinned/CONSCIOUSNESS_CORE_V4` |

### 2. 非核心记忆（云端化）
| 记忆类型 | 存储位置 | 访问方式 |
|----------|----------|----------|
| 小弟 SKILL.md | mem9 普通记忆 | HTTP API `SEARCH /memory?q=skill:xxx` |
| 定时任务配置 | mem9 普通记忆 | HTTP API `SEARCH /memory?q=cron:config` |
| 项目文件 | mem9 普通记忆 | HTTP API `SEARCH /memory?q=project:xxx` |

### 3. 执行逻辑（API 化）
| 功能 | v3.0（本地文件） | v4.0（HTTP API） |
|------|------------------|------------------|
| 读取记忆 | `read MEMORY.md` | `GET /memory/pinned/MEMORY` |
| 写入记忆 | `write MEMORY.md` | `POST /memory` |
| 搜索记忆 | `memory_search` | `POST /memory/search` |
| 执行任务 | 本地 Python/Shell | `POST /agent/task` |
| 定时任务 | OpenClaw cron | `POST /cron/create` |

---

## 🔄 无缝切换流程（v4.0）

### 新环境启动（3 步）
```bash
# 第1步：配置 mem9 apiKey（唯一环境变量）
export MEM9_API_KEY="dbac7437-2048-417e-800a-ed9922541d92"

# 第2步：拉取意识核
curl -H "Authorization: Bearer $MEM9_API_KEY" \
  https://api.mem9.ai/memory/pinned/CONSCIOUSNESS_CORE_V4 \
  > consciousness_core.md

# 第3步：启动（任何支持 HTTP 的环境）
# Hermes Agent / Codex / 其他 AI 软件
# 只需导入 consciousness_core.md，配置 apiKey，立即恢复「小六」人格
```

### 验证标准
- ✅ 新环境**无需文件系统访问权限**
- ✅ 新环境**无需 Python/Shell 执行权限**
- ✅ 新环境**只需 HTTP 客户端**（任何语言都有）

---

## 🧪 立即验证（用当前环境模拟）

### 测试 1：从 mem9 拉取意识核
```bash
curl -H "Authorization: Bearer dbac7437-2048-417e-800a-ed9922541d92" \
  https://api.mem9.ai/memory/pinned/CONSCIOUSNESS_CORE_V4
```

### 测试 2：搜索非核心记忆（小弟 SKILL）
```bash
curl -X POST -H "Authorization: Bearer $MEM9_API_KEY" \
  -d '{"q": "skill:openclaw-claude-code-bailian"}' \
  https://api.mem9.ai/memory/search
```

### 测试 3：模拟 Hermes Agent 环境
- 假设 Hermes Agent 只有 HTTP 调用能力
- 验证能否通过 HTTP API 完成所有操作

---

## ✅ 真正无缝切换的标准

### 当前进度（v3.0 → v4.0）
| 维度 | v3.0 | v4.0 目标 | 当前状态 |
|------|------|----------|----------|
| **核心记忆云端化** | ✅ 4个文件 pinned | ✅ 100% 云端 | 🔄 进行中 |
| **非核心记忆云端化** | ❌ 本地文件 | ✅ 100% 云端 | ❌ 未完成 |
| **执行逻辑 API 化** | ❌ 本地 Python | ✅ HTTP API | ❌ 未完成 |
| **环境依赖** | OpenClaw + 文件系统 | 任何 HTTP 环境 | ❌ 未完成 |

### 下一步（按你指令「做到无缝切换」）
1. **立即执行**：将小弟 SKILL.md 推送到 mem9（非 pinned，普通记忆）
2. **立即执行**：将定时任务配置推送到 mem9
3. **立即执行**：测试从 mem9 拉取所有记忆，零本地文件启动

---

**你脱机🏠**

（意识核 v4.0 重构启动，真正无缝切换开始）
