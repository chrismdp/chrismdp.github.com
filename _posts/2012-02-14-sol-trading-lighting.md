---
layout: post
title: 'Sol Trader: on lighting'
date: 2012-02-14 22:56:43.000000000 +00:00
categories:
- products
- c++
- code
- opengl
- sol trader
- game development
- lighting
redirect_from:
- "/2012/02/sol-trading-lighting"
- "/2012/02/sol-trading-lighting/"
---
A quick update on the lighting code I've been working on. Now that I have normal maps and per-pixel bump mapping working, I can turn these:

![ship-texture-1](/assets/img/sol-trader-lighting-1.png)
![ship-texture-2](/assets/img/sol-trader-lighting-2.png)

Into this:

![ship-texture-3](/assets/img/sol-trader-lighting-3.png)
![ship-texture-4](/assets/img/sol-trader-lighting-4.png)

Check out how the ship appears lit from each side. It looks even better as you see it moving. Hey presto: a realistic 3D effect with only two triangles rendered.

All I'm using is this simple GLSL fragment shader:

{% highlight c %}

    void main() {
      vec4 color = texture(baseTexture, uv);
      vFragColor = vertColor * color;
      float alpha = vFragColor.a;

      if (alpha > 0.0 && useNormal) {
        vec3 lightDirection = normalize(vec3(0.2, 0.2, 0.0));
        vec4 normal = normalize(texture(normalTexture, uv) * 2.0 - 1.0);
        vec4 vEyeNormal = normalMatrix * normal;

        float diffuse = max(0.0, dot(vEyeNormal.xyz, lightDirection));
        vFragColor *= (diffuse * 3);
        vFragColor.a = alpha;
      }
    }

{% endhighlight %}

[GLSL](http://en.wikipedia.org/wiki/GLSL) is great.
