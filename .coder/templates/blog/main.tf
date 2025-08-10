terraform {
  required_providers {
    coder = {
      source = "coder/coder"
    }
    docker = {
      source = "kreuzwerker/docker"
    }
  }
}

provider "docker" {}

# Coder Login module for authentication with Coder instance
module "coder-login" {
  count    = data.coder_workspace.me.start_count
  source   = "registry.coder.com/coder/coder-login/coder"
  agent_id = coder_agent.main.id
}

# The Claude Code module does the automatic task reporting
module "claude-code" {
  count               = data.coder_workspace.me.start_count
  source              = "registry.coder.com/coder/claude-code/coder"
  version             = "2.0.0"
  agent_id            = coder_agent.main.id
  folder              = "/projects/blog"
  install_claude_code = false  # Install manually in setup script instead
  claude_code_version = "latest"
  order               = 999

  experiment_post_install_script = data.coder_parameter.setup_script.value

  # This enables Coder Tasks - disabled for debugging
  experiment_report_tasks = false
}

# We are using presets to set the prompts, image, and set up instructions
data "coder_workspace_preset" "default" {
  name    = "Chris MDP Blog Development"
  default = true
  parameters = {
    "system_prompt" = <<-EOT
      You are a helpful assistant running inside a Coder Workspace for Jekyll blog development.
      
      The blog project is located at /projects/blog. This is a Jekyll blog using GitHub Pages.
      
      Key files and structure:
      - _config.yml: Jekyll configuration
      - _posts/: Blog posts in Markdown format
      - _layouts/: Page templates
      - _includes/: Reusable template components
      - Gemfile: Ruby dependencies (uses github-pages gem)
      
      Common commands:
      - bundle install: Install Ruby gems
      - bundle exec jekyll serve: Start development server
      - bundle exec jekyll build: Build the site
      
      IMPORTANT: 
      - Do NOT push to git until we've had a chance to review the changes together
      - Always ask if anything is missing or unclear before proceeding with implementation
      - When making changes, explain what you're doing so we can ensure it aligns with expectations
      - NEVER automatically update your own Coder workspace - always let the user decide when to update the workspace
    EOT

    "setup_script" = <<-EOT
    set -x  # Enable debug output
    
    echo "Starting blog setup script..."
    whoami
    id
    
    # Wait for container to be fully ready
    echo "Waiting 3 seconds for container to be ready..."
    sleep 3
    
    echo "Navigating to /projects directory..."
    cd /projects

    # Ensure PATH includes pre-installed tools
    export PATH="$HOME/.local/bin:$PATH"
    
    # Install Claude Code manually for coder user (avoids permission issues with module)
    if ! command -v claude >/dev/null 2>&1; then
      echo "Installing Claude Code for coder user..."
      echo "Debug: Current user: $(whoami)"
      echo "Debug: HOME: $HOME"
      
      # Install Claude Code using curl method (more reliable than npm in containers)
      curl -fsSL https://claude.ai/install.sh | sh
      export PATH="$HOME/.local/bin:$PATH"
      echo "Claude Code installed successfully! Run 'claude login' to authenticate."
    else
      echo "Claude Code already installed: $(claude --version)"
    fi

    # Clone blog project if it doesn't exist as a proper git repository
    if [ ! -d "blog/.git" ]; then
      echo "Blog project not found or not a git repository. Cloning repository..."
      rm -rf blog  # Remove any existing non-git directory
      git clone https://github.com/chrismdp/chrismdp.github.com.git blog || {
        echo "Failed to clone blog repository. Please check network connectivity or authentication."
        echo "You can manually clone with: git clone https://github.com/chrismdp/chrismdp.github.com.git blog"
        exit 1
      }
      echo "✅ Blog project cloned to /projects/blog"
    else
      echo "✅ Blog project already exists in /projects/blog"
      cd blog
      # Only update if repo is clean (don't interfere with development)
      if git fetch 2>/dev/null; then
        if git diff-index --quiet HEAD -- && \
          [ -z "$(git status --porcelain --untracked-files=no)" ] && \
          [ -z "$(git log --branches --not --remotes)" ]; then
          echo "Repo is clean. Pulling latest changes..."
          git pull
        else
          echo "Repo has uncommitted or unpushed changes. Skipping pull to preserve work."
        fi
      else
        echo "Warning: git fetch failed, skipping pull"
      fi
      cd ..
    fi

    # Create symlink for easy access (only if it doesn't exist)
    if [ ! -L ~/blog ] && [ ! -e ~/blog ]; then
      ln -sf /projects/blog ~/blog
    fi

    # Navigate to project
    cd /projects/blog

    # Install Ruby dependencies if Gemfile exists
    if [ -f "Gemfile" ]; then
      echo "Installing Ruby dependencies..."
      bundle install
      
      echo "Dependencies installed. Run 'bundle exec jekyll serve' to start the development server."
    else
      echo "No Gemfile found - repository may need to be cloned manually."
    fi
    EOT

    "preview_port"    = "4000"
  }
}

# Advanced parameters (these are all set via preset)
data "coder_parameter" "system_prompt" {
  name         = "system_prompt"
  display_name = "System Prompt"
  type         = "string"
  form_type    = "textarea"
  description  = "System prompt for the agent with generalized instructions"
  mutable      = false
}
data "coder_parameter" "ai_prompt" {
  type        = "string"
  name        = "AI Prompt"
  default     = ""
  description = "Write a prompt for Claude Code"
  mutable     = true
}
data "coder_parameter" "setup_script" {
  name         = "setup_script"
  display_name = "Setup Script"
  type         = "string"
  form_type    = "textarea"
  description  = "Script to run before running the agent"
  mutable      = false
}
data "coder_parameter" "preview_port" {
  name         = "preview_port"
  display_name = "Preview Port"
  description  = "The port the Jekyll server is running on to preview in Tasks"
  type         = "number"
  default      = "4000"
  mutable      = false
}

# Environment variables for Claude Code (no API key needed for claude login)
resource "coder_env" "claude_task_prompt" {
  agent_id = coder_agent.main.id
  name     = "CODER_MCP_CLAUDE_TASK_PROMPT"
  value    = data.coder_parameter.ai_prompt.value
}
resource "coder_env" "app_status_slug" {
  agent_id = coder_agent.main.id
  name     = "CODER_MCP_APP_STATUS_SLUG"
  value    = "blog"
}
resource "coder_env" "claude_system_prompt" {
  agent_id = coder_agent.main.id
  name     = "CODER_MCP_CLAUDE_SYSTEM_PROMPT"
  value    = data.coder_parameter.system_prompt.value
}

data "coder_provisioner" "me" {}
data "coder_workspace" "me" {}
data "coder_workspace_owner" "me" {}

resource "coder_agent" "main" {
  arch           = data.coder_provisioner.me.arch
  os             = "linux"
  startup_script = <<-EOF
    #!/bin/sh
    set -e

    # Ensure /projects directory has correct ownership (mounted from persistent volume)
    echo "Setting up persistent /projects directory permissions..."
    sudo chown -R coder:coder /projects || echo "Failed to set /projects ownership, continuing..."
    sudo chmod 755 /projects || echo "Failed to set /projects permissions, continuing..."
    
    # Debug: Show startup environment
    echo "=== STARTUP SCRIPT DEBUG ==="
    echo "Current time: $(date)"
    echo "Working directory: $(pwd)"
    echo "Home directory: $HOME"
    echo "User: $(whoami)"
    echo "Home directory contents BEFORE any changes:"
    ls -la $HOME/ || echo "Home directory doesn't exist or is empty"
    
    # Check for persistence indicators
    echo "Checking persistence indicators:"
    if [ -f ~/.init_done ]; then
      echo "✓ ~/.init_done exists - this should be a persistent restart"
      echo "Contents of ~/.init_done:"
      cat ~/.init_done || echo "File exists but is empty"
    else
      echo "✗ ~/.init_done does not exist - this appears to be first startup"
    fi
    
    # Ensure persistent home directory exists with correct permissions
    echo "Setting up persistent home directory permissions..."
    USER_HOME_DIR="/host-workspace-homes/${data.coder_workspace_owner.me.id}"
    if [ -d "$USER_HOME_DIR" ]; then
      echo "User home directory exists, checking/fixing permissions..."
      sudo chown -R 1000:1000 "$USER_HOME_DIR" 2>/dev/null || echo "Some files may have been moved, continuing..."
      sudo chmod 755 "$USER_HOME_DIR"
      echo "Permissions fixed for $USER_HOME_DIR"
    else
      echo "Creating user home directory with correct permissions..."
      sudo mkdir -p "$USER_HOME_DIR"
      sudo chown -R 1000:1000 "$USER_HOME_DIR"
      sudo chmod 755 "$USER_HOME_DIR"
      echo "Created $USER_HOME_DIR with proper permissions"
    fi
    
    # Prepare user home with default files on first start.
    echo "Checking if we need to initialize home directory..."
    if [ ! -f ~/.init_done ]; then
      echo "First time setup detected - preparing home directory"
      echo "Contents of /etc/skel:"
      ls -la /etc/skel/ || echo "/etc/skel directory not found"
      
      echo "Copying skeleton files (without overwriting existing files)..."
      # Use -n to not overwrite existing files, much safer
      cp -rn /etc/skel/. ~ 2>/dev/null || echo "No skeleton files to copy or copy failed"
      
      echo "Creating ~/.init_done marker with timestamp..."
      echo "Initialized at $(date)" > ~/.init_done
      
      echo "Home directory contents AFTER skeleton copy:"
      ls -la $HOME/
    else
      echo "Skipping home initialization - ~/.init_done exists"
      echo "Init marker content: $(cat ~/.init_done)"
    fi
    
    echo "=== END STARTUP SCRIPT DEBUG ==="
  EOF

  # These environment variables allow you to make Git commits right away after creating a
  # workspace. Note that they take precedence over configuration defined in ~/.gitconfig!
  env = {
    GIT_AUTHOR_NAME     = coalesce(data.coder_workspace_owner.me.full_name, data.coder_workspace_owner.me.name)
    GIT_AUTHOR_EMAIL    = "${data.coder_workspace_owner.me.email}"
    GIT_COMMITTER_NAME  = coalesce(data.coder_workspace_owner.me.full_name, data.coder_workspace_owner.me.name)
    GIT_COMMITTER_EMAIL = "${data.coder_workspace_owner.me.email}"
  }

  # The following metadata blocks are optional. They are used to display
  # information about your workspace in the dashboard. You can remove them
  # if you don't want to display any information.
  metadata {
    display_name = "CPU Usage"
    key          = "0_cpu_usage"
    script       = "coder stat cpu"
    interval     = 10
    timeout      = 1
  }

  metadata {
    display_name = "RAM Usage"
    key          = "1_ram_usage"
    script       = "coder stat mem"
    interval     = 10
    timeout      = 1
  }

  metadata {
    display_name = "Home Disk"
    key          = "3_home_disk"
    script       = "coder stat disk --path $HOME"
    interval     = 60
    timeout      = 1
  }
}

# See https://registry.coder.com/modules/coder/code-server
module "code-server" {
  count  = data.coder_workspace.me.start_count
  folder = "/projects/blog"
  source = "registry.coder.com/coder/code-server/coder"

  settings = {
    "workbench.colorTheme" : "Default Dark Modern"
  }

  subdomain = true

  # This ensures that the latest non-breaking version of the module gets downloaded
  version = "~> 1.0"

  agent_id = coder_agent.main.id
  order    = 1
}

module "vscode" {
  count    = data.coder_workspace.me.start_count
  source   = "registry.coder.com/coder/vscode-desktop/coder"
  version  = "1.1.0"
  agent_id = coder_agent.main.id
  folder   = "/projects/blog"
}

resource "coder_app" "preview" {
  agent_id     = coder_agent.main.id
  slug         = "blog"
  display_name = "Blog Preview"
  icon         = "https://chrismdp.com/assets/favicons/favicon.ico"
  url          = "http://localhost:${data.coder_parameter.preview_port.value}"
  share        = "public"
  subdomain    = true
  open_in      = "tab"
  order        = 0
  healthcheck {
    url       = "http://localhost:${data.coder_parameter.preview_port.value}/"
    interval  = 5
    threshold = 15
  }
}

resource "coder_app" "jekyll_server" {
  agent_id     = coder_agent.main.id
  slug         = "jekyll-server"
  display_name = "Jekyll Server Terminal"
  icon         = "${data.coder_workspace.me.access_url}/emojis/1f6e0.png"
  command      = <<-EOF
    bash -c '
      cd /projects/blog
      # Check if tmux session exists and attach to it, otherwise create new one
      if tmux has-session -t jekyll-server 2>/dev/null; then
        echo "Attaching to existing Jekyll server session..."
        tmux attach-session -t jekyll-server
      else
        echo "Creating new Jekyll server session..."
        tmux new-session -d -s jekyll-server -c /projects/blog "bundle exec jekyll serve --host 0.0.0.0 --port 4000 --livereload || bash"
        tmux attach-session -t jekyll-server
      fi
    '
  EOF
  share        = "authenticated"
  subdomain    = true
  open_in      = "tab"
  order        = 3
}

resource "coder_app" "vim" {
  agent_id     = coder_agent.main.id
  slug         = "vim"
  display_name = "Vim"
  icon         = "https://raw.githubusercontent.com/coder/coder/main/site/static/icon/vim.svg"
  command      = <<-EOF
    bash -c '
      cd /projects/blog
      # Check if tmux session exists and attach to it, otherwise create new one
      if tmux has-session -t vim-session 2>/dev/null; then
        echo "Attaching to existing vim session..."
        tmux attach-session -t vim-session
      else
        echo "Creating new vim session..."
        tmux new-session -d -s vim-session -c /projects/blog "vim || bash"
        tmux attach-session -t vim-session
      fi
    '
  EOF
  share        = "authenticated"
  subdomain    = true
  open_in      = "tab"
  order        = 4
}

resource "coder_app" "claude_code" {
  agent_id     = coder_agent.main.id
  slug         = "claude-code"
  display_name = "Claude Code"
  icon         = "https://claude.ai/favicon.ico"
  command      = <<-EOF
    bash -c '
      cd /projects/blog
      # Check if tmux session exists and attach to it, otherwise create new one
      if tmux has-session -t claude-code 2>/dev/null; then
        echo "Attaching to existing Claude Code session..."
        tmux attach-session -t claude-code
      else
        echo "Creating new Claude Code session..."
        tmux new-session -d -s claude-code -c /projects/blog "claude || bash"
        tmux attach-session -t claude-code
      fi
    '
  EOF
  share        = "authenticated"
  subdomain    = true
  open_in      = "tab"
  order        = 5
}

# Build custom image for blog development
resource "null_resource" "build_blog_image" {
  count = data.coder_workspace.me.start_count

  # Rebuild if Dockerfile changes or force rebuild
  triggers = {
    dockerfile_hash = filemd5("${path.module}/Dockerfile")
    force_rebuild = timestamp()
  }

  provisioner "local-exec" {
    command = <<-EOF
      set -e
      echo "=== BUILDING BLOG DEVELOPMENT IMAGE ==="
      cd ${path.module}
      
      # Clean up dangling images before building to save disk space
      echo "Cleaning up dangling Docker images..."
      docker image prune -f || echo "No dangling images to prune"
      
      # Build image with Ruby and Jekyll pre-installed (cache bust with timestamp)
      DOCKER_BUILDKIT=0 docker build --build-arg CACHE_BUST=$(date +%s) -t chrismdpcom/blog-coder:latest .
      
      # Clean up any intermediate/dangling images after build
      docker image prune -f || echo "No dangling images to prune after build"
      
      echo "✅ Successfully built blog development image!"
    EOF
  }
}

# Persistent volume for /projects directory that survives workspace restarts
resource "docker_volume" "projects" {
  name = "coder-${data.coder_workspace_owner.me.name}-${lower(data.coder_workspace.me.name)}-projects"
  
  # This volume persists across workspace restarts but gets destroyed on workspace deletion
  lifecycle {
    prevent_destroy = false  # Allow destruction when workspace is deleted
  }
}

resource "docker_container" "workspace" {
  count   = data.coder_workspace.me.start_count
  name    = "coder-${data.coder_workspace_owner.me.name}-${lower(data.coder_workspace.me.name)}"
  # Use custom blog development image
  image   = "chrismdpcom/blog-coder:latest"
  
  # Prevent long destruction hangs but allow reasonable cleanup time
  stop_timeout = 60
  
  # Ensure custom image and volume are available first
  depends_on = [null_resource.build_blog_image, docker_volume.projects]
  env     = [
    "CODER_AGENT_TOKEN=${coder_agent.main.token}",
    "TZ=Europe/London"
  ]
  
  # Ensure /projects has correct permissions before agent starts
  command = ["sh", "-c", "sudo chown -R coder:coder /projects && sudo chmod 755 /projects && ${coder_agent.main.init_script}"]
  
  # Run as coder user (already set up in custom image)
  user     = "coder"
  # Hostname makes the shell more user friendly: coder@my-workspace:~$
  hostname = data.coder_workspace.me.name
  host {
    host = "host.docker.internal"
    ip   = "host-gateway"
  }
  volumes {
    container_path = "/home/coder"
    host_path      = "/home/coder/workspace-homes/${data.coder_workspace_owner.me.id}"
    read_only      = false
  }
  
  # Mount the workspace-homes parent directory so we can fix permissions from inside container
  volumes {
    container_path = "/host-workspace-homes"
    host_path      = "/home/coder/workspace-homes"
    read_only      = false
  }
  
  # Mount persistent projects volume
  volumes {
    container_path = "/projects"
    volume_name    = docker_volume.projects.name
    read_only      = false
  }

  # Add labels in Docker to keep track of orphan resources.
  labels {
    label = "coder.owner"
    value = data.coder_workspace_owner.me.name
  }
  labels {
    label = "coder.owner_id"
    value = data.coder_workspace_owner.me.id
  }
  labels {
    label = "coder.workspace_id"
    value = data.coder_workspace.me.id
  }
  labels {
    label = "coder.workspace_name"
    value = data.coder_workspace.me.name
  }
}