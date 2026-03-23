# 项目结构预览

```
douyinwenan/
│
├── 📄 README.md                    # 项目说明文档
├── 📄 requirements.txt             # Python 依赖
├── 📄 run.sh                       # 快速运行脚本
├── 📄 .gitignore                   # Git 忽略文件
│
├── 📁 scripts/                     # 脚本目录
│   ├── douyin_batch_processor.py   # 主处理脚本
│   └── README_抖音批量处理.md       # 详细使用说明
│
├── 📁 input/                       # 输入目录
│   └── douyin_texts/               # JSON 文案文件
│       └── 模板.json                # JSON 格式模板
│
├── 📁 output/                      # 输出目录（自动生成 Excel）
│   ├── 抖音文案汇总_X 个视频_时间戳.xlsx
│   ├── 抖音文案详细_X 个视频_时间戳.xlsx
│   └── 抖音文案统计_X 个视频_时间戳.xlsx
│
└── 📁 examples/                    # 示例数据
    ├── 示例视频文案.json
    ├── 视频 1_推拉技巧.json
    ├── 视频 2_防御驾驶.json
    └── 视频 3_AI 军火商.json
```

## 快速开始

```bash
# 1. 安装依赖
pip install -r requirements.txt

# 2. 运行处理
./run.sh

# 或直接运行
python scripts/douyin_batch_processor.py
```

## 输出示例

每次运行会生成 3 个 Excel 文件：

1. **汇总文件** - 所有视频在一个表格
2. **详细文件** - 每个视频独立 Sheet
3. **统计文件** - 字数、时长统计
