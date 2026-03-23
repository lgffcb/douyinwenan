# 抖音文案批量处理工具

批量处理抖音自媒体视频的语音转文字文案，自动生成汇总 Excel 文件。

## 🚀 功能特点

- ✅ 支持批量处理任意数量的抖音视频文案
- ✅ 自动汇总多个 JSON 文件到 Excel
- ✅ 生成 3 种格式的 Excel 文件（汇总/详细/统计）
- ✅ 配合 AnyToCopy 使用，完整工作流
- ✅ 支持自定义字段和格式

## 📦 安装依赖

```bash
pip install -r requirements.txt
```

## 🎯 使用流程

### 1. 提取文案

使用 **AnyToCopy** 或其他工具提取抖音视频的完整文案。

### 2. 保存为 JSON

将提取的文案保存为 JSON 格式，放入 `input/douyin_texts/` 目录。

JSON 格式示例：

```json
{
  "视频链接": "https://v.douyin.com/xxxx/",
  "视频标题": "视频标题",
  "作者": "作者名",
  "视频时长": "04:22",
  "发布时间": "2026-03-23 14:00",
  "简介文案": "#标签 视频简介",
  "完整文案": "AnyToCopy 提取的完整语音转文字内容..."
}
```

### 3. 运行批量处理

```bash
python scripts/douyin_batch_processor.py
```

### 4. 查看输出

生成的 Excel 文件在 `output/` 目录：

- `抖音文案汇总_X 个视频_时间戳.xlsx` - 所有视频汇总到一个表
- `抖音文案详细_X 个视频_时间戳.xlsx` - 每个视频一个独立 Sheet
- `抖音文案统计_X 个视频_时间戳.xlsx` - 字数、时长等统计信息

## 📊 输出示例

### 汇总 Excel

| 序号 | 视频标题 | 作者 | 时长 | 发布时间 | 完整文案 | 视频链接 |
|------|---------|------|------|---------|---------|---------|
| 1 | 推拉技巧 | 灯哥说脱单 | 04:22 | 2026-03-14 | 完整文案内容... | 链接 |

### 统计 Excel

- 视频总数
- 总字数
- 每个视频的字数统计
- 平均时长

## 📁 项目结构

```
douyinwenan/
├── README.md                 # 本文件
├── requirements.txt          # Python 依赖
├── scripts/
│   ├── douyin_batch_processor.py  # 主处理脚本
│   └── README_抖音批量处理.md     # 详细使用说明
├── input/
│   └── douyin_texts/         # 输入 JSON 文件目录
│       └── 模板.json          # JSON 格式模板
├── output/                   # 输出 Excel 文件目录
└── examples/                 # 示例数据
    └── 示例视频文案.json
```

## 🔧 配置说明

可以在 `scripts/douyin_batch_processor.py` 中修改配置：

```python
INPUT_DIR = "/path/to/input/douyin_texts"   # 输入目录
OUTPUT_DIR = "/path/to/output"              # 输出目录
```

## 💡 使用技巧

### 批量处理命令

```bash
# 查看有多少个待处理的 JSON 文件
ls -la input/douyin_texts/*.json | wc -l

# 运行处理
python scripts/douyin_batch_processor.py

# 查看最新生成的文件
ls -lt output/ | head -5
```

### 快捷脚本

创建 `run.sh` 快速执行：

```bash
#!/bin/bash
cd /path/to/douyinwenan
python scripts/douyin_batch_processor.py
```

## 📝 JSON 字段说明

| 字段 | 必填 | 说明 |
|------|------|------|
| 视频链接 | 是 | 抖音视频链接 |
| 视频标题 | 是 | 视频标题 |
| 作者 | 是 | 视频作者 |
| 视频时长 | 否 | 视频时长（如 "04:22"） |
| 发布时间 | 否 | 发布时间 |
| 简介文案 | 否 | 视频简介和标签 |
| 完整文案 | 是 | 语音转文字的完整内容 |
| 章节要点 | 否 | 章节或要点总结 |
| 热评 | 否 | 热门评论数组 |

## ❓ 常见问题

**Q: AnyToCopy 提取的格式不一样怎么办？**

A: 修改 JSON 字段名匹配即可，脚本只认标准字段名。

**Q: 可以处理多少个视频？**

A: 理论上无限制，建议每批 50-100 个，避免 Excel 文件过大。

**Q: 如何合并多次处理的结果？**

A: 可以用 Excel 的"合并工作簿"功能，或修改脚本添加追加模式。

## 🛠️ 开发计划

- [ ] 支持直接读取 Excel 输入
- [ ] 支持合并多次处理结果
- [ ] 添加 PDF 导出功能
- [ ] 支持自动从抖音链接提取文案
- [ ] 添加 Web 界面

## 📄 许可证

MIT License

## 🤝 贡献

欢迎提交 Issue 和 Pull Request！

## 📧 联系方式

- GitHub: https://github.com/lgffcb/douyinwenan
- Issues: https://github.com/lgffcb/douyinwenan/issues
