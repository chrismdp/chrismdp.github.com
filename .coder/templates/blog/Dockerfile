FROM codercom/enterprise-base:ubuntu

# Set non-interactive frontend to avoid prompts during build
ENV DEBIAN_FRONTEND=noninteractive

# Fix apt permissions and install Ruby and Jekyll dependencies
# Note: enterprise-base may need sudo even in Dockerfile
RUN sudo mkdir -p /var/lib/apt/lists/partial && \
    sudo chmod 755 /var/lib/apt/lists/partial && \
    sudo apt-get update && sudo apt-get install -y \
    ruby-full \
    build-essential \
    zlib1g-dev \
    git \
    curl \
    && sudo rm -rf /var/lib/apt/lists/*

# Install bundler
RUN sudo gem install bundler jekyll

# Create coder user (should already exist in enterprise-base but ensure it's set up)
RUN sudo usermod -s /bin/bash coder 2>/dev/null || sudo useradd -u 1000 -m -s /bin/bash coder
RUN echo "coder ALL=(ALL) NOPASSWD:ALL" | sudo tee /etc/sudoers.d/coder

# Set up directories
RUN sudo mkdir -p /projects && sudo chown -R coder:coder /projects

# Switch to coder user
USER coder
WORKDIR /home/coder

# Set up Ruby environment for coder user
RUN echo 'export PATH="$HOME/.gem/ruby/3.0.0/bin:$PATH"' >> ~/.bashrc
RUN echo 'export GEM_HOME="$HOME/.gem/ruby/3.0.0"' >> ~/.bashrc