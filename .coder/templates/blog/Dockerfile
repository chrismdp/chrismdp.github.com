FROM codercom/enterprise-base:ubuntu

# Set non-interactive frontend to avoid prompts during build
ENV DEBIAN_FRONTEND=noninteractive

# Cache bust to force rebuild after Dockerfile changes  
ARG CACHE_BUST=1

# Switch to root to install packages (enterprise-base runs as coder by default)
USER root

# Fix apt permissions and install Ruby and Jekyll dependencies
RUN mkdir -p /var/lib/apt/lists/partial && \
    chmod 755 /var/lib/apt/lists/partial && \
    apt-get update && apt-get install -y \
    ruby-full \
    build-essential \
    zlib1g-dev \
    git \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Install bundler
RUN gem install bundler jekyll

# Create coder user (should already exist in enterprise-base but ensure it's set up)
RUN usermod -s /bin/bash coder 2>/dev/null || useradd -u 1000 -m -s /bin/bash coder
RUN echo "coder ALL=(ALL) NOPASSWD:ALL" > /etc/sudoers.d/coder

# Set up directories
RUN mkdir -p /projects && chown -R coder:coder /projects

# Switch to coder user
USER coder
WORKDIR /home/coder

# Set up Ruby environment for coder user
RUN echo 'export PATH="$HOME/.gem/ruby/3.0.0/bin:$PATH"' >> ~/.bashrc
RUN echo 'export GEM_HOME="$HOME/.gem/ruby/3.0.0"' >> ~/.bashrc