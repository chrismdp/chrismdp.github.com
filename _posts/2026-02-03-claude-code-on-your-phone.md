---
layout: post
title: "Run Claude Code From Your Phone"
date: 2026-02-03 09:00:00 +0000
image: /assets/img/claude-code-phone-hero.jpg
infographic: /assets/img/claude-code-phone-infographic.jpg
categories:
- ai
- claude-code
- productivity
---

Your laptop is a terrible development environment. It sleeps when you close the lid, loses state when you reboot, and chains you to a single device. The solution is obvious once you see it: run your development environment on a cheap cloud server and connect from whatever device is in front of you.

I spent a week with [OpenClaw](/dont-let-your-ceo-install-openclaw/), the always-on Claude agent that promised to solve this problem, but it did not deliver. So I uninstalled it and set up Claude Code on a VPS instead. The setup costs less than a coffee subscription, and now I connect from my laptop at my desk, from my phone on the train, from an iPad at a conference. The server is the constant, and my devices are just windows into it. Whether that is a superpower or a recipe for burnout depends on your discipline.

<!--more-->

## What I Use It For

After a week, here is what works for me:

**Writing and blogging** is where I spend most of my time. Drafting posts, editing articles, working through ideas. Voice dictation using Wispr Flow works even better than typing.[^wispr]

[^wispr]: [Wispr Flow](https://wisprflow.ai/r?CHRIS104){:target="_blank"} is an excellent voice-to-text app. This is a referral link, but I would recommend it regardless.

**Code** of all kinds: quick fixes, new features, refactoring. I have tried mobile coding before and every attempt failed because typing code on a phone is miserable. Brackets, semicolons, precise indentation, all painful on a touchscreen. Claude Code inverts this. You are not typing code, you are having a conversation, and Claude handles the translation.

**Reminders and automation**. I have a heartbeat script running on the server every thirty minutes that spawns a small Claude Code prompt to check my reminders. I have a Max 20 subscription, so I can afford the tokens. When something needs attention, it pings me via Telegram. The server never sleeps, so the reminders work.

**Planning and strategy**. Describing what I want to build, having Claude sketch out approaches. I have had productive design sessions while travelling or walking.

**Emergencies**. Production issues do not wait for convenient timing. I can now diagnose and fix deployment issues from the queue at a coffee shop.

The small screen requires workarounds. When I need to read a diff properly, I push a PR and review it on GitHub's mobile site. When I need to extract a document or preview an image, I use the `gog` CLI tool to post it to a shared Google Drive folder where I can grab it on my phone.[^gog]

[^gog]: [`gog`](https://github.com/skyscrapr/gog){:target="_blank"} is a command-line Google Drive client. Install with `go install github.com/skyscrapr/gog@latest` and authenticate with `gog auth add --manual` (the manual flag lets you copy/paste the OAuth URL since the VPS cannot open a browser).

## The Setup

The full setup takes about an hour, broken into four stages: provision a VPS and create a user account, configure SSH keys and harden security, install Claude Code with sensible defaults, and finally set up Termius on your phone.

### Choosing a VPS Provider

You need a basic Linux VPS with SSH access. Any provider works, but I recommend [Hostinger](https://www.hostinger.com/){:target="_blank"} for their competitive pricing and reliable uptime. When you set up your VPS, look for the application templates and search for "Claude Code". Hostinger will pre-install Claude Code and Node.js for you, which saves time on the installation steps below. You will still need to handle security hardening and mobile access yourself. Look for Ubuntu 24.04 LTS (Long Term Support), at least 2GB RAM (4GB is more comfortable), and decent network connectivity. Most providers offer this for under £10 per month.[^thenetworkchuck]

[^thenetworkchuck]: NetworkChuck has an excellent [video walkthrough](https://www.youtube.com/watch?v=FEDiAHzS0zw){:target="_blank"} and [GitHub guide](https://github.com/theNetworkChuck/remote-claude-code){:target="_blank"} covering this setup if you prefer video instructions.

Once you have your server, SSH in and start setting up your environment:

{% highlight bash %}
ssh root@your-server-ip
{% endhighlight %}

### Base System Setup

Start with a fresh Ubuntu 24.04 installation. Update everything and install the core packages you will need for development and terminal work.

{% highlight bash %}
sudo apt update && sudo apt upgrade -y
sudo apt install -y git curl jq tmux python3 python3-pip build-essential
{% endhighlight %}

Create a non-root user if your VPS provider gave you only root access. Working as root is asking for trouble, and Claude Code should run under a regular user account with sudo privileges when needed.

{% highlight bash %}
sudo adduser yourname
sudo usermod -aG sudo yourname
{% endhighlight %}

Switch to your new user:

{% highlight bash %}
su - yourname
{% endhighlight %}

Set up your directory structure. I keep code repositories in `~/code`, personal scripts in `~/bin`, and let Claude Code manage its own configuration in `~/.claude`. Create a logical structure that makes sense for how you work, and stick to it.

{% highlight bash %}
mkdir -p ~/code ~/bin ~/.local/bin ~/.config
{% endhighlight %}

### SSH Keys and Security

Copy your SSH public key to the server for passwordless login. This is essential for mobile access because typing passwords on a phone keyboard is miserable.

On your local machine, if you do not already have an SSH key:

{% highlight bash %}
ssh-keygen -t ed25519 -C "your-email@example.com"
{% endhighlight %}

Copy the public key to your server:

{% highlight bash %}
ssh-copy-id yourname@your-server-ip
{% endhighlight %}

You can do the same from your phone. [Termius](https://termius.com/){:target="_blank"} is an SSH client for iOS and Android that handles keys properly. To generate a key in Termius, go to Keychain, tap the plus icon, select "Generate Key", and give it a name. Then hold down on the key, tap "Share", and "Export to Host" to push it to your VPS.

Once key-based auth works from both devices, consider disabling password authentication entirely. This makes your server significantly more secure against brute-force attacks:

{% highlight bash %}
sudo sed -i 's/#PasswordAuthentication yes/PasswordAuthentication no/' /etc/ssh/sshd_config
sudo sed -i 's/PasswordAuthentication yes/PasswordAuthentication no/' /etc/ssh/sshd_config
sudo systemctl restart ssh
{% endhighlight %}

### Hardening Your Server

Your VPS is accessible to the entire internet, so take a few minutes to lock it down. Install fail2ban to automatically block IP addresses that attempt brute-force attacks:

{% highlight bash %}
sudo apt install -y fail2ban
sudo systemctl enable fail2ban
sudo systemctl start fail2ban
{% endhighlight %}

Enable the firewall and allow only SSH traffic:

{% highlight bash %}
sudo ufw allow 22
sudo ufw enable
{% endhighlight %}

These two steps block the most common attacks. If you plan to run web services on the same VPS, you can open additional ports later with `ufw allow 80` and `ufw allow 443`.

### tmux: Persistent Sessions

tmux is the critical piece that makes mobile access practical. Without it, closing your SSH connection kills whatever you were running. With tmux, your session persists on the server. You can disconnect, reconnect hours later from a different device, and find everything exactly as you left it.

Create a configuration file that makes tmux pleasant to use:

{% highlight bash %}
cat > ~/.tmux.conf << 'EOF'
set -g mouse on
set -g default-terminal "tmux-256color"
setw -g mode-keys vi
set -g status-right "%H:%M"
EOF
{% endhighlight %}

Add this to your `~/.bashrc` to automatically attach to tmux when you SSH in:

{% highlight bash %}
cat >> ~/.bashrc << 'EOF'

# Auto-attach to tmux
if command -v tmux &>/dev/null && [ -z "$TMUX" ]; then
    tmux attach -t main 2>/dev/null || tmux new -s main
fi
EOF
{% endhighlight %}

Now every SSH connection drops you straight into your persistent session.

### Installing Claude Code

Claude Code requires Node.js. Install the LTS version:

{% highlight bash %}
curl -fsSL https://deb.nodesource.com/setup_lts.x | sudo -E bash -
sudo apt install -y nodejs
{% endhighlight %}

Then install Claude Code globally:

{% highlight bash %}
npm install -g @anthropic-ai/claude-code
{% endhighlight %}

Run `claude` once to authenticate. You will need your Anthropic API key, or you can use `claude login` to authenticate via the browser. Since the VPS cannot open browser windows, you will need to copy the URL it prints, open it on your local machine, complete authentication, then copy the resulting key back to the terminal. This is fiddly but only needs doing once.

### Connecting from Your Phone

Add your VPS as a new host in Termius using your server's IP address or hostname. If you set up your key earlier, it should connect without a password. Connect and you should land directly in your tmux session with Claude Code ready to go.

<figure class="float-right w-1/3 ml-6 mb-4">
<img src="/assets/img/termius-claude-code.jpg" alt="Termius running Claude Code on iPhone" class="rounded-lg" />
<figcaption class="text-sm text-brand-black/60 mt-2 text-center italic">Editing a blog post, Saturday lunchtime while making coffee.</figcaption>
</figure>

## Automation

A VPS enables automation that would be impractical on a laptop that sleeps and wakes unpredictably. I run cron jobs that sync my notes to git every five minutes, export Claude Code session logs for later review, and ping me via Telegram when something needs attention.

Here is a [simple vault sync script](https://github.com/chrismdp/dotfiles/blob/master/bin/vault-sync.sh){:target="_blank"} that keeps a repository backed up automatically. Add it to crontab to run every few minutes:

{% highlight bash %}
crontab -e
{% endhighlight %}

Then add this line:

{% highlight bash %}
*/5 * * * * ~/bin/vault-sync.sh
{% endhighlight %}

Your work saves itself. No more "did I commit that before I left the house" anxiety.

## The Honest Assessment

Mobile Claude Code makes certain things easier and makes overwork more convenient. Whether that is net positive depends entirely on your discipline.

The friction that kept me from working everywhere was also protecting my downtime. When coding required a laptop, I had natural boundaries: no laptop on the train, too awkward while waiting for the kids, excessive in bed.

Now I can do all of those things. Every spare moment becomes a potential coding session: the queue at the coffee shop, the five minutes before a meeting, the gap between putting kids to bed and dinner being ready.

For me, the ability to clear small tasks from anywhere reduces the mental load of "things I need to remember to do later." That is worth something. But I have also had to set explicit rules. The tool does not enforce boundaries. I have to.

If you struggle with work-life separation, this setup might make things worse. If you are good at boundaries but frustrated by the friction of context-switching back to work, this might be exactly what you need.

## Where to Go Next

I wrote about [how I use AI tools daily](/coding-with-ai/) and [why repositories beat chatbots for writing and thinking](/writing-and-thinking-with-ai-why-repositories-beat-chatbots/), and this setup has become central to both workflows. If you want to extend it further with custom skills and automation, [I covered that process too](/how-to-use-claude-code-skills/).

The server is always on, the session is always waiting, and my phone is always in my pocket. Whether that is a superpower or a trap is up to you.
