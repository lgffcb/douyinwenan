# 推送到 GitHub 指南

## 方式一：使用 HTTPS（推荐）

```bash
cd /home/admin/openclaw/workspace/douyinwenan

# 推送代码
git push -u origin main
```

系统会提示输入 GitHub 用户名和密码（或个人访问令牌）。

### 使用个人访问令牌

1. 访问 https://github.com/settings/tokens
2. 点击 "Generate new token (classic)"
3. 勾选 `repo` 权限
4. 生成后复制令牌
5. 推送时使用令牌作为密码

## 方式二：使用 SSH

```bash
# 配置 SSH 远程地址
git remote set-url origin git@github.com:lgffcb/douyinwenan.git

# 推送
git push -u origin main
```

## 方式三：在 GitHub 网站操作

1. 访问 https://github.com/lgffcb/douyinwenan
2. 点击 "uploading an existing file"
3. 拖拽文件上传
4. 或者使用 GitHub Desktop 客户端

## 验证推送

推送成功后，访问 https://github.com/lgffcb/douyinwenan 应该能看到所有文件。

## 后续更新

```bash
# 提交新更改
git add -A
git commit -m "描述你的更改"
git push
```
