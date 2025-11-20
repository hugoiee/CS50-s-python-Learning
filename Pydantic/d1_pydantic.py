from pydantic import BaseModel, Field, ValidationError
from typing import List, Optional


# 1. 定义一个类，描述你希望数据长什么样
class EvaluationResult(BaseModel):
    query_id: str = Field(..., description="用户问题的ID")
    score: int = Field(..., ge=1, le=5, description="评分，1-5分")  # 自动限制范围 1-5
    tags: List[str] = Field(default=[], description="评估标签，如：幻觉、逻辑错误")
    comment: Optional[str] = None  # 允许为空


# 2. 模拟一组来自 LLM 的脏数据（比如模型有时候会输出奇怪的格式）
raw_data_success = {
    "query_id": "Q1001",
    "score": 4,
    "tags": ["逻辑清晰"],
    "comment": "回答得不错"
}

raw_data_fail = {
    "query_id": "Q1002",
    "score": 10,  # 错误：超过了5分
    "tags": "不是列表"  # 错误：类型不对
}

# 3. 验证
try:
    result = EvaluationResult(**raw_data_success)
    print(f"✅ 验证成功: {result.score}")

    # 自动转成 JSON，这是传给前端或存库的格式
    print(f"📤 输出 JSON: {result.model_dump_json()}")

    EvaluationResult(**raw_data_fail)
except ValidationError as e:
    print(f"❌ 验证失败:\n{e}")