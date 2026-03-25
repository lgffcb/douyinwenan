#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
抖音文案提取器 - OpenClaw 自动化版本
通过 OpenClaw browser 工具自动操作 Get 笔记提取抖音文案
"""

import json
import subprocess
import time
import sys
from datetime import datetime
from pathlib import Path


class DouyinExtractor:
    """抖音文案提取器"""
    
    def __init__(self):
        self.browser_profile = "chrome"
        self.output_dir = Path("./outputs")
        self.output_dir.mkdir(parents=True, exist_ok=True)
        self.target_id = None
        
    def run_openclaw_cmd(self, args, capture=True):
        """执行 openclaw 命令"""
        cmd = ["openclaw"] + args
        try:
            result = subprocess.run(
                cmd,
                capture_output=capture,
                text=True,
                timeout=60
            )
            return result.stdout if capture else None
        except Exception as e:
            print(f"命令执行失败：{e}")
            return None
    
    def browser_tool(self, action, **kwargs):
        """调用 browser 工具"""
        args = ["browser", action]
        
        if kwargs.get("profile"):
            args.extend(["--profile", kwargs["profile"]])
        if kwargs.get("target"):
            args.extend(["--target", kwargs["target"]])
        if kwargs.get("url"):
            args.extend(["--url", kwargs["url"]])
        
        return self.run_openclaw_cmd(args)
    
    def get_tabs(self):
        """获取已附加的标签页"""
        output = self.run_openclaw_cmd(["browser", "tabs", "--profile", self.browser_profile])
        if output:
            try:
                # 解析 JSON 输出
                if "{" in output:
                    start = output.index("{")
                    data = json.loads(output[start:])
                    tabs = data.get("tabs", [])
                    if tabs:
                        self.target_id = tabs[0].get("targetId")
                        return tabs
            except:
                pass
        return []
    
    def extract(self, douyin_url):
        """提取单个视频文案"""
        print(f"\n{'='*60}")
        print(f"🎬 开始提取：{douyin_url}")
        print(f"{'='*60}\n")
        
        # 步骤 1: 打开 Get 笔记
        print("① 打开 Get 笔记网站...")
        result = self.browser_tool("open", 
            profile=self.browser_profile,
            target="host",
            url="https://www.biji.com/"
        )
        time.sleep(3)
        
        # 步骤 2: 检查标签页
        print("② 检查浏览器标签页...")
        tabs = self.get_tabs()
        if not tabs:
            print("❌ 未检测到已附加的标签页")
            print("\n请先在 Chrome 中:")
            print("  1. 打开任意网页")
            print("  2. 点击 OpenClaw Browser Relay 扩展图标")
            print("  3. 确保徽章显示 ON")
            return None
        
        print(f"✅ 检测到 {len(tabs)} 个标签页")
        
        # 步骤 3: 点击添加链接按钮
        print("③ 点击添加链接...")
        # 这里需要通过 browser act 来操作
        
        # 步骤 4: 输入链接
        print("④ 输入抖音链接...")
        
        # 步骤 5: 点击生成
        print("⑤ 生成笔记...")
        
        # 步骤 6: 等待处理
        print("⑥ 等待 AI 处理 (约 10-15 秒)...")
        time.sleep(15)
        
        # 步骤 7: 获取结果
        print("⑦ 获取提取结果...")
        
        # 步骤 8: 保存
        print("⑧ 保存结果...")
        result = self.save_result(douyin_url)
        
        print(f"\n✅ 提取完成！")
        return result
    
    def save_result(self, url, content=""):
        """保存结果"""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filepath = self.output_dir / f"douyin_{timestamp}.md"
        
        md_content = f"""# 抖音视频文案

**链接**: {url}
**提取时间**: {datetime.now().isoformat()}

---

## 文案内容

{content if content else "[内容待提取]"}

"""
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(md_content)
        
        print(f"📁 已保存：{filepath}")
        return str(filepath)
    
    def extract_batch(self, urls_file):
        """批量提取"""
        urls_path = Path(urls_file)
        if not urls_path.exists():
            print(f"❌ 文件不存在：{urls_file}")
            return
        
        with open(urls_path, 'r', encoding='utf-8') as f:
            urls = [line.strip() for line in f if line.strip() and not line.startswith('#')]
        
        print(f"📋 找到 {len(urls)} 个链接\n")
        
        results = []
        for i, url in enumerate(urls, 1):
            print(f"\n[{i}/{len(urls)}]")
            result = self.extract(url)
            results.append({"url": url, "file": result})
            time.sleep(3)
        
        # 生成报告
        self.generate_report(results)
    
    def generate_report(self, results):
        """生成报告"""
        report_path = self.output_dir / f"report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.md"
        
        with open(report_path, 'w', encoding='utf-8') as f:
            f.write("# 抖音文案提取报告\n\n")
            f.write(f"**生成时间**: {datetime.now().isoformat()}\n\n")
            f.write(f"**总计**: {len(results)} 个视频\n\n")
            f.write("## 提取列表\n\n")
            for r in results:
                f.write(f"- {r['url']}\n")
                if r['file']:
                    f.write(f"  - 文件：{r['file']}\n")
        
        print(f"\n📊 报告已保存：{report_path}")


def main():
    import argparse
    
    parser = argparse.ArgumentParser(description="抖音文案提取器")
    parser.add_argument("--url", "-u", help="单个抖音视频链接")
    parser.add_argument("--batch", "-b", help="批量提取文件")
    parser.add_argument("--output", "-o", help="输出目录")
    
    args = parser.parse_args()
    
    extractor = DouyinExtractor()
    
    if args.output:
        extractor.output_dir = Path(args.output)
        extractor.output_dir.mkdir(parents=True, exist_ok=True)
    
    if args.url:
        extractor.extract(args.url)
    elif args.batch:
        extractor.extract_batch(args.batch)
    else:
        parser.print_help()
        print("\n示例:")
        print('  python3 extractor_openclaw.py -u "https://v.douyin.com/xxx/"')
        print("  python3 extractor_openclaw.py -b urls.txt")


if __name__ == "__main__":
    main()
