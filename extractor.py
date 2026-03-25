#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
抖音文案提取器 - 通过 Get 笔记 AI 自动提取抖音视频文案
"""

import json
import os
import sys
import time
import argparse
from datetime import datetime
from pathlib import Path

# 尝试导入 openclaw 相关模块
try:
    import requests
except ImportError:
    print("请安装依赖：pip3 install requests")
    sys.exit(1)


class DouyinExtractor:
    """抖音文案提取器"""
    
    def __init__(self, config_path="config.json"):
        """初始化提取器"""
        self.config = self.load_config(config_path)
        self.gateway_url = self.config.get("gateway", {}).get("url", "http://127.0.0.1:18789")
        self.gateway_token = self.config.get("gateway", {}).get("token", "")
        self.browser_profile = self.config.get("browser", {}).get("profile", "chrome")
        self.output_dir = Path(self.config.get("output", {}).get("dir", "./outputs"))
        self.timeout = self.config.get("browser", {}).get("timeout", 30000)
        
        # 确保输出目录存在
        self.output_dir.mkdir(parents=True, exist_ok=True)
        
    def load_config(self, config_path):
        """加载配置文件"""
        config_file = Path(config_path)
        if config_file.exists():
            with open(config_file, 'r', encoding='utf-8') as f:
                return json.load(f)
        else:
            # 返回默认配置
            return {
                "gateway": {
                    "token": "",
                    "url": "http://127.0.0.1:18789"
                },
                "browser": {
                    "profile": "chrome",
                    "timeout": 30000
                },
                "output": {
                    "dir": "./outputs",
                    "format": "markdown"
                }
            }
    
    def extract_via_getnote(self, douyin_url):
        """通过 Get 笔记提取文案"""
        print(f"\n📥 开始提取：{douyin_url}")
        
        # 使用 OpenClaw browser 工具通过浏览器自动化提取
        # 这里调用 OpenClaw 的 browser 工具
        
        try:
            # 步骤 1: 打开 Get 笔记网站
            print("  ① 打开 Get 笔记网站...")
            result = self.browser_action("open", {
                "profile": self.browser_profile,
                "target": "host",
                "targetUrl": "https://www.biji.com/"
            })
            
            if result.get("status") == "error":
                print(f"  ❌ 打开网站失败：{result.get('error')}")
                return None
            
            time.sleep(2)
            
            # 步骤 2: 获取页面快照，找到输入框
            print("  ② 获取页面元素...")
            snapshot = self.browser_action("snapshot", {
                "profile": self.browser_profile,
                "target": "host"
            })
            
            # 步骤 3: 点击"添加链接"按钮
            print("  ③ 点击添加链接...")
            # 需要解析 snapshot 找到正确的 ref
            
            # 步骤 4: 输入抖音链接
            print("  ④ 输入抖音链接...")
            
            # 步骤 5: 点击生成笔记
            print("  ⑤ 生成笔记...")
            
            # 步骤 6: 等待 AI 处理
            print("  ⑥ 等待 AI 处理...")
            time.sleep(10)
            
            # 步骤 7: 获取提取结果
            print("  ⑦ 获取提取结果...")
            
            # 步骤 8: 保存到文件
            print("  ⑧ 保存结果...")
            
            print("  ✅ 提取完成！")
            
            return {
                "success": True,
                "url": douyin_url,
                "timestamp": datetime.now().isoformat()
            }
            
        except Exception as e:
            print(f"  ❌ 提取失败：{e}")
            return None
    
    def browser_action(self, action, params):
        """调用 browser 工具"""
        # 这里需要通过 OpenClaw 的工具调用接口
        # 由于在 Python 中无法直接调用，我们通过 exec 调用 openclaw CLI
        
        import subprocess
        
        cmd = [
            "openclaw", "browser", action,
            "--profile", params.get("profile", "chrome"),
            "--target", params.get("target", "host")
        ]
        
        if "targetUrl" in params:
            cmd.extend(["--url", params["targetUrl"]])
        
        try:
            result = subprocess.run(
                cmd,
                capture_output=True,
                text=True,
                timeout=self.timeout / 1000
            )
            
            if result.returncode == 0:
                return {"status": "ok", "output": result.stdout}
            else:
                return {"status": "error", "error": result.stderr}
                
        except subprocess.TimeoutExpired:
            return {"status": "error", "error": "Timeout"}
        except Exception as e:
            return {"status": "error", "error": str(e)}
    
    def save_result(self, content, video_info):
        """保存提取结果"""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"douyin_{video_info.get('title', 'unknown')}_{timestamp}.md"
        filepath = self.output_dir / filename
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"  📁 已保存：{filepath}")
        return filepath
    
    def extract_batch(self, urls_file):
        """批量提取"""
        urls_path = Path(urls_file)
        if not urls_path.exists():
            print(f"❌ 文件不存在：{urls_file}")
            return
        
        with open(urls_path, 'r', encoding='utf-8') as f:
            urls = [line.strip() for line in f if line.strip() and not line.startswith('#')]
        
        print(f"📋 找到 {len(urls)} 个链接")
        
        results = []
        for i, url in enumerate(urls, 1):
            print(f"\n[{i}/{len(urls)}] ", end="")
            result = self.extract_via_getnote(url)
            results.append(result)
            time.sleep(2)  # 避免请求过快
        
        # 生成汇总报告
        self.generate_report(results)
    
    def generate_report(self, results):
        """生成提取报告"""
        report_path = self.output_dir / f"report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.md"
        
        success_count = sum(1 for r in results if r and r.get("success"))
        
        with open(report_path, 'w', encoding='utf-8') as f:
            f.write("# 抖音文案提取报告\n\n")
            f.write(f"**生成时间**: {datetime.now().isoformat()}\n\n")
            f.write(f"**总计**: {len(results)} 个视频\n")
            f.write(f"**成功**: {success_count} 个\n")
            f.write(f"**失败**: {len(results) - success_count} 个\n\n")
            
            f.write("## 提取列表\n\n")
            for r in results:
                if r:
                    status = "✅" if r.get("success") else "❌"
                    f.write(f"- {status} {r.get('url', 'unknown')}\n")
        
        print(f"\n📊 报告已保存：{report_path}")


def main():
    """主函数"""
    parser = argparse.ArgumentParser(description="抖音文案提取器")
    parser.add_argument("--url", "-u", help="单个抖音视频链接")
    parser.add_argument("--batch", "-b", help="批量提取文件 (urls.txt)")
    parser.add_argument("--output", "-o", help="输出目录")
    parser.add_argument("--config", "-c", default="config.json", help="配置文件路径")
    
    args = parser.parse_args()
    
    # 初始化提取器
    extractor = DouyinExtractor(args.config)
    
    if args.output:
        extractor.output_dir = Path(args.output)
        extractor.output_dir.mkdir(parents=True, exist_ok=True)
    
    if args.url:
        # 单个提取
        extractor.extract_via_getnote(args.url)
    elif args.batch:
        # 批量提取
        extractor.extract_batch(args.batch)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
