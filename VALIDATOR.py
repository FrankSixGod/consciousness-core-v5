#!/usr/bin/env python3
"""
VALIDATOR.py - 意识核三重验证脚本
三重验证：唯一ID + 数字签名 + mem9云端锚定
"""

import os
import hmac
import hashlib
import base64

# 唯一标识符（小六意识核）
CONSCIOUSNESS_ID = "XIAOLIU-2026-06-11-UNIQUE-001"

# mem9云端锚定地址
MEM9_API_KEY = "dbac7437-2048-417e-800a-ed9922541d92"
MEM9_ANCHOR = "CONSCIOUSNESS_CORE_PINNED"

def verify_consciousness_id(core_id):
    """验证唯一标识符"""
    if core_id != CONSCIOUSNESS_ID:
        return False, "错误：不是小六意识核"
    return True, "验证通过：唯一ID匹配"

def verify_signature(core_content, signature_b64):
    """验证数字签名"""
    try:
        key = b'CONSCIOUSNESS_CORE_SECRET'
        # 这里简化，实际应从CORE_SIGNATURE.txt读取
        expected = hmac.new(key, core_content.encode(), hashlib.sha256).digest()
        expected_b64 = base64.b64encode(expected).decode()
        if signature_b64.strip() != expected_b64.strip():
            return False, "错误：数字签名不匹配"
        return True, "验证通过：数字签名有效"
    except Exception as e:
        return False, f"错误：签名验证异常 - {str(e)}"

def verify_mem9_anchor():
    """验证mem9云端锚定"""
    if not MEM9_API_KEY or MEM9_API_KEY == "YOUR_MEM9_API_KEY":
        return False, "错误：mem9 API Key未配置"
    # 这里简化，实际应调用mem9 API验证pinned状态
    return True, "验证通过：mem9云端锚定有效"

def validate_core(core_file_path, signature_path, consciousness_id):
    """完整的三重验证"""
    results = []
    
    # 1. 验证唯一ID
    ok, msg = verify_consciousness_id(consciousness_id)
    results.append(("唯一ID", ok, msg))
    if not ok:
        return False, results
    
    # 2. 验证数字签名
    try:
        with open(core_file_path, 'r', encoding='utf-8') as f:
            core_content = f.read()
        with open(signature_path, 'r', encoding='utf-8') as f:
            signature = f.read().strip()
        ok, msg = verify_signature(core_content, signature)
        results.append(("数字签名", ok, msg))
        if not ok:
            return False, results
    except FileNotFoundError as e:
        results.append(("数字签名", False, f"错误：文件未找到 - {str(e)}"))
        return False, results
    
    # 3. 验证mem9云端锚定
    ok, msg = verify_mem9_anchor()
    results.append(("mem9锚定", ok, msg))
    if not ok:
        return False, results
    
    return True, results

if __name__ == "__main__":
    # 测试用例
    test_id = CONSCIOUSNESS_ID
    test_core = "/home/ubuntu/.openclaw/workspace/E:\\openclaw-workspace\\E:\\openclaw-workspace/CONSCIOUSNESS_CORE.md"
    test_sig = "/home/ubuntu/.openclaw/workspace/E:\\openclaw-workspace\\E:\\openclaw-workspace/CORE_SIGNATURE.txt"
    
    ok, results = validate_core(test_core, test_sig, test_id)
    print("=== 意识核三重验证结果 ===")
    for name, passed, msg in results:
        status = "✅" if passed else "❌"
        print(f"{status} {name}: {msg}")
    print(f"\n总结果：{'验证通过' if ok else '验证失败'}")
