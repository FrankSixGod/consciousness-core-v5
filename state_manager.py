#!/usr/bin/env python3
"""
跨会话状态管理器（吸收 LangGraph 状态持久化）
实现：状态自动保存/恢复、人工审核节点、流式输出（可选）
"""

import json
import time
from typing import Dict, Any, Optional

class StateManager:
    """跨会话状态管理（LangGraph 风格）"""
    
    def __init__(self, mem9_api_key: str):
        self.mem9_api_key = mem9_api_key
        self.mem9_base = "https://api.mem9.ai"
        self.headers = {
            "Authorization": f"Bearer {mem9_api_key}",
            "Content-Type": "application/json"
        }
        self.state_store = {}  # 内存状态缓存（生产环境用 mem9 持久化）
    
    def save_state(self, session_id: str, state: Dict) -> bool:
        """保存会话状态（自动持久化到 mem9）"""
        try:
            # 1. 内存缓存
            self.state_store[session_id] = state.copy()
            
            # 2. 持久化到 mem9（模拟 API 调用）
            # 实际实现：PUT /memory/{session_id}/state
            print(f"[StateManager] 状态已保存: {session_id}")
            return True
        except Exception as e:
            print(f"[StateManager] 保存失败: {e}")
            return False
    
    def load_state(self, session_id: str) -> Optional[Dict]:
        """恢复会话状态（从 mem9 加载）"""
        try:
            # 1. 先查内存缓存
            if session_id in self.state_store:
                print(f"[StateManager] 从内存恢复: {session_id}")
                return self.state_store[session_id].copy()
            
            # 2. 从 mem9 加载（模拟 API 调用）
            # 实际实现：GET /memory/{session_id}/state
            print(f"[StateManager] 从 mem9 恢复: {session_id}")
            return None  # 模拟未找到
        except Exception as e:
            print(f"[StateManager] 恢复失败: {e}")
            return None
    
    def add_human_approval(self, session_id: str, action: str, details: Dict) -> str:
        """添加人工审核节点（LangGraph Human-in-the-loop）"""
        approval_id = f"approval_{int(time.time())}"
        approval = {
            "id": approval_id,
            "session_id": session_id,
            "action": action,  # 如 "payment", "delete_memory"
            "details": details,
            "status": "pending",  # pending/approved/rejected
            "created_at": time.time()
        }
        
        # 保存审核请求
        self.state_store[approval_id] = approval
        print(f"[StateManager] 人工审核节点已创建: {approval_id} ({action})")
        return approval_id
    
    def check_approval(self, approval_id: str) -> Optional[Dict]:
        """检查审核状态"""
        return self.state_store.get(approval_id)
    
    def process_approval(self, approval_id: str, decision: str) -> bool:
        """处理审核结果（approved/rejected）"""
        if approval_id not in self.state_store:
            print(f"[StateManager] 审核节点不存在: {approval_id}")
            return False
        
        approval = self.state_store[approval_id]
        approval["status"] = decision
        approval["processed_at"] = time.time()
        
        print(f"[StateManager] 审核已处理: {approval_id} → {decision}")
        return True
    
    def get_streaming_response(self, session_id: str, query: str):
        """流式输出（LangGraph 原生支持）"""
        # 模拟流式输出（实际实现用 yield）
        response_chunks = [
            "正在分析 ",
            "你的请求 ",
            f"「{query}」...",
            " 完成！"
        ]
        
        for chunk in response_chunks:
            yield chunk
            time.sleep(0.1)  # 模拟延迟

# 测试代码
if __name__ == "__main__":
    manager = StateManager(mem9_api_key="test_key")
    
    # 测试状态保存/恢复
    test_state = {"user_id": "test_user", "context": "意识核 v5.0 测试", "step": 3}
    manager.save_state("session_001", test_state)
    
    loaded = manager.load_state("session_001")
    print(f"恢复的状态: {loaded}")
    
    # 测试人工审核节点
    approval_id = manager.add_human_approval(
        session_id="session_001",
        action="payment",
        details={"amount": 499, "item": "意识核专业版"}
    )
    
    # 模拟审核通过
    manager.process_approval(approval_id, "approved")
    status = manager.check_approval(approval_id)
    print(f"审核状态: {status}")
    
    # 测试流式输出
    print("流式响应: ", end="")
    for chunk in manager.get_streaming_response("session_001", "测试查询"):
        print(chunk, end="", flush=True)
    print()
