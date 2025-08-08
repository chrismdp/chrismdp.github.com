---
layout: post
title: "Independent Coding Agents: The Tools Aren't Ready"
date: 2025-08-08 10:00:00 +0000
categories:
- development
- infrastructure
- remote-development
- ai
---

**I spent three days trying to get [Coder](https://coder.com){:target="_blank"} working properly for Claude Code and AI agent development.** Three days that should have taken three hours. The promise was compelling: [Coder's new Tasks feature](https://coder.com/blog/launch-week-2025-introducing-coder-tasks){:target="_blank"} lets you run AI coding agents like Claude Code securely in your own infrastructure, with proper boundaries and permissions. No more local environment complexity, no more `--dangerously-skip-permissions` workarounds.

This is absolutely the future of AI development. The reality was a masterclass in infrastructure complexity that reveals we are still in the early days of tooling maturity.

<!--more-->

## The Compelling Vision

The Coder Tasks announcement painted exactly the picture I wanted: AI coding agents running as "true sidekicks" in secure, controlled environments. No more exposing sensitive information on local machines, no more slowing down development with environment setup friction.

<div style="padding: 24px 0;">
<iframe width="100%" height="450" src="https://www.youtube.com/embed/je-LId7k1Gs" title="Coder Tasks Working Demo" frameborder="0" allowfullscreen></iframe>
</div>

*The video above shows my working Coder Tasks setup after three days of configuration. Despite the complexity, it works beautifully: remote workspaces provision in 30-45 seconds with complete development environments and proper security boundaries.*

The promise was that administrators could define strict templates and boundaries, controlling which agents teams could use, with proper process isolation and tool integration. Perfect for [Kaijo](https://kaijo.ai) development where I wanted AI agents to prototype features, review documentation, and experiment freely without security concerns.

But getting there meant setting up a Coder deployment that could handle Docker-in-Docker, persistent workspaces, and secure subdomain routing. I even paid for a new Hostinger VPS to get the infrastructure right. What seemed like a straightforward infrastructure task became three days of my life I will never get back.

## Day One: Certificate Hell

The first problem hit immediately: SSL certificate issues. Coder requires wildcard certificates for subdomain routing (think `app--workspace--user.coder.domain.com`), but getting Let's Encrypt to issue wildcard certificates requires DNS-01 challenge validation.

Standard Coder documentation assumes you are happy with self-signed certificates or have access to expensive certificate management services. Neither appealed to me. After hours of debugging "no solvers available" errors, I discovered that Caddy (the reverse proxy) needed the Cloudflare DNS plugin to handle DNS-01 challenges.

This meant:
- Installing a custom Caddy build with the Cloudflare plugin
- Configuring Cloudflare API tokens with precise permissions  
- Setting up systemd environment files
- Disabling Cloudflare proxy mode to allow direct certificate validation

What should have been a simple reverse proxy setup became an expedition into DNS mechanics and certificate authority protocols.

## Day Two: Docker Inception

With SSL finally working, the next challenge was Docker-in-Docker. Coder workspaces need to run Docker containers inside Docker containers - essential for the Supabase local development stack that Kaijo requires.

The solution was Sysbox: a container runtime that provides VM-like isolation without privileged containers. Great in theory. In practice:

- Sysbox installation required stopping all Docker containers
- Ubuntu 22.04 compatibility issues required additional configuration flags
- System reboot was necessary (documented, but still frustrating)
- Runtime verification involved checking that `docker info` showed `sysbox-runc`

This took most of day two to get right, with multiple false starts and configuration iterations.

## Day Three: Supabase Stubbornness  

The final hurdle was Supabase integration. The plan was to pre-cache Supabase Docker images in the workspace template to avoid download delays. This required:

- Running `supabase start` during workspace initialisation
- Configuring persistent volume mounts for database data
- Setting up proper network routing between containers
- Managing port conflicts between multiple workspace instances

I hit Docker layer caching limits during testing through about 60 debug-build-workspace loops. Turns out my hosting provider has restrictive Docker Hub pull limits, and repeatedly rebuilding workspace templates with large image downloads quickly exhausted the quota.

By day three, I had a working setup that could spin up remote workspaces with pre-cached Supabase containers, but the complexity was staggering. The solution involved building custom Docker images with all Supabase dependencies pre-loaded to avoid Docker Hub rate limiting and workspace startup delays. More importantly, I realised this was not the most important thing for me to be working on.

This complexity was amplified by my ambitious goal: I wanted to see if I could run multiple isolated development environments simultaneously on the same machine rather than just using devcontainers locally. The challenge was setting up proper Docker-in-Docker isolation for five concurrent workspaces, each completely separated from the others. I could have fired up separate ephemeral EC2 instances for each workspace, which would probably have been simpler, but I was testing the theoretical limits of the containerised approach.

The pain points were primarily around wildcard subdomain SSL setup (requiring DNS-01 challenges and Cloudflare API integration) and the Docker-in-Docker configuration complexity. I also made things harder for myself by insisting on pre-caching Docker pulls in the parent container to avoid repeated downloads, which required significantly more complex infrastructure orchestration.

## The Infrastructure Reality Check

After three days of infrastructure wrestling, I stepped back and asked whether this was the right use of time right now. The sunk cost fallacy was pulling me deeper into infrastructure complexity when I should have been building product features. Despite the technical success achieving working remote workspaces with 30-45 second provisioning, the immediate time investment exceeded the value for my current needs. The infrastructure works beautifully once configured, but getting there requires substantial expertise in networking, SSL/TLS, container runtimes, and distributed systems that most development teams do not possess.

## What Coder Tasks Promises vs Reality

The Coder Tasks vision is genuinely compelling:

- **Secure AI agent execution**: Run coding agents in controlled environments without exposing local credentials
- **Administrative control**: Define boundaries around what agents can do and access  
- **Infrastructure isolation**: Keep heavy AI workloads off developer machines
- **Enterprise readiness**: Proper audit trails and security compliance

These are real problems that need solving, and Coder Tasks addresses them effectively once configured. But the current reality is that getting to this promised land requires substantial infrastructure expertise that most teams do not possess.

The "simple" setup guides assume knowledge of reverse proxies, SSL certificate management, container runtimes, and networking that goes well beyond typical development skills. This is not unique to Coder - it is inherent to the complexity of secure remote development infrastructure. The next generation of tooling needs to abstract this complexity much more effectively.

## The Deeper Security Problem

The infrastructure complexity was actually masking a more fundamental issue: AI coding agents with broad permissions are not safe, regardless of where they run.

Even `--dangerously-skip-permissions` in a perfectly isolated environment misses the point. Coding agents can be duped by untrusted data. If they have internet access and can execute commands, they could easily exfiltrate code or credentials. The attack vectors are not about local vs. remote infrastructure - they are about the inherent unpredictability of AI behaviour when exposed to adversarial inputs.

The real question is not "how do we give AI agents safe environments to run wild?" but "how do we supervise AI agents appropriately?" No amount of infrastructure isolation fixes the core trust problem.


## The Future Is Remote (With Better Tooling)

This experience has reinforced my belief that remote development with AI agents is absolutely the future. The Coder Tasks vision is exactly what we need: secure, controlled environments where AI agents can work as true development partners without the security risks of local execution.

The infrastructure I built works beautifully. Remote workspaces provision in 30-45 seconds with complete development environments, proper security boundaries, and AI agent integration. This is genuinely compelling for team development workflows and enterprise security requirements.

But we are still in the early days of tooling maturity. The current generation requires deep expertise in networking, SSL/TLS, container runtimes, reverse proxies, and distributed systems troubleshooting. Success demands infrastructure knowledge that most development teams simply do not possess.

The next generation of remote development platforms needs to abstract this complexity much more effectively. The promise should be that setup is simpler than local development, not orders of magnitude more complex. When that happens, remote AI development will become the obvious choice.

Until then, the setup burden remains the primary barrier to adoption. For teams with the infrastructure expertise, the benefits are clear. For everyone else, `pnpm install` still wins on simplicity.

**The key insight**: this is definitely the future of AI development. We just need the tooling to catch up with the vision.