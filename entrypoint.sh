#!/bin/sh
set -e

cd /site

# 删除宿主机带入的旧 Gemfile.lock，用容器内 Bundler 重新生成
rm -f Gemfile.lock

# 安装依赖
bundle install

# 启动 Jekyll 开发服务器
exec bundle exec jekyll serve \
    --host 0.0.0.0 \
    --port 4000 \
    --livereload \
    --livereload-port 35729 \
    --incremental
