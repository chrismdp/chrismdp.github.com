---
layout: post
title: "Run Claude Code From Your Phone"
date: 2026-02-10 09:00:00 +0000
categories:
- ai
- claude-code
- productivity
---

Your laptop is a terrible development environment. It sleeps when you close the lid, loses state when you reboot, and chains you to a single device. The solution is obvious once you see it: run your development environment on a cheap cloud server and connect from whatever device is in front of you.

I spent a week with [OpenClaw](/dont-let-your-ceo-install-openclaw/), the always-on Claude agent that promised to solve this problem, but it did not deliver. So I uninstalled it and set up Claude Code on a VPS instead. The setup costs less than a coffee subscription, and now I connect from my laptop at my desk, from my phone on the train, from a borrowed computer at a conference. The server is the constant, and my devices are just windows into it.

<!--more-->

## The Setup

The full setup takes about an hour:

**First fifteen minutes**: provision a VPS, SSH in, update packages, create a user account.

**Next fifteen minutes**: configure SSH keys, harden security, install tmux with persistence plugins.

**Next fifteen minutes**: install Node.js and Claude Code, authenticate, configure sensible defaults.

**Final fifteen minutes**: install Termius on your phone, add your VPS as a host, connect and verify everything works.

## Choosing a VPS Provider

You need a basic Linux VPS with SSH access. Any provider works, but I recommend [Hostinger](https://www.hostinger.com/){:target="_blank"} for their competitive pricing and reliable uptime.[^hostinger] When you set up your VPS, look for the application templates and search for "Claude Code". Hostinger will pre-install Claude Code and Node.js for you, which saves time on the installation steps below. You will still need to handle security hardening and mobile access yourself. Look for Ubuntu 24.04 LTS, at least 2GB RAM (4GB is more comfortable), and decent network connectivity. Most providers offer this for under £10 per month.[^thenetworkchuck]

[^hostinger]: I am setting up an affiliate code with Hostinger. Check back soon for a discount link.

[^thenetworkchuck]: NetworkChuck has an excellent [video walkthrough](https://www.youtube.com/watch?v=FEDiAHzS0zw){:target="_blank"} and [GitHub guide](https://github.com/theNetworkChuck/remote-claude-code){:target="_blank"} covering this setup if you prefer video instructions.

Once you have your server, the rest is configuration. SSH in and start setting up your environment:

```bash
ssh root@your-server-ip
```

## Base System Setup

Start with a fresh Ubuntu 24.04 installation. Update everything and install the core packages you will need for development and terminal work.

```bash
sudo apt update && sudo apt upgrade -y
sudo apt install -y git curl jq tmux python3 python3-pip build-essential
```

Create a non-root user if your VPS provider gave you only root access. Working as root is asking for trouble, and Claude Code should run under a regular user account with sudo privileges when needed.

```bash
sudo adduser yourname
sudo usermod -aG sudo yourname
```

Switch to your new user:

```bash
su - yourname
```

Set up your directory structure. I keep code repositories in `~/code`, personal scripts in `~/bin`, and let Claude Code manage its own configuration in `~/.claude`. Create a logical structure that makes sense for how you work, and stick to it.

```bash
mkdir -p ~/code ~/bin ~/.local/bin ~/.config
```

## SSH Keys and Security

Copy your SSH public key to the server for passwordless login. This is essential for mobile access because typing passwords on a phone keyboard is miserable, and you want the connection to be as frictionless as possible.

On your local machine, if you do not already have an SSH key:

```bash
ssh-keygen -t ed25519 -C "your-email@example.com"
```

Copy the public key to your server:

```bash
ssh-copy-id yourname@your-server-ip
```

Consider disabling password authentication entirely once key-based auth works. This makes your server significantly more secure against brute-force attacks:

```bash
sudo sed -i 's/#PasswordAuthentication yes/PasswordAuthentication no/' /etc/ssh/sshd_config
sudo sed -i 's/PasswordAuthentication yes/PasswordAuthentication no/' /etc/ssh/sshd_config
sudo systemctl restart ssh
```

## Hardening Your Server

Your VPS is accessible to the entire internet, so take a few minutes to lock it down. Install fail2ban to automatically block IP addresses that attempt brute-force attacks:

```bash
sudo apt install -y fail2ban
sudo systemctl enable fail2ban
sudo systemctl start fail2ban
```

Enable the firewall and allow only SSH traffic:

```bash
sudo ufw allow 22
sudo ufw enable
```

These two steps block the most common attacks. If you plan to run web services on the same VPS, you can open additional ports later with `ufw allow 80` and `ufw allow 443`.

## tmux: Persistent Sessions

tmux is the critical piece that makes mobile access practical. Without it, closing your SSH connection kills whatever you were running. With tmux, your session persists on the server. You can disconnect, reconnect hours later from a different device, and find everything exactly as you left it.

Create a configuration file that makes tmux pleasant to use:

```bash
cat > ~/.tmux.conf << 'EOF'
set -g mouse on
set -g default-terminal "tmux-256color"
setw -g mode-keys vi
set -g status-right "%H:%M"

# Plugins for session persistence
set -g @plugin 'tmux-plugins/tpm'
set -g @plugin 'tmux-plugins/tmux-resurrect'
run '~/.tmux/plugins/tpm/tpm'
EOF
```

The tmux-resurrect plugin saves and restores your session layout across server reboots. Install the plugin manager:

```bash
git clone https://github.com/tmux-plugins/tpm ~/.tmux/plugins/tpm
```

Then start tmux and press `prefix + I` to install the plugins. Your sessions will now survive everything except a complete server wipe.

Add this to your `~/.bashrc` to automatically attach to tmux when you SSH in:

```bash
cat >> ~/.bashrc << 'EOF'

# Auto-attach to tmux
if command -v tmux &>/dev/null && [ -z "$TMUX" ]; then
    tmux attach -t main 2>/dev/null || tmux new -s main
fi
EOF
```

Now every SSH connection drops you straight into your persistent session.

## Installing Claude Code

Claude Code requires Node.js. Install the LTS version:

```bash
curl -fsSL https://deb.nodesource.com/setup_lts.x | sudo -E bash -
sudo apt install -y nodejs
```

Then install Claude Code globally:

```bash
npm install -g @anthropic-ai/claude-code
```

Run `claude` once to authenticate. You will need your Anthropic API key, or you can use `claude login` to authenticate via the browser.

Claude Code stores its configuration in `~/.claude/`. This is where your settings, session history, and any custom skills live. Create a `settings.json` to pre-approve common git operations so you do not have to confirm them on every commit:

```bash
mkdir -p ~/.claude
cat > ~/.claude/settings.json << 'EOF'
{
  "permissions": {
    "allow": [
      "Bash(git add:*)",
      "Bash(git commit:*)",
      "Bash(git push:*)"
    ],
    "defaultMode": "acceptEdits"
  }
}
EOF
```

## Connecting from Your Phone

[Termius](https://termius.com/){:target="_blank"} is an SSH client that runs on iOS and Android. It is polished, handles keys properly, and the free tier is sufficient for personal use.

Add your VPS as a new host in Termius using your server's IP address or hostname. You can import an existing SSH key, or generate one directly in the app. To generate a key in Termius, go to Keychain, tap the plus icon, select "Generate Key", and give it a name. Then hold down on the key, tap "Share", and "Export to Host" to push it to your VPS. This is the cleanest workflow if you are setting everything up from your phone.

Once your key is exported, edit your host in Termius and remove the password. You should now connect using only the key. If you have already disabled password authentication on the server, this is the only way in.

Connect and you should land directly in your tmux session with Claude Code ready to go. The experience is nearly identical to using a desktop terminal, just smaller.

## Why Mobile Coding Works Now

I have tried mobile coding before. Every attempt failed for the same reason: typing code on a phone is miserable. Brackets, semicolons, precise indentation, all painful on a touchscreen.

Claude Code inverts this problem. You are not typing code. You are having a conversation about code. Natural language works fine on a phone keyboard, and even better with voice dictation. Saying "add error handling to the checkout flow" is easy. Typing the equivalent code changes is not. Claude handles the translation.

This connects to a broader shift in how we work with AI. As I wrote in [Claude Code Is For Everything](/claude-code-is-for-everything/), the tool becomes genuinely useful when you give it more context and more persistent memory. A VPS with tmux sessions provides exactly that persistence. Your Claude Code conversations survive between connections, retaining context about what you were working on.

## What I Actually Use It For

After several weeks of mobile Claude Code, I have settled into patterns.

**Quick fixes** are the obvious use case. Typos, small bugs, config changes. Things that would nag at me until I got back to a proper computer. Now I fix them in the moment and move on.

**Code review** works surprisingly well on mobile. Reading diffs and discussing changes with Claude requires no code typing, just reading and commenting. The conversation interface suits the small screen better than a traditional IDE would.

**Planning sessions** are perhaps the best mobile use case. Describing what I want to build, having Claude sketch out approaches, thinking through architecture. The conversation-first nature suits mobile perfectly. I have had some of my most productive design discussions while walking the dog.

**Emergencies** round out the practical uses. Production issues do not wait for convenient timing. Being able to investigate and potentially fix problems from anywhere is genuinely valuable. I once diagnosed and fixed a deployment issue from the queue at a coffee shop, which would have been impossible without this setup.

What I do not use it for: writing substantial new features, complex refactoring, anything requiring careful visual inspection of code. The screen is too small and the context too fragmented for deep work.

## Automation: Keep It Running

A VPS enables automation that would be impractical on a laptop that sleeps and wakes unpredictably. I run cron jobs that sync my notes to git every five minutes, export Claude Code session logs for later review, and ping me via Telegram when something needs attention.

Here is a [simple vault sync script](https://github.com/chrismdp/dotfiles/blob/main/bin/vault-sync.sh){:target="_blank"} that keeps a repository backed up automatically. Add it to crontab to run every few minutes:

```bash
crontab -e
```

Then add this line:

```bash
*/5 * * * * ~/bin/vault-sync.sh
```

Your work saves itself. No more "did I commit that before I left the house" anxiety.

## The Honest Assessment

Mobile Claude Code makes certain things easier and makes overwork more convenient. Whether that is net positive depends entirely on your discipline.

The friction that kept me from working everywhere was also protecting my downtime. When coding required a laptop, I had natural boundaries. Cannot code on the train, no laptop. Cannot code waiting for the kids, too awkward. Cannot code in bed, well, I could, but it felt excessive.

Now I can do all of those things. Every spare moment becomes a potential coding session. The queue at the coffee shop. The five minutes before a meeting. The gap between putting kids to bed and dinner being ready.

For me, the ability to clear small tasks from anywhere reduces the mental load of "things I need to remember to do later." That is worth something. But I have also had to set explicit rules: no coding after 9pm, no coding during family activities, no coding just because I could. The tool does not enforce boundaries. I have to.

If you struggle with work-life separation, this might make things worse. If you are good at boundaries but frustrated by the friction of context-switching back to work, this might be exactly what you need.

I wrote about [how I use AI tools daily](/coding-with-ai/) and this setup has become central to that workflow. If you want to extend it further with custom skills and automation, [I covered that process too](/how-to-use-claude-code-skills/).
