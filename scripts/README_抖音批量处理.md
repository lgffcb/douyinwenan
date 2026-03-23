# 抖音视频批量文案处理工具

## 📋 功能说明

配合 **AnyToCopy** 使用，批量处理抖音自媒体视频的语音转文字文案，自动生成汇总 Excel 文件。

## 🚀 使用流程

### 步骤 1: 用 AnyToCopy 提取文案

1. 打开抖音视频
2. 使用 AnyToCopy 提取视频完整文案
3. 保存为 JSON 格式

### 步骤 2: 整理 JSON 文件

将提取的文案保存为 JSON 文件，放入目录：
```
/home/admin/openclaw/workspace/input/douyin_texts/
```

JSON 格式参考 `模板.json`：
```json
{
  "视频链接": "https://v.douyin.com/xxxxx/",
  "视频标题": "视频标题",
  "作者": "作者名",
  "视频时长": "04:22",
  "发布时间": "2026-03-23 14:00",
  "简介文案": "#标签 视频简介",
  "完整文案": "AnyToCopy 提取的完整语音转文字内容..."
}
```

### 步骤 3: 运行批量处理脚本

```bash
cd /home/admin/openclaw/workspace
python3 scripts/douyin_batch_processor.py
```

### 步骤 4: 查看输出

生成的 Excel 文件在：
```
/home/admin/openclaw/workspace/output/
```

会生成 3 个文件：
- `抖音文案汇总_X 个视频_时间戳.xlsx` - 所有视频汇总到一个表
- `抖音文案详细_X 个视频_时间戳.xlsx` - 每个视频一个独立 Sheet
- `抖音文案统计_X 个视频_时间戳.xlsx` - 字数、时长等统计信息

## 📊 输出示例

### 汇总 Excel 包含：
| 序号 | 视频标题 | 作者 | 时长 | 发布时间 | 完整文案 | 视频链接 |
|------|---------|------|------|---------|---------|---------|
| 1 | 推拉技巧 | 灯哥说脱单 | 04:22 | 2026-03-14 | 完整文案内容... | 链接 |
| 2 | 防御驾驶 | 抚州交警 | 00:45 | 2026-03-21 | 完整文案内容... | 链接 |

### 统计 Excel 包含：
- 视频总数
- 总字数
- 每个视频的字数统计
- 平均时长等

## 💡 快捷命令

```bash
# 查看有多少个待处理的 JSON 文件
ls -la /home/admin/openclaw/workspace/input/douyin_texts/*.json | wc -l

# 运行处理
python3 /home/admin/openclaw/workspace/scripts/douyin_batch_processor.py

# 查看最新生成的文件
ls -lt /home/admin/openclaw/workspace/output/ | head -5
```

## 🔧 依赖

```bash
pip install openpyxl
```

## 📝 注意事项

1. JSON 文件必须使用 UTF-8 编码
2. 文件名建议包含视频标题或 ID，方便识别
3. 如果某个字段没有内容，可以留空或省略
4. 批量处理前建议先用 1-2 个文件测试

## 🎯 典型工作流

```
1. 批量下载抖音视频链接列表
2. 用 AnyToCopy 逐个提取文案 → 保存 JSON
3. 运行批量处理脚本 → 生成汇总 Excel
4. 在 Excel 中整理、编辑、导出
```

## ❓ 常见问题

**Q: AnyToCopy 提取的格式不一样怎么办？**

A: 修改 JSON 字段名匹配即可，脚本只认以下字段：
- `视频链接`、`视频标题`、`作者`、`时长`、`发布时间`、`完整文案`

**Q: 可以处理多少个视频？**

A: 理论上无限制，但建议每批 50-100 个，避免 Excel 文件过大

**Q: 如何合并多次处理的结果？**

A: 可以用 Excel 的"合并工作簿"功能，或修改脚本添加追加模式
