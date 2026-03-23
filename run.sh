#!/bin/bash
# 抖音文案批量处理 - 快速运行脚本

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

echo "=================================================="
echo "🎬 抖音文案批量处理器"
echo "=================================================="
echo ""

# 检查依赖
if ! python3 -c "import openpyxl" 2>/dev/null; then
    echo "⚠️  检测到未安装依赖，正在安装..."
    pip3 install -r requirements.txt
    echo ""
fi

# 显示输入文件数量
JSON_COUNT=$(find input/douyin_texts -name "*.json" 2>/dev/null | wc -l)
echo "📂 待处理文件数：$JSON_COUNT"
echo ""

# 运行处理
python3 scripts/douyin_batch_processor.py

echo ""
echo "=================================================="
echo "✅ 处理完成！"
echo "=================================================="
