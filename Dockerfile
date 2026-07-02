FROM ruby:3.1-alpine

# 安装 Jekyll 所需的系统依赖
# build-base 已包含 gcc/g++/make/libc-dev，无需重复声明
RUN apk add --no-cache \
    build-base \
    libffi-dev \
    nodejs \
    git

# 设置工作目录
WORKDIR /site

# 镜像内 bundler 默认路径
ENV BUNDLE_PATH=/usr/local/bundle

# 只复制 Gemfile（不复制 Gemfile.lock，避免 Bundler 版本冲突）
# 容器内 Bundler 2.x 会重新解析生成锁文件
COPY Gemfile ./

# 安装 Ruby 依赖
RUN bundle install

# 复制项目所有文件
COPY . .

# 暴露端口：4000 Jekyll 服务，35729 Livereload
EXPOSE 4000 35729

# 复制入口脚本
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]
